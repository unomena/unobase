'''
Created on 27 Mar 2013

@author: euan
'''
from copy import copy

from django import template
from django.contrib.contenttypes.models import ContentType

from unobase.commenting import models, utils

register = template.Library()

@register.inclusion_tag('commenting/inclusion_tags/comment_replies.html')
def comment_replies(comment_pk):
    return {'object_list' : models.CustomComment.objects.get(pk=comment_pk).replies.all() }

@register.inclusion_tag('unobase/inclusion_tags/comment_pagination_ajax.html', takes_context=True)
def comment_pagination_ajax(context, page_obj):
    context = copy(context)
    context.update({'page_obj': page_obj,
                    'paginator': getattr(page_obj, 'paginator', None),
                    })
    return context

@register.simple_tag(takes_context=True)
def get_comment_count(context, obj):
    return utils.get_permitted_comments(queryset=models.CustomComment.objects.filter(content_type=ContentType.objects.get_for_model(obj),
                                                                                     object_pk=obj.id,
                                                                                     report_count__lt=3),
                                                                                     user=context['user']).count()    
@register.simple_tag(takes_context=True)
def get_comment_count_pluralize(context, obj):
    
    if get_comment_count(context, obj) == 1:
        return ''
    else:
        return 's'