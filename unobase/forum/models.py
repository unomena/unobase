__author__ = 'michael'

from django.db import models

from unobase import models as unobase_models

class Forum(unobase_models.ContentModel):
    pass

class ForumCategory(unobase_models.ContentModel, unobase_models.StateModel):
    forum = models.ForeignKey(Forum, related_name='categories')

    class Meta():
        permissions = (('can_moderate', 'Can moderate forum category'),)

class ForumThread(unobase_models.ContentModel, unobase_models.StateModel):
    category = models.ForeignKey(ForumCategory, related_name='threads')
    edited = models.BooleanField(default=False)

    class Meta():
        ordering = ['-created']
        verbose_name_plural = 'Forum thread'
        permissions = (('can_moderate', 'Can moderate forum thread'),)

class ForumPost(unobase_models.ContentModel, unobase_models.StateModel):
    thread = models.ForeignKey(ForumThread)
    edited = models.BooleanField(default=False)

    class Meta():
        ordering = ['created']
        verbose_name_plural = 'Forum post'
        permissions = (('can_moderate', 'Can moderate forum post'),)