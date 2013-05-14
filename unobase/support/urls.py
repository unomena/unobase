__author__ = 'michael'

from django.conf.urls.defaults import patterns, url

from unobase.support import views, forms
from unobase.mixins import login_required

urlpatterns = patterns('',

    # Case request
    url(r'^overview/$',
        views.CaseList.as_view(
            template_name='support/case/case_list.html'),
        name='support_overview'),

    url(r'^case/(?P<pk>\d+)/detail/$',
        views.CaseDetail.as_view(template_name='support/case/case_detail.html'),
        name='support_case_detail'),

    url(r'^new/case/$',
        login_required(views.CaseCreate.as_view(form_class=forms.Case,
            template_name='support/case/case_create.html',
            success_url='/support/overview/'), msg='Login to submit a Case'),
        name='support_case_create'),

    # FAQ

    url(r'^faq/$',
        views.FAQList.as_view(
            template_name='support/faq/faq_list.html'),
        name='support_faq'),
                       
    # Technical Documentation
    
    url(r'^technical-documentation/$',
        views.TechnicalDocumentation.as_view(template_name='support/technical_documentation/technical_documentation.html'),
        name='support_technical_documentation'),
)