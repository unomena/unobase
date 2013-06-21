'''
Created on 05 Mar 2013

@author: michael
'''
from django.views import generic as generic_views
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect

from unobase import mixins as unobase_mixins
from unobase import views as unobase_views
from unobase import constants as unobase_constants
from unobase import utils as unobase_utils

from unobase.corporate_site import models as corporate_site_models

class AdminMixin(unobase_mixins.ConsoleUserRequiredMixin, unobase_mixins.PermissionRequiredMixin):
    raise_exception = False
    
# Events

class EventCreate(AdminMixin, generic_views.CreateView):
    permission_required = 'corporate_site.add_event'

    def get_initial(self):
        return {'user' : self.request.user }
    
    def get_success_url(self):
        return reverse('console_event_detail', args=(self.object.pk,))

class EventUpdate(AdminMixin, generic_views.UpdateView):
    permission_required = 'corporate_site.change_event'

    def get_initial(self):
        return {'user' : self.request.user }

    def get_queryset(self):
        return corporate_site_models.Event.permitted.all()
    
    def get_success_url(self):
        return reverse('console_event_detail', args=(self.object.pk,))

class EventDetail(AdminMixin, generic_views.DetailView):
    permission_required = 'corporate_site.change_event'

    def get_object(self):
        return get_object_or_404(corporate_site_models.Event,
            pk=self.kwargs['pk'])

class EventDelete(AdminMixin, generic_views.DeleteView):
    permission_required = 'corporate_site.delete_event'

    def get_queryset(self):
        return corporate_site_models.Event.permitted.all()

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.state = unobase_constants.STATE_DELETED
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)
    
    def get_success_url(self):
        return reverse('console_event_list')

class EventList(AdminMixin, generic_views.ListView):
    permission_required = 'corporate_site.change_event'

    def get_queryset(self):
        return corporate_site_models.Event.permitted.all()
    
# Media Coverage

class MediaCoverageCreate(AdminMixin, generic_views.CreateView):
    permission_required = 'corporate_site.add_mediacoverage'

    def get_initial(self):
        return {'user' : self.request.user }
    
    def get_success_url(self):
        return reverse('console_media_coverage_detail', args=(self.object.pk,))

class MediaCoverageUpdate(AdminMixin, generic_views.UpdateView):
    permission_required = 'corporate_site.change_mediacoverage'

    def get_initial(self):
        return {'user' : self.request.user }

    def get_queryset(self):
        return corporate_site_models.MediaCoverage.permitted.all()
    
    def get_success_url(self):
        return reverse('console_media_coverage_detail', args=(self.object.pk,))

class MediaCoverageDetail(AdminMixin, generic_views.DetailView):
    permission_required = 'corporate_site.change_mediacoverage'

    def get_object(self):
        return get_object_or_404(corporate_site_models.MediaCoverage,
            pk=self.kwargs['pk'])

class MediaCoverageDelete(AdminMixin, generic_views.DeleteView):
    permission_required = 'corporate_site.delete_mediacoverage'

    def get_queryset(self):
        return corporate_site_models.MediaCoverage.permitted.all()

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.state = unobase_constants.STATE_DELETED
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)
    
    def get_success_url(self):
        return reverse('console_media_coverage_list')

class MediaCoverageList(AdminMixin, generic_views.ListView):
    permission_required = 'corporate_site.change_mediacoverage'

    def get_queryset(self):
        return corporate_site_models.MediaCoverage.permitted.all()
    
# News

class NewsCreate(AdminMixin, generic_views.CreateView):
    permission_required = 'corporate_site.add_news'

    def get_initial(self):
        return {'user' : self.request.user }
    
    def get_success_url(self):
        return reverse('console_news_detail', args=(self.object.pk,))

class NewsUpdate(AdminMixin, generic_views.UpdateView):
    permission_required = 'corporate_site.change_news'

    def get_initial(self):
        return {'user' : self.request.user }

    def get_queryset(self):
        return corporate_site_models.News.permitted.all()
    
    def get_success_url(self):
        return reverse('console_news_detail', args=(self.object.pk,))

class NewsDetail(AdminMixin, generic_views.DetailView):
    permission_required = 'corporate_site.change_news'

    def get_object(self):
        return get_object_or_404(corporate_site_models.News,
            pk=self.kwargs['pk'])

