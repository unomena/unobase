__author__ = 'michael'

from django.contrib import admin
from unobase.email_tracking import models


class OutboundEmailAdmin(admin.ModelAdmin):
    list_display = ['user', 'subject', 'sent_timestamp']
    list_filter = ['user__email', 'subject', 'sent_timestamp']


admin.site.register(models.OutboundEmail, OutboundEmailAdmin)
