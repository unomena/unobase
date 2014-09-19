__author__ = 'michael'
from django.dispatch import Signal

user_commented = Signal(providing_args=['user', 'request', 'comment'])