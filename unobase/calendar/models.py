'''
Created on 22 Mar 2013

@author: euan
'''
from datetime import datetime, timedelta

from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

from ckeditor.fields import RichTextField
from unobase.models import ContentModel

class Calendar(ContentModel):

    class Meta:
        verbose_name = "Calendar"
        verbose_name_plural = "Calendars"

class Venue(models.Model):
    name = models.CharField(max_length=255, help_text='A short descriptive name.')
    address = models.CharField(max_length=512, help_text='Physical venue address.')

    def __unicode__(self):
        return self.name

class Event(ContentModel):
    
    parent_ptr = models.OneToOneField(
        ContentModel,
        primary_key=True,
        parent_link=True,
        related_name='+'
    )
    
    venue = models.ForeignKey(Venue, blank=True, null=True,
                              help_text='Venue where the event will take place.',
                              )
    start = models.DateTimeField(db_index=True)
    end = models.DateField(db_index=True)
    
    repeat = models.CharField(
        max_length=64,
        choices=(
            ('does_not_repeat', 'Does Not Repeat'),
            ('daily', 'Daily'),
            ('weekdays', 'Weekdays'),
            ('weekends', 'Weekends'),
            ('weekly', 'Weekly'),
            ('monthly_by_day_of_month', 'Monthly By Day Of Month'),
        ),
        default='does_not_repeat',
    )
    repeat_until = models.DateField(blank=True, null=True)
    external_link = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="The url of the event's external webpage, if there is one."
    )
    
    class Meta:
        ordering = ('start', )
        
    @property
    def duration(self):
        return self.end - self.start

    @property
    def next(self):
        now = timezone.now()
        # if the first iteration of the event has not yet ended
        if now < self.end:
            return self.start
        # calculate next repeat of event
        elif self.repeat != 'does_not_repeat' and \
                (self.repeat_until is None or now.date() <= self.repeat_until):
            if now.timetz() < self.end.timetz() or self.duration > \
                    (self.start.replace(hour=23, minute=59, second=59,
                    microsecond=999999) - self.start):
                date = self._next_repeat(now.date())
            else:
                date = self._next_repeat(now.date() + timedelta(days=1))

            if self.repeat_until is None or date <= self.repeat_until:
                return datetime.combine(date, self.start.timetz())
        return None
    
    @property
    def last(self):
        if self.repeat == 'does_not_repeat':
            return self.start
        else:
            return datetime.combine(self.repeat_until, self.start.timetz())
        