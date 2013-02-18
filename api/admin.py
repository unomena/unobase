'''
Created on 15 Jan 2013

@author: euan
'''
from django.contrib import admin

from unobase.api import models

class RequestAdmin(admin.ModelAdmin):
    list_display = ('service', 'status', 'created_timestamp', 'completed_timestamp',)
    list_filter = ('service', 'status', 'created_timestamp', 'completed_timestamp',)

admin.site.register(models.Destination)
admin.site.register(models.Service)
admin.site.register(models.Request, RequestAdmin)
admin.site.register(models.RequestLog)