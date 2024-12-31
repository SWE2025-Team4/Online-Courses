from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from base.models import Profile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    

    class Meta:
        model = User
        fields = ['username', 'email','first_name', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']        
        print("Phone field value:", self.cleaned_data['phone'])  # Debug print
        if commit:
            user.save()
            profile, created = Profile.objects.get_or_create(user=user)
            profile.phone = self.cleaned_data['phone']            
            print("Profile phone before saving:", profile.phone)  # Debug print
            profile.save()
            print("Profile saved successfully:", Profile.objects.get(user=user).phone)
        return user
