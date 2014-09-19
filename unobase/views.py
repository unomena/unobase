from django.views import generic as generic_views
from django.http import Http404
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from django.shortcuts import get_object_or_404

from unobase import models, utils, mixins

class ListWithDetailView(generic_views.ListView):

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        if not allow_empty and len(self.object_list) == 0:
            raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.")
                          % {'class_name': self.__class__.__name__})
        context = self.get_context_data(object=self.object,
            object_list=self.object_list,
            request=self.request)
        return self.render_to_response(context)
    
class ContentBlockUpdate(mixins.AdminRequiredMixin, generic_views.View):
    
    def post(self, request, *args, **kwargs):
        slug = request.POST.get('slug')
        content = request.POST.get('content')
        
        content_block = get_object_or_404(models.ContentBlock, slug=slug)
        content_block.content = content
        content_block.save()
        
        return utils.respond_with_json({'status': 'success'})

