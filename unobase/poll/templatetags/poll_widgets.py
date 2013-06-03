__author__ = 'michael'

from django import template

from preferences import preferences

from unobase.poll import forms, utils

register = template.Library()

@register.inclusion_tag('poll/widgets/poll.html')
def poll():
    poll = preferences.SitePreferences.active_poll
    
    if not poll:
        return {}
    
    return {
        'form': forms.PollAnswerForm(initial={'poll': poll}),
        'results': utils.get_poll_percentages(poll.answers.all())
    }
