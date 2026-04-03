from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from apps.categories.models import Category
from apps.folders.models import Folder
from apps.todos.models import Todo


class CategoryModelTest(TestCase):
    def test_create_category(self):
        category = Category.objects.create(name="Personal")

        self.assertEqual(category.name, "Personal")
        self.assertEqual(category.icon, "tag")


class CategoryAPITest(APITestCase):
    def test_list_categories_includes_todo_count(self):
        category = Category.objects.create(name="Personal")
        folder = Folder.objects.create(name="Inbox")
        Todo.objects.create(folder=folder, category=category, title="Plan weekend")

        response = self.client.get("/api/v1/categories/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["name"], "Personal")
        self.assertEqual(response.data[0]["todo_count"], 1)

    def test_create_category_uses_expected_payload_fields(self):
        payload = {
            "name": "Work",
            "color": "#112233",
            "icon": "briefcase",
        }

        response = self.client.post("/api/v1/categories/", payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["icon"], "briefcase")
        self.assertNotIn("position", response.data)
