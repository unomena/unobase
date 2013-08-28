__author__ = 'michael'

from django.db import models
from django.core.urlresolvers import reverse

from unobase import models as unobase_models
from unobase import settings as unobase_settings

class Blog(unobase_models.StatefulContentModel):
    pass

class BlogEntry(unobase_models.StatefulContentModel):
    blog = models.ForeignKey(Blog)
    posted_on_behalf_by = models.ForeignKey(unobase_settings.AUTH_USER_MODEL, null=True, blank=True, related_name='blog_entries_posted_on_behalf')
    co_authored_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta():
        ordering = ['-publish_date_time']
        verbose_name_plural = 'Blog entries'
        
    def get_absolute_url(self):
        return reverse('blog_entry_detail', args=(self.slug,))
