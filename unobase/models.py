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
from django.contrib.contenttypes import generic
from django.core.urlresolvers import reverse

from photologue.models import ImageModel

from unobase import constants, fields
from unobase import settings as unobase_settings
from constants import STATE_PUBLISHED

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


class PublishedVersionsManager(SiteObjectsManager):
    STATE = constants.STATE_PUBLISHED
    NEXT_STATE = constants.STATE_STAGED
    BOTTOM_STATE = constants.STATE_UNPUBLISHED

    def get_list(self):
        model_type = ContentType.objects.get_for_model(self.model)
        model_qs = Version.objects.filter(
            content_type__pk=model_type.id,
            state=self.STATE
        )
        model_pks = model_qs.values_list('object_id', flat=True)
        model_series = model_qs.values_list('series_id', flat=True)
        next_model_qs = Version.objects.filter(
            content_type__pk=model_type.id,
            state=self.NEXT_STATE
        ).exclude(series_id__in=model_series)
        next_model_pks = next_model_qs.values_list('object_id', flat=True)
        next_model_series = next_model_qs.values_list('series_id', flat=True)
        bottom_model_qs = Version.objects.filter(
            content_type__pk=model_type.id,
            state=self.BOTTOM_STATE
        ).exclude(series_id__in=list(model_series) + list(next_model_series))
        series_ids = {}
        bottom_model_pks = []
        for bottom_model in bottom_model_qs:
            if bottom_model.series_id not in series_ids:
                series_ids[bottom_model.series_id] = None
                bottom_model_pks.append(bottom_model.object_id)
        return self.model.objects.filter(
            pk__in=list(model_pks) + list(next_model_pks) + list(bottom_model_pks)
        ).exclude(state=constants.STATE_DELETED)

    def get_query_set(self):
        model_type = ContentType.objects.get_for_model(self.model)
        model_pks = Version.objects.filter(
            content_type__pk=model_type.id,
            state=self.STATE
        ).values_list('object_id', flat=True)
        return self.model.objects.filter(pk__in=model_pks).exclude(
            state=constants.STATE_DELETED
        )

    def get_console_query_set(self):
        model_type = ContentType.objects.get_for_model(self.model)
        model_pks = Version.objects.filter(
            content_type__pk=model_type.id,
        ).values_list('object_id', flat=True)
        return self.model.objects.filter(pk__in=model_pks).exclude(
            state=constants.STATE_DELETED
        )

    def version_list(self, object_id):
        series = self.get_series(object_id)
        if series is not None:
            qs = series.versions.filter(state=self.STATE)
            for model in qs:
                model.change_url = reverse('%s_%s_change' % (
                    model.content_object._meta.app_label,
                    model.content_object._meta.module_name),
                    args=(model.object_id,)
                )
            return qs
        return []

    def get_series(self, object_id):
        model_type = ContentType.objects.get_for_model(self.model)
        try:
            return Version.objects.get(
                content_type__pk=model_type.id,
                object_id=object_id
            ).series
        except:
            return None

    def add_series(self, slug):
        return VersionSeries.objects.create(
            slug=slug
        )

    def add_version(self, obj):
        model_type = ContentType.objects.get_for_model(self.model)
        series = self.add_series(slugify(str(obj)))
        Version.objects.create(
            content_type=model_type,
            object_id=obj.pk,
            series=series,
            number=1,
            state=obj.state
        )

    def add_to_series(self, series, obj):
        model_type = ContentType.objects.get_for_model(self.model)
        try:
            latest_version_number = Version.objects.filter(
                series=series
            ).order_by('-number')[0].number + 1
        except:
            latest_version_number = 1

