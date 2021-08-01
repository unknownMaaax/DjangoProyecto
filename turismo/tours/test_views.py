from django.http import response
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class TourViewsUnitTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_superuser(
            username="admin",
            password="Secret.123",
            email="admin@example.com")
        self.credentials={"username":"admin","password":"Secret.123"}

    def test_home_link(self):
        url = reverse("index")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
    
    def test_login(self):
        response = self.client.post(reverse("login"), self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)
    
    def test_tours(self):
        self.client.login(**self.credentials)
        response=self.client.get(reverse("tours"),follow=True)
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'Tours en Chile', 1)
