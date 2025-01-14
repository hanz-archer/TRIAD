from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from functools import wraps
from django.contrib import messages

def superuser_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # First check if user is authenticated
        if not request.user.is_authenticated:
            messages.error(request, 'Please log in to access this page.')
            return redirect('login')  # Replace 'login' with your login URL name
        
        # Then check if user is superuser
        if not request.user.is_superuser:
            messages.error(request, 'You do not have permission to access this page.')
            return redirect('home')   # Replace 'home' with your homepage URL name
        
        return view_func(request, *args, **kwargs)
    return _wrapped_view 