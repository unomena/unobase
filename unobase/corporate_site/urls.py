__author__ = 'michael'

from django.conf.urls.defaults import patterns, url

from unobase.corporate_site import views

urlpatterns = patterns('django.contrib.flatpages.views',
    url(r'^about/$', 'flatpage', {'url': '/about/'}, 
        name='corporate_site_about'),
                        
    url(r'^contact/$', 'flatpage', {'url': '/contact/'}, 
        name='corporate_site_contact'),
                       
    url(r'^privacy/$', 'flatpage', {'url': '/privacy/'}, 
        name='corporate_site_privacy'),
                        
    url(r'^legal/$', 'flatpage', {'url': '/legal/'}, 
        name='corporate_site_legal'),
)

urlpatterns += patterns('',
    # News
    
    url(r'^news/$',
        views.NewsList.as_view(template_name='corporate_site/news/news_list.html',
                               paginate_by=20),
        name='corporate_site_news_list'),
                       
    url(r'^news/detail/(?P<pk>\d+)/$',
        views.NewsDetail.as_view(template_name='corporate_site/news/news_detail.html'),
        name='corporate_site_news_detail'),
                       
    # Awards
    
    url(r'^awards/$',
        views.AwardList.as_view(template_name='corporate_site/awards/award_list.html',
                                paginate_by=20),
        name='corporate_site_awards_list'),
                       
    url(r'^awards/detail/(?P<pk>\d+)/$',
        views.AwardDetail.as_view(template_name='corporate_site/awards/award_detail.html'),
        name='corporate_site_awards_detail'),
                       
    # Events
    
    url(r'^events/$',
        views.EventList.as_view(template_name='corporate_site/events/event_list.html',
                                paginate_by=20),
        name='corporate_site_events_list'),
                       
    # Media Coverage
    
    url(r'^media_coverage/$',
        views.MediaCoverageList.as_view(template_name='corporate_site/media_coverage/media_coverage_list.html',
                                        paginate_by=20),
        name='corporate_site_media_coverage_list'),
                       
    # Press Release
    
    url(r'^press_releases/$',
        views.PressReleaseList.as_view(template_name='corporate_site/press_releases/press_release_list.html',
                                       paginate_by=20),
        name='corporate_site_press_release_list'),
                       
    url(r'^press_releases/detail/(?P<pk>\d+)/$',
        views.PressReleaseDetail.as_view(template_name='corporate_site/press_releases/press_release_detail.html'),
        name='corporate_site_press_release_detail'),
                       
    # Vacancy
    
    url(r'^careers/$',
        views.VacancyList.as_view(template_name='corporate_site/vacancies/vacancy_list.html',
                                  paginate_by=20),
        name='corporate_site_vacancy_list'),
                       
    # Leadership
    
    url(r'^leadership/$',
        views.LeadershipList.as_view(template_name='corporate_site/leadership/leadership_list.html',
                                     paginate_by=20),
        name='corporate_site_leadership_list'),
                       
    url(r'^leadership/detail/(?P<pk>\d+)/$',
        views.LeadershipDetail.as_view(template_name='corporate_site/leadership/leadership_detail.html'),
        name='corporate_site_leadership_detail'),
                       
    # Team
    
    url(r'^team/$',
        views.TeamList.as_view(template_name='corporate_site/team/team_list.html',
                               paginate_by=20),
        name='corporate_site_team_list'),
                       
    url(r'^team/detail/(?P<pk>\d+)/$',
        views.TeamDetail.as_view(template_name='corporate_site/team/team_detail.html'),
        name='corporate_site_team_detail'),
                       
    # Board
    
    url(r'^board_members/$',
        views.BoardList.as_view(template_name='corporate_site/board_members/board_member_list.html',
                                paginate_by=20),
        name='corporate_site_board_member_list'),
                       
    url(r'^board_members/detail/(?P<pk>\d+)/$',
        views.LeadershipDetail.as_view(template_name='corporate_site/board_members/board_member_detail.html'),
        name='corporate_site_board_member_detail'),
                       
    # Investors
    
    url(r'^investors/$',
        views.InvestorList.as_view(template_name='corporate_site/investors/investor_list.html',
                                   paginate_by=20),
        name='corporate_site_investor_list'),
                       
    url(r'^investors/detail/(?P<pk>\d+)/$',
        views.InvestorDetail.as_view(template_name='corporate_site/investors/investor_detail.html'),
        name='corporate_site_investor_detail'),
)
