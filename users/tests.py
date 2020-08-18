from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve 
from .forms import CustomUserCreationForm 
from .views import SignupPageView 


class CustomUserTests(TestCase):

	def test_create_user(self):
		User = get_user_model()
		user = User.objects.create_user(
			username='elsaeed',
			email='email@email.com',
			password='testpass123' 
		)
		self.assertEquals(user.username,'elsaeed')
		self.assertEquals(user.email,'email@email.com')
		self.assertTrue(user.is_active)
		self.assertFalse(user.is_staff)
		self.assertFalse(user.is_superuser)

	def test_create_superuser(self):
		User = get_user_model()
		user = User.objects.create_superuser(
			username='admin',
			email='admin@admin.com',
			password='testadmin123'
		)
		self.assertEquals(user.username,'admin')
		self.assertEquals(user.email,'admin@admin.com')
		self.assertTrue(user.is_active)
		self.assertTrue(user.is_staff)
		self.assertTrue(user.is_superuser)

class SignUpTest(TestCase):

	def setUp(self):
		url = reverse('signup')
		self.response = self.client.get(url)

	def test_signup_template(self):
		self.assertEqual(self.response.status_code,200)
		self.assertTemplateUsed(self.response, 'signup.html')
		self.assertContains(self.response, 'Sign Up')
		self.assertNotContains(self.response, 'Hi there I shoudnt be here ')

	def test_signup_form(self): # new
		form = self.response.context.get('form')
		self.assertIsInstance(form, CustomUserCreationForm)
		self.assertContains(self.response, 'csrfmiddlewaretoken')

	def test_signup_view(self): # new
		view = resolve('/accounts/signup/')
		self.assertEqual(view.func.__name__,SignupPageView.as_view().__name__)

