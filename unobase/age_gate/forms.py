'''
Created on 27 Mar 2013

@author: michael
'''
import datetime

from django import forms

from unobase.age_gate import settings


class AgeGateForm(forms.Form):
    location = forms.ChoiceField(choices=settings.AGE_GATE_LOCATION_CHOICES, required=False)
    birth_day = forms.ChoiceField(choices=[(i, i) for i in range(1, 32)])
    birth_month = forms.ChoiceField(choices=[(i, i) for i in range(1, 13)])
    birth_year = forms.ChoiceField(choices=[(i, i) for i in reversed(range((datetime.datetime.now() - datetime.timedelta(days=80*365)).year, 
                                                                    (datetime.datetime.now()).year+1))
                                            ])
    terms_accept = forms.BooleanField(required=False)
    next = forms.CharField(widget=forms.HiddenInput, required=False)
    
    def clean_terms_accept(self):
        if not self.cleaned_data['terms_accept']:
            raise forms.ValidationError('You must accept the terms to continue.')
        
        return self.cleaned_data['terms_accept']