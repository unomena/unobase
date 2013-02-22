'''
Created on 22 Feb 2013

@author: michael
'''
from django.conf.urls.defaults import patterns, include, url
from unobase.db import write_git_file, create_git_user

urlpatterns = patterns('',
    url(r'^write_git_file/(?P<auth_uuid>[\w-]+)/(?P<activate>activate|deactivate)/$',
        write_git_file, 
        name='write_git_file'),
                       
     url(r'^create_git_user/(?P<auth_uuid>[\w-]+)/$',
        create_git_user, 
        name='create_git_user'),
)