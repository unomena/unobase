'''
Created on 10 Jan 2013

@author: euan
'''
from django import forms
from django.forms.models import inlineformset_factory

from unobase.poll import models as poll_models
        
class PollForm(forms.ModelForm):
    
    class Meta:
        model = poll_models.PollQuestion

PollAnswerFormSet = inlineformset_factory(poll_models.PollQuestion, poll_models.PollAnswer, extra=1)
    