class NewsDelete(AdminMixin, generic_views.DeleteView):
    permission_required = 'corporate_site.delete_news'

    def get_queryset(self):
        return corporate_site_models.News.permitted.all()

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.state = unobase_constants.STATE_DELETED
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)
    
    def get_success_url(self):
        return reverse('console_news_list')

class NewsList(AdminMixin, generic_views.ListView):
    permission_required = 'corporate_site.change_news'

    def get_queryset(self):
        return corporate_site_models.News.permitted.all()
    
# Awards

class AwardCreate(AdminMixin, generic_views.CreateView):
    permission_required = 'corporate_site.add_award'

    def get_initial(self):
        return {'user' : self.request.user }
    
    def get_success_url(self):
        return reverse('console_awards_detail', args=(self.object.pk,))

class AwardUpdate(AdminMixin, generic_views.UpdateView):
    permission_required = 'corporate_site.change_award'

    def get_initial(self):
        return {'user' : self.request.user }

    def get_queryset(self):
        return corporate_site_models.Award.permitted.all()
    
    def get_success_url(self):
        return reverse('console_awards_detail', args=(self.object.pk,))

class AwardDetail(AdminMixin, generic_views.DetailView):
    permission_required = 'corporate_site.change_award'

    def get_object(self):
        return get_object_or_404(corporate_site_models.Award,
            pk=self.kwargs['pk'])

class AwardDelete(AdminMixin, generic_views.DeleteView):
    permission_required = 'corporate_site.delete_award'

    def get_queryset(self):
        return corporate_site_models.Award.permitted.all()

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.state = unobase_constants.STATE_DELETED
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)
    
    def get_success_url(self):
        return reverse('console_awards_list')

class AwardList(AdminMixin, generic_views.ListView):
    permission_required = 'corporate_site.change_award'

    def get_queryset(self):
        return corporate_site_models.Award.permitted.all()
    
# Press Releases

class PressReleaseCreate(AdminMixin, generic_views.CreateView):
    permission_required = 'corporate_site.add_pressrelease'

    def get_initial(self):
        return {'user' : self.request.user }
    
    def get_success_url(self):
        return reverse('console_press_releases_detail', args=(self.object.pk,))

class PressReleaseUpdate(AdminMixin, generic_views.UpdateView):
    permission_required = 'corporate_site.change_pressrelease'

    def get_initial(self):
        return {'user' : self.request.user }

    def get_queryset(self):
        return corporate_site_models.PressRelease.permitted.all()
    
    def get_success_url(self):
        return reverse('console_press_releases_detail', args=(self.object.pk,))

class PressReleaseDetail(AdminMixin, generic_views.DetailView):
    permission_required = 'corporate_site.change_pressrelease'

    def get_object(self):
        return get_object_or_404(corporate_site_models.PressRelease,
            pk=self.kwargs['pk'])

class PressReleaseDelete(AdminMixin, generic_views.DeleteView):
    permission_required = 'corporate_site.delete_pressrelease'

    def get_queryset(self):
        return corporate_site_models.PressRelease.permitted.all()

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.state = unobase_constants.STATE_DELETED
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)
    
    def get_success_url(self):
        return reverse('console_press_releases_list')

class PressReleaseList(AdminMixin, generic_views.ListView):
    permission_required = 'corporate_site.change_pressrelease'

    def get_queryset(self):
        return corporate_site_models.PressRelease.permitted.all()
    
# Vacancies

class VacancyCreate(AdminMixin, generic_views.CreateView):
    permission_required = 'corporate_site.add_vacancy'

    def get_initial(self):
        return {'user' : self.request.user }
    
    def get_success_url(self):
        return reverse('console_vacancies_detail', args=(self.object.pk,))

class VacancyUpdate(AdminMixin, generic_views.UpdateView):
    permission_required = 'corporate_site.change_vacancy'

    def get_initial(self):
        return {'user' : self.request.user }

    def get_queryset(self):
        return corporate_site_models.Vacancy.permitted.all()
    
    def get_success_url(self):
        return reverse('console_vacancies_detail', args=(self.object.pk,))

class VacancyDetail(AdminMixin, generic_views.DetailView):
    permission_required = 'corporate_site.change_vacancy'

    def get_object(self):
        return get_object_or_404(corporate_site_models.Vacancy,
            pk=self.kwargs['pk'])

