from django.contrib import admin
from .models import Profile, ContactMessage

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'image']



@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'message')  # Fields to display in the list view
    search_fields = ('name', 'phone')  # Fields to search by
    list_filter = ('name',)  # Filters for the list view


