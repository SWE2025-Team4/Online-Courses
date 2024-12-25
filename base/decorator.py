from django.http import HttpResponse
from django.shortcuts import render, redirect
from functools import wraps
from django.http import HttpResponseForbidden


def group_required(group_name, redirect_url=None):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.groups.filter(name=group_name).exists():
                return view_func(request, *args, **kwargs)
            else:
                if redirect_url:
                    return redirect(redirect_url)
                else:
                    return HttpResponseForbidden("You do not have permission to access this page.")

        return _wrapped_view

    return decorator


def group_and_authenticated_required(group_name, redirect_url='/login/'):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                # Redirect unauthenticated users to a login page
                return redirect(redirect_url)

            if request.user.groups.filter(name=group_name).exists():
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden("You do not have permission to access this page.")

        return _wrapped_view

    return decorator

# @group_and_authenticated_required('Admin', redirect_url='/login/')

# @group_required('Admin', redirect_url='/not-authorized/')
# def my_view(request):
