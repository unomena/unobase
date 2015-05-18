from django.contrib import admin
from django.contrib.auth.models import User

import models
import constants

def make_published(modeladmin, request, queryset):
    queryset.update(state=constants.STATE_PUBLISHED)
make_published.short_description = "Mark selected items as published"

def make_staged(modeladmin, request, queryset):
    queryset.update(state=constants.STATE_STAGED)
make_staged.short_description = "Mark selected items as staged"

def make_deleted(modeladmin, request, queryset):
    queryset.update(state=constants.STATE_DELETED)
make_deleted.short_description = "Mark selected items as deleted"

def make_unpublished(modeladmin, request, queryset):
    queryset.update(state=constants.STATE_UNPUBLISHED)
make_unpublished.short_description = "Mark selected items as unpublished"

class StateModelAdmin(admin.ModelAdmin):
    actions = [make_published, make_staged, make_unpublished, make_deleted]
    
class ContentModelAdmin(StateModelAdmin):
    list_display = ('title', 'slug', 'leaf_content_type', 'admin_thumbnail',)
    

class DefaultImageAdmin(StateModelAdmin):
    list_display = ('title', 'state', 'admin_thumbnail',)
    list_filter = ('state',)
    fieldsets = (
        (None, {'fields': ('title','image','category','state',)}),
        )

admin.site.register(models.DefaultImage, DefaultImageAdmin)
admin.site.register(models.TagModel)


class ContentBlockAdmin(StateModelAdmin):
    list_display = ('title', 'slug',)
    fieldsets = (
        (None, {'fields': ('title', 'slug', 'description', 'content', 'sites',)}),
        )

admin.site.register(models.ContentBlock, ContentBlockAdmin)


class SiteListAdmin(admin.ModelAdmin):
    list_display = ('title', 'site_list')

    def site_list(self, model):
        return ', '.join([site.domain for site in model.sites.all()])

admin.site.register(models.ImageBanner, SiteListAdmin)
admin.site.register(models.HTMLBanner, SiteListAdmin)

admin.site.register(models.ImageBannerSet)
admin.site.register(models.HTMLBannerSet)


class VersionAdmin(admin.ModelAdmin):
    list_display = ('content_type', 'object_id', 'series', 'number', 'state')

admin.site.register(models.Version, VersionAdmin)
admin.site.register(models.VersionSeries)
admin.site.register(models.Template)
