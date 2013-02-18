__author__ = 'michael'

from django.db import models
from django.contrib.auth.models import User

from unobase import models as unobase_models

class Blog(unobase_models.ContentModel):
    pass

class BlogEntry(unobase_models.ContentModel):
    blog = models.ForeignKey(Blog)
    posted_on_behalf_by = models.ForeignKey(User, null=True, blank=True, related_name='blog_entries_posted_on_behalf')

    class Meta():
        ordering = ['-created']
        verbose_name_plural = 'Blog entries'
