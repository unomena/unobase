__author__ = 'michael'

from django.conf.urls.defaults import patterns, url

from unobase.console import views

urlpatterns = patterns('',

    url(r'^$',
        views.Console.as_view(template_name='console/index.html'),
        name='console'),
                       
    url(r'^content/image/url/(?P<content_type>\w+)/(?P<pk>\d+)/$',
        views.ContentImageUrl.as_view(),
        name='console_news_and_events_content_image_url'),
)