from django.shortcuts import redirect

class CustomLoginMiddleware:
    """
    Middleware to redirect unauthenticated users to a custom login page.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path.startswith('/course/enroll/'):
            return redirect('/auth/login/?form=login')
        return self.get_response(request)
