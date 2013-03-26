'''
Created on 05 Mar 2013

@author: michael
'''
from django.views import generic as generic_views

from unobase import mixins as unobase_mixins

from preferences import preferences

class PollAnswer(generic_views.FormView):
    
    def get_initial(self):
        return {'poll': preferences.SitePreferences.active_poll}