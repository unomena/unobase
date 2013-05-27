try:
    from urllib.parse import urlparse, urlunparse
except ImportError:     # Python 2
    from urlparse import urlparse, urlunparse

from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.views import redirect_to_login
from django.core import serializers
from django.core.exceptions import ImproperlyConfigured, PermissionDenied
from django.core.serializers.json import DjangoJSONEncoder
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from django.utils.decorators import method_decorator
from django.utils.http import urlquote
from django.views.generic import CreateView
from django.utils.decorators import available_attrs

from functools import wraps

from unobase.decorators import login_required
from unobase import models
from unobase.eula import models as eula_models

class LoginRequiredMixin(object):
    """
    View mixin which verifies that the user has authenticated.

    NOTE:
        This should be the left-most mixin of a view.
    """
    message = None

    @method_decorator(login_required(msg=message))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request,
            *args, **kwargs)
        
class ConsoleUserRequiredMixin(object):
    """
    Mixin allows you to require a user with `is_superuser` set to True.
    """
    login_url = settings.LOGIN_URL  # LOGIN_URL from project settings
    raise_exception = False  # Default whether to raise an exception to none
    redirect_field_name = REDIRECT_FIELD_NAME  # Set by django.contrib.auth

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_console_user and not request.user.is_admin and not request.user.is_admin:  # If the user is a standard user,
            if self.raise_exception:  # *and* if an exception was desired
                raise PermissionDenied  # return a forbidden response.
            else:
                return redirect_to_login(request.get_full_path(),
                    self.login_url,
                    self.redirect_field_name)

        return super(ConsoleUserRequiredMixin, self).dispatch(request,
            *args, **kwargs)

class SuperuserRequiredMixin(object):
    """
    Mixin allows you to require a user with `is_superuser` set to True.
    """
    login_url = settings.LOGIN_URL  # LOGIN_URL from project settings
    raise_exception = False  # Default whether to raise an exception to none
    redirect_field_name = REDIRECT_FIELD_NAME  # Set by django.contrib.auth

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:  # If the user is a standard user,
            if self.raise_exception:  # *and* if an exception was desired
                raise PermissionDenied  # return a forbidden response.
            else:
                return redirect_to_login(request.get_full_path(),
                    self.login_url,
                    self.redirect_field_name)

        return super(SuperuserRequiredMixin, self).dispatch(request,
            *args, **kwargs)
        
class AdminRequiredMixin(object):
    """
    Mixin allows you to require a user with `is_superuser` set to True.
    """
    login_url = settings.LOGIN_URL  # LOGIN_URL from project settings
    raise_exception = False  # Default whether to raise an exception to none
    redirect_field_name = REDIRECT_FIELD_NAME  # Set by django.contrib.auth

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_admin:  # If the user is a standard user,
            if self.raise_exception:  # *and* if an exception was desired
                raise PermissionDenied  # return a forbidden response.
            else:
                return redirect_to_login(request.get_full_path(),
                    self.login_url,
                    self.redirect_field_name)

        return super(AdminRequiredMixin, self).dispatch(request,
            *args, **kwargs)

class PermissionRequiredMixin(object):
    """
    View mixin which verifies that the logged in user has the specified
    permission.

    Class Settings
    `permission_required` - the permission to check for.
    `login_url` - the login url of site
    `redirect_field_name` - defaults to "next"
    `raise_exception` - defaults to False - raise 403 if set to True

    Example Usage

        class SomeView(PermissionRequiredMixin, ListView):
            ...
            # required
            permission_required = "app.permission"

            # optional
            login_url = "/signup/"
            redirect_field_name = "hollaback"
            raise_exception = True
            ...
    """
    login_url = settings.LOGIN_URL  # LOGIN_URL from project settings
    permission_required = None  # Default required perms to none
    raise_exception = False  # Default whether to raise an exception to none
    redirect_field_name = REDIRECT_FIELD_NAME  # Set by django.contrib.auth

    def dispatch(self, request, *args, **kwargs):
        # Make sure that a permission_required is set on the view,
        # and if it is, that it only has two parts (app.action_model)
        # or raise a configuration error.
        if self.permission_required == None or len(
            self.permission_required.split(".")) != 2:
            raise ImproperlyConfigured("'PermissionRequiredMixin' requires "
                                       "'permission_required' attribute to be set.")

        # Check to see if the request's user has the required permission.
        has_permission = request.user.has_perm(self.permission_required)

        if not has_permission:  # If the user lacks the permission
            if self.raise_exception:  # *and* if an exception was desired
                raise PermissionDenied  # return a forbidden response.
            else:
                return redirect_to_login(request.get_full_path(),
                    self.login_url,
                    self.redirect_field_name)

        return super(PermissionRequiredMixin, self).dispatch(request,
            *args, **kwargs)

