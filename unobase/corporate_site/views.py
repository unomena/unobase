'''
Created on 15 Apr 2013

@author: michael
'''
from django.views import generic as generic_views
from django.shortcuts import get_object_or_404
from django.utils import timezone

from unobase.corporate_site import models
from unobase import utils as unobase_utils

# News


class NewsList(generic_views.ListView):

    def get_queryset(self):
        return models.News.published_versions.all()


class NewsDetail(generic_views.DetailView):

    def get_object(self):
        return unobase_utils.get_published_version_object_or_404(
            models.News, slug=self.kwargs['slug']
        )

# Awards


class AwardList(generic_views.ListView):

    def get_queryset(self):
        return models.Award.published_versions.all()


class AwardDetail(generic_views.DetailView):

    def get_object(self):
        return unobase_utils.get_published_version_object_or_404(
            models.Award,
            slug=self.kwargs['slug']
        )

# Events


class EventList(generic_views.ListView):

    def get_context_data(self, **kwargs):
        context = super(EventList, self).get_context_data(**kwargs)

        context['current_events'] = self.object_list.filter(
            end__gte=timezone.now().replace(
                hour=0, minute=0, second=0, microsecond=0
            )
        )

        context['past_events'] = self.object_list.filter(
            end__lt=timezone.now().replace(
                hour=0, minute=0, second=0, microsecond=0
            )
        ).order_by('-start')

        return context

    def get_queryset(self):
        return models.Event.published_versions.all().order_by('start')

# Media Coverage


class MediaCoverageList(generic_views.ListView):

    def get_queryset(self):
        return models.MediaCoverage.published_versions.all()

# Press Releases


class PressReleaseList(generic_views.ListView):

    def get_queryset(self):
        return models.PressRelease.published_versions.all()


class PressReleaseDetail(generic_views.DetailView):

    def get_object(self):
        return unobase_utils.get_published_version_object_or_404(
            models.PressRelease, slug=self.kwargs['slug']
        )

# Vacancies


class VacancyList(generic_views.ListView):

    def get_queryset(self):
        return models.Vacancy.published_versions.all()

# Leadership


class LeadershipList(generic_views.ListView):

    def get_queryset(self):
        return models.CompanyMember.published_versions.filter(is_leader=True)


class LeadershipDetail(generic_views.DetailView):

    def get_object(self):
        return unobase_utils.get_published_version_object_or_404(
            models.CompanyMember,
            slug=self.kwargs['slug'],
            is_leader=True
        )

# Team


class TeamList(generic_views.ListView):

    def get_queryset(self):
        return models.CompanyMember.published_versions.all()


class TeamDetail(generic_views.DetailView):

    def get_object(self):
        return unobase_utils.get_published_version_object_or_404(
            models.CompanyMember,
            slug=self.kwargs['slug']
        )

# Board members


class BoardList(generic_views.ListView):

    def get_queryset(self):
        return models.CompanyMember.published_versions.filter(
            is_board_member=True
        )


class BoardDetail(generic_views.DetailView):

    def get_object(self):
        return unobase_utils.get_published_version_object_or_404(
            models.CompanyMember,
            slug=self.kwargs['slug'],
            is_board_member=True
        )

# Investors


class InvestorList(generic_views.ListView):

    def get_queryset(self):
        return models.CompanyMember.published_versions.filter(is_investor=True)


class InvestorDetail(generic_views.DetailView):

    def get_object(self):
        return unobase_utils.get_published_version_object_or_404(
            models.CompanyMember,
            slug=self.kwargs['slug'],
            is_investor=True
        )
