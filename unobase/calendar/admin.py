from django.contrib import admin

from unobase.calendar import models

admin.site.register(models.Calendar)
admin.site.register(models.Venue)
admin.site.register(models.Event)