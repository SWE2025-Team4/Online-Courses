from django.contrib.auth.views import PasswordChangeView
from .forms import CustomPasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Profile
from .forms import ProfileForm, ContactMessageForm

from .forms import ProfileForm, ContactMessageForm


class EditProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'base/personInfo.html'

    def get_object(self):
        return self.request.user.profile

    def form_valid(self, form):
        print("Form is valid and saving image.")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Form is invalid.")
        print("Errors:", form.errors)
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('edit-profile')



class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'base/change_password.html'
    success_url = reverse_lazy('password_change_done')

    def dispatch(self, request, *args, **kwargs):
        print("Dispatch method called")  # Debug dispatch method
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print("POST data received:", request.POST)  # Debug POST data
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        # Print a success message for debugging
        print("Password change successful for user:", self.request.user)
        return super().form_valid(form)

    def form_invalid(self, form):
        # Print error details for debugging if the form fails validation
        print("Password change failed. Errors:", form.errors)
        return super().form_invalid(form)

def homeElearning(request):
        courses = Course.objects.all()
        print('courses ==> ', courses)  # Fetch all courses
        return render(request, 'base/main.html', {
            'courses': courses,
            'rating_range': list(range(1, 6)),  # Pass range as a list
        })
    # return render(request, 'base/main.html')

def about_us(request):
    return render(request, 'base/aboutUs.html')

def change_password(request):
    return render(request, 'base/change_password.html')

def person_info(request):
    return render(request, 'base/personInfo.html')


def contact_us(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()  # Save the contact message to the database
            return redirect('contact_success')  # Redirect to the success page
    else:
        form = ContactMessageForm()

    return render(request, 'base/contactUs.html', {'form': form})

def contact_success(request):
    return render(request, 'base/contact_success.html')


from django.shortcuts import render
from course.models import Course


