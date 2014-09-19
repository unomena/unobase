__author__ = 'michael'

from django.conf.urls.defaults import patterns, url

from unobase.forum import views, forms

urlpatterns = patterns('',

    # Forum
    url(r'^(?P<slug>[\w-]+)/$',
        views.ForumDetail.as_view(paginate_by=6, template_name='forum/forum_detail.html'),
        name='forum_detail'),
                       
     url(r'^tagged/list/(?P<slug>[\w-]+)/$',
        views.ForumTaggedList.as_view(paginate_by=20, template_name='forum/forum_tagged_list.html'),
        name='forum_tagged_list'),

    # Forum category

    url(r'^(?P<slug1>[\w-]+)/category/(?P<slug2>[\w-]+)/$',
        views.ForumCategoryDetail.as_view(paginate_by=6, template_name='forum/forum_category_detail.html'),
        name='forum_category_detail'),

    url(r'^category/create/(?P<slug>[\w-]+)/$',
        views.ForumCategoryCreate.as_view(form_class=forms.ForumCategory,
            template_name='forum/forum_category_edit.html',
        ),
        name='forum_category_create'),

    url(r'^category/update/(?P<slug>[\w-]+)/$',
        views.ForumCategoryUpdate.as_view(form_class=forms.ForumCategory,
            template_name='forum/forum_category_edit.html',
        ),
        name='forum_category_edit'),

    url(r'^category/delete/(?P<slug>[\w-]+)/$',
        views.ForumCategoryDelete.as_view(),
        name='forum_category_delete'),

    # Forum thread

    url(r'^(?P<slug1>[\w-]+)/category/(?P<slug2>[\w-]+)/thread/(?P<slug3>[\w-]+)/$',
        views.ForumThreadDetail.as_view(paginate_by=6, template_name='forum/forum_thread_detail.html'),
        name='forum_thread_detail'),

    url(r'^thread/create/(?P<slug>[\w-]+)/$',
        views.ForumThreadCreate.as_view(form_class=forms.ForumThread,
            template_name='forum/forum_thread_edit.html',
        ),
        name='forum_thread_create'),

    url(r'^thread/update/(?P<slug>[\w-]+)/$',
        views.ForumThreadUpdate.as_view(form_class=forms.ForumThread,
            template_name='forum/forum_thread_edit.html',
        ),
        name='forum_thread_edit'),

    url(r'^thread/delete/(?P<slug>[\w-]+)/$',
        views.ForumThreadDelete.as_view(),
        name='forum_thread_delete'),

    # Forum post

    url(r'^post/create/(?P<slug>[\w-]+)/$',
        views.ForumPostCreate.as_view(form_class=forms.ForumPost,
            template_name='forum/forum_post_edit.html',
        ),
        name='forum_post_create'),

    url(r'^post/update/(?P<slug>[\w-]+)/$',
        views.ForumPostUpdate.as_view(form_class=forms.ForumPost,
            template_name='forum/forum_post_edit.html',
        ),
        name='forum_post_edit'),

    url(r'^post/delete/(?P<slug>[\w-]+)/$',
        views.ForumPostDelete.as_view(),
        name='forum_post_delete'),
)