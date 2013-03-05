'''
Created on 05 Mar 2013

@author: michael
'''
from django.views import generic as generic_views

class AdminMixin(object):
    pass

class Console(AdminMixin, generic_views.TemplateView):
    pass