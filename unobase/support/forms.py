__author__ = 'michael'

from unobase.forms import Content
from unobase.support import models, constants

class Case(Content):
    class Meta(Content.Meta):
        model = models.Case
        fields = ['image', 'title',
                  'content', 'modified_by', 'created_by',
                  'tags', 'type', 'reason', 'priority']