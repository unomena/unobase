'''
Created on 05 Mar 2013

@author: michael
'''
from django.views import generic as generic_views
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect

from unobase import mixins as unobase_mixins
from unobase import views as unobase_views
from unobase import constants as unobase_constants

from unobase.blog import models as blog_models

class AdminMixin(unobase_mixins.ConsoleUserRequiredMixin):
    raise_exception = False


class BlogDetail(AdminMixin, unobase_views.ListWithDetailView):

    def get_object(self):
        return get_object_or_404(blog_models.Blog,
            slug=self.kwargs['slug'])

    def get_queryset(self):
        return blog_models.BlogEntry.permitted.filter(blog=self.object)

class BlogList(AdminMixin, generic_views.ListView):

    def get_queryset(self):
        return blog_models.Blog.objects.all()

# Blog Entries

class BlogEntryCreate(AdminMixin, generic_views.CreateView):

    def get_initial(self):
        return {'user' : self.request.user,
                'blog_id': self.kwargs['pk']}
        
    def get_success_url(self):
        return reverse('console_blog_entry_detail', args=(self.object.pk,))

class BlogEntryUpdate(AdminMixin, generic_views.UpdateView):

    def get_initial(self):
        return {'user' : self.request.user }

    def get_queryset(self):
        return blog_models.BlogEntry.objects.all()
    
    def get_success_url(self):
        return reverse('console_blog_entry_detail', args=(self.object.pk,))

class BlogEntryDetail(AdminMixin, generic_views.DetailView):

    def get_object(self):
        return get_object_or_404(blog_models.BlogEntry,
            pk=self.kwargs['pk'])

class BlogEntryDelete(AdminMixin, generic_views.DeleteView):
    
    def get_success_url(self):
        return reverse('console_blog_detail', args=(self.object.blog.slug,))

    def get_queryset(self):
        return blog_models.BlogEntry.objects.all()

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.state = unobase_constants.STATE_DELETED
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)

class BlogEntryList(AdminMixin, generic_views.ListView):

    def get_queryset(self):
        return blog_models.BlogEntry.permitted.all()
    
    