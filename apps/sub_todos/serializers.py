from rest_framework import serializers

from apps.sub_todos.models import SubTodo


class SubTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTodo
        fields = ["id", "todo", "title", "is_completed", "position", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
