from django.db import models

from apps.common.models import TimeStampedModel


class Category(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    color = models.CharField(max_length=7, default="#8B5CF6")
    icon = models.CharField(max_length=50, default="tag")

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.name
