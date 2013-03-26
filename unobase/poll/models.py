'''
Created on 26 Mar 2013

@author: michael
'''
from django.db import models

class PollQuestion(models.Model):
    question = models.CharField(max_length=1024)
    multiple_choice = models.BooleanField(default=False)
    
    def __unicode__(self):
        return u'%s' % self.question
    
class PollAnswer(models.Model):
    poll = models.ForeignKey(PollQuestion, related_name='answers')
    
    answer = models.CharField(max_length=1024)
    vote_count = models.PositiveIntegerField(default=0)
    
    def __unicode__(self):
        return u'%s' % self.answer