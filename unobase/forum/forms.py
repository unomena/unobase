__author__ = 'michael'

from django import forms

from unobase import constants
from unobase.forms import Content
from unobase.forum import models

class ForumCategory(Content):
    class Meta(Content.Meta):
        model = models.ForumCategory
        fields = Content.Meta.fields + ['forum']

    def __init__(self, *args, **kwargs):
        super(ForumCategory, self).__init__(*args, **kwargs)

        self.forum = kwargs['initial'].get('forum')

        self.fields['state'].widget = forms.HiddenInput()
        self.fields['state'].initial = constants.STATE_PUBLISHED

        self.fields['forum'].widget = forms.HiddenInput()

        if self.forum is not None:
            self.fields['forum'].initial = self.forum

    def save(self, *args, **kwargs):
        #self.cleaned_data['state'] =
        #self.cleaned_data['forum'] =
        return super(ForumCategory, self).save(*args, **kwargs)

class ForumThread(Content):
    class Meta(Content.Meta):
        model = models.ForumThread
        fields = Content.Meta.fields + ['category']

    def __init__(self, *args, **kwargs):
        super(ForumThread, self).__init__(*args, **kwargs)

        self.category = kwargs['initial'].get('category')

        self.fields['state'].widget = forms.HiddenInput()
        self.fields['state'].initial = constants.STATE_PUBLISHED

        self.fields['category'].widget = forms.HiddenInput()

        if self.category is not None:
            self.fields['category'].initial = self.category

    def save(self, *args, **kwargs):
        #self.cleaned_data['state'] =
        #self.cleaned_data['category'] =
        return super(ForumThread, self).save(*args, **kwargs)

class ForumPost(Content):
    class Meta(Content.Meta):
        model = models.ForumPost
        fields = Content.Meta.fields + ['thread']

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

    def save(self, *args, **kwargs):
        #self.cleaned_data['state'] =
        #self.cleaned_data['category'] =
        return super(ForumPost, self).save(*args, **kwargs)