from django.db import models
from django.db.models import Count

class FolderQuerySet(models.QuerySet):
    def with_counts(self):
        return self.annotate(
            todo_count=Count("todos", distinct=True)
        )