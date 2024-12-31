from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=15, blank=True, null=True)  # Phone number field
    image = models.ImageField(null=True, blank=True, upload_to='profile_images/', default='profile_images/default.png')

    def __str__(self):
        return self.user.username




class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    message = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.phone}"