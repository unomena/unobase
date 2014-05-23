'''
Created on 24 Apr 2013

@author: euan
'''
import datetime
from django.core.management.base import BaseCommand
from django.utils import timezone

from django.contrib.contenttypes.models import ContentType

from unobase import constants, models

class Command(BaseCommand):
    """
    Auto publishes and retracts objects based on their publish_date_time and retract_date_time dates.
    """
    def handle(self, *args, **options):
        
        for ct in ContentType.objects.all():
            try:
                if issubclass(ct.model_class(), models.StateModel):
                    # Publish everything that needs to be published
                    for obj in ct.model_class().objects.filter(publish_date_time__lte=timezone.datetime.now()):
                        obj.state = constants.STATE_PUBLISHED
                        obj.publish_date_time = None
                        obj.save()
            except:
                pass
        
        
        for ct in ContentType.objects.all():
            try:
                if issubclass(ct.model_class(), models.StateModel):
                    # Retract everything that needs to be retracted
                    for obj in ct.model_class().objects.filter(retract_date_time__lte=timezone.datetime.now()):
                        obj.state = constants.STATE_UNPUBLISHED
                        obj.retract_date_time = None
                        obj.save()
            except:
                pass