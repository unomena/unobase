'''
Created on 31 May 2013

@author: euan
'''

from django.conf.urls.defaults import patterns, url
from django.views import generic as genric_views

from unobase.questionnaire import views, forms, models

urlpatterns = patterns('',

    url(r'^questionnaire/(?P<slug>[\w-]+)/thanks/$',
        genric_views.DetailView.as_view(model=models.Questionnaire,
                                        template_name='questionnaire/questionnaire_thanks.html'),
        name='questionnaire_thanks'),

    url(r'^questionnaire/(?P<slug>[\w-]+)/already_completed/$',
         genric_views.DetailView.as_view(model=models.Questionnaire,
                                         template_name='questionnaire/questionnaire_already_completed.html'),
        name='questionnaire_already_completed'),

    url(r'^questionnaire/(?P<slug>[\w-]+)/$',
        views.Questionnaire.as_view(form_class=forms.Questionnaire,
                                          template_name='questionnaire/questionnaire_form.html',
                                          success_url='thanks/'),
        name='questionnaire_form'),
)