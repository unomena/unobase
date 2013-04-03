from django.conf import settings

DEFAULT_IMAGE_CATEGORY_CHOICES = getattr(settings, "DEFAULT_IMAGE_CATEGORY_CHOICES")

AUTH_USER_MODEL = getattr(
    settings,
    "AUTH_USER_MODEL",
    "auth.User"
)
