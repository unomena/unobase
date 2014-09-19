__author__ = 'michael'

from django import forms
from django.utils import timezone

from unobase import constants
from unobase.forms import Content, State
from unobase.forum import models

class ForumCategory(Content):
    class Meta(Content.Meta):
        model = models.ForumCategory
        fields = Content.Meta.fields + ['forum', 'state']

    def __init__(self, *args, **kwargs):
        super(ForumCategory, self).__init__(*args, **kwargs)

        self.forum = kwargs['initial'].get('forum')

        self.fields['state'].widget = forms.HiddenInput()
        self.fields['state'].initial = constants.STATE_PUBLISHED

        self.fields['forum'].widget = forms.HiddenInput()

        if self.forum is not None:
            self.fields['forum'].initial = self.forum

class ForumThread(Content):
    class Meta(Content.Meta):
        model = models.ForumThread
        fields = Content.Meta.fields + ['category', 'state', 'publish_date_time']

    def __init__(self, *args, **kwargs):
        super(ForumThread, self).__init__(*args, **kwargs)

        self.category = kwargs['initial'].get('category')

        self.fields['state'].widget = forms.HiddenInput()
        self.fields['state'].initial = constants.STATE_PUBLISHED

        self.fields['category'].widget = forms.HiddenInput()

        if self.category is not None:
            self.fields['category'].initial = self.category

    def save(self, *args, **kwargs):
        commit = kwargs.pop('commit', True)
        
        instance = super(ForumThread, self).save(*args, commit=False, **kwargs)
        
        if self.cleaned_data['publish_date_time'] > timezone.now():
            instance.state = constants.STATE_UNPUBLISHED
        
        if commit:
            instance.save()
        
        return instance

class ForumPost(Content):
    class Meta(Content.Meta):
        model = models.ForumPost
        fields = Content.Meta.fields + ['thread', 'state']

    def __init__(self, *args, **kwargs):
        super(ForumPost, self).__init__(*args, **kwargs)

        self.thread = kwargs['initial'].get('thread')

        self.fields['title'].required = True
        self.fields['content'].required = True

        self.fields['state'].widget = forms.HiddenInput()
        self.fields['state'].initial = constants.STATE_PUBLISHED

        self.fields['thread'].widget = forms.HiddenInput()

        if self.thread is not None:
            self.fields['thread'].initial = self.thread