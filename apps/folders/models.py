from django.db import models

from .manager import FolderQuerySet


class Folder(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=7, default="#6366F1")
    icon = models.CharField(max_length=50, default="folder")
    position = models.PositiveIntegerField(default=0, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = FolderQuerySet.as_manager()

    class Meta:
        ordering = ["position", "created_at"]

    def __str__(self):
        return self.name
