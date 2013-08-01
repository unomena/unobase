from django.views import generic as generic_views
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.http import Http404
from django.contrib.syndication.views import Feed
from django.conf import settings
from django.utils.html import strip_tags

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

class SingleBlogDetail(BlogDetail):

    def get_object(self):
        blogs = models.Blog.objects.filter(state=unobase_constants.STATE_PUBLISHED)
        if blogs:
            return blogs[0]
        
        raise Http404('No blogs available')

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
    
class BlogFeed(Feed):
    title = "%s Blog" % settings.APP_NAME
    link = "/blog/"
    description = "Blog entries for %s" % settings.APP_NAME

    def items(self):
        return models.BlogEntry.objects.filter(
            state=unobase_constants.STATE_PUBLISHED
        ).order_by('-publish_date_time')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return strip_tags(item.content)