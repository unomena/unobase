from unobase.forum import models

__author__ = 'michael'

from django.contrib import admin
    
admin.site.register(models.Forum)
admin.site.register(models.ForumCategory)
admin.site.register(models.ForumThread)
admin.site.register(models.ForumPost)