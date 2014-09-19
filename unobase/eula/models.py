'''
Created on 06 Mar 2013

@author: michael
'''
from django.db import models

from ckeditor.fields import RichTextField

class EULA(models.Model):
    title = models.CharField(max_length=255, default='')
    
    def latest_version(self):
        try:
            return self.instances.all().order_by('-date_created')[0]
        except IndexError:
            return None
    
    def __unicode__(self):
        return u'%s' % self.title
    
class EULAVersion(models.Model):
    eula = models.ForeignKey(EULA, related_name='instances')
    content = RichTextField()
    version = models.CharField(max_length=255)
    date_created = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_created']
    
    def __unicode__(self):
        return u'%s Version %s' % (self.eula, self.version)