from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from .decorators import custom_login_required
from .forms import CourseForm
from .models import Course, Enrollment


# View to list all courses
class CourseListView(ListView):
    model = Course
    template_name = 'course/coursesCatalog.html'
    context_object_name = 'courses'
    paginate_by = 10

    def get_queryset(self):
        search_query = self.request.GET.get('search', '').strip()
        if search_query:
            query = (
                Q(name__icontains=search_query) |
                Q(category__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(notes__icontains=search_query)
            )
            return Course.objects.filter(query).distinct()
        else:
            return Course.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_query = self.request.GET.get('search', '').strip()

        # Group courses by category if no search query
        if not search_query:
            grouped_courses = {}
            for category_key, category_display in Course.CATEGORY_CHOICES:
                grouped_courses[category_display] = Course.objects.filter(category=category_key)
            context['categories_with_courses'] = grouped_courses

        context['search_query'] = search_query

        # Add enrollment data
        if self.request.user.is_authenticated:
            user_enrollments = self.request.user.enrollments.all()
            enrolled_course_ids = user_enrollments.values_list('course_id', flat=True)
            context['user_enrolled_courses'] = set(enrolled_course_ids)
        else:
            context['user_enrolled_courses'] = set()

        return context


class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = 'course/courseDetails.html'
    context_object_name = 'course'
    login_url = '/auth/login/?form=login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['playlist'] = self.object.playlists.all()
        return context


@custom_login_required
def enroll_in_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    user = request.user

    if not Enrollment.objects.filter(user=user, course=course).exists():
        Enrollment.objects.create(user=user, course=course)

    return redirect('course_detail', pk=course.id)


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'course/create_course.html'
    success_url = reverse_lazy('course_list')

    def form_valid(self, form):
        form.instance.instructor = self.request.user
        return super().form_valid(form)


class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'course/update_course.html'
    success_url = reverse_lazy('course_list')

    def form_valid(self, form):
        if form.instance.instructor != self.request.user:
            form.instance.instructor = self.request.user
        return super().form_valid(form)


class CourseDeleteView(LoginRequiredMixin, DeleteView):
    model = Course
    template_name = 'course/delete_course.html'
    success_url = reverse_lazy('course_list')
