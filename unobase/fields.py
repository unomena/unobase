'''
Created on 23 Apr 2013

@author: michael
'''
from django import forms
from django.db import models
import uuid

class UUIDField(models.CharField) :

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', 64 )
        kwargs['blank'] = True
        models.CharField.__init__(self, *args, **kwargs)

    def pre_save(self, model_instance, add):
        if add :
            value = str(uuid.uuid4())
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super(models.CharField, self).pre_save(model_instance, add)


class RedactorTextField(models.TextField):
    def __init__(self, *args, **kwargs):
        super(RedactorTextField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': RedactorTextFormField
        }
        defaults.update(kwargs)
        return super(RedactorTextField, self).formfield(**defaults)


class RedactorTextFormField(forms.fields.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.update({'widget': forms.Textarea()})
        kwargs['widget'].attrs.update({
                    'class': 'redactor'
                })
        print kwargs['widget'].attrs
        super(RedactorTextFormField, self).__init__(*args, **kwargs)

try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^unobase\.fields\.RedactorTextField"])
except:
    pass
