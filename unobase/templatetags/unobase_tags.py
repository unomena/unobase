from copy import copy

from django import template
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType

from unobase import models, utils
from unobase.commenting import models as commenting_models

register = template.Library()

@register.inclusion_tag('unobase/inclusion_tags/tag_list.html', takes_context=True)
def tag_list(context, obj):
    context = copy(context)
    tags = list(obj.tags.all())

    if context['user'].is_authenticated() and context['user'].is_staff:
        tags.append({'title': '+'})
    context.update({'object': obj.as_leaf_class(),
                    'content_type_id': ContentType.objects.get_for_model(obj).id,
                    'tags': tags,
                    })

    return context


@register.inclusion_tag('unobase/inclusion_tags/pagination.html', takes_context=True)
def pagination(context, page_obj):
    context = copy(context)
    context.update({'page_obj': page_obj,
                    'paginator': getattr(page_obj, 'paginator', None),
                    })
    return context

@register.tag
def smart_query_string(parser, token):
    """
    Outputs current GET query string with additions appended.
    Additions are provided in token pairs.
    """
    args = token.split_contents()
    additions = args[1:]

    addition_pairs = []
    while additions:
        addition_pairs.append(additions[0:2])
        additions = additions[2:]

    return SmartQueryStringNode(addition_pairs)


class SmartQueryStringNode(template.Node):
    def __init__(self, addition_pairs):
        self.addition_pairs = []
        for key, value in addition_pairs:
            self.addition_pairs.append((template.Variable(key) if key \
                    else None, template.Variable(value) if value else None))

    def render(self, context):
        q = dict([(k, v) for k, v in context['request'].GET.items()])
        for key, value in self.addition_pairs:
            if key:
                key = key.resolve(context)
                if value:
                    value = value.resolve(context)
                    q[key] = value
                else:
                    q.pop(key, None)
            qs = '&'.join(['%s=%s' % (k, v) for k, v in q.items()])
        return '?' + qs if len(q) else ''
