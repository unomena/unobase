'''
Created on 17 Apr 2013

@author: michael
'''
from django.contrib import admin
from unobase.cms import models

class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(models.Menu, MenuAdmin)
admin.site.register(models.MenuItem, MenuAdmin)