class PermissionOrCreatorRequiredMixin(object):
    """
    View mixin which verifies that the logged in user has the specified
    permission.

    Class Settings
    `permission_required` - the permission to check for.
    `login_url` - the login url of site
    `redirect_field_name` - defaults to "next"
    `raise_exception` - defaults to False - raise 403 if set to True

    Example Usage

        class SomeView(PermissionRequiredMixin, ListView):
            ...
            # required
            permission_required = "app.permission"

            # optional
            login_url = "/signup/"
            redirect_field_name = "hollaback"
            raise_exception = True
            ...
    """
    login_url = settings.LOGIN_URL  # LOGIN_URL from project settings
    permission_required = None  # Default required perms to none
    raise_exception = False  # Default whether to raise an exception to none
    redirect_field_name = REDIRECT_FIELD_NAME  # Set by django.contrib.auth

    def get(self, request, *args, **kwargs):
        # Make sure that a permission_required is set on the view,
        # and if it is, that it only has two parts (app.action_model)
        # or raise a configuration error.
        if self.permission_required == None or len(
            self.permission_required.split(".")) != 2:
            raise ImproperlyConfigured("'PermissionOrCreatorRequiredMixin' requires "
                                       "'permission_required' attribute to be set.")

        # Check to see if the request's user has the required permission.
        has_permission = request.user.has_perm(self.permission_required)
        user_created = request.user == self.get_object().created_by

        if not has_permission and not user_created:  # If the user lacks the permission
            if self.raise_exception:  # *and* if an exception was desired
                raise PermissionDenied  # return a forbidden response.
            else:
                return redirect_to_login(request.get_full_path(),
                    self.login_url,
                    self.redirect_field_name)

        return super(PermissionOrCreatorRequiredMixin, self).get(request,
            *args, **kwargs)

class MultiplePermissionsRequiredMixin(object):
    """
    View mixin which allows you to specify two types of permission
    requirements. The `permissions` attribute must be a dict which
    specifies two keys, `all` and `any`. You can use either one on
    it's own or combine them. Both keys values are required be a list or
    tuple of permissions in the format of
    <app label>.<permission codename>

    By specifying the `all` key, the user must have all of
    the permissions in the passed in list.

    By specifying The `any` key , the user must have ONE of the set
    permissions in the list.

    Class Settings
        `permissions` - This is required to be a dict with one or both
            keys of `all` and/or `any` containing a list or tuple of
            permissions in the format of <app label>.<permission codename>
        `login_url` - the login url of site
        `redirect_field_name` - defaults to "next"
        `raise_exception` - defaults to False - raise 403 if set to True

    Example Usage
        class SomeView(MultiplePermissionsRequiredMixin, ListView):
            ...
            #required
            permissions = {
                "all": (blog.add_post, blog.change_post),
                "any": (blog.delete_post, user.change_user)
            }

            #optional
            login_url = "/signup/"
            redirect_field_name = "hollaback"
            raise_exception = True
    """
    login_url = settings.LOGIN_URL  # LOGIN_URL from project settings
    permissions = None  # Default required perms to none
    raise_exception = False  # Default whether to raise an exception to none
    redirect_field_name = REDIRECT_FIELD_NAME  # Set by django.contrib.auth

    def dispatch(self, request, *args, **kwargs):
        self._check_permissions_attr()

        perms_all = self.permissions.get('all') or None
        perms_any = self.permissions.get('any') or None

        self._check_permissions_keys_set(perms_all, perms_any)
        self._check_perms_keys("all", perms_all)
        self._check_perms_keys("any", perms_any)

        # If perms_all, check that user has all permissions in the list/tuple
        if perms_all:
            if not request.user.has_perms(perms_all):
                if self.raise_exception:
                    raise PermissionDenied
                return redirect_to_login(request.get_full_path(),
                    self.login_url,
                    self.redirect_field_name)

        # If perms_any, check that user has at least one in the list/tuple
        if perms_any:
            has_one_perm = False
            for perm in perms_any:
                if request.user.has_perm(perm):
                    has_one_perm = True
                    break

            if not has_one_perm:
                if self.raise_exception:
                    raise PermissionDenied
                return redirect_to_login(request.get_full_path(),
                    self.login_url,
                    self.redirect_field_name)

        return super(MultiplePermissionsRequiredMixin, self).dispatch(request,
            *args, **kwargs)

    def _check_permissions_attr(self):
        """
        Check permissions attribute is set and that it is a dict.
        """
        if self.permissions is None or not isinstance(self.permissions, dict):
            raise ImproperlyConfigured("'PermissionsRequiredMixin' requires "
                                       "'permissions' attribute to be set to a dict.")

    def _check_permissions_keys_set(self, perms_all=None, perms_any=None):
        """
        Check to make sure the keys `any` or `all` are not both blank.
        If both are blank either an empty dict came in or the wrong keys
        came in. Both are invalid and should raise an exception.
        """
        if perms_all is None and perms_any is None:
            raise ImproperlyConfigured("'PermissionsRequiredMixin' requires"
                                       "'permissions' attribute to be set to a dict and the 'any' "
                                       "or 'all' key to be set.")

    def _check_perms_keys(self, key=None, perms=None):
        """
        If the permissions list/tuple passed in is set, check to make
        sure that it is of the type list or tuple.
        """
        if perms and not isinstance(perms, (list, tuple)):
            raise ImproperlyConfigured("'MultiplePermissionsRequiredMixin' "
                                       "requires permissions dict '%s' value to be a list "
                                       "or tuple." % key)

