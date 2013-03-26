__author__ = 'michael'

from django import template

from unobase.poll import forms

register = template.Library()

@register.inclusion_tag('poll/widgets/poll.html')
def poll(blog_slug):
    
    return {
        'form': forms.PollAnswerForm
    }
