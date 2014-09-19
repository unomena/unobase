'''
Created on 15 Jan 2013

@author: euan
'''

from django.conf import settings

REQUEST_STATUS_CREATED = 0
REQUEST_STATUS_SUCCESS = 1
REQUEST_STATUS_ERROR = 2
REQUEST_STATUS_RETRY = 3
REQUEST_STATUS_ABORT = 4

REQUEST_STATUS_CHOICES = ((REQUEST_STATUS_CREATED,'Created'),
                          (REQUEST_STATUS_SUCCESS,'Success'),
                          (REQUEST_STATUS_ERROR,'Error'),
                          (REQUEST_STATUS_RETRY,'Retry'),
                          (REQUEST_STATUS_ABORT,'Abort'),
                          )

REQUEST_ACTION_CREATE = 0
REQUEST_ACTION_SEND = 1

REQUEST_ACTION_CHOICES = ((REQUEST_STATUS_CREATED,'Created'),
                          (REQUEST_STATUS_RETRY,'Retry'),
                          )

REQUEST_ACTION_STATUS_CREATED = 0
REQUEST_ACTION_STATUS_RETRY = 1
REQUEST_ACTION_STATUS_COMPLETED = 2


REQUEST_ACTION_STATUS_CHOICES = ((REQUEST_ACTION_STATUS_CREATED,'Created'),
                                 (REQUEST_ACTION_STATUS_RETRY,'Retry'),
                                 (REQUEST_ACTION_STATUS_COMPLETED,'Completed'),
                                 )