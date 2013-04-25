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
    try:
        content = models.ContentBlock.permitted.get(slug=slug)
    except  models.ContentBlock.DoesNotExist:
        content = None
    
    return {'content': content,
            'user': context['request'].user,
            'slug': slug}