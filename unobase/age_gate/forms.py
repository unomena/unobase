'''
Created on 27 Mar 2013

@author: michael
'''
from django import forms
import datetime

class AgeGateForm(forms.Form):
    location = forms.ChoiceField(choices=(('Nigeria', 'Nigeria'),), required=False)
    birth_day = forms.ChoiceField(choices=[(i, i) for i in range(1, 32)])
    birth_month = forms.ChoiceField(choices=[(i, i) for i in range(1, 13)])
    birth_year = forms.ChoiceField(choices=[(i, i) for i in range((datetime.datetime.now() - datetime.timedelta(days=73*365)).year, 
                                                                  (datetime.datetime.now() - datetime.timedelta(days=17*365)).year)])
    terms_accept = forms.BooleanField(required=False)
    next = forms.CharField(widget=forms.HiddenInput, required=False)
    
    def clean_terms_accept(self):
        if not self.cleaned_data['terms_accept']:
            raise forms.ValidationError('You must accept the terms to continue.')
        
        return self.cleaned_data['terms_accept']