__author__ = 'michael'

from django.db import models

from unobase import models as unobase_models

class Tag(unobase_models.StateModel):
    title = models.CharField(max_length=32)
    description = models.TextField(null=True, blank=True)
