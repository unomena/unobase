__author__ = 'michael'

from django import forms

class OutboundEmailFilter(forms.Form):
    subject = forms.CharField(required=False)
    name = forms.CharField(required=False)
    email = forms.CharField(required=False)