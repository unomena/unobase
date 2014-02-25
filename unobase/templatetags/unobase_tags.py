from copy import copy

from django import template
from django.template import loader, Node, Variable
from django.utils.encoding import smart_str, smart_unicode
from django.template.defaulttags import url
from django.template import VariableDoesNotExist
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext as _

from unobase import models, utils
from unobase.commenting import models as commenting_models

register = template.Library()

@register.filter
def letterify(value):
    return str(unichr(65 + value))

@register.tag
def breadcrumb(parser, token):
    """
    Renders the breadcrumb.
    Examples:
        {% breadcrumb "Title of breadcrumb" url_var %}
        {% breadcrumb context_var  url_var %}
        {% breadcrumb "Just the title" %}
        {% breadcrumb just_context_var %}

    Parameters:
    -First parameter is the title of the crumb,
    -Second (optional) parameter is the url variable to link to, produced by url tag, i.e.:
        {% url person_detail object.id as person_url %}
        then:
        {% breadcrumb person.name person_url %}

    @author Andriy Drozdyuk
    """
    return BreadcrumbNode(token.split_contents()[1:])


@register.tag
def breadcrumb_url(parser, token):
    """
    Same as breadcrumb
    but instead of url context variable takes in all the
    arguments URL tag takes.
        {% breadcrumb "Title of breadcrumb" person_detail person.id %}
        {% breadcrumb person.name person_detail person.id %}
    """

    bits = token.split_contents()
    if len(bits)==2:
        return breadcrumb(parser, token)

    # Extract our extra title parameter
    title = bits.pop(1)
    token.contents = ' '.join(bits)

    url_node = url(parser, token)

    return UrlBreadcrumbNode(title, url_node)


class BreadcrumbNode(Node):
    def __init__(self, vars):
        """
        First var is title, second var is url context variable
        """
        self.vars = map(Variable,vars)

    def render(self, context):
        title = self.vars[0].var

        if title.find("'")==-1 and title.find('"')==-1:
            try:
                val = self.vars[0]
                title = val.resolve(context)
            except:
                title = ''

        else:
            title=title.strip("'").strip('"')
            title=_(smart_unicode(title))

        url = None

        if len(self.vars)>1:
            val = self.vars[1]
            try:
                url = val.resolve(context)
            except VariableDoesNotExist:
                print 'URL does not exist', val
                url = None

        return create_crumb(title, url)


class UrlBreadcrumbNode(Node):
    def __init__(self, title, url_node):
        self.title = Variable(title)
        self.url_node = url_node

    def render(self, context):
        title = self.title.var

        if title.find("'")==-1 and title.find('"')==-1:
            try:
                val = self.title
                title = val.resolve(context)
            except:
                title = ''
        else:
            title=title.strip("'").strip('"')
            title=smart_unicode(title)

        url = self.url_node.render(context)
        return create_crumb(title, url)


def create_crumb(title, url=None):
    """
    Helper function
    """
    crumb = '<img src="/static/breadcrumbs/img/crumb.png" />'
    if url:
        crumb = "%s<a href='%s'>%s</a>" % (crumb, url, title)
    else:
        crumb = "%s&nbsp;%s" % (crumb, title)

    return crumb

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
