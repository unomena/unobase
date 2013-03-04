__author__ = 'michael'

from django.db import models
from unobase import settings as unobase_settings

class OutboundEmail(models.Model):
    user = models.ForeignKey(unobase_settings.AUTH_USER_MODEL, related_name='inbound_emails')
    subject = models.CharField(max_length=250)
    message = models.TextField()
    sent_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-sent_timestamp']
