from functools import wraps
from django.contrib.auth.decorators import user_passes_test

from django.contrib.auth.models import Group
from django.http import Http404
from django.shortcuts import render_to_response, render


def group_required(groups=[]):
    def decorator(func):
        def inner_decorator(request,*args, **kwargs):
            for group in groups:
                try:

                    #print request.user.is_superuser

                    if request.user.is_superuser:
                        return func(request, *args, **kwargs)
                    elif Group.objects.get(name=group) in request.user.groups.all():
                        return func(request, *args, **kwargs)


                except:
                    pass

            return render(request,'users/authentication_message.html')

        return wraps(func)(inner_decorator)

    return decorator




from functools import wraps
from django.utils.translation import ugettext as _
from django.contrib.admin.forms import AdminAuthenticationForm
from django.contrib.auth.views import login
from django.contrib.auth import REDIRECT_FIELD_NAME


def super_user_member_required(view_func):
    """
    Decorator for views that checks that the user is logged in and is a staff
    member, displaying the login page if necessary.
    """
    @wraps(view_func)
    def _checklogin(request, *args, **kwargs):
        if request.user.is_active and request.user.is_superuser:
            # The user is valid. Continue to the admin page.
            return view_func(request, *args, **kwargs)

        assert hasattr(request, 'session'), "The Django admin requires session middleware to be installed. Edit your MIDDLEWARE_CLASSES setting to insert 'django.contrib.sessions.middleware.SessionMiddleware'."
        defaults = {
            'template_name': 'users/authentication_message.html',
            #'authentication_form': AdminAuthenticationForm,
            # 'extra_context': {
            #     'title': _('Log in'),
            #     'app_path': request.get_full_path(),
            #     REDIRECT_FIELD_NAME: request.get_full_path(),
            # },
        }
        return login(request, **defaults)
    return _checklogin


def login_required_custom(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated() and  u.is_active==True,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
from django.contrib.auth import logout
def make_user_logout(u):
    #us
    #logout(request)
    return True