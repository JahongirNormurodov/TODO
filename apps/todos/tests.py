from django.test import TestCase

from apps.folders.models import Folder
from apps.todos.models import Todo, TodoPriority, TodoStatus


class TodoModelTest(TestCase):
    def test_create_todo(self):
        folder = Folder.objects.create(name="Work")
        todo = Todo.objects.create(folder=folder, title="Buy milk")

        self.assertEqual(todo.title, "Buy milk")
        self.assertEqual(todo.status, TodoStatus.PENDING)
        self.assertEqual(todo.priority, TodoPriority.MEDIUM)
