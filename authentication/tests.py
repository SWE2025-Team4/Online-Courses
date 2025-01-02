from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from base.models import Profile

class AuthenticationViewsTests(TestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')

        self.test_user = User.objects.create_user(username='testuser', password='password123')
        profile, created = Profile.objects.get_or_create(user=self.test_user, defaults={'phone': '1234567890'})
        if not created:
            profile.phone = '1234567890'
            profile.save()


    def test_register_get(self):
        """Test GET request to the registration view."""
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/login.html')
        self.assertContains(response, 'signup')

    def test_register_post_valid_data(self):
        """Test POST request to the registration view with valid data."""
        data = {
            'username': 'newuser',
            'password1': 'password123',
            'password2': 'password123',
            'phone': '9876543210',  
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        user = User.objects.get(username='newuser')
        self.assertIsNotNone(user)
        profile = Profile.objects.get(user=user)
        self.assertEqual(profile.phone, '9876543210')


    def test_register_post_invalid_data(self):
        """Test POST request to the registration view with invalid data."""
        data = {
            'username': '',  
            'password1': 'password123',
            'password2': 'password123',
            'phone': '',  
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/login.html')
        self.assertContains(response, 'This field is required.')  


    def test_login_view_valid_credentials(self):
        """Test POST request to the login view with valid credentials."""
        data = {
            'username': 'testuser',
            'password': 'password123',
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_login_view_invalid_credentials(self):
        """Test POST request to the login view with invalid credentials."""
        data = {
            'username': 'wronguser',
            'password': 'wrongpassword',
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/login.html')
        self.assertContains(response, 'Invalid username or password.')

    def test_logout_view(self):
        """Test GET request to the logout view."""
        self.client.login(username='testuser', password='password123')
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
