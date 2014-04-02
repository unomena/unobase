'''
Created on 05 Mar 2013

@author: michael
'''
from django.views import generic as generic_views
from django.http import HttpResponseRedirect
from django.conf import settings

class AgeGate(generic_views.FormView):
    
    def get_initial(self):
        return {'next': self.request.GET.get('next')}
    
    def form_valid(self, form):
        form.save(self.request)
        
        return HttpResponseRedirect(self.request.POST.get('next') or '/')