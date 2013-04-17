'''
Created on 17 Apr 2013

@author: michael
'''
from django.db import models
from django.contrib.sites.models import Site

class MenuBase(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    url = models.CharField(max_length=255)
    new_tab = models.BooleanField(default=False)
    order = models.PositiveSmallIntegerField(default=0)
    
    def __unicode__(self):
        return u'%s' % self.title
    
    class Meta:
        abstract = True
        
class MenuManager(models.Manager):
    def get_queryset(self):
        return super(MenuManager, self).get_queryset().filter(sites=Site.objects.get_current())
        
class Menu(MenuBase):
    sites = models.ManyToManyField(Site)
    
    objects = MenuManager()
    
class MenuItem(MenuBase):
    menu = models.ForeignKey(Menu, related_name='menu_items')
    menu_item = models.ForeignKey('self', blank=True, null=True, related_name='children')
    