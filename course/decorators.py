from django.shortcuts import redirect
from functools import wraps

def custom_login_required(view_func):
    """
    Custom login_required decorator that redirects to /auth/login/?form=login
    """
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/auth/login/?form=login')
        return view_func(request, *args, **kwargs)
    return wrapped_view
