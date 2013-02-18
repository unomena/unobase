__author__ = 'michael'

from django.views import generic as generic_views
from django.shortcuts import get_object_or_404
from django.contrib import messages

from unobase.support import models, signals
from unobase import mixins

class CaseCreate(generic_views.CreateView):

    def get_initial(self):
        return {'user' : self.request.user }

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Your support case has been sent to our staff.')
        signals.user_submitted_support_case.send(sender=models.Case, user=self.request.user, request=self.request, case=self.object)

        return super(CaseCreate, self).form_valid(form)

class CaseList(mixins.LoginRequiredMixin, generic_views.ListView):

    def get_queryset(self):
        return models.Case.objects.filter(created_by=self.request.user)

class CaseDetail(mixins.LoginRequiredMixin, generic_views.DetailView):

    def get_object(self):
        return get_object_or_404(models.Case,
            pk=self.kwargs['pk'], created_by=self.request.user)

class FAQList(generic_views.ListView):

    def get_queryset(self):
        return models.FrequentlyAskedQuestion.objects.all()