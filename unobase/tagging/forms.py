__author__ = 'michael'

from django import forms

import models
from unobase import models as unobase_models

class BulkSelectedMixin(forms.Form):
    """
    Mixin form used for bulk actions, used to determine bulk selected users.
    """

    selected = forms.CharField(
        widget=forms.HiddenInput(),
    )

    def __new__(cls, *args, **kwargs):
        new_class = super(BulkSelectedMixin, cls).__new__(cls, *args, **kwargs)
        new_class._meta = getattr(new_class, 'Meta', None)
        return new_class

    def get_selected(self):
        ids = self.cleaned_data['selected']
        if ids:
            return self._meta.model.objects.filter(id__in=ids.split(','))
        return None

class BulkTagForm(BulkSelectedMixin):
    """
    Form used to bulk tag objects.
    """

    class Meta:
        model = unobase_models.TagModel

    tag_id = forms.IntegerField(required=False)

    tag = forms.CharField(
        required=False,
        initial='Create a new tag',
    )
    action = forms.CharField(
        required=False,
        widget=forms.HiddenInput()
    )

    def save(self, request, *args, **kwargs):
        objs = self.get_selected()
        tag_title = self.cleaned_data['tag'].lower()
        if self.cleaned_data['action'] == 'save':
            tag, created = models.Tag.objects.get_or_create(
                title=tag_title
            )
            old_tag = None
            if self.cleaned_data['tag_id']:
                old_tag = models.Tag.objects.get(pk=int(self.cleaned_data['tag_id']))

            for obj in objs:
                if old_tag:
                    obj.tags.remove(old_tag)
                obj.tags.add(tag)

        if self.cleaned_data['action'] == 'delete':
            try:
                tag = models.Tag.objects.get(title=tag_title)
            except models.Tag.DoesNotExist:
                return

            for obj in objs:
                obj.tags.remove(tag)