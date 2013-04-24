from django.conf.urls import patterns, include, url

from unobase import views

urlpatterns = patterns('',
    url(r'^content-block-update/$',
        views.ContentBlockUpdate.as_view(),
        name='content_block_update'),
)