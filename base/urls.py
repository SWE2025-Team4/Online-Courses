from django.urls import path
from base.views import homeElearning, contact_us, about_us, change_password, person_info, EditProfileView
from .views import CustomPasswordChangeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', homeElearning, name='homeElearning'),
    path('contactUs', contact_us, name='contactUs'),
    path('aboutUs', about_us, name='aboutUs'),
    path('person-info', person_info, name='person-info'),
    path('change-password/', CustomPasswordChangeView.as_view(), name='change-password'),
    path('password-change-done/', CustomPasswordChangeView.as_view(template_name='base/password_change_done.html'),
         name='password_change_done'),
    path('edit-profile/', EditProfileView.as_view(), name='edit-profile'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
