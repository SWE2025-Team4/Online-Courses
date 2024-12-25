from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class CustomPasswordChangeForm(PasswordChangeForm):
    full_name = forms.CharField(max_length=100, required=False, label="Full Name")
    email = forms.EmailField(required=False, label="Email Address")
    phone = forms.CharField(max_length=15, required=False, label="Phone")

    def clean(self):
        print("Form clean method called")  #
        return super().clean()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'image']
        widgets = {
            'phone': forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
        }
