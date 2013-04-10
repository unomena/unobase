import models

__author__ = 'michael'

from unobase.forms import Content, State

class Blog(Content, State):
    class Meta(Content.Meta):
        model = models.Blog
        
        fields = Content.Meta.fields + ['state']

class BlogEntry(Content, State):
    class Meta(Content.Meta):
        model = models.BlogEntry
        fields = Content.Meta.fields + ['posted_on_behalf_by', 'state']

    def save(self, *args, **kwargs):
        if self.initial.has_key('blog_id'):
            self.instance.blog_id = self.initial['blog_id']

        obj = super(BlogEntry, self).save(*args, **kwargs)

        return obj