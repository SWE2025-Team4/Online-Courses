from django.contrib import admin
from .models import Course, Playlist

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'instructor', 'description', 'created_date', 'written_date', 'category')
    search_fields = ('name', 'description')
    list_filter = ('instructor', 'created_date')
    ordering = ('created_date',)

    # Pagination settings
    list_per_page = 20

class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')

admin.site.register(Course, CourseAdmin)
admin.site.register(Playlist, PlaylistAdmin)
