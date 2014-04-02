'''
Created on 27 Mar 2013

@author: michael
'''
import datetime

from django import forms
from django.conf import settings

class AgeGateForm(forms.Form):
    location = forms.ChoiceField(choices=(('Nigeria', 'Nigeria'),), required=False)
    birth_day = forms.ChoiceField(choices=[(i, i) for i in range(1, 32)])
    birth_month = forms.ChoiceField(choices=[(i, i) for i in range(1, 13)])
    birth_year = forms.ChoiceField(choices=[(i, i) for i in reversed(
        range((datetime.datetime.now() - datetime.timedelta(days=73*365)).year, 
        datetime.datetime.now().year+1))])
    terms_accept = forms.BooleanField(required=False)
    next = forms.CharField(widget=forms.HiddenInput)
    
    def clean_terms_accept(self):
        if not self.cleaned_data['terms_accept']:
            raise forms.ValidationError('You must accept the terms to continue')
        
        return self.cleaned_data['terms_accept']
    
    def save(self, request):
        request.session['user_date_of_birth'] = datetime.datetime(
            int(self.cleaned_data['birth_year']), 
            int(self.cleaned_data['birth_month']), 
            int(self.cleaned_data['birth_day'])
        )
        
        age = settings.COUNTRY_LEGAL_AGES[self.cleaned_data['location']]
        request.session['country_date_of_birth_required'] = \
            datetime.datetime.now() - datetime.timedelta(days=age*365)