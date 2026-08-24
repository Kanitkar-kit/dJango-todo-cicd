from django.test import TestCase
from .models import Todo


class TodoTest(TestCase):

    def test_create_todo(self):
        todo = Todo.objects.create(title="Learn Jenkins")

        self.assertEqual(todo.title, "Learn Jenkins")
        self.assertFalse(todo.completed)
