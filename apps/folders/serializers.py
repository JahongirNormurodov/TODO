from django.db.models import Count
from rest_framework import serializers

from apps.folders.models import Folder



class FolderSerializer(serializers.ModelSerializer):
    todo_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Folder
        fields = ["id", "name", "color", "icon", "position", "todo_count", "created_at", "updated_at"]
        read_only_fields = ["id", "todo_count", "created_at", "updated_at"]

    @staticmethod
    def with_counts(queryset):
        return queryset.annotate(todo_count=Count("todos", distinct=True))
