'''
Created on 31 May 2013

@author: euan
'''
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode
from django.conf import settings
from django.core.urlresolvers import reverse

from unobase.questionnaire import constants
from unobase.models import ContentModel, StateModel

class Questionnaire(ContentModel, StateModel):
    
    multiple_entries_permitted = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('id',)
        
    def absolute_url(self):
        return reverse('questionnaire_form', args=[self.slug])

class QuestionnaireQuestion(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, related_name='questions')
    question = models.CharField(max_length=128)
    type = models.SmallIntegerField(choices=constants.QUESTIONNAIRE_QUESTION_TYPES)
    options = models.ManyToManyField('QuestionnaireOption', 
                                     through='QuestionnaireQuestionOption')
    required = models.BooleanField(default=False)
    order = models.SmallIntegerField(default=0)
    
    class Meta:
        ordering = ('order',)
    
    def __unicode__(self):
        return smart_unicode(self.question)

class QuestionnaireOption(models.Model):
    title = models.CharField(max_length=64)
    
    def __unicode__(self):
        return smart_unicode(self.title)

class QuestionnaireQuestionOption(models.Model):
    question = models.ForeignKey(QuestionnaireQuestion, related_name='ordered_options')
    option = models.ForeignKey(QuestionnaireOption)
    order = models.SmallIntegerField(default=0)
    
    class Meta:
        ordering = ('order',)
    
    def __unicode__(self):
        return smart_unicode(self.option.title)
    
class UserQuestionnaire(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    questionnaire = models.ForeignKey(Questionnaire)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modfied = models.DateTimeField(auto_now=True, editable=False)
    
class UserQuestionnaireAnswer(models.Model):
    user_questionnaire = models.ForeignKey(UserQuestionnaire, related_name='answers')
    question = models.ForeignKey(QuestionnaireQuestion)
    rating = models.SmallIntegerField(blank=True, null=True)
    options = models.ManyToManyField(QuestionnaireOption, blank=True, null=True)
    free_text = models.TextField(blank=True, null=True)
    file_upload = models.FileField(upload_to='questionnaires')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modfied = models.DateTimeField(auto_now=True, editable=False)
    
    class Meta:
        unique_together = (('user_questionnaire', 'question'),)
        
        