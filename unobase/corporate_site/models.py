'''
Created on 15 Apr 2013

@author: michael
'''
from django.db import models

from unobase import models as unobase_models
from unobase.calendar import models as calendar_models
from unobase.corporate_site import constants

class Article(unobase_models.StatefulContentModel, unobase_models.RelatedModel):
    "An article"
    image_name = models.CharField(max_length=255, blank=True, null=True, unique=True)

class News(Article):
    "News about the company"
    default_image_category = constants.DEFAULT_IMAGE_CATEGORY_NEWS
    
    class Meta:
        ordering = ['-created']

class Award(Article):
    "Company's awards"
    default_image_category = constants.DEFAULT_IMAGE_CATEGORY_AWARD
    
    class Meta:
        ordering = ['-created']
    

class PressRelease(Article):
    "Company's press releases"
    default_image_category = constants.DEFAULT_IMAGE_CATEGORY_PRESS_RELEASE
    
    pdf = models.FileField(upload_to='press_releases', blank=True, null=True)
    
    class Meta:
        ordering = ['-created']

class MediaCoverage(Article):
    "Media coverage about the company"
    default_image_category = constants.DEFAULT_IMAGE_CATEGORY_MEDIA_COVERAGE

    pdf = models.FileField(upload_to='media_coverage', blank=True, null=True)
    external_link = models.URLField(blank=True, null=True)
    
    class Meta:
        ordering = ['-created']

class Event(calendar_models.Event, unobase_models.RelatedModel, unobase_models.StateModel):
    "Trade Show, Festival, Market"
    default_image_category = constants.DEFAULT_IMAGE_CATEGORY_EVENT
    
    image_name = models.CharField(max_length=255, blank=True, null=True, unique=True)
    
    class Meta:
        ordering = ['-start']

class Vacancy(unobase_models.ContentModel, unobase_models.StateModel):
    "Job vacancies within the company"
    external_link = models.URLField(blank=True, null=True)
    
class Product(unobase_models.StatefulContentModel, unobase_models.RelatedModel):
    "Products a company is selling"
    default_image_category = constants.DEFAULT_IMAGE_CATEGORY_PRODUCT
    
    file = models.FileField(upload_to='products', blank=True, null=True)
    image_name = models.CharField(max_length=255, blank=True, null=True, unique=True)
    
class CompanyMember(unobase_models.StatefulContentModel):
    "Members of the company"
    
    default_image_category = constants.DEFAULT_IMAGE_CATEGORY_COMPANY_MEMBER
    
    is_board_member = models.BooleanField(default=False)
    is_leader = models.BooleanField(default=False)
    is_investor = models.BooleanField(default=False)
    
    job_title = models.CharField(max_length=255, blank=True, null=True)
    image_name = models.CharField(max_length=255, blank=True, null=True, unique=True)
    
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']