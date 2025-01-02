from django.test import TestCase
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser, User
from course.decorators import custom_login_required
from django.test import TestCase
from course.forms import CourseForm
from django.contrib.auth.models import User
from course.models import Course, Playlist
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from course.views import CourseListView, CourseDetailView, enroll_in_course, my_list
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from course.views import CourseListView, CourseDetailView, enroll_in_course, my_list
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from course.models import Course, Enrollment
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from course.models import Course, Enrollment


class CustomLoginRequiredTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username="admin", password="password")

    def test_authenticated_user(self):
        request = self.factory.get("/")
        request.user = self.user

        @custom_login_required
        def test_view(request):
            return "View Accessed"

        response = test_view(request)
        self.assertEqual(response, "View Accessed")

    def test_anonymous_user(self):
        request = self.factory.get("/")
        request.user = AnonymousUser()

        @custom_login_required
        def test_view(request):
            return "View Accessed"

        response = test_view(request)
        self.assertNotEqual(response, "View Accessed")


class CourseFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="admin", password="password")

    def test_valid_form(self):
        form = CourseForm(
            data={
                "name": "Test Course",
                "description": "Test description",
                "notes": "Test notes",
                "video_url": "https://example.com",
                "instructor": self.user.id,
                "category": "frontend",
            }
        )
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = CourseForm(data={})
        self.assertFalse(form.is_valid())


class CourseModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="admin", password="admin")
        self.course = Course.objects.create(
            name="Test Course",
            description="This is a test course",
            notes="Test notes",
            category="frontend",
            instructor=self.user,
        )

    def test_course_creation(self):
        self.assertEqual(self.course.name, "Test Course")
        self.assertEqual(self.course.category, "frontend")
        self.assertEqual(self.course.instructor, self.user)

    def test_playlist_creation(self):
        playlist = Playlist.objects.create(
            course=self.course, title="Test Playlist", video_url="https://example.com/video"
        )
        self.assertEqual(playlist.title, "Test Playlist")
        self.assertEqual(playlist.course, self.course)

    def test_enrollment_creation(self):
        enrollment = Enrollment.objects.create(user=self.user, course=self.course)
        self.assertEqual(enrollment.user, self.user)
        self.assertEqual(enrollment.course, self.course)

    def test_unique_enrollment(self):
        Enrollment.objects.create(user=self.user, course=self.course)
        with self.assertRaises(Exception):
            Enrollment.objects.create(user=self.user, course=self.course)


class TestUrls(SimpleTestCase):
    def test_course_list_url(self):
        url = reverse("course_list")
        self.assertEqual(resolve(url).func.view_class, CourseListView)

    def test_course_detail_url(self):
        url = reverse("course_detail", args=[1])
        self.assertEqual(resolve(url).func.view_class, CourseDetailView)

    def test_enroll_in_course_url(self):
        url = reverse("course_enroll", args=[1])
        self.assertEqual(resolve(url).func, enroll_in_course)

    def test_my_list_url(self):
        url = reverse("my_list")
        self.assertEqual(resolve(url).func, my_list)


class CourseListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="admin", password="password")
        self.course = Course.objects.create(
            name="Test Course",
            description="Test description",
            category="frontend",
            instructor=self.user,
        )

    def test_course_list_view(self):
        response = self.client.get(reverse("course_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "course/coursesCatalog.html")
        self.assertContains(response, "Test Course")

    def test_course_detail_view(self):
        self.client.login(username="admin", password="password")
        response = self.client.get(reverse("course_detail", args=[self.course.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "course/courseDetails.html")
        self.assertContains(response, "Test Course")

    def test_enroll_in_course_view(self):
        self.client.login(username="admin", password="password")
        response = self.client.get(reverse("course_enroll", args=[self.course.id]))
        self.assertRedirects(response, reverse("course_detail", args=[self.course.id]))
        self.assertTrue(Enrollment.objects.filter(user=self.user, course=self.course).exists())

class MyListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="admin", password="password")
        self.course = Course.objects.create(
            name="Test Course",
            description="Test description",
            category="frontend",
            instructor=self.user,
        )
        Enrollment.objects.create(user=self.user, course=self.course)

    def test_my_list_view(self):
        self.client.login(username="admin", password="password")
        response = self.client.get(reverse("my_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "course/my_list.html")
        self.assertContains(response, "Test Course")
