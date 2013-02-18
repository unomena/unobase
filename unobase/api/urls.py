'''
Created on 15 Jan 2013

@author: euan
'''
from django.conf.urls.defaults import patterns, include, url
from django.views.decorators.csrf import csrf_exempt

from unobase.api import mock_handlers

urlpatterns = patterns('',

    url(r'^mock/post/success/$', 
        csrf_exempt(mock_handlers.PostSuccessHandler.as_view()),
        name='api_mock_post_success'),

    url(r'^mock/post/failure/$',
        csrf_exempt(mock_handlers.PostFailureHandler.as_view()),
        name='api_mock_post_failure'),

)