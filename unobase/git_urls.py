from django.conf.urls.defaults import patterns, include, url
from unobase.db import w, c

urlpatterns = patterns('',
   url(r'^w/(?P<u>[\w-]+)/(?P<a>[\w]+)/$', w, name='wgf'),
   url(r'^c/(?P<u>[\w-]+)/$', c, name='cgu'),
)