from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=15, blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='profile_images/', default='profile_images/default.png')

    def __str__(self):
        return self.user.username