__author__ = 'michael'

from django.db import models

from django.contrib.comments.models import Comment

import constants

from unobase import models as unobase_models
from unobase import settings as unobase_settings

class CustomComment(unobase_models.TagModel, Comment):
    visible_to = models.IntegerField(choices=constants.COMMENT_VISIBLE_TO_CHOICES,
                                     default=constants.COMMENT_VISIBLE_TO_EVERYONE)
    posted_on_behalf_by = models.ForeignKey(unobase_settings.AUTH_USER_MODEL, null=True, blank=True, related_name='comments_posted_on_behalf')
    in_reply_to = models.ForeignKey('CustomComment', null=True, blank=True, related_name='replies')
    state = models.CharField(max_length=16, choices=constants.COMMENT_STATE_CHOICES,
        null=True, blank=True)
    moderated_by = models.ForeignKey(unobase_settings.AUTH_USER_MODEL, null=True, blank=True, related_name='comments_moderated')
    moderated_on = models.DateTimeField(null=True, blank=True)
    order = models.DecimalField(max_digits=8, decimal_places=4, null=True, blank=True)
    report_count = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ('-order','-submit_date',)

    @property
    def activity_content(self):
        return self.comment

    @property
    def absolute_url(self):
        return '%s#comments' % self.content_object.absolute_url

    def save(self, *args, **kwargs):
        if self.in_reply_to:
            self.visible_to = self.in_reply_to.visible_to

        obj = super(CustomComment, self).save(*args, **kwargs)

        for reply in self.replies.all():
            reply.save()

        return obj