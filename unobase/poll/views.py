'''
Created on 05 Mar 2013

@author: michael
'''
from django.views import generic as generic_views

from unobase import mixins as unobase_mixins
from unobase import utils as unobase_utils
from unobase.poll import utils as poll_utils

from preferences import preferences

class PollAnswer(generic_views.FormView):
    
    def get_initial(self):
        return {'poll': preferences.SitePreferences.active_poll}
    
    def form_valid(self, form):
        answers = form.save()
        
        return self.render_to_response(self.get_context_data(
            results=poll_utils.get_poll_percentages(
            preferences.SitePreferences.active_poll.answers.all())))