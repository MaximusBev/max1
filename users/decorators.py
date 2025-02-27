from django.http import HttpResponseForbidden
from functools import wraps

def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.role != 'admin':
            return HttpResponseForbidden("Tylko administratorzy mają dostęp do tej strony.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view
