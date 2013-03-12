'''
Created on 06 Mar 2013

@author: michael
'''
from django.db import models

class EULAManager(models.Manager):
    def latest_eula(self):
        try:
            return self.get_query_set().order_by('-version')[0]
        except IndexError:
            return None

class EULA(models.Model):
    content = models.TextField()
    version = models.PositiveIntegerField(default=1)
    
    objects = EULAManager()
    
    def __unicode__(self):
        return u'Version %i' % self.version