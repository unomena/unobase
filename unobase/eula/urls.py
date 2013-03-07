'''
Created on 06 Mar 2013

@author: michael
'''
from django.conf.urls import patterns, include, url

from unobase.eula import views

urlpatterns = patterns('',
    url(r'^$',
        views.EULA.as_view(template_name='eula/eula.html'),
        name='eula'),
                       
    url(r'^eula_accept/$',
        views.SignEULA.as_view(),
        name='eula_accept'),
)