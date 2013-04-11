'''
Created on 10 Jan 2013

@author: euan
'''
from django import forms
from django.forms.models import inlineformset_factory

from unobase.eula import models as eula_models
        
class EULAForm(forms.ModelForm):
    
    class Meta:
        model = eula_models.EULA
        fields = ['title']

EULAVersionFormSet = inlineformset_factory(eula_models.EULA, eula_models.EULAVersion, extra=1)
    
