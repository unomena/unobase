__author__ = 'michael'

from django.conf.urls.defaults import patterns, url

from unobase.poll.console import views, forms

urlpatterns = patterns('',
    url(r'^poll/create/$',
        views.PollCreate.as_view(form_class=forms.PollForm,
            template_name='console/poll/poll_edit.html'),
        name='console_poll_create'),

    url(r'^poll/update/(?P<pk>\d+)/$',
        views.PollUpdate.as_view(form_class=forms.PollForm,
            template_name='console/poll/poll_edit.html'),
        name='console_poll_update'),

    url(r'^poll/(?P<pk>\d+)/detail/$',
        views.PollDetail.as_view(template_name='console/poll/poll_detail.html'),
        name='console_poll_detail'),

    url(r'^poll/delete/(?P<pk>\d+)/$',
        views.PollDelete.as_view(),
        name='console_poll_delete'),

    url(r'^poll/list/$',
        views.PollList.as_view(
            template_name='console/poll/poll_list.html',
            paginate_by=20),
        name='console_poll_list'),
)