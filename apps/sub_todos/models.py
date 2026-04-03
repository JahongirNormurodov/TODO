from django.db import models

from apps.common.models import TimeStampedModel
from apps.todos.models import Todo


class SubTodo(TimeStampedModel):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name="sub_todos")
    title = models.CharField(max_length=500)
    is_completed = models.BooleanField(default=False)
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["position"]
        indexes = [
            models.Index(fields=["todo"]),
            models.Index(fields=["todo", "position"]),
        ]

    def __str__(self):
        return self.title
