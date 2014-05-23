'''
Created on 31 May 2013

@author: euan
'''

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views import generic as generic_views

from unobase import constants as unobase_constants
from unobase.questionnaire import models

class Questionnaire(generic_views.FormView):
    
    def get_questionnaire(self):
        return get_object_or_404(models.Questionnaire, 
                                 slug=self.kwargs['slug'], 
                                 state=unobase_constants.STATE_PUBLISHED)
    
    def get_form_kwargs(self):
        kwargs = super(Questionnaire, self).get_form_kwargs()
        kwargs.update({'questionnaire' : self.questionnaire,
                       'user' : self.request.user
                       })
        return kwargs
    
    def form_valid(self, form):
        form.save()
        return generic_views.FormView.form_valid(self, form)
    
    def can_enter(self):
        if self.questionnaire.multiple_entries_permitted:
            return True
        user = self.request.user
        if user.is_authenticated() and models.UserQuestionnaire.objects.filter(questionnaire=self.questionnaire,
                                                                               user__id=user.id).count() > 0:
            return False
        return True
        
    
    def get(self, request, *args, **kwargs):
        self.questionnaire = self.get_questionnaire()
        if self.can_enter():
            return generic_views.FormView.get(self, request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('questionnaire_already_completed', args=[self.questionnaire.slug]))

    def post(self, request, *args, **kwargs):
        self.questionnaire = self.get_questionnaire()
        if self.can_enter():
            return generic_views.FormView.post(self, request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('questionnaire_already_completed', args=[self.questionnaire.slug]))
        
    
