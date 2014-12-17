'''
Created on 17 Dec 2014

@author: michaelwhelehan
'''
from django.conf import settings

AGE_GATE_LOCATION_CHOICES = getattr(
    settings,
    'AGE_GATE_LOCATION_CHOICES',
    (('Nigeria', 'Nigeria'),)
)
