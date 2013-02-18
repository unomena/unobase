'''
Created on 15 Jan 2013

@author: euan
'''
import uuid

from django.conf import settings
from django.db import models

from unobase.api import exceptions, constants

class Destination(models.Model):
    """
    Where to send stuff.
    """
    title = models.CharField(max_length=32)
    url = models.URLField()
    username = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=200, blank=True, null=True)
    
    def __unicode__(self):
        return self.title
    
class Service(models.Model):
    """
    Where to send stuff of a certain type and how many times to retry.
    """
    type = models.CharField(max_length=200, unique=True,
                            choices=settings.API_REQUEST_TYPE_CHOICES)
    destination = models.ForeignKey(Destination)
    retries = models.PositiveSmallIntegerField(default=3)
    success_string = models.CharField(max_length=200)
    error_string = models.CharField(max_length=200, blank=True, null=True)
    
    def __unicode__(self):
        return self.get_type_display()

class Request(models.Model):
    """
    The actual stuff being sent.
    """
    uuid = models.CharField(max_length=64, editable=False)
    service = models.ForeignKey(Service)
    request_data = models.TextField()
    response_data = models.TextField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(choices=constants.REQUEST_STATUS_CHOICES,
                                              default=constants.REQUEST_STATUS_CREATED)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    completed_timestamp = models.DateTimeField(blank=True, null=True)
    
    @property
    def send_count(self):
        return RequestLog.objects.filter(request=self,
                                         action=constants.REQUEST_ACTION_SEND).count()
    
    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = uuid.uuid4()
            while Request.objects.filter(uuid=self.uuid).count() > 1:
                self.uuid = uuid.uuid4()
        
        super(Request, self).save(*args, **kwargs)

def post_save_request(sender, instance, created, **kwargs):
    if created:
        RequestLog.objects.create(request=instance,
                                  action=constants.REQUEST_ACTION_CREATE,
                                  result=constants.REQUEST_STATUS_CREATED)

models.signals.post_save.connect(post_save_request, sender=Request)

class RequestLog(models.Model):
    """
    A log of what happened.
    """
    request = models.ForeignKey(Request)
    action = models.PositiveSmallIntegerField(choices=constants.REQUEST_ACTION_CHOICES)
    result = models.PositiveSmallIntegerField(choices=constants.REQUEST_STATUS_CHOICES)
    narration = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    