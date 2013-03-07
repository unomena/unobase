'''
Created on 06 Mar 2013

@author: michael
'''
import urlparse

from django.views import generic as generic_views
from django.http import HttpResponse, HttpResponseRedirect

from unobase.eula import models

class SignEULA(generic_views.View):
    def get(self, request, *args, **kwargs):
        request.user.eula_accepted = models.EULA.objects.latest_eula()
        request.user.save()
        
        return HttpResponseRedirect(self.request.GET.get('next') or '/')
    
class EULA(generic_views.DetailView):
    def get_context_data(self, **kwargs):
        context = super(EULA, self).get_context_data(**kwargs)
        
        context['next_url'] = self.request.GET.get('next')
        
        return context
    
    def get_object(self):
        return models.EULA.objects.latest_eula
    
