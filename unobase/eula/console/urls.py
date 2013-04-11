__author__ = 'michael'

from django.conf.urls.defaults import patterns, url

from unobase.eula.console import views, forms

urlpatterns = patterns('',
    url(r'^eula/create/$',
        views.EULACreate.as_view(form_class=forms.EULAForm,
            template_name='console/eula/eula_edit.html'),
        name='console_eula_create'),

    url(r'^eula/update/(?P<pk>\d+)/$',
        views.EULAUpdate.as_view(form_class=forms.EULAForm,
            template_name='console/eula/eula_edit.html'),
        name='console_eula_update'),

    url(r'^eula/(?P<pk>\d+)/detail/$',
        views.EULADetail.as_view(template_name='console/eula/eula_detail.html'),
        name='console_eula_detail'),

    url(r'^eula/delete/(?P<pk>\d+)/$',
        views.EULADelete.as_view(),
        name='console_eula_delete'),

    url(r'^eula/list/$',
        views.EULAList.as_view(
            template_name='console/eula/eula_list.html',
            paginate_by=20),
        name='console_eula_list'),
)