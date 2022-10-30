from django.test import TestCase
from django.urls import reverse

class HomePageTest(TestCase):
    def test_home_url(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)


class HomeTemplateTest(TestCase):
    def test_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')