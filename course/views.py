# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .decorators import custom_login_required
from .forms import CourseForm
from django.db.models import Q
from .models import Course, Enrollment



# View to list all courses
class CourseListView(ListView):
    model = Course
    template_name = 'course/coursesCatalog.html'
    context_object_name = 'courses'
    paginate_by = 10

    def get_queryset(self):

        search_query = self.request.GET.get('search', '').strip()  # Get search query and strip leading/trailing spaces

        print('search_query==>', search_query)  # Debugging output

        if search_query:
            query = (
                    Q(name__icontains=search_query) |
                    Q(category__icontains=search_query) |
                    Q(description__icontains=search_query) |
                    Q(notes__icontains=search_query)
            )
            courses = Course.objects.filter(query).distinct()
            print('courses===>', courses)
            return courses
        else:
            return Course.objects.all()

    def get_context_data(self, **kwargs):
        """
        Add context for grouping courses by category if no search query is provided.
        """
        context = super().get_context_data(**kwargs)
        search_query = self.request.GET.get('search', '').strip()

        # If there's no search query, group courses by category
        if not search_query:
            grouped_courses = {}
            for category_key, category_display in Course.CATEGORY_CHOICES:
                grouped_courses[category_display] = Course.objects.filter(category=category_key)
            context['categories_with_courses'] = grouped_courses

        # Add search query to the context
        context['search_query'] = search_query
        if self.request.user.is_authenticated:
            context['user_enrollments'] = self.request.user.enrollments.all()
        return context

    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_superuser:
    #         return Course.objects.all()
    #
    #     else:
    #         print(f'Instructor {user.username} is viewing their own courses')
    #         return Course.objects.filter(instructor=user)

class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = 'course/courseDetails.html'
    context_object_name = 'course'
    login_url = '/auth/login/?form=login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['playlist'] = self.object.playlists.all()  # Fetch the course's playlist
        return context

@custom_login_required
def enroll_in_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    user = request.user

    # Check if the user is already enrolled
    if not Enrollment.objects.filter(user=user, course=course).exists():
        Enrollment.objects.create(user=user, course=course)

    # Redirect to course details after enrollment
    return redirect('course_detail', pk=course.id)


# View to create a new course
class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'course/create_course.html'
    success_url = reverse_lazy('course_list')

    def form_valid(self, form):
        form.instance.instructor = self.request.user  # Assign the current user as the instructor
        return super().form_valid(form)



# View to update an existing course
class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'course/update_course.html'
    success_url = reverse_lazy('course_list')

    def form_valid(self, form):
        if form.instance.instructor != self.request.user:
            form.instance.instructor = self.request.user  # Ensure the instructor cannot be changed by someone else
        return super().form_valid(form)


# View to delete a course
class CourseDeleteView(LoginRequiredMixin, DeleteView):
    model = Course
    template_name = 'course/delete_course.html'
    success_url = reverse_lazy('course_list')
