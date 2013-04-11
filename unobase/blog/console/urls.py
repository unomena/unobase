__author__ = 'michael'

from django.conf.urls.defaults import patterns, url

from unobase.blog.console import views
from unobase.blog.console import forms as blog_forms

urlpatterns = patterns('',
    url(r'^(?P<slug>[\w-]+)/detail/$',
        views.BlogDetail.as_view(template_name='console/blog/blog_detail.html'),
        name='console_blog_detail'),
                       
    url(r'^(?P<pk>\d+)/entry/create/$',
        views.BlogEntryCreate.as_view(form_class=blog_forms.BlogEntry,
            template_name='console/blog/blog_entries/blog_entry_edit.html'),
        name='console_blog_entry_create'),

    url(r'^entry/update/(?P<pk>\d+)/$',
        views.BlogEntryUpdate.as_view(form_class=blog_forms.BlogEntry,
            template_name='console/blog/blog_entries/blog_entry_edit.html'),
        name='console_blog_entry_update'),

    url(r'^entry/(?P<pk>\d+)/detail/$',
        views.BlogEntryDetail.as_view(template_name='console/blog/blog_entries/blog_entry_detail.html'),
        name='console_blog_entry_detail'),

    url(r'^entry/delete/(?P<pk>\d+)/$',
        views.BlogEntryDelete.as_view(),
        name='console_blog_entry_delete'),
)