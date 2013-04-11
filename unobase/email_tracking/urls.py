__author__ = 'michael'

from django.conf.urls.defaults import patterns, url

from unobase.email_tracking import views

urlpatterns = patterns('',

    url(r'^email_tracking/list/$',
        views.OutboundEmailList.as_view(template_name='email_tracking/outbound_email_list.html',
                                        paginate_by=20),
        name='outbound_email_list'),

    url(r'^email_tracking/detail/(?P<pk>\d+)/$',
        views.OutboundEmailDetail.as_view(template_name='email_tracking/outbound_email_detail.html'),
        name='outbound_email_detail'),
)