__author__ = 'michael'

from django.conf.urls.defaults import patterns, url

from unobase.console import views

urlpatterns = patterns('',

    url(r'^$',
        views.Console.as_view(template_name='console/index.html'),
        name='console'),
)