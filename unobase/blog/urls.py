__author__ = 'michael'

from django.conf.urls.defaults import patterns, url

from unobase.blog import views

urlpatterns = patterns('',
                       
    url(r'^list/$',
        views.BlogList.as_view(template_name='blog/blog_list.html'),
        name='blog_list'),

    # Blog Entry

    url(r'^detail/(?P<slug>[\w-]+)/$',
        views.BlogEntryDetail.as_view(template_name='blog/blog_entry_detail.html'),
        name='blog_entry_detail'),
                       
    # Feed
    
    (r'^feed/$', views.BlogFeed()),

    # Blog
    url(r'^(?P<slug>[\w-]+)/$',
        views.BlogDetail.as_view(paginate_by=6, template_name='blog/blog_detail.html'),
        name='blog_detail'),
)