class RoleCheckMixin(object):
    """
    Mixin allows you to require a user with `is_superuser` set to True.
    """
    login_url = settings.LOGIN_URL  # LOGIN_URL from project settings
    raise_exception = False  # Default whether to raise an exception to none
    redirect_field_name = REDIRECT_FIELD_NAME  # Set by django.contrib.auth
    role_required = None
    role_only = False

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if self.role_required == None:
            raise ImproperlyConfigured("'RoleCheckMixin' requires "
                                       "'role_required' attribute to be set.")

        if self.role_only:
            role_meets_requirements = request.user.is_staff or \
                                      request.user.role >= settings.ADMIN_ROLE or \
                                      request.user.role == self.role_required
        else:
            role_meets_requirements = request.user.is_staff or \
                                      request.user.role >= settings.ADMIN_ROLE or \
                                      request.user.role >= self.role_required

        if not role_meets_requirements:  # If the user doesn't have role,
            if self.raise_exception:  # *and* if an exception was desired
                raise PermissionDenied  # return a forbidden response.
            else:
                return redirect_to_login(request.get_full_path(),
                    self.login_url,
                    self.redirect_field_name)

        return super(RoleCheckMixin, self).dispatch(request,
            *args, **kwargs)

class FilterMixin(object):

    def get_queryset_filters(self):
        filters = {}
        for item in self.allowed_filters:
            if item in self.request.GET and self.request.GET[item]:
                filters[self.allowed_filters[item]] = self.request.GET[item]

        return filters

    def get_queryset(self):
        return super(FilterMixin, self).get_queryset()\
            .filter(**self.get_queryset_filters())
        
def redirect_to_eula(next, eula_url=None,
                      redirect_field_name='next'):
    """
    Redirects the user to the login page, passing the given 'next' page
    """

    login_url_parts = list(urlparse(eula_url))
    if redirect_field_name:
        querystring = QueryDict(login_url_parts[4], mutable=True)
        querystring[redirect_field_name] = next
        login_url_parts[4] = querystring.urlencode(safe='/')

    return HttpResponseRedirect(urlunparse(login_url_parts))
        
class EULAAcceptedMixin(object):
    eula_url = None
    raise_exception = False  # Default whether to raise an exception to none

    def dispatch(self, request, *args, **kwargs):
        try:
            if request.user.eula_accepted.version != eula_models.EULA.objects.latest_eula().version:  # If the user is a standard user,
                if self.raise_exception:  # *and* if an exception was desired
                    raise PermissionDenied  # return a forbidden response.
                else:
                    return redirect_to_eula(request.get_full_path(),
                        self.eula_url)
        except AttributeError:
            if self.raise_exception:  # *and* if an exception was desired
                raise PermissionDenied  # return a forbidden response.
            else:
                return redirect_to_eula(request.get_full_path(),
                    self.eula_url)

        return super(EULAAcceptedMixin, self).dispatch(request,
            *args, **kwargs)
        
def redirect_to_age_gate(next, age_gate_url=None,
                      redirect_field_name='next'):
    """
    Redirects the user to the login page, passing the given 'next' page
    """

    login_url_parts = list(urlparse(age_gate_url))
    if redirect_field_name:
        querystring = QueryDict(login_url_parts[4], mutable=True)
        querystring[redirect_field_name] = next
        login_url_parts[4] = querystring.urlencode(safe='/')

    return HttpResponseRedirect(urlunparse(login_url_parts))
        
class AgeGateMixin(object):
    age_gate_url = None
    raise_exception = False  # Default whether to raise an exception to none

    def dispatch(self, request, *args, **kwargs):
        user_date_of_birth = request.session.get('user_date_of_birth')
        country_date_of_birth_required = request.session.get('country_date_of_birth_required')
        
        if user_date_of_birth is not None and country_date_of_birth_required is not None:
            if  user_date_of_birth > country_date_of_birth_required:  # If the user is a standard user,
                if self.raise_exception:  # *and* if an exception was desired
                    raise PermissionDenied  # return a forbidden response.
                else:
                    return redirect_to_age_gate(request.get_full_path(), self.age_gate_url)
        else:
            if self.raise_exception:  # *and* if an exception was desired
                raise PermissionDenied  # return a forbidden response.
            else:
                return redirect_to_age_gate(request.get_full_path(), self.age_gate_url)

        return super(AgeGateMixin, self).dispatch(request,
            *args, **kwargs)
    