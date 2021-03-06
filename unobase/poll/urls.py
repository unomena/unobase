__author__ = 'michael'

from django.conf.urls.defaults import patterns, url

from unobase.poll import views, forms

urlpatterns = patterns('',

    url(r'^answer$',
        views.PollAnswer.as_view(form_class=forms.PollAnswerForm,
                                 template_name='poll/includes/poll_results.html'),
        name='poll_answer'),
)