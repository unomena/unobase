__author__ = 'michael'

from django.conf.urls.defaults import patterns, include, url

import views

urlpatterns = patterns('',

    url(r'^manage/$',
        views.TagAjax.as_view(
            template_name='unobase/inclusion_tags/tag_manage.html'),
        name='tagging_manage'),
)