import random
import re

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.comments.models import Comment
from django.utils.encoding import smart_unicode
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from django.template.defaultfilters import slugify

from photologue.models import ImageModel
from ckeditor.fields import RichTextField

from unobase import constants

RE_NUMERICAL_SUFFIX = re.compile(r'^[\w-]*-(\d+)+$')

class BaseModel(ImageModel):
    leaf_content_type = models.ForeignKey(ContentType, editable=False, null=True)

    def as_leaf_class(self):
        """
        Returns the leaf class no matter where the calling instance is in
        the inheritance hierarchy.
        Inspired by http://www.djangosnippets.org/snippets/1031/
        """
        try:
            return self.__getattribute__(self.class_name.lower())
        except AttributeError:
            content_type = self.leaf_content_type
            model = content_type.model_class()
            if(model == BaseModel):
                return self
            return model.objects.get(id=self.id)

    def save(self, *args, **kwargs):
        # set leaf class content type
        if not self.leaf_content_type:
            self.leaf_content_type = ContentType.objects.get_for_model(
                self.__class__
            )

        return super(BaseModel, self).save(*args, **kwargs)

class TagModel(BaseModel):
    tags = models.ManyToManyField('tagging.Tag', null=True, blank=True, related_name='tag_models')

    @staticmethod
    def get_tags(model_type):
        tags = []
        for tag_model in TagModel.objects.filter(leaf_content_type__model=model_type):
            for tag in tag_model.tags.all():
                tags.append(tag)

        return tags
    
    @staticmethod
    def get_distinct_tags(model_type):
        from unobase.tagging.models import Tag
        return Tag.objects.filter(tag_models__leaf_content_type__model=model_type).distinct()

    @staticmethod
    def get_tag_ratio(tag, model_type):
        tag_list = TagModel.get_tags(model_type)

        tag_set = set(tag_list)
        tag_numbers = []
        total_tags = float(len(tag_list))
        ratios = []

        for i, tag in enumerate(tag_set):
            tag_numbers.append(tag_list.count(tag))
            ratios.append(int((tag_numbers[i] / total_tags) * 10))

        return ratios[list(tag_set).index(tag)]

class StateManager(models.Manager):

    def get_query_set(self):
        queryset = super(StateManager,
            self).get_query_set().filter(state__in=[constants.STATE_PUBLISHED,
                                                    constants.STATE_STAGED])
        # exclude objects in staging state if not in staging mode (settings.STAGING = False)
        if not getattr(settings, 'STAGING', False):
            queryset = queryset.exclude(state=constants.STATE_STAGED)
        return queryset

class StateModel(TagModel):
    state = models.IntegerField(choices=constants.STATE_CHOICES,
        default=constants.STATE_PUBLISHED)
    publish_date_time = models.DateTimeField(blank=True, null=True)
    retract_date_time = models.DateTimeField(blank=True, null=True)

    class Meta():
        ordering = ['-publish_date_time']
        
    def save(self, *args, **kwargs):
        if not self.publish_date_time and self.state == constants.STATE_PUBLISHED:
            self.publish_date_time = timezone.now()
            
        return super(StateModel, self).save(*args, **kwargs)

#    @staticmethod
#    def set_permitted_manager(sender, **kwargs):
#        if issubclass(sender, StateModel) and not hasattr(sender, 'permitted'):
#            sender.add_to_class('permitted', StateManager())
#
#models.signals.class_prepared.connect(StateModel.set_permitted_manager)

class ContentModel(StateModel):
    """
    A model with useful fields and methods.
    """

    default_image_category = None

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, editable=False, db_index=True, unique=True)
    content = RichTextField(blank=True, null=True)
    modified = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, related_name='modified_objects', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_objects', blank=True, null=True)
        
    def __unicode__(self):
        if hasattr(self,'title'):
            return smart_unicode(self.title)
        elif hasattr(self,'name'):
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
            
        query = ContentModel.objects.filter(
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
            self.image = DefaultImage.permitted.get_random(self.default_image_category)

        return super(ContentModel, self).save(*args, **kwargs)

class TagOnlyContentModel(TagModel):
    """
    A model with useful fields and methods.
    """

    default_image_category = None

    title = models.CharField(max_length=200)
    content = RichTextField(blank=True, null=True)
    modified = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, related_name='tag_only_modified_objects', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='tag_only_created_objects', blank=True, null=True)

    class Meta():
        def __init__(self, *args, **kwargs):
            if hasattr(self,'title'):
                self.ordering = ['title']
            elif hasattr(self,'name'):
                self.ordering = ['name']

    def __unicode__(self):
        if hasattr(self,'title'):
            return smart_unicode(self.title)
        elif hasattr(self,'name'):
            return smart_unicode(self.name)
        else:
            return unicode(self.id)

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()

        if not self.image:
            self.image = DefaultImage.permitted.get_random(self.default_image_category)

        return super(TagOnlyContentModel, self).save(*args, **kwargs)

class DefaultImageManager(StateManager):

    def get_random(self, category=None):
        pre_def_images = self.filter(models.Q(category=category)|models.Q(category=None))
        if pre_def_images:
            return random.choice(pre_def_images).image
        else:
            return None

class DefaultImage(StateModel):
    title = models.CharField(max_length=32)
    category = models.CharField(max_length=16, null=True, blank=True,
        choices=constants.DEFAULT_IMAGE_CATEGORY_CHOICES)

    permitted = DefaultImageManager()
    
def get_display_name(self):
    """Returns the most available name for a user."""
    if self.first_name or self.last_name:
        return self.get_full_name()
    else:
        return self.username

User.get_display_name = get_display_name
User.display_name = property(get_display_name)    