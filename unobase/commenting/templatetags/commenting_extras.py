'''
Created on 27 Mar 2013

@author: euan
'''
from django import template

from unobase.commenting import models

register = template.Library()

@register.inclusion_tag('commenting/inclusion_tags/comment_replies.html')
def comment_replies(comment_pk):
    return {'object_list' : models.CustomComment.objects.get(pk=comment_pk).replies.all() }