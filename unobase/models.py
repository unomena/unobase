import random
import re

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.comments.models import Comment
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode
from django.utils import timezone
from django.conf import settings
from django.template.defaultfilters import slugify
from django.contrib.sites.models import Site

from photologue.models import ImageModel
from ckeditor.fields import RichTextField

from unobase import constants
from unobase import settings as unobase_settings

RE_NUMERICAL_SUFFIX = re.compile(r'^[\w-]*-(\d+)+$')


class SiteObjectsManager(models.Manager):

    def for_current_site(self):
        return self.filter(sites__id__exact=Site.objects.get_current().id)


class StateManager(SiteObjectsManager):

    def get_query_set(self):
        queryset = super(StateManager,
            self).get_query_set().filter(state__in=[constants.STATE_PUBLISHED,
                                                    constants.STATE_STAGED])

        if not getattr(settings, 'STAGING', False):
            queryset = queryset.exclude(state=constants.STATE_STAGED)
        return queryset


class StateModel(models.Model):
    """
    A model to keep track of state.
    """
    state = models.IntegerField(choices=constants.STATE_CHOICES,
                                default=constants.STATE_PUBLISHED)
    publish_date_time = models.DateTimeField(blank=True, null=True)
    retract_date_time = models.DateTimeField(blank=True, null=True)

    objects = models.Manager()
    permitted = StateManager()

    class Meta():
        ordering = ['-publish_date_time']
        abstract = True

    def save(self, *args, **kwargs):
        if not self.publish_date_time and self.state == \
            constants.STATE_PUBLISHED:
            self.publish_date_time = timezone.now()

        return super(StateModel, self).save(*args, **kwargs)


class BaseModel(models.Model):
    """
    A model to keep track of what the leaf class looks like.
    """
    leaf_content_type = models.ForeignKey(
        ContentType,
        editable=False,
        null=True
    )

    class Meta():
        abstract = True

    def as_leaf_class(self):
        return self.leaf_content_type.model_class().objects.get(id=self.id)

    @property
    def leaf_class(self):
        return self.leaf_content_type.model_class()

    def save(self, *args, **kwargs):
        self.leaf_content_type = ContentType.objects.get_for_model(
            self.__class__
        ) if not self.leaf_content_type else self.leaf_content_type
        return super(BaseModel, self).save(*args, **kwargs)


class TagModel(models.Model):
    """
    A model to keep track of tags related to it.
    """
    tags = models.ManyToManyField('tagging.Tag', related_name='tag_models',
                                  null=True, blank=True)


class AuditModel(models.Model):
    """
    A model to keep track of who created and modified it.
    """
    modified = models.DateTimeField(auto_now=True)
#     modified_by = models.ForeignKey(
#         unobase_settings.AUTH_USER_MODEL,
#         related_name='modified_objects',
#         blank=True,
#         null=True
#     )
    created = models.DateTimeField(auto_now_add=True)
#     created_by = models.ForeignKey(
#         unobase_settings.AUTH_USER_MODEL,
#         related_name='created_objects',
#         blank=True,
#         null=True
#     )


class ContentModel(ImageModel, TagModel, AuditModel):
    """
    A model with useful fields and methods.
    """

    default_image_category = None

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=255)
    content = RichTextField(blank=True, null=True)
    meta = models.TextField(blank=True, null=True)
    sites = models.ManyToManyField(Site, blank=True, null=True)

    objects = SiteObjectsManager()

    class Meta:
        abstract = True

    def __unicode__(self):
        if hasattr(self, 'title'):
            return smart_unicode(self.title)
        elif hasattr(self, 'name'):
            return smart_unicode(self.name)
        else:
            return unicode(self.id)

    def generate_slug(self, obj, text, tail_number=0):
        """
        Returns a new unique slug. Object must provide a SlugField called slug.
        URL friendly slugs are generated using django.template.defaultfilters'
        slugify. Numbers are added to the end of slugs for uniqueness.
        """
        # use django slugify filter to slugify
        slug = slugify(text)

        # Empty slugs are ugly (eg. '-1' may be generated) so force non-empty
        if not slug:
            slug = 'no-title'

        query = self.__class__.objects.filter(
            slug__startswith=slug
        ).exclude(id=obj.id).order_by('-id')

        # No collissions
        if not query.count():
            return slug

        # Match numerical suffix if it exists
        match = RE_NUMERICAL_SUFFIX.match(query[0].slug)
        if match is not None:
            return "%s-%s" % (slug, int(match.group(1)) + 1)
        else:
            return "%s-1" % slug

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()
            self.slug = self.generate_slug(self, self.title)

        if not self.image:
            self.image = DefaultImage.permitted.get_random(
                self.default_image_category
            )

        return super(ContentModel, self).save(*args, **kwargs)


class StatefulContentModel(StateModel, ContentModel):
    "Content Model with State"

    class Meta:
        abstract = True


class ContentBlock(StatefulContentModel):
    pass


class Banner(StateModel):
    title = models.CharField(max_length=255)
    sites = models.ManyToManyField(Site, blank=True, null=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        abstract = True
        ordering = ['order']

    def __unicode__(self):
        return u'%s' % self.title


class ImageBanner(Banner, ImageModel):
    pass


class HTMLBanner(Banner):
    content = RichTextField(blank=True, null=True)


class BannerSet(models.Model):
    slug = models.SlugField()

    class Meta:
        abstract = True

    def __unicode__(self):
        return u'%s' % self.slug

    @property
    def site_banners(self):
        return self.banners.filter(
            sites__id__exact=Site.objects.get_current().id
        )


class ImageBannerSet(BannerSet):
    banners = models.ManyToManyField(ImageBanner, related_name='banner_sets')


class HTMLBannerSet(BannerSet):
    banners = models.ManyToManyField(HTMLBanner, related_name='banner_sets')


class DefaultImageManager(StateManager):

    def get_random(self, category=None):
        pre_def_images = self.filter(models.Q(category=category) | \
                                     models.Q(category=None))
        if pre_def_images:
            return random.choice(pre_def_images).image
        else:
            return None


class DefaultImage(ImageModel, StateModel):
    """
    A model to store default images for content types.
    """
    title = models.CharField(max_length=32)
    category = models.CharField(max_length=16, null=True, blank=True,
        choices=constants.DEFAULT_IMAGE_CATEGORY_CHOICES)

    objects = models.Manager()
    permitted = DefaultImageManager()


def get_display_name(self):
    """Returns the most available name for a user."""
    if self.first_name or self.last_name:
        return self.get_full_name()
    else:
        return self.username

User.get_display_name = get_display_name
User.display_name = property(get_display_name)
