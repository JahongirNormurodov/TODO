from django.db import models

from apps.categories.models import Category
from apps.common.models import TimeStampedModel
from apps.folders.models import Folder
from apps.labels.models import Label
from apps.tags.models import Tag


class TodoPriority(models.TextChoices):
    LOW = "low", "Low"
    MEDIUM = "medium", "Medium"
    HIGH = "high", "High"
    URGENT = "urgent", "Urgent"


class TodoStatus(models.TextChoices):
    PENDING = "pending", "Pending"
    IN_PROGRESS = "in_progress", "In Progress"
    DONE = "done", "Done"
    CANCELLED = "cancelled", "Cancelled"


class Todo(TimeStampedModel):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name="todos")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name="todos",
        null=True,
        blank=True,
    )
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True, default="")
    priority = models.CharField(max_length=10, choices=TodoPriority.choices, default=TodoPriority.MEDIUM)
    status = models.CharField(max_length=15, choices=TodoStatus.choices, default=TodoStatus.PENDING)
    due_date = models.DateTimeField(null=True, blank=True)
    position = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField(Tag, related_name="todos", blank=True)
    labels = models.ManyToManyField(Label, related_name="todos", blank=True)

    class Meta:
        ordering = ["position", "-created_at"]
        indexes = [
            models.Index(fields=["folder"]),
            models.Index(fields=["category"]),
            models.Index(fields=["status"]),
            models.Index(fields=["priority"]),
            models.Index(fields=["due_date"]),
            models.Index(fields=["folder", "position"]),
        ]

    def __str__(self):
        return self.title
