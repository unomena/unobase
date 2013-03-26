__author__ = 'michael'

from django.conf import settings
from django.conf.urls.defaults import patterns, include, url

from unobase.commenting import views
from unobase.commenting import forms

urlpatterns = patterns('',

    url(r'^comment_form/(?P<content_type_pk>\d+)/(?P<object_pk>\d+)/$',
        views.CustomCommentCreate.as_view(form_class=forms.CustomCommentForm,
            template_name='commenting/comment_form.html'),
        name='comment_create'),

    url(r'^comment_report/(?P<content_type_pk>\d+)/(?P<object_pk>\d+)/(?P<pk>\d+)/$',
        views.CustomCommentReport.as_view(template_name='commenting/comment_list.html',
                                          paginate_by=20),
        name='comment_report'),

    url(r'^comment_list/(?P<content_type_pk>\d+)/(?P<object_pk>\d+)/$',
        views.CustomCommentList.as_view(
            paginate_by=20,
            template_name='commenting/comment_list.html'),
        name='comment_list'),
)