from django import forms

from unobase.forms import Content
from unobase.calendar import models

class EventForm(Content):
    
    class Meta(Content.Meta):
        model = models.Event
        
        fields = Content.Meta.fields + ['venue', 'start', 'end', 'repeat', 'repeat_until', 'external_link']