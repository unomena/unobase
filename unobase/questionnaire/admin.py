'''
Created on 31 May 2013

@author: euan
'''
from django.contrib import admin

from unobase.admin import ContentModelAdmin
from unobase.questionnaire import models
 
class QuestionnaireOptionInline(admin.StackedInline):
    model = models.QuestionnaireQuestionOption
 
class QuestionnaireQuestionAdmin(admin.ModelAdmin):
    list_display = ('questionnaire', 'question', 'type')
    list_filter = ('question', 'questionnaire', 'type')
    inlines = [QuestionnaireOptionInline,]
     
class UserQuestionnaireAnswerInline(admin.StackedInline):
    model = models.UserQuestionnaireAnswer
 
class UserQuestionnaireAdmin(admin.ModelAdmin):
    list_display = ('user', 'questionnaire', 'created')
    list_filter = ('user', 'questionnaire', 'created')
    inlines = [UserQuestionnaireAnswerInline,]
 
class QuestionnaireQuestionInline(admin.StackedInline):
    model = models.QuestionnaireQuestion
     
class QuestionnaireAdmin(ContentModelAdmin):
    list_display = ('title', 'absolute_url', 'multiple_entries_permitted')
    inlines = [QuestionnaireQuestionInline,]
 
admin.site.register(models.Questionnaire, QuestionnaireAdmin)
admin.site.register(models.QuestionnaireQuestion, QuestionnaireQuestionAdmin)
admin.site.register(models.QuestionnaireOption)
admin.site.register(models.UserQuestionnaire, UserQuestionnaireAdmin)
admin.site.register(models.UserQuestionnaireAnswer)