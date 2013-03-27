__author__ = 'michael'

from django.conf.urls.defaults import patterns, url

from unobase.age_gate import views, forms

urlpatterns = patterns('',

    url(r'^$',
        views.AgeGate.as_view(form_class=forms.AgeGateForm,
                              template_name='age_gate/age_gate_form.html'),
        name='age_gate'),
)