from django.urls import path
from base.views import homeElearning, contact_us, about_us, change_password, person_info, EditProfileView, \
    contact_success, update_person_info
from .views import CustomPasswordChangeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', homeElearning, name='homeElearning'),
    path('contactUs', contact_us, name='contactUs'),
    path('contact-success', contact_success, name='contact_success'),
    path('aboutUs', about_us, name='aboutUs'),
    path('change-password', CustomPasswordChangeView.as_view(), name='change-password'),
    path('password-change-done', CustomPasswordChangeView.as_view(template_name='base/password_change_done.html'),
         name='password_change_done'),
    path('person-info/', person_info, name='person-info'),  # URL for viewing personal info
    path('update-person-info/', update_person_info, name='update-person-info'),  # URL to handle info update
    path('edit-profile', EditProfileView.as_view(), name='edit-profile'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
