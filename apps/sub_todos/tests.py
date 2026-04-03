from django.test import TestCase

from apps.folders.models import Folder
from apps.sub_todos.models import SubTodo
from apps.todos.models import Todo


class SubTodoModelTest(TestCase):
    def test_create_sub_todo(self):
        folder = Folder.objects.create(name="Work")
        todo = Todo.objects.create(folder=folder, title="Build API")
        sub_todo = SubTodo.objects.create(todo=todo, title="Write tests")

        self.assertEqual(sub_todo.todo, todo)
        self.assertFalse(sub_todo.is_completed)
