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
            print("Registration form is invalid.")
            print(form.errors)  # Debugging: Log form errors
    else:
        print("Request method is GET for registration.")
        form = CustomUserCreationForm()

    return render(request, 'authentication/login.html', {'form': form, 'form_type': 'signup'})


# Login View
def login_view(request):
    if request.method == 'POST':
        print("Request method is POST for login.")
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"Attempting to authenticate user: {username}")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(f"Authentication successful for user: {username}")
            login(request, user)
            return redirect('/')  # Redirect to home page after login
        else:
            print(f"Authentication failed for user: {username}")
            return redirect('login')  # Redirect back to login if authentication fails
    else:
        print("Request method is GET for login.")
    return render(request, 'authentication/login.html', {'form_type': 'login'})


def logout_view(request):
    logout(request)
    return redirect('/')
