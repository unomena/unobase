'''
Created on 15 Apr 2013

@author: michael
'''
from django.contrib import admin

from unobase.corporate_site import models

class PressReleaseAdmin(admin.ModelAdmin):
    exclude = ('image_name',)

admin.site.register(models.Article)
admin.site.register(models.News)
admin.site.register(models.Award)
admin.site.register(models.PressRelease, PressReleaseAdmin)
admin.site.register(models.MediaCoverage)
admin.site.register(models.Event)
admin.site.register(models.Vacancy)
admin.site.register(models.Product)
admin.site.register(models.CompanyMember)