class VacancyDelete(AdminMixin, generic_views.DeleteView):
    permission_required = 'corporate_site.delete_vacancy'

    def get_queryset(self):
        return corporate_site_models.Vacancy.permitted.all()

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.state = unobase_constants.STATE_DELETED
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)
    
    def get_success_url(self):
        return reverse('console_vacancies_list')

class VacancyList(AdminMixin, generic_views.ListView):
    permission_required = 'corporate_site.change_vacancy'

    def get_queryset(self):
        return corporate_site_models.Vacancy.permitted.all()
    
# Products

class ProductCreate(AdminMixin, generic_views.CreateView):
    permission_required = 'corporate_site.add_product'

    def get_initial(self):
        return {'user' : self.request.user }
    
    def get_success_url(self):
        return reverse('console_products_detail', args=(self.object.pk,))

class ProductUpdate(AdminMixin, generic_views.UpdateView):
    permission_required = 'corporate_site.change_product'

    def get_initial(self):
        return {'user' : self.request.user }

    def get_queryset(self):
        return corporate_site_models.Product.permitted.all()
    
    def get_success_url(self):
        return reverse('console_products_detail', args=(self.object.pk,))

class ProductDetail(AdminMixin, generic_views.DetailView):
    permission_required = 'corporate_site.change_product'

    def get_object(self):
        return get_object_or_404(corporate_site_models.Product,
            pk=self.kwargs['pk'])

class ProductDelete(AdminMixin, generic_views.DeleteView):
    permission_required = 'corporate_site.delete_product'

    def get_queryset(self):
        return corporate_site_models.Product.permitted.all()

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.state = unobase_constants.STATE_DELETED
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)
    
    def get_success_url(self):
        return reverse('console_products_list')

class ProductList(AdminMixin, generic_views.ListView):
    permission_required = 'corporate_site.change_product'

    def get_queryset(self):
        return corporate_site_models.Product.permitted.all()
    
# Leader

class LeaderCreate(AdminMixin, generic_views.CreateView):
    permission_required = 'corporate_site.add_companymember'

    def get_initial(self):
        return {'user' : self.request.user }
    
    def get_success_url(self):
        return reverse('console_leadership_detail', args=(self.object.pk,))

class LeaderUpdate(AdminMixin, generic_views.UpdateView):
    permission_required = 'corporate_site.change_companymember'

    def get_initial(self):
        return {'user' : self.request.user }

    def get_queryset(self):
        return corporate_site_models.CompanyMember.permitted.filter(is_leader=True)
    
    def get_success_url(self):
        return reverse('console_leadership_detail', args=(self.object.pk,))

class LeaderDetail(AdminMixin, generic_views.DetailView):
    permission_required = 'corporate_site.change_companymember'

    def get_object(self):
        return get_object_or_404(corporate_site_models.CompanyMember,
            pk=self.kwargs['pk'], is_leader=True)

class LeaderDelete(AdminMixin, generic_views.DeleteView):
    permission_required = 'corporate_site.delete_companymember'

    def get_queryset(self):
        return corporate_site_models.CompanyMember.permitted.filter(is_leader=True)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.state = unobase_constants.STATE_DELETED
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)
    
    def get_success_url(self):
        return reverse('console_leadership_list')

class LeaderList(AdminMixin, generic_views.ListView):
    permission_required = 'corporate_site.change_companymember'

    def get_queryset(self):
        return corporate_site_models.CompanyMember.permitted.filter(is_leader=True)
    
# Board Member

class BoardMemberCreate(AdminMixin, generic_views.CreateView):
    permission_required = 'corporate_site.add_companymember'

    def get_initial(self):
        return {'user' : self.request.user }
    
    def get_success_url(self):
        return reverse('console_board_members_detail', args=(self.object.pk,))

class BoardMemberUpdate(AdminMixin, generic_views.UpdateView):
    permission_required = 'corporate_site.change_companymember'

    def get_initial(self):
        return {'user' : self.request.user }

    def get_queryset(self):
        return corporate_site_models.CompanyMember.permitted.filter(is_board_member=True)
    
    def get_success_url(self):
        return reverse('console_board_members_detail', args=(self.object.pk,))

class BoardMemberDetail(AdminMixin, generic_views.DetailView):
    permission_required = 'corporate_site.change_companymember'

    def get_object(self):
        return get_object_or_404(corporate_site_models.CompanyMember,
            pk=self.kwargs['pk'], is_board_member=True)

