from django.urls import reverse
from rest_framework.test import APITestCase


class ApiTests(APITestCase):
    def test_health_returns_ok(self):
        response = self.client.get(reverse("health"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")

    def test_hello_default_name(self):
        response = self.client.get(reverse("hello"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Hello, World!")

    def test_hello_custom_name(self):
        response = self.client.get(reverse("hello"), {"name": "Cole"})
        self.assertEqual(response.json()["message"], "Hello, Cole!")

    def test_health_includes_version(self):
        response = self.client.get(reverse("health"))
        self.assertEqual(response.json()["version"], "1.1")
