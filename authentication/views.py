from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm  # Import the custom form

def register(request):
    if request.method == 'POST':
        print("Registration form:", request.POST)
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print("Registration form is valid.")
            user = form.save()
            login(request, user)
            return redirect('/')  # Redirect to the login page after successful registration
        else:
            return render(request, 'authentication/login.html', {
                'form': form,
                'form_type': 'signup',  # Indicate this is the signup form
                'error_message': form.errors.as_ul()  # Render errors as an unordered list
            })            
    else:
        print("Request method is GET for registration.")
        form = CustomUserCreationForm()

    return render(request, 'authentication/login.html', {'form': form, 'form_type': 'signup'})


# Login View
def login_view(request):
    error_message = None  # Initialize error message
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # Redirect to the homepage on successful login
        else:
            error_message = "Invalid username or password. Please try again."

    # Preserve the query parameters    
    return render(request, 'authentication/login.html', {
        'form_type': 'login',
        'error_message': error_message        
    })


def logout_view(request):
    logout(request)
    return redirect('/')
