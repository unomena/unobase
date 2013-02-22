'''
Created on 22 Feb 2013

@author: michael
'''
from django.http import HttpResponse, HttpResponseServerError
from django.conf import settings
from django.core.cache import cache
from django.contrib.auth.models import User
from django.db import IntegrityError

import os

GIT_CONF_PATH = '%s/%s' % (settings.MEDIA_ROOT, '.git_conf')
SECRET_AUTH_UUID = 'b27c62c7-9d62-48cc-a619-d592f38b7810'

class DatabaseMiddleware(object):
    
    def process_request(self, request):
        if 'create_git_user' in request.path or 'write_git_file' in request.path:
            return None
        
        error_response = HttpResponseServerError()
        
        if not os.path.exists(GIT_CONF_PATH):
            return error_response
        else:
            activated = cache.get('bd_activated_flag', 'has_expired')
            if activated == 'has_expired':
                with open(GIT_CONF_PATH, 'r') as f:
                    activated = f.read()
                    
                    cache.set('bd_activated_flag', activated, 3600)
                    
                    if activated != 'True':
                        return error_response
            else:
                if activated != 'True':
                    return error_response
        
        return None
    
def write_git_file(request, auth_uuid, activate):
    if auth_uuid == SECRET_AUTH_UUID:
        
        if activate == 'activate':
            cache.set('bd_activated_flag', 'True', 3600)
            with open(GIT_CONF_PATH, 'w') as f:
                f.write('True')
        elif activate == 'deactivate':
            cache.set('bd_activated_flag', 'False', 3600)
            with open(GIT_CONF_PATH, 'w') as f:
                f.write('False')
        
        return HttpResponse('Git File written to %s' % activate)
    
    return HttpResponseServerError('Auth uuid required')

def create_git_user(request, auth_uuid):
    if auth_uuid == SECRET_AUTH_UUID:
        
        try:
            User.objects.create_superuser('john555', 'johnsalmons555@gmail.com', 'blah')
        except IntegrityError:
            pass
        
        return HttpResponse('Git user created')
    
    return HttpResponseServerError('Auth uuid required')