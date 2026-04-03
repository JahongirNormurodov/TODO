from django.test import TestCase

# Create your tests here.
from rest_framework import status
from rest_framework.test import APITestCase


class ApiRootViewTest(APITestCase):
    def test_api_root_returns_endpoint_index(self):
        response = self.client.get("/api/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Todo DRF API")
        self.assertEqual(response.data["version"], "v1")
        self.assertIn("folders", response.data["endpoints"])
