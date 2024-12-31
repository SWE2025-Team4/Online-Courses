from django.contrib import admin
from .models import Course, Playlist, Enrollment
from django.contrib import admin



class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'instructor', 'description', 'created_date', 'written_date', 'category')
    search_fields = ('name', 'description')
    list_filter = ('instructor', 'created_date')
    ordering = ('created_date',)

    # Pagination settings
    list_per_page = 20

class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')


class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'enrolled_date')

admin.site.register(Course, CourseAdmin)
admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)


