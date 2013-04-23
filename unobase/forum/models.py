__author__ = 'michael'

from django.db import models
from django.core.urlresolvers import reverse

from unobase import models as unobase_models

class Forum(unobase_models.StatefulContentModel):
    pass

class ForumCategory(unobase_models.StatefulContentModel):
    forum = models.ForeignKey(Forum, related_name='categories')

    class Meta():
        permissions = (('can_moderate', 'Can moderate forum category'),)

class ForumThread(unobase_models.StatefulContentModel):
    category = models.ForeignKey(ForumCategory, related_name='threads')
    edited = models.BooleanField(default=False)

    class Meta():
        ordering = ['-created']
        verbose_name_plural = 'Forum thread'
        permissions = (('can_moderate', 'Can moderate forum thread'),)
    
    def get_absolute_url(self):    
        return reverse('forum_thread_detail', args=(self.category.forum.slug, 
                                                    self.category.slug, 
                                                    self.slug))

class ForumPost(unobase_models.StatefulContentModel):
    thread = models.ForeignKey(ForumThread)
    edited = models.BooleanField(default=False)

    class Meta():
        ordering = ['created']
        verbose_name_plural = 'Forum post'
        permissions = (('can_moderate', 'Can moderate forum post'),)