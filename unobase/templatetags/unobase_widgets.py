'''
Created on 15 Nov 2012

@author: euan
'''
from django import template
from django.shortcuts import get_object_or_404

from unobase import models, constants

register = template.Library()

@register.inclusion_tag('unobase/inclusion_tags/content_block.html', takes_context=True)
def content_block(context, slug):
    
    return {'content': get_object_or_404(models.ContentBlock, 
                                         state=constants.STATE_PUBLISHED, 
                                         slug=slug),
            'user': context['request'].user}