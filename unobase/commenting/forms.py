__author__ = 'michael'

from copy import copy

from django import forms
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site

import models
import constants

class CustomCommentForm(forms.ModelForm):

    class Meta:
        model = models.CustomComment

        widgets = {'user' : forms.HiddenInput,
                   'content_type' : forms.HiddenInput,
                   'object_pk' : forms.HiddenInput,
                   'submit_date' : forms.HiddenInput,
                   'site' : forms.HiddenInput,
                   'ip_address' : forms.HiddenInput,
                   'is_public' : forms.HiddenInput,
                   'comment' : forms.Textarea,
                   'in_reply_to' : forms.HiddenInput,
                   }

    def __init__(self, *args, **kwargs):
        super(CustomCommentForm, self).__init__(*args, **kwargs)

        self.initial = kwargs.pop('initial')
        self.object = self.initial.pop('object')
        self.object_content_type = ContentType.objects.get_for_model(self.object)
        self.user = self.initial.pop('user')
        self.ip_address = self.initial.pop('ip_address')

        self.fields['user'].initial = self.user
        self.fields['content_type'].initial = self.object_content_type
        self.fields['object_pk'].initial = self.object.id
        self.fields['submit_date'].required = False
        self.fields['site'].initial = Site.objects.get_current()
        self.fields['ip_address'].initial = self.ip_address
        self.fields['is_public'].initial = True
        
        self.fields['visible_to'].widget = forms.Select(choices=constants.COMMENT_VISIBLE_TO_CHOICES if self.user.is_superuser else constants.COMMENT_VISIBLE_TO_CHOICES_STAFF)
        if not self.user.is_staff or not self.user.is_superuser:
            self.fields['visible_to'].widget = forms.HiddenInput()
            
        self.fields['comment'].widget.attrs.update({'class':'commentbox'})

    def clean(self):
        cleaned_data = copy(self.cleaned_data)

        if cleaned_data.has_key('posted_on_behalf_by') and cleaned_data['posted_on_behalf_by']:
            cleaned_data['user'] = cleaned_data['posted_on_behalf_by']
            cleaned_data['posted_on_behalf_by'] = self.user

        return cleaned_data
    