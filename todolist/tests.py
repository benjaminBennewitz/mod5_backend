from django.test import Client
from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
class URLTests(TestCase):
    def test_login(self):
        self.client = Client()
        self.user = User.objects.create_user('test_user', password='test_user')
        self.client.login(username='test_user', password='test_user')
        
        response = self.client.get('/chat/')
        self.assertEqual(response.status_code, 200)
