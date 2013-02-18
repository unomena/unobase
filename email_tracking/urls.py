__author__ = 'michael'

from django.conf.urls.defaults import patterns, url

from unobase.email_tracking import views

urlpatterns = patterns('',

    # Blog
#    url(r'^(?P<slug>[\w-]+)/$',
#        views.BlogDetail.as_view(paginate_by=6, template_name='blog/blog_detail.html'),
#        name='blog_detail'),

    url(r'^list/$',
        views.OutboundEmailList.as_view(template_name='email_tracking/outbound_email_list.html'),
        name='outbound_email_list'),

    url(r'^detail/(?P<pk>\d+)/$',
        views.OutboundEmailDetail.as_view(template_name='email_tracking/outbound_email_detail.html'),
        name='outbound_email_detail'),
)