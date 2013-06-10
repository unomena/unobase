'''
Created on 04 Mar 2013

@author: michael
'''
from django.conf.urls.defaults import patterns, url

from unobase.invoicing import views

urlpatterns = patterns('',                    
    url(r'^download_invoice/(?P<pk>\d+)/$',
        views.download_invoice,
        name='download_invoice'),
                       
)