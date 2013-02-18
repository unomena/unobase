'''
Created on 24 Jan 2013

@author: euan
'''
from celery.decorators import task
from unobase.api import constants, utils, models
from django.utils import timezone

@task()
def send_request_body(request_id):
    
    request = models.Request.objects.get(pk=request_id)
    request.response_data = utils.do_post(url=request.service.destination.url, body='data=%s' % request.request_data).strip()
    complete_request(request, constants.REQUEST_ACTION_SEND)

@task()
def send_request_data(request_id):
    
    request = models.Request.objects.get(pk=request_id)
    request.response_data = utils.do_post(url=request.service.destination.url, body='data=%s' % request.request_data).strip()
    complete_request(request, constants.REQUEST_ACTION_SEND)
    
def complete_request(request, action):
    
    if request.service.success_string in request.response_data:
        request.status = constants.REQUEST_STATUS_SUCCESS
        result = constants.REQUEST_ACTION_STATUS_COMPLETED
        request.completed_timestamp = timezone.now()
    else:
        if request.service.error_string and request.service.error_string in request.response_data:
            request.status = constants.REQUEST_STATUS_ERROR
            result = constants.REQUEST_ACTION_STATUS_COMPLETED
        else:
            if request.send_count > request.service.retries:
                request.status = constants.REQUEST_STATUS_ABORT
                result = constants.REQUEST_ACTION_STATUS_COMPLETED
            else:
                request.status = constants.REQUEST_STATUS_RETRY
                result = constants.REQUEST_ACTION_STATUS_RETRY

    request.save()

    models.RequestLog.objects.create(request=request, action=action, result=result)