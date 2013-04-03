import models

__author__ = 'michael'

from unobase.forms import Content

class Blog(Content):
    class Meta(Content.Meta):
        model = models.Blog

class BlogEntry(Content):
    class Meta(Content.Meta):
        model = models.BlogEntry
        fields = Content.Meta.fields + ['posted_on_behalf_by']

    def save(self, *args, **kwargs):
        if self.initial.has_key('blog_id'):
            self.instance.blog_id = self.initial['blog_id']

        obj = super(BlogEntry, self).save(*args, **kwargs)

        return obj