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

class AuditModelAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        obj.modified_by = request.user
        try:
            if not obj.created_by:
                obj.created_by = request.user
        except User.DoesNotExist:
            obj.created_by = request.user

        return super(AuditModelAdmin, self).save_model(request, obj, form, change)
    
class ContentModelAdmin(StateModelAdmin, AuditModelAdmin):
    list_display = ('title', 'leaf_content_type', 'admin_thumbnail',)
    

class DefaultImageAdmin(StateModelAdmin):
    list_display = ('title', 'state', 'admin_thumbnail',)
    list_filter = ('state',)
    fieldsets = (
        (None, {'fields': ('title','image','category','state',)}),
        )

admin.site.register(models.DefaultImage, DefaultImageAdmin)
admin.site.register(models.TagModel)
admin.site.register(models.ContentBlock)

admin.site.register(models.ImageBanner)
admin.site.register(models.HTMLBanner)
admin.site.register(models.ImageBannerSet)
admin.site.register(models.HTMLBannerSet)