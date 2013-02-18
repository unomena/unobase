'''
Created on 14 Jan 2013

@author: euan
'''
from unobase.commenting import constants

def get_permitted_comments(queryset, user):
    if user.is_superuser:
        return queryset
    elif user.is_staff:
        return queryset.filter(visible_to__lte=constants.COMMENT_VISIBLE_TO_STAFF)
    else:
        return queryset.filter(visible_to=constants.COMMENT_VISIBLE_TO_EVERYONE)