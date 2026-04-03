from django.db import models

from apps.common.models import TimeStampedModel


class Label(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    color = models.CharField(max_length=7, default="#6B7280")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
