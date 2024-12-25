# urls.py
from django.urls import path
from .views import CourseListView, CourseCreateView, CourseUpdateView, CourseDeleteView, CourseDetailView

urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('coursedetails/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    # path('create/', CourseCreateView.as_view(), name='course_create'),
    # path('update/<int:pk>/', CourseUpdateView.as_view(), name='course_update'),
    # path('delete/<int:pk>/', CourseDeleteView.as_view(), name='course_delete'),
]