#         if Version.objects.filter(
#                 series=series, state=constants.STATE_PUBLISHED).exists():
#             published_version = Version.objects.get(
#                 series=series,
#                 state=constants.STATE_PUBLISHED
#             )
#             published_version.state = constants.STATE_UNPUBLISHED
#             published_version.save()
#             published_version.content_object.state = constants.STATE_UNPUBLISHED
#             published_version.content_object.save()
        Version.objects.create(
            content_type=model_type,
            object_id=obj.pk,
            series=series,
            number=latest_version_number,
            state=constants.STATE_UNPUBLISHED
        )

    def stage_version(self, object_id):
        series = self.get_series(object_id)
        model_type = ContentType.objects.get_for_model(self.model)
        if series is not None and Version.objects.filter(
                series=series, state=constants.STATE_STAGED).exists():
            staged_version = Version.objects.get(
                series=series,
                state=constants.STATE_STAGED
            )
            staged_version.state = constants.STATE_UNPUBLISHED
            staged_version.save()
            staged_version.content_object.state = constants.STATE_UNPUBLISHED
            staged_version.content_object.save()

        version = Version.objects.get(
            content_type__pk=model_type.id,
            object_id=object_id
        )
        version.state = constants.STATE_STAGED
        version.save()
        version.content_object.state = constants.STATE_STAGED
        #version.content_object.publish_date_time = timezone.now()
        version.content_object.save()

    def publish_version(self, object_id):
        series = self.get_series(object_id)
        model_type = ContentType.objects.get_for_model(self.model)

        if series is not None and Version.objects.filter(
                series=series, state=constants.STATE_PUBLISHED).exists():
            published_version = Version.objects.get(
                series=series,
                state=constants.STATE_PUBLISHED
            )
            published_version.state = constants.STATE_UNPUBLISHED
            published_version.save()
            published_version.content_object.state = constants.STATE_UNPUBLISHED
            published_version.content_object.save()
        version = Version.objects.get(
            content_type__pk=model_type.id,
            object_id=object_id
        )
        version.state = constants.STATE_PUBLISHED
        version.save()
        version.content_object.state = constants.STATE_PUBLISHED
        #version.content_object.publish_date_time = timezone.now()
        version.content_object.save()

    def unpublish_version(self, object_id):
        model_type = ContentType.objects.get_for_model(self.model)

        version = Version.objects.get(
            content_type__pk=model_type.id,
            object_id=object_id
        )
        version.state = constants.STATE_UNPUBLISHED
        version.save()
        version.content_object.state = constants.STATE_UNPUBLISHED
        version.content_object.publish_date_time = timezone.now()
        version.content_object.save()

    def delete_version(self, object_id):
        model_type = ContentType.objects.get_for_model(self.model)

        version = Version.objects.get(
            content_type__pk=model_type.id,
            object_id=object_id
        )
        version.state = constants.STATE_DELETED
        version.save()
        version.content_object.state = constants.STATE_DELETED
        #version.content_object.publish_date_time = timezone.now()
        version.content_object.save()


class StagedVersionsManager(PublishedVersionsManager):
    STATE = constants.STATE_STAGED


class UnpublishedVersionsManager(PublishedVersionsManager):
    STATE = constants.STATE_UNPUBLISHED


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
    published_versions = PublishedVersionsManager()
    staged_versions = StagedVersionsManager()
    unpublished_versions = UnpublishedVersionsManager()

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
    slug = models.SlugField(max_length=255, unique=False)
    content = fields.RedactorTextField(blank=True, null=True)
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

        return slug

#         query = self.__class__.objects.filter(
#             slug__startswith=slug
#         ).exclude(id=obj.id).order_by('-id')
#
#         # No collissions
#         if not query.count():
#             return slug
#
#         # Match numerical suffix if it exists
#         match = RE_NUMERICAL_SUFFIX.match(query[0].slug)
#         if match is not None:
#             return "%s-%s" % (slug, int(match.group(1)) + 1)
#         else:
#             return "%s-1" % slug

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


class Template(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='template_images_template')
    path = models.CharField(max_length=255)
    num_contents = models.PositiveSmallIntegerField(default=0)
    num_images = models.PositiveSmallIntegerField(default=0)

    def __unicode__(self):
        return u'%s' % self.name


class ContentTemplate(models.Model):
    slug = models.SlugField()
    template = models.ForeignKey(Template, related_name='content_templates')

    content_1 = models.TextField(blank=True, null=True)
    content_2 = models.TextField(blank=True, null=True)
    content_3 = models.TextField(blank=True, null=True)
    content_4 = models.TextField(blank=True, null=True)
    content_5 = models.TextField(blank=True, null=True)
    content_6 = models.TextField(blank=True, null=True)
    content_7 = models.TextField(blank=True, null=True)
    content_8 = models.TextField(blank=True, null=True)
    content_9 = models.TextField(blank=True, null=True)
    content_10 = models.TextField(blank=True, null=True)

    image_1 = models.ImageField(
        upload_to='template_images', blank=True, null=True
    )
    image_2 = models.ImageField(
        upload_to='template_images', blank=True, null=True
    )
    image_3 = models.ImageField(
        upload_to='template_images', blank=True, null=True
    )
    image_4 = models.ImageField(
        upload_to='template_images', blank=True, null=True
    )
    image_5 = models.ImageField(
        upload_to='template_images', blank=True, null=True
    )
    image_6 = models.ImageField(
        upload_to='template_images', blank=True, null=True
    )
    image_7 = models.ImageField(
        upload_to='template_images', blank=True, null=True
    )
    image_8 = models.ImageField(
        upload_to='template_images', blank=True, null=True
    )
    image_9 = models.ImageField(
        upload_to='template_images', blank=True, null=True
    )
    image_10 = models.ImageField(
        upload_to='template_images', blank=True, null=True
    )

    class Meta:
        abstract = True

    def __unicode__(self):
        return u'%s' % self.slug


class VersionSeries(models.Model):
    slug = models.SlugField(max_length=255)
    staged_slug = models.SlugField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.slug


class Version(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    series = models.ForeignKey(VersionSeries, related_name='versions')
    number = models.PositiveIntegerField()
    state = models.PositiveSmallIntegerField(
        choices=constants.STATE_CHOICES
    )

    def __unicode__(self):
        return u'%s' % self.series


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
    content = models.TextField(blank=True, null=True)


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
