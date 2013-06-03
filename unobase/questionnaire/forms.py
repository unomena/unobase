'''
Created on 31 May 2013

@author: euan
'''
from django import forms
from django.contrib.auth import get_user_model

from unobase.questionnaire import constants, models

class Questionnaire(forms.Form):
    
    id = 'frmQuestionnaire'
    
    questionnaire = forms.ModelChoiceField(queryset=models.Questionnaire.permitted.all())
    user = forms.ModelChoiceField(queryset=get_user_model().objects.all(), required=False)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(required=False)
    
    def __init_rating__(self, question):
        self.base_fields.update({'question_%d' % question.id : forms.ChoiceField(label=question.question,
                                                                                 choices=((i+1,i+1) for i in range(10)))})
    
    def __init_radio__(self, question):
        options = question.ordered_options.all()
        if options:
            self.base_fields.update({'question_%d' % question.id : forms.ModelChoiceField(label=question.question,
                                                                                          widget=forms.RadioSelect(),
                                                                                          queryset=options,
                                                                                          initial=options[0])})
        else:
            raise Exception('Question of type radio select has no options configured.')
        
    def __init_checkbox__(self, question):
        self.base_fields.update({'question_%d' % question.id : forms.ModelMultipleChoiceField(label=question.question,
                                                                                              widget=forms.CheckboxSelectMultiple(),
                                                                                              queryset=question.ordered_options.all())})
        
    def __init_freetext__(self, question):
        self.base_fields.update({'question_%d' % question.id : forms.CharField(label=question.question)})
    
    def __init_freetext_blob__(self, question):
        self.base_fields.update({'question_%d' % question.id : forms.TextField(label=question.question)})
    
    def __init_file__(self, question):
        self.base_fields.update({'question_%d' % question.id : forms.FileField(label=question.question,
                                                                               widget=forms.FileInput)})
    
    def __init__(self, *args, **kwargs):
        
        self.questionnaire_obj = kwargs.pop('questionnaire')
        self.user_obj = kwargs.pop('user')
        
        for field_name in self.base_fields.keys():
            if field_name.startswith('question_'):
                self.base_fields.pop(field_name)
        
        for question in self.questionnaire_obj.questions.all():
            
            if question.type == constants.QUESTIONNAIRE_QUESTION_TYPE_RATING:
                self.__init_rating__(question)
            if question.type == constants.QUESTIONNAIRE_QUESTION_TYPE_RADIO:
                self.__init_radio__(question)
            if question.type == constants.QUESTIONNAIRE_QUESTION_TYPE_CHECKBOX:
                self.__init_checkbox__(question)
            if question.type == constants.QUESTIONNAIRE_QUESTION_TYPE_FREETEXT:
                self.__init_freetext__(question)
            if question.type == constants.QUESTIONNAIRE_QUESTION_TYPE_FREETEXT_BLOB:
                self.__init_freetext_blob__(question)
            if question.type == constants.QUESTIONNAIRE_QUESTION_TYPE_FILE:
                self.__init_file__(question)

            self.base_fields['question_%d' % question.id].required = question.required
        
        super(Questionnaire, self).__init__(*args, **kwargs)
        
        self.fields['questionnaire'].widget = forms.HiddenInput()
        self.fields['questionnaire'].initial = self.questionnaire_obj
        
        self.fields['user'].widget = forms.HiddenInput()
        
        if self.user_obj.is_authenticated():
            self.fields['first_name'].initial = self.user_obj.first_name
            self.fields['last_name'].initial = self.user_obj.last_name
            self.fields['email'].initial = self.user_obj.email
            self.fields['user'].initial = self.user_obj
        else:
            self.fields['first_name'].required = True
            self.fields['last_name'].required = True
            self.fields['email'].required = True
            
    def clean_email(self):
        email = self.cleaned_data['email']
        if self.questionnaire_obj.multiple_entries_permitted:
            return email
        if models.UserQuestionnaire.objects.filter(questionnaire=self.questionnaire_obj,
                                                   email=email).count() > 0:
            raise forms.ValidationError('You have already entered. You can only enter once.')
        else:
            return email
        
    def __save_rating__(self, question, user_questionnaire):
        models.UserQuestionnaireAnswer.objects.create(user_questionnaire=user_questionnaire,
                                                  question=question,
                                                  rating=self.cleaned_data['question_%d' % question.id]
                                                  )
    
    def __save_radio__(self, question, user_questionnaire):
        user_questionnaire_answer = models.UserQuestionnaireAnswer.objects.create(user_questionnaire=user_questionnaire,
                                                                          question=question,
                                                                          )
        user_questionnaire_answer.options.add(self.cleaned_data['question_%d' % question.id].option)
    
    def __save_checkbox__(self, question, user_questionnaire):
        user_questionnaire_answer = models.UserQuestionnaireAnswer.objects.create(user_questionnaire=user_questionnaire,
                                                                          question=question,
                                                                          )
        for option in self.cleaned_data['question_%d' % question.id]:
            user_questionnaire_answer.options.add(option.option)
    
    def __save_freetext__(self, question, user_questionnaire):
        models.UserQuestionnaireAnswer.objects.create(user_questionnaire=user_questionnaire,
                                                      question=question,
                                                      free_text=self.cleaned_data['question_%d' % question.id]
                                                      )
    
    def __save_file__(self, question, user_questionnaire):
        models.UserQuestionnaireAnswer.objects.create(user_questionnaire=user_questionnaire,
                                                      question=question,
                                                      file_upload=self.cleaned_data['question_%d' % question.id]
                                                      )
        
    def save(self):
        
        if self.user_obj.is_authenticated():
            user_questionnaire = models.UserQuestionnaire.objects.create(user=self.user_obj, 
                                                                         questionnaire=self.questionnaire_obj)
        else:
            user_questionnaire = models.UserQuestionnaire.objects.create(first_name=self.cleaned_data['first_name'], 
                                                                         last_name=self.cleaned_data['last_name'], 
                                                                         email=self.cleaned_data['email'], 
                                                                         questionnaire=self.questionnaire_obj)
        
        for question in self.questionnaire_obj.questions.all():
            
            if question.type == constants.QUESTIONNAIRE_QUESTION_TYPE_RATING:
                self.__save_rating__(question, user_questionnaire)
            if question.type == constants.QUESTIONNAIRE_QUESTION_TYPE_RADIO:
                self.__save_radio__(question, user_questionnaire)
            if question.type == constants.QUESTIONNAIRE_QUESTION_TYPE_CHECKBOX:
                self.__save_checkbox__(question, user_questionnaire)
            if question.type in [constants.QUESTIONNAIRE_QUESTION_TYPE_FREETEXT,
                                 constants.QUESTIONNAIRE_QUESTION_TYPE_FREETEXT]:
                self.__save_freetext__(question, user_questionnaire)
            if question.type == constants.QUESTIONNAIRE_QUESTION_TYPE_FILE:
                self.__save_file__(question, user_questionnaire)
                
                
        return user_questionnaire
