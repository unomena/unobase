'''
Created on 05 Mar 2013

@author: michael
'''
from django.views import generic as generic_views
from django.shortcuts import get_object_or_404

from unobase import mixins as unobase_mixins
from unobase import utils as unobase_utils
from unobase.corporate_site import models as corporate_site_models

class AdminMixin(unobase_mixins.ConsoleUserRequiredMixin):
    raise_exception = False

class Console(AdminMixin, generic_views.TemplateView):
    pass

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