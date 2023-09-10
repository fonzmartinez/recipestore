from django.test import TestCase
from .models import User

# Create your tests here.

class UserModelTest(TestCase):
    def setUpTestData():
        User.objects.create(user_id='1', username='johndoe',
        password= 'password123')

    def test_username(self):
        user_recipe = User.objects.get(user_id=1)
        user_field_label = user_recipe._meta.get_field('username').verbose_name
        self.assertEqual(user_field_label, 'username')

    def test_username_max_length(self):
          user_recipe = User.objects.get(user_id=1)
          user_max_length = user_recipe._meta.get_field('username').max_length
          self.assertEqual(user_max_length, 120)

    def test_password(self):
          user_recipe = User.objects.get(user_id=1)
          password_field_label = user_recipe._meta.get_field('password').verbose_name
          self.assertEqual(password_field_label, 'password')

    def test_password_max_length(self):
          user_recipe = User.objects.get(user_id=1)
          password_max_length = user_recipe._meta.get_field('password').max_length
          self.assertEqual(password_max_length, 120)