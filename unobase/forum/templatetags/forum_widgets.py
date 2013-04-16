__author__ = 'michael'

from django import template

from unobase import models as unobase_models

register = template.Library()

@register.inclusion_tag('forum/widgets/tag_cloud.html')
def tag_cloud(forum_slug):
    tags = unobase_models.TagModel.get_distinct_tags('forumthread')

    return {
        'forum_slug': forum_slug,
        'tags': tags
    }
