__author__ = 'michael'

from django.db import models

from unobase import models as unobase_models
from unobase import settings as unobase_settings

class Blog(unobase_models.ContentModel, unobase_models.StateModel):
    pass

class BlogEntry(unobase_models.ContentModel, unobase_models.StateModel):
    blog = models.ForeignKey(Blog)
    posted_on_behalf_by = models.ForeignKey(unobase_settings.AUTH_USER_MODEL, null=True, blank=True, related_name='blog_entries_posted_on_behalf')

    class Meta():
        ordering = ['-created']
        verbose_name_plural = 'Blog entries'
