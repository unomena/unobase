__author__ = 'michael'

from django.views import generic as generic_views
from django.http import Http404
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from django.shortcuts import get_object_or_404

from unobase import mixins as unobase_mixins
from unobase import utils as unobase_utils
from unobase.commenting  import models, signals, utils

class CustomCommentCreate(generic_views.CreateView):

    def get_initial(self):
        return {'user' : self.request.user,
                'object': ContentType.objects.get(pk=self.kwargs['content_type_pk']).get_object_for_this_type(pk=self.kwargs['object_pk']),
                'ip_address': self.get_user_ip(self.request)}

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Your comment has been posted.')
        signals.user_commented.send(sender=models.CustomComment, user=self.request.user, request=self.request, comment=self.object)
        form_class = self.get_form_class()
        form = form_class(initial=self.get_initial())
        return self.render_to_response(self.get_context_data(form=form))


    def get_user_ip(self, request):
        """
        Finds a user's real ip address, taking load balancer proxy into consideration
        """
        try:
            return request.META['HTTP_X_REAL_IP'] if 'HTTP_X_REAL_IP' in request.META and request.META['HTTP_X_REAL_IP'] else request.META['REMOTE_ADDR']
        except:
            return '0.0.0.0'
        
class CustomCommentListMixin(generic_views.ListView):
    
    def get_context_data(self, **kwargs):
        context = super(CustomCommentListMixin, self).get_context_data(**kwargs)

        context['comment_count'] = self.comments.count()
        return context
    
    def get_queryset(self):
        self.comments = utils.get_permitted_comments(queryset=models.CustomComment.objects.filter(content_type=self.kwargs['content_type_pk'],
                                                                                                  object_pk=self.kwargs['object_pk'],
                                                                                                  report_count__lt=3),
                                                                                                  user=self.request.user)
        
        return self.comments
        

class CustomCommentReport(CustomCommentListMixin):

    def get(self, request, *args, **kwargs):
        comments_reported = request.session.get('comments_reported', [])
        
        if not self.kwargs['pk'] in comments_reported:
            comments_reported.append(self.kwargs['pk'])
            request.session['comments_reported'] = comments_reported
            
            comment = get_object_or_404(models.CustomComment, pk=self.kwargs['pk'])

            comment.report_count += 1
            comment.save()
    
            messages.success(self.request, 'Comment has been reported.')
        else:
            messages.success(self.request, 'You have already reported this comment.')
        
        return super(CustomCommentReport, self).get(request, *args, **kwargs)

class CustomCommentList(CustomCommentListMixin):
    """
    List for comments
    """