class BoardMemberDelete(AdminMixin, generic_views.DeleteView):
    permission_required = 'corporate_site.delete_companymember'

    def get_queryset(self):
        return corporate_site_models.CompanyMember.permitted.filter(is_board_member=True)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.state = unobase_constants.STATE_DELETED
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)
    
    def get_success_url(self):
        return reverse('console_board_members_list')

class BoardMemberList(AdminMixin, generic_views.ListView):
    permission_required = 'corporate_site.change_companymember'

    def get_queryset(self):
        return corporate_site_models.CompanyMember.permitted.filter(is_board_member=True)
    
# Investors

class InvestorCreate(AdminMixin, generic_views.CreateView):
    permission_required = 'corporate_site.add_companymember'

    def get_initial(self):
        return {'user' : self.request.user }
    
    def get_success_url(self):
        return reverse('console_investors_detail', args=(self.object.pk,))

class InvestorUpdate(AdminMixin, generic_views.UpdateView):
    permission_required = 'corporate_site.change_companymember'

    def get_initial(self):
        return {'user' : self.request.user }

    def get_queryset(self):
        return corporate_site_models.CompanyMember.permitted.filter(is_investor=True)
    
    def get_success_url(self):
        return reverse('console_investors_detail', args=(self.object.pk,))

class InvestorDetail(AdminMixin, generic_views.DetailView):
    permission_required = 'corporate_site.change_companymember'

    def get_object(self):
        return get_object_or_404(corporate_site_models.CompanyMember,
            pk=self.kwargs['pk'], is_investor=True)

class InvestorDelete(AdminMixin, generic_views.DeleteView):
    permission_required = 'corporate_site.delete_companymember'

    def get_queryset(self):
        return corporate_site_models.CompanyMember.permitted.filter(is_investor=True)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.state = unobase_constants.STATE_DELETED
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)
    
    def get_success_url(self):
        return reverse('console_investors_list')

class InvestorList(AdminMixin, generic_views.ListView):
    permission_required = 'corporate_site.change_companymember'

    def get_queryset(self):
        return corporate_site_models.CompanyMember.permitted.filter(is_investor=True)
    
# Team

class TeamCreate(AdminMixin, generic_views.CreateView):
    permission_required = 'corporate_site.add_companymember'

    def get_initial(self):
        return {'user' : self.request.user }
    
    def get_success_url(self):
        return reverse('console_team_detail', args=(self.object.pk,))

class TeamUpdate(AdminMixin, generic_views.UpdateView):
    permission_required = 'corporate_site.change_companymember'

    def get_initial(self):
        return {'user' : self.request.user }

    def get_queryset(self):
        return corporate_site_models.CompanyMember.permitted.all()
    
    def get_success_url(self):
        return reverse('console_team_detail', args=(self.object.pk,))

class TeamDetail(AdminMixin, generic_views.DetailView):
    permission_required = 'corporate_site.change_companymember'

    def get_object(self):
        return get_object_or_404(corporate_site_models.CompanyMember,
            pk=self.kwargs['pk'])

class TeamDelete(AdminMixin, generic_views.DeleteView):
    permission_required = 'corporate_site.delete_companymember'

    def get_queryset(self):
        return corporate_site_models.CompanyMember.permitted.all()

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.state = unobase_constants.STATE_DELETED
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)
    
    def get_success_url(self):
        return reverse('console_team_list')

class TeamList(AdminMixin, generic_views.ListView):
    permission_required = 'corporate_site.change_companymember'

    def get_queryset(self):
        return corporate_site_models.CompanyMember.permitted.all()
    
# Content Images

class ContentImageUrl(AdminMixin, generic_views.View):

    def get(self, request, *args, **kwargs):

        content_type = kwargs['content_type']

        if content_type == 'event':
            content_object = get_object_or_404(corporate_site_models.Event, pk=kwargs['pk'])
        elif content_type == 'media_coverage':
            content_object = get_object_or_404(corporate_site_models.MediaCoverage, pk=kwargs['pk'])
        elif content_type == 'news':
            content_object = get_object_or_404(corporate_site_models.News, pk=kwargs['pk'])
        elif content_type == 'award':
            content_object = get_object_or_404(corporate_site_models.Award, pk=kwargs['pk'])

        return unobase_utils.respond_with_json({'url': content_object.get_120x120_url()})