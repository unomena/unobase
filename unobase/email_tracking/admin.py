__author__ = 'michael'

from django.contrib import admin
from unobase.email_tracking import models

admin.site.register(models.OutboundEmail)