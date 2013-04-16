__author__ = 'michael'

from django.conf.urls.defaults import patterns, url

from unobase.corporate_site.console import views, forms

urlpatterns = patterns('',
   # Events
   
   url(r'^events/create/$',
        views.EventCreate.as_view(form_class=forms.Event,
                                  template_name='console/corporate_site/events/event_edit.html'),
        name='console_event_create'),

    url(r'^events/update/(?P<pk>\d+)/$',
        views.EventUpdate.as_view(form_class=forms.Event,
                                  template_name='console/corporate_site/events/event_edit.html'),
        name='console_event_update'),

    url(r'^events/detail/(?P<pk>\d+)/$',
        views.EventDetail.as_view(template_name='console/corporate_site/events/event_detail.html'),
        name='console_event_detail'),

    url(r'^events/delete/(?P<pk>\d+)/$',
        views.EventDelete.as_view(),
        name='console_event_delete'),

    url(r'^events/list/$',
        views.EventList.as_view(template_name='console/corporate_site/events/event_list.html',
                                 paginate_by=10),
        name='console_event_list'),
                       
   # Media Coverage
   
   url(r'^media_coverage/create/$',
        views.MediaCoverageCreate.as_view(form_class=forms.MediaCoverage,
                                  template_name='console/corporate_site/media_coverage/media_coverage_edit.html'),
        name='console_media_coverage_create'),

    url(r'^media_coverage/update/(?P<pk>\d+)/$',
        views.MediaCoverageUpdate.as_view(form_class=forms.MediaCoverage,
                                  template_name='console/corporate_site/media_coverage/media_coverage_edit.html'),
        name='console_media_coverage_update'),

    url(r'^media_coverage/detail/(?P<pk>\d+)/$',
        views.MediaCoverageDetail.as_view(template_name='console/corporate_site/media_coverage/media_coverage_detail.html'),
        name='console_media_coverage_detail'),

    url(r'^media_coverage/delete/(?P<pk>\d+)/$',
        views.MediaCoverageDelete.as_view(),
        name='console_media_coverage_delete'),

    url(r'^media_coverage/list/$',
        views.MediaCoverageList.as_view(template_name='console/corporate_site/media_coverage/media_coverage_list.html',
                                 paginate_by=10),
        name='console_media_coverage_list'),
                       
   # News
   
   url(r'^news/create/$',
        views.NewsCreate.as_view(form_class=forms.News,
                                  template_name='console/corporate_site/news/news_edit.html'),
        name='console_news_create'),

    url(r'^news/update/(?P<pk>\d+)/$',
        views.NewsUpdate.as_view(form_class=forms.News,
                                  template_name='console/corporate_site/news/news_edit.html'),
        name='console_news_update'),

    url(r'^news/detail/(?P<pk>\d+)/$',
        views.NewsDetail.as_view(template_name='console/corporate_site/news/news_detail.html'),
        name='console_news_detail'),

    url(r'^news/delete/(?P<pk>\d+)/$',
        views.NewsDelete.as_view(),
        name='console_news_delete'),

    url(r'^news/list/$',
        views.NewsList.as_view(template_name='console/corporate_site/news/news_list.html',
                                 paginate_by=10),
        name='console_news_list'),
                       
   # Awards
   
   url(r'^awards/create/$',
        views.AwardCreate.as_view(form_class=forms.Award,
                                  template_name='console/corporate_site/awards/award_edit.html'),
        name='console_awards_create'),

    url(r'^awards/update/(?P<pk>\d+)/$',
        views.AwardUpdate.as_view(form_class=forms.Award,
                                  template_name='console/corporate_site/awards/award_edit.html'),
        name='console_awards_update'),

    url(r'^awards/detail/(?P<pk>\d+)/$',
        views.AwardDetail.as_view(template_name='console/corporate_site/awards/award_detail.html'),
        name='console_awards_detail'),

    url(r'^awards/delete/(?P<pk>\d+)/$',
        views.AwardDelete.as_view(),
        name='console_awards_delete'),

    url(r'^awards/list/$',
        views.AwardList.as_view(template_name='console/corporate_site/awards/award_list.html',
                                 paginate_by=10),
        name='console_awards_list'),
                       
   # Press Releases
   
   url(r'^press_releases/create/$',
        views.PressReleaseCreate.as_view(form_class=forms.PressRelease,
                                  template_name='console/corporate_site/press_releases/press_release_edit.html'),
        name='console_press_releases_create'),

    url(r'^press_releases/update/(?P<pk>\d+)/$',
        views.PressReleaseUpdate.as_view(form_class=forms.PressRelease,
                                  template_name='console/corporate_site/press_releases/press_release_edit.html'),
        name='console_press_releases_update'),

    url(r'^press_releases/detail/(?P<pk>\d+)/$',
        views.PressReleaseDetail.as_view(template_name='console/corporate_site/press_releases/press_release_detail.html'),
        name='console_press_releases_detail'),

    url(r'^press_releases/delete/(?P<pk>\d+)/$',
        views.PressReleaseDelete.as_view(),
        name='console_press_releases_delete'),

    url(r'^press_releases/list/$',
        views.PressReleaseList.as_view(template_name='console/corporate_site/press_releases/press_release_list.html',
                                 paginate_by=10),
        name='console_press_releases_list'),
                       
    # Vacancies
   
   url(r'^vacancies/create/$',
        views.VacancyCreate.as_view(form_class=forms.Vacancy,
                                  template_name='console/corporate_site/vacancies/vacancy_edit.html'),
        name='console_vacancies_create'),

    url(r'^vacancies/update/(?P<pk>\d+)/$',
        views.VacancyUpdate.as_view(form_class=forms.Vacancy,
                                  template_name='console/corporate_site/vacancies/vacancy_edit.html'),
        name='console_vacancies_update'),

    url(r'^vacancies/detail/(?P<pk>\d+)/$',
        views.VacancyDetail.as_view(template_name='console/corporate_site/vacancies/vacancy_detail.html'),
        name='console_vacancies_detail'),

    url(r'^vacancies/delete/(?P<pk>\d+)/$',
        views.VacancyDelete.as_view(),
        name='console_vacancies_delete'),

    url(r'^vacancies/list/$',
        views.VacancyList.as_view(template_name='console/corporate_site/vacancies/vacancy_list.html',
                                 paginate_by=10),
        name='console_vacancies_list'),
                       
    # Products
   
   url(r'^products/create/$',
        views.ProductCreate.as_view(form_class=forms.Product,
                                  template_name='console/corporate_site/products/product_edit.html'),
        name='console_products_create'),

    url(r'^products/update/(?P<pk>\d+)/$',
        views.ProductUpdate.as_view(form_class=forms.Product,
                                  template_name='console/corporate_site/products/product_edit.html'),
        name='console_products_update'),

    url(r'^products/detail/(?P<pk>\d+)/$',
        views.ProductDetail.as_view(template_name='console/corporate_site/products/product_detail.html'),
        name='console_products_detail'),

    url(r'^products/delete/(?P<pk>\d+)/$',
        views.ProductDelete.as_view(),
        name='console_products_delete'),

    url(r'^products/list/$',
        views.ProductList.as_view(template_name='console/corporate_site/products/product_list.html',
                                 paginate_by=10),
        name='console_products_list'),
                       
    # Leadership
   
   url(r'^leadership/create/$',
        views.LeaderCreate.as_view(form_class=forms.Leader,
                                  template_name='console/corporate_site/leadership/leadership_edit.html'),
        name='console_leadership_create'),

    url(r'^leadership/update/(?P<pk>\d+)/$',
        views.LeaderUpdate.as_view(form_class=forms.Leader,
                                  template_name='console/corporate_site/leadership/leadership_edit.html'),
        name='console_leadership_update'),

    url(r'^leadership/detail/(?P<pk>\d+)/$',
        views.LeaderDetail.as_view(template_name='console/corporate_site/leadership/leadership_detail.html'),
        name='console_leadership_detail'),

    url(r'^leadership/delete/(?P<pk>\d+)/$',
        views.LeaderDelete.as_view(),
        name='console_leadership_delete'),

    url(r'^leadership/list/$',
        views.LeaderList.as_view(template_name='console/corporate_site/leadership/leadership_list.html',
                                 paginate_by=10),
        name='console_leadership_list'),
                       
    # Board Members
   
   url(r'^board_members/create/$',
        views.BoardMemberCreate.as_view(form_class=forms.BoardMember,
                                  template_name='console/corporate_site/board_members/board_member_edit.html'),
        name='console_board_members_create'),

    url(r'^board_members/update/(?P<pk>\d+)/$',
        views.BoardMemberUpdate.as_view(form_class=forms.BoardMember,
                                  template_name='console/corporate_site/board_members/board_member_edit.html'),
        name='console_board_members_update'),

    url(r'^board_members/detail/(?P<pk>\d+)/$',
        views.BoardMemberDetail.as_view(template_name='console/corporate_site/board_members/board_member_detail.html'),
        name='console_board_members_detail'),

    url(r'^board_members/delete/(?P<pk>\d+)/$',
        views.BoardMemberDelete.as_view(),
        name='console_board_members_delete'),

    url(r'^board_members/list/$',
        views.BoardMemberList.as_view(template_name='console/corporate_site/board_members/board_member_list.html',
                                 paginate_by=10),
        name='console_board_members_list'),
                       
    # Investors
   
   url(r'^investors/create/$',
        views.InvestorCreate.as_view(form_class=forms.Investor,
                                  template_name='console/corporate_site/investors/investor_edit.html'),
        name='console_investors_create'),

    url(r'^investors/update/(?P<pk>\d+)/$',
        views.InvestorUpdate.as_view(form_class=forms.Investor,
                                  template_name='console/corporate_site/investors/investor_edit.html'),
        name='console_investors_update'),

    url(r'^investors/detail/(?P<pk>\d+)/$',
        views.InvestorDetail.as_view(template_name='console/corporate_site/investors/investor_detail.html'),
        name='console_investors_detail'),

    url(r'^investors/delete/(?P<pk>\d+)/$',
        views.InvestorDelete.as_view(),
        name='console_investors_delete'),

    url(r'^investors/list/$',
        views.InvestorList.as_view(template_name='console/corporate_site/investors/investor_list.html',
                                 paginate_by=10),
        name='console_investors_list'),
                       
    # Team
   
   url(r'^team/create/$',
        views.TeamCreate.as_view(form_class=forms.CompanyMember,
                                  template_name='console/corporate_site/team/team_edit.html'),
        name='console_team_create'),

    url(r'^team/update/(?P<pk>\d+)/$',
        views.TeamUpdate.as_view(form_class=forms.CompanyMember,
                                  template_name='console/corporate_site/team/team_edit.html'),
        name='console_team_update'),

    url(r'^team/detail/(?P<pk>\d+)/$',
        views.TeamDetail.as_view(template_name='console/corporate_site/team/team_detail.html'),
        name='console_team_detail'),

    url(r'^team/delete/(?P<pk>\d+)/$',
        views.TeamDelete.as_view(),
        name='console_team_delete'),

    url(r'^team/list/$',
        views.TeamList.as_view(template_name='console/corporate_site/team/team_list.html',
                                 paginate_by=10),
        name='console_team_list'),
)