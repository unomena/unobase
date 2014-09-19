__author__ = 'michael'

from django.db import models

from unobase import models as unobase_models
from unobase.support import constants

class Case(unobase_models.ContentModel):
    status = models.PositiveSmallIntegerField(choices=constants.CASE_STATUS_CHOICES, default=constants.CASE_STATUS_NEW)
    origin = models.PositiveSmallIntegerField(choices=constants.CASE_ORIGIN_CHOICES, default=constants.CASE_ORIGIN_WEB)
    type = models.PositiveSmallIntegerField(blank=True, null=True, choices=constants.CASE_TYPE_CHOICES)
    reason = models.PositiveSmallIntegerField(blank=True, null=True, choices=constants.CASE_REASON_CHOICES)
    priority = models.PositiveSmallIntegerField(blank=True, null=True, choices=constants.CASE_PRIORITY_CHOICES, default=constants.CASE_PRIORITY_MEDIUM)
    internal_comments = models.TextField(blank=True, null=True)

class FrequentlyAskedQuestion(unobase_models.StateModel):
    question = models.CharField(max_length=1000)
    answer = models.CharField(max_length=1000)

    def __unicode__(self):
        return u'%s' % self.question
    
class TechnicalDocumentation(unobase_models.StatefulContentModel):
    file = models.FileField(upload_to='technical_documentation')
    
class Guide(TechnicalDocumentation):
    pass

class Reference(TechnicalDocumentation):
    pass

class BestPractice(TechnicalDocumentation):
    pass

class WhitePaper(TechnicalDocumentation):
    pass

class ProductManual(TechnicalDocumentation):
    pass