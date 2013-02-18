__author__ = 'michael'

from django.contrib import admin

import models

class CustomCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'visible_to', 'posted_on_behalf_by', 'in_reply_to', 'moderated_by', 'moderated_on')
    list_filter = ('user',)
    search_fields = ('comment',) 

admin.site.register(models.CustomComment, CustomCommentAdmin)