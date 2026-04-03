from django.db import models

from apps.common.models import TimeStampedModel


class Tag(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True, db_index=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
