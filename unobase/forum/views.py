__author__ = 'michael'

from django.views import generic as generic_views
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core.urlresolvers import reverse

from unobase.views import ListWithDetailView
from unobase.forum import models
from unobase import mixins, constants

class ForumTaggedList(ListWithDetailView):
    
    def get_object(self):
        return get_object_or_404(models.Forum,
            slug=self.kwargs['slug'])
    
    def get_queryset(self):
        if self.request.GET.has_key('filter_by_tag') and self.request.GET['filter_by_tag'].strip():
            return models.ForumThread.objects.filter(category__forum=self.object, state=constants.STATE_PUBLISHED,
                                                     tags__title__iexact=self.request.GET['filter_by_tag'].strip())

        return models.ForumThread.objects.filter(category__forum=self.object, state=constants.STATE_PUBLISHED)

class ForumDetail(ListWithDetailView):

    def get_object(self):
        return get_object_or_404(models.Forum,
            slug=self.kwargs['slug'])

    def get_queryset(self):
        return models.ForumCategory.objects.filter(forum=self.object, state=constants.STATE_PUBLISHED)

# Forum category

class ForumCategoryDetail(ListWithDetailView):

    def get_object(self):
        return get_object_or_404(models.ForumCategory,
            slug=self.kwargs['slug2'])

    def get_queryset(self):
        return models.ForumThread.objects.filter(category=self.object, state=constants.STATE_PUBLISHED)

class ForumCategoryCreate(mixins.LoginRequiredMixin, mixins.PermissionRequiredMixin, generic_views.CreateView):

    permission_required = 'forum.can_moderate'
    raise_exception = True

    def get_initial(self):
        return {'user' : self.request.user,
                'forum' : models.Forum.objects.get(slug=self.kwargs['slug'])}

    def get_success_url(self):
        return reverse('forum_detail', args=(self.object.forum.slug,))

class ForumCategoryUpdate(mixins.LoginRequiredMixin, mixins.PermissionRequiredMixin, generic_views.UpdateView):

    permission_required = 'forum.can_moderate'
    raise_exception = True

    def get_initial(self):
        return {'user' : self.request.user}

    def get_success_url(self):
        return reverse('forum_detail', args=(self.object.forum.slug,))

    def get_queryset(self):
        return models.ForumCategory.objects.all()

class ForumCategoryDelete(mixins.LoginRequiredMixin, mixins.PermissionRequiredMixin, generic_views.DeleteView):

    permission_required = 'forum.can_moderate'
    raise_exception = True

    def get_queryset(self):
        return models.ForumCategory.objects.all()

    def get_success_url(self):
        return reverse('forum_detail', args=(self.object.forum.slug,))

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.state = constants.STATE_DELETED
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)

# Forum thread

class ForumThreadDetail(ListWithDetailView):

    def get_object(self):
        return get_object_or_404(models.ForumThread,
            slug=self.kwargs['slug3'])

    def get_queryset(self):
        return models.ForumPost.objects.filter(thread=self.object, state=constants.STATE_PUBLISHED).order_by('created')

class ForumThreadCreate(mixins.LoginRequiredMixin, generic_views.CreateView):

    def get_initial(self):
        return {'user' : self.request.user,
                'category': models.ForumCategory.objects.get(slug=self.kwargs['slug'])}

    def get_success_url(self):
        return reverse('forum_thread_detail', args=(self.object.category.forum.slug, 
                                                    self.object.category.slug, 
                                                    self.object.slug))

class ForumThreadUpdate(mixins.LoginRequiredMixin, mixins.PermissionOrCreatorRequiredMixin, generic_views.UpdateView):

    permission_required = 'forum.can_moderate'
    raise_exception = True

    def get_initial(self):
        return {'user' : self.request.user}

    def get_success_url(self):
        return reverse('forum_thread_detail', args=(self.object.category.forum.slug, 
                                                    self.object.category.slug, 
                                                    self.object.slug))

    def get_queryset(self):
        return models.ForumThread.objects.all()

    def form_valid(self, form):
        self.object = form.save()
        if not self.object.edited:
            self.object.edited = True
            self.object.save()
        return super(ForumThreadUpdate, self).form_valid(form)

class ForumThreadDelete(mixins.LoginRequiredMixin, mixins.PermissionRequiredMixin, generic_views.DeleteView):

    permission_required = 'forum.can_moderate'
    raise_exception = True

    def get_queryset(self):
        return models.ForumThread.objects.all()

    def get_success_url(self):
        return reverse('forum_thread_detail', args=(self.object.category.forum.slug, 
                                                    self.object.category.slug, 
                                                    self.object.slug))

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.state = constants.STATE_DELETED
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)

# Forum Post

class ForumPostCreate(mixins.LoginRequiredMixin, generic_views.CreateView):

    def get_initial(self):
        return {'user' : self.request.user,
                'thread': models.ForumThread.objects.get(slug=self.kwargs['slug'])}

    def get_success_url(self):
        return reverse('forum_thread_detail', args=(self.object.thread.category.forum.slug, 
                                                    self.object.thread.category.slug, 
                                                    self.object.thread.slug))

class ForumPostUpdate(mixins.LoginRequiredMixin, generic_views.UpdateView):

    def get_initial(self):
        return {'user' : self.request.user}

    def get_success_url(self):
        return reverse('forum_thread_detail', args=(self.object.thread.category.forum.slug, 
                                                    self.object.thread.category.slug, 
                                                    self.object.thread.slug))

    def get_queryset(self):
        return models.ForumPost.objects.all()

    def form_valid(self, form):
        self.object = form.save()
        if not self.object.edited:
            self.object.edited = True
            self.object.save()
        return super(ForumPostUpdate, self).form_valid(form)

class ForumPostDelete(mixins.LoginRequiredMixin, generic_views.DeleteView):

    def get_queryset(self):
        return models.ForumPost.objects.all()

    def get_success_url(self):
        return reverse('forum_thread_detail', args=(self.object.thread.category.forum.slug, 
                                                    self.object.thread.category.slug, 
                                                    self.object.thread.slug))

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.state = constants.STATE_DELETED
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)

