__author__ = 'michael'

from django.contrib import admin

from unobase.poll import models

admin.site.register(models.PollQuestion)
admin.site.register(models.PollAnswer)