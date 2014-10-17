from unobase.blog import models

__author__ = 'michael'

from django.contrib import admin

class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog', 'created',)
    list_filter = ('title',)

class BlogEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'blog', 'created',)
    list_filter = ('posted_on_behalf_by',)
    search_fields = ('title', 'content')
    
admin.site.register(models.Blog, BlogAdmin)
admin.site.register(models.BlogEntry, BlogEntryAdmin)