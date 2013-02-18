__author__ = 'michael'

from django import template

from unobase import models as unobase_models

register = template.Library()

@register.inclusion_tag('blog/tags/tag_size.html')
def get_tag_size(tag):
    tag_size = unobase_models.TagModel.get_tag_ratio(tag, 'blogentry')

    return {'tag_size': tag_size}