from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django import forms
from .models import Profile, ContactMessage

class CustomPasswordChangeForm(PasswordChangeForm):
    full_name = forms.CharField(max_length=100, required=False, label="Full Name")
    email = forms.EmailField(required=True, label="Email Address")
    phone = forms.CharField(max_length=15, required=True, label="Phone")

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


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your Name',
                'class': 'form-input'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Phone Number',
                'class': 'form-input'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Type your message here',
                'class': 'form-textarea',
                'rows': 4
            }),
        }
