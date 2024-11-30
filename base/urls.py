from django.urls import path
from base.views import homeElearning

urlpatterns = [
    path('', homeElearning, name='homeElearning'),
]