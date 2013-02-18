__author__ = 'michael'

from django.db import models
from django.contrib.auth.models import User

class OutboundEmail(models.Model):
    user = models.ForeignKey(User, related_name='inbound_emails')
    subject = models.CharField(max_length=250)
    message = models.TextField()
    sent_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-sent_timestamp']
