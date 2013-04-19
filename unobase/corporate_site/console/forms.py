'''
Created on 10 Jan 2013

@author: euan
'''
from django import forms
from django.db.models import Q

from unobase.forms import Content
from unobase.calendar.forms import EventForm

from unobase.corporate_site import models
from unobase.corporate_site.console import fields

from ckeditor.widgets import CKEditorWidget

class ExistingImageMixin(object):
    
    def __init__(self, *args, **kwargs):
        super(ExistingImageMixin, self).__init__(*args, **kwargs)

        if self.fields['existing_image']._queryset:
            self.existing_images = True
        else:
            self.existing_images = False

    def save(self, *args, **kwargs):
        obj = super(ExistingImageMixin, self).save(*args, **kwargs)

        if self.cleaned_data['image_choice'] == 'existing':
            if self.cleaned_data['existing_image'] is not None:
                obj.image = self.cleaned_data['existing_image'].image
                obj.save()

        return obj
    

class Event(Content, ExistingImageMixin):
    image_choice = forms.ChoiceField(choices=(('new', 'new'), ('existing', 'existing')))
    existing_image = fields.ImageModelChoiceField(required=False,
        queryset=models.Event.objects.filter(~Q(image=None)).only('image', 'image_name').distinct())
    
    class Meta(Content.Meta):
        model = models.Event
        fields = Content.Meta.fields + ['venue', 'start', 'end', 'repeat', 'repeat_until', 'external_link', 'image_name', 'state']
        
class MediaCoverage(Content, ExistingImageMixin):
    image_choice = forms.ChoiceField(choices=(('new', 'new'), ('existing', 'existing')))
    existing_image = fields.ImageModelChoiceField(required=False,
        queryset=models.MediaCoverage.objects.filter(~Q(image=None)).only('image', 'image_name').distinct())
    
    class Meta(Content.Meta):
        model = models.MediaCoverage
        fields = Content.Meta.fields + ['image_name', 'state', 'publish_date_time', 'external_link', 'pdf']


class News(ExistingImageMixin, Content):
    image_choice = forms.ChoiceField(choices=(('new', 'new'), ('existing', 'existing')))
    existing_image = fields.ImageModelChoiceField(required=False,
        queryset=models.News.objects.filter(~Q(image=None)).only('image', 'image_name').distinct())
    
    class Meta(Content.Meta):
        model = models.News
        fields = Content.Meta.fields + ['image_name', 'state', 'publish_date_time']
        
class Award(ExistingImageMixin, Content):
    image_choice = forms.ChoiceField(choices=(('new', 'new'), ('existing', 'existing')))
    existing_image = fields.ImageModelChoiceField(required=False,
        queryset=models.Award.objects.filter(~Q(image=None)).only('image', 'image_name').distinct())
    
    class Meta(Content.Meta):
        model = models.Award
        fields = Content.Meta.fields + ['image_name', 'state', 'publish_date_time']
        
class PressRelease(Content):
    
    class Meta(Content.Meta):
        model = models.PressRelease
        fields = Content.Meta.fields + ['state', 'publish_date_time']
        
class Vacancy(Content):
    
    class Meta(Content.Meta):
        model = models.Vacancy
        fields = Content.Meta.fields + ['state']
        
class Product(Content):
    
    class Meta(Content.Meta):
        model = models.Product
        fields = Content.Meta.fields + ['image_name', 'state', 'file']
        
class CompanyMember(Content):
    
    class Meta(Content.Meta):
        model = models.CompanyMember
        fields = Content.Meta.fields + ['state', 'is_leader', 'is_board_member', 
                                        'is_investor', 'job_title', 'image_name']
        
    def __init__(self, *args, **kwargs):
        super(CompanyMember, self).__init__(*args, **kwargs)
        
        self.fields['is_leader'].required = False
        self.fields['is_board_member'].required = False
        self.fields['is_investor'].required = False
        
class Leader(CompanyMember):
    
    def __init__(self, *args, **kwargs):
        super(Leader, self).__init__(*args, **kwargs)
    
        self.fields['is_leader'].initial = True
        self.fields['is_leader'].widget = forms.HiddenInput()
        
        self.fields['is_board_member'].widget = forms.HiddenInput()
        self.fields['is_investor'].widget = forms.HiddenInput()
        
class BoardMember(CompanyMember):
    
    def __init__(self, *args, **kwargs):
        super(BoardMember, self).__init__(*args, **kwargs)
    
        self.fields['is_board_member'].initial = True
        self.fields['is_board_member'].widget = forms.HiddenInput()
        
        self.fields['is_leader'].widget = forms.HiddenInput()
        self.fields['is_investor'].widget = forms.HiddenInput()
        
class Investor(CompanyMember):
    
    def __init__(self, *args, **kwargs):
        super(Investor, self).__init__(*args, **kwargs)
    
        self.fields['is_investor'].initial = True
        self.fields['is_investor'].widget = forms.HiddenInput()
        
        self.fields['is_board_member'].widget = forms.HiddenInput()
        self.fields['is_leader'].widget = forms.HiddenInput()