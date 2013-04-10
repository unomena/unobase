from copy import copy

from django import forms
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site

from ckeditor.widgets import CKEditorWidget

import models
import constants

from tagging import models as tagging_models

class State(forms.ModelForm):
    
    class Meta:
        model = models.StateModel
        
        fields = ['state', 'publish_date_time', 'retract_date_time']

class Content(forms.ModelForm):
    comma_seperated_tags = forms.CharField(max_length=512, required=False)
    default_image = forms.BooleanField(initial=False, required=False)

    class Meta:
        model = models.ContentModel

        fields = ['image', 'title','content', 'modified_by', 'created_by', 'tags']

        widgets = {'image' : forms.FileInput,
                   'modified_by' : forms.HiddenInput,
                   'created_by' : forms.HiddenInput,
                   'content': CKEditorWidget
        }

    def __init__(self, *args, **kwargs):
        super(Content, self).__init__(*args, **kwargs)

        self.object = kwargs['instance']

        self.fields['image'].required = False
        self.fields['tags'].widget.attrs.update({'class':'chozen'})

        if kwargs['initial'].has_key('user'):
            self.fields['modified_by'].initial = kwargs['initial']['user']

            if not self.object:
                self.fields['created_by'].initial = kwargs['initial']['user']

        if self.object:
            tag_list = ', '.join([tag.title for tag in self.object.tags.all()])
            self.fields['comma_seperated_tags'].initial = tag_list
        else:
            self.fields['comma_seperated_tags'].initial = ''

    def save(self, *args, **kwargs):

        obj = super(Content, self).save(*args, **kwargs)
        if self.cleaned_data.has_key('default_image') and self.cleaned_data['default_image']:
            obj.image = None
            obj.save()

        for tag in obj.tags.all():
            obj.tags.remove(tag)

        for tag_title in self.cleaned_data['comma_seperated_tags'].split(','):
            if tag_title.strip():
                tag, _ = tagging_models.Tag.objects.get_or_create(title=tag_title.strip())
                obj.tags.add(tag)

        return obj