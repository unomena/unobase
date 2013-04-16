__author__ = 'michael'

from django import template

from unobase import models as unobase_models

register = template.Library()

@register.inclusion_tag('blog/widgets/tag_cloud.html')
def tag_cloud(blog_slug):
    tags = unobase_models.TagModel.get_distinct_tags('blogentry')

    return {
        'blog_slug': blog_slug,
        'tags': tags
    }
