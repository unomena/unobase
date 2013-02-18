__author__ = 'michael'

from django.conf import settings
from django.conf.urls.defaults import patterns, include, url

import views
import forms

urlpatterns = patterns('',

    url(r'^comment_form/(?P<content_type_pk>\d+)/(?P<object_pk>\d+)/$',
        views.CustomCommentCreate.as_view(form_class=forms.CustomCommentForm,
            template_name='commenting/comment_form.html'),
        name='comment_create'),

    url(r'^comment_list/(?P<content_type_pk>\d+)/(?P<object_pk>\d+)/$',
        views.CustomCommentList.as_view(
            paginate_by=20,
            template_name='commenting/comment_list.html'),
        name='comment_list'),
)