from unobase.blog import models as blog_models

from unobase.forms import Content, State

class Blog(Content):
    class Meta(Content.Meta):
        model = blog_models.Blog
        
        fields = Content.Meta.fields + ['state']

class BlogEntry(Content):
    class Meta(Content.Meta):
        model = blog_models.BlogEntry
        fields = Content.Meta.fields + ['posted_on_behalf_by', 'co_authored_by', 'state']

    def save(self, *args, **kwargs):
        if self.initial.has_key('blog_id'):
            self.instance.blog_id = self.initial['blog_id']

        obj = super(BlogEntry, self).save(*args, **kwargs)

        return obj