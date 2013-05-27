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
        
class EULAVersionForm(forms.ModelForm):
    
    class Meta:
        model = eula_models.EULAVersion
        
    def __init__(self, *args, **kwargs):
        super(EULAVersionForm, self).__init__(*args, **kwargs)
        
        if self.instance.pk:
            self.fields['version'].attrs.update({'readonly': 'readonly'})
            self.fields['content'].attrs.update({'readonly': 'readonly'})
        
    
EULAVersionFormSet = inlineformset_factory(
    eula_models.EULA, 
    eula_models.EULAVersion, 
    form=EULAVersionForm, 
    extra=1
)
    
