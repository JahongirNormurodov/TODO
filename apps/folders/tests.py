from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from apps.folders.models import Folder
from apps.todos.models import Todo


class FolderModelTest(TestCase):
    def test_create_folder(self):
        folder = Folder.objects.create(name="Work")

        self.assertEqual(folder.name, "Work")
        self.assertEqual(folder.icon, "folder")


class FolderAPITest(APITestCase):
    def test_list_folders_is_sorted_by_position_and_includes_todo_count(self):
        later = Folder.objects.create(name="Later", position=2)
        earlier = Folder.objects.create(name="Earlier", position=1)
        Todo.objects.create(folder=earlier, title="First task")
        Todo.objects.create(folder=later, title="Second task")

        response = self.client.get("/api/v1/folders/")
        items_by_name = {item["name"]: item for item in response.data}
        ordered_names = [item["name"] for item in response.data]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Earlier", items_by_name)
        self.assertIn("Later", items_by_name)
        self.assertLess(ordered_names.index("Earlier"), ordered_names.index("Later"))
        self.assertEqual(items_by_name["Earlier"]["todo_count"], 1)

    def test_create_folder_accepts_position_field(self):
        payload = {
            "name": "Backlog",
            "color": "#445566",
            "icon": "archive",
            "position": 3,
        }

        response = self.client.post("/api/v1/folders/", payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["position"], 3)
