__author__ = 'michael'

from django.views import generic as generic_views
from django.shortcuts import render_to_response
from django.template import RequestContext

import forms

from unobase import models as unobase_models

class TagAjax(generic_views.FormView):
    form_class = forms.BulkTagForm

    def form_valid(self, form):
        form.save(self.request)
        # Return tag listing for client side HTML replace.

        return render_to_response(
            self.template_name,
            {'object': unobase_models.TagModel.objects.get(id=form.cleaned_data['selected'])},
            context_instance=RequestContext(self.request)
        )