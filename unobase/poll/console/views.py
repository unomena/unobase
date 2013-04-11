'''
Created on 05 Mar 2013

@author: michael
'''
from django.views import generic as generic_views
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpResponseRedirect

from unobase import mixins as unobase_mixins
from unobase import views as unobase_views
from unobase import constants as unobase_constants

from unobase.poll import models as poll_models
from unobase.poll.console import forms

class AdminMixin(unobase_mixins.ConsoleUserRequiredMixin):
    raise_exception = False

class PollAnswerFormSetMixin(object):
    
    def get_context_data(self, **kwargs):
        context = super(PollAnswerFormSetMixin, self).get_context_data(**kwargs)
        
        if self.request.method == 'POST':
            context['formset'] = forms.PollAnswerFormSet(self.request.POST, instance=self.object)
        else:
            context['formset'] = forms.PollAnswerFormSet(instance=self.object)
            
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        
        formset = context['formset']
        
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return HttpResponseRedirect(self.get_success_url())
        
        return self.render_to_response(self.get_context_data(form=form))

class PollCreate(AdminMixin, PollAnswerFormSetMixin, generic_views.CreateView):
    
    def get_success_url(self):
        return reverse('console_poll_detail', args=(self.object.pk,))

class PollUpdate(AdminMixin, PollAnswerFormSetMixin, generic_views.UpdateView):
    
    def get_success_url(self):
        return reverse('console_poll_detail', args=(self.object.pk,))

    def get_queryset(self):
        return poll_models.PollQuestion.objects.all()

class PollDetail(AdminMixin, generic_views.DetailView):

    def get_object(self):
        return get_object_or_404(poll_models.PollQuestion, pk=self.kwargs['pk'])

class PollDelete(AdminMixin, generic_views.DeleteView):
    
    def get_success_url(self):
        return reverse('console_poll_list')

    def get_queryset(self):
        return poll_models.PollQuestion.objects.all()

class PollList(AdminMixin, generic_views.ListView):
    
    def get_queryset(self):
        return poll_models.PollQuestion.objects.all()
    
    