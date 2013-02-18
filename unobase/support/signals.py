__author__ = 'michael'
from django.dispatch import Signal

user_submitted_support_case = Signal(providing_args=['user', 'request', 'case'])