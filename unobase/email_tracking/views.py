__author__ = 'michael'

from django.views import generic as generic_views
from django.shortcuts import get_object_or_404
from django.conf import settings

from unobase import views as unobase_views
from unobase import mixins as unobase_mixins
from unobase.email_tracking import models, forms

class OutboundEmailList(unobase_mixins.ConsoleUserRequiredMixin, unobase_mixins.FilterMixin, generic_views.ListView):

    raise_exception = True

    allowed_filters = {
        'subject': 'subject__icontains',
        'name': 'user__first_name__icontains',
        'email': 'user__email__icontains'
    }

    def get_context_data(self, **kwargs):
        context = super(OutboundEmailList, self).get_context_data(**kwargs)
        context['filter_form'] = forms.OutboundEmailFilter(self.request.GET)
        return context

    def get_queryset(self):
        return models.OutboundEmail.objects.filter(**self.get_queryset_filters())

class OutboundEmailDetail(generic_views.DetailView):

    def get_object(self):
        return get_object_or_404(models.OutboundEmail,
            pk=self.kwargs['pk'])