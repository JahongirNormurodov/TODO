from django.db.models import Count
from rest_framework import serializers

from apps.tags.models import Tag


class TagSerializer(serializers.ModelSerializer):
    todo_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Tag
        fields = ["id", "name", "todo_count", "created_at", "updated_at"]
        read_only_fields = ["id", "todo_count", "created_at", "updated_at"]

    @staticmethod
    def with_counts(queryset):
        return queryset.annotate(todo_count=Count("todos", distinct=True))
