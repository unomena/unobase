'''
Created on 05 Mar 2013

@author: michael
'''
from django.views import generic as generic_views
from django.shortcuts import get_object_or_404

from unobase import mixins as unobase_mixins
from unobase import utils as unobase_utils

class AdminMixin(unobase_mixins.ConsoleUserRequiredMixin):
    raise_exception = False
