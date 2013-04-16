'''
Created on 15 Apr 2013

@author: michael
'''
from django.views import generic as generic_views
from django.shortcuts import get_object_or_404

from unobase.corporate_site import models

# News

class NewsList(generic_views.ListView):

    def get_queryset(self):
        return models.News.permitted.all()
    
class NewsDetail(generic_views.DetailView):

    def get_object(self):
        return get_object_or_404(models.News, pk=self.kwargs['pk'])
    
# Awards
    
class AwardList(generic_views.ListView):

    def get_queryset(self):
        return models.Award.permitted.all()
    
class AwardDetail(generic_views.DetailView):

    def get_object(self):
        return get_object_or_404(models.Award, pk=self.kwargs['pk'])
    
# Events
    
class EventList(generic_views.ListView):

    def get_queryset(self):
        return models.Event.permitted.all()
    
# Media Coverage
    
class MediaCoverageList(generic_views.ListView):

    def get_queryset(self):
        return models.MediaCoverage.permitted.all()
    
# Press Releases
    
class PressReleaseList(generic_views.ListView):

    def get_queryset(self):
        return models.PressRelease.permitted.all()
    
class PressReleaseDetail(generic_views.DetailView):

    def get_object(self):
        return get_object_or_404(models.PressRelease, pk=self.kwargs['pk'])
    
# Vacancies
    
class VacancyList(generic_views.ListView):

    def get_queryset(self):
        return models.Vacancy.permitted.all()
    
# Leadership
    
class LeadershipList(generic_views.ListView):

    def get_queryset(self):
        return models.CompanyMember.permitted.filter(is_leader=True)
    
class LeadershipDetail(generic_views.DetailView):

    def get_object(self):
        return get_object_or_404(models.CompanyMember, pk=self.kwargs['pk'], is_leader=True)
    
# Team
    
class TeamList(generic_views.ListView):

    def get_queryset(self):
        return models.CompanyMember.permitted.all()
    
class TeamDetail(generic_views.DetailView):

    def get_object(self):
        return get_object_or_404(models.CompanyMember, pk=self.kwargs['pk'])
    
# Board members
    
class BoardList(generic_views.ListView):

    def get_queryset(self):
        return models.CompanyMember.permitted.filter(is_board_member=True)
    
class BoardDetail(generic_views.DetailView):

    def get_object(self):
        return get_object_or_404(models.CompanyMember, pk=self.kwargs['pk'], is_board_member=True)
    
# Investors
    
class InvestorList(generic_views.ListView):

    def get_queryset(self):
        return models.CompanyMember.permitted.filter(is_investor=True)
    
class InvestorDetail(generic_views.DetailView):

    def get_object(self):
        return get_object_or_404(models.CompanyMember, pk=self.kwargs['pk'], is_investor=True)