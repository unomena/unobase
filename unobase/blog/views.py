from django.views import generic as generic_views
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from unobase import constants as unobase_constants
from unobase import views as unobase_views
from unobase.blog import models

class BlogDetail(unobase_views.ListWithDetailView):

    def get_object(self):
        return get_object_or_404(models.Blog,
            state=unobase_constants.STATE_PUBLISHED, slug=self.kwargs['slug'])

    def get_queryset(self):
        if self.request.GET.has_key('filter_by_tag') and self.request.GET['filter_by_tag'].strip():
            return models.BlogEntry.objects.filter(tags__title__iexact=self.request.GET['filter_by_tag'].strip())

        return models.BlogEntry.objects.filter(blog=self.object)

class BlogList(generic_views.ListView):

    def get_queryset(self):
        return models.Blog.objects.filter(state=unobase_constants.STATE_PUBLISHED)

class BlogEntryDetail(generic_views.DetailView):

    def get_object(self):
        return get_object_or_404(models.BlogEntry,
            state=unobase_constants.STATE_PUBLISHED,
            slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(BlogEntryDetail, self).get_context_data(**kwargs)
        context.update({'content_type':ContentType.objects.get_for_model(self.object)})
        return context