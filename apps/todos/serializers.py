from rest_framework import serializers

from apps.categories.models import Category
from apps.folders.models import Folder
from apps.labels.models import Label
from apps.sub_todos.models import SubTodo
from apps.sub_todos.serializers import SubTodoSerializer
from apps.tags.models import Tag
from apps.todos.models import Todo


class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"


class TagCompactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


class LabelCompactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ["id", "name", "color"]


class FolderCompactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = ["id", "name", "color"]


class CategoryCompactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "color"]


class TodoListSerializer(serializers.ModelSerializer):
    tags = TagCompactSerializer(many=True, read_only=True)
    labels = LabelCompactSerializer(many=True, read_only=True)
    sub_todo_stats = serializers.SerializerMethodField()
    tag_ids = serializers.ListField(
        child=serializers.UUIDField(), write_only=True, required=False, allow_empty=True
    )
    label_ids = serializers.ListField(
        child=serializers.UUIDField(), write_only=True, required=False, allow_empty=True
    )

    class Meta:
        model = Todo
        fields = [
            "id",
            "folder",
            "category",
            "title",
            "description",
            "priority",
            "status",
            "due_date",
            "position",
            "tags",
            "labels",
            "tag_ids",
            "label_ids",
            "sub_todo_stats",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "tags", "labels", "sub_todo_stats", "created_at", "updated_at"]

    def get_sub_todo_stats(self, obj):
        total = obj.sub_todos.count()
        completed = obj.sub_todos.filter(is_completed=True).count()
        return {"total": total, "completed": completed}

    def _set_m2m(self, instance, tag_ids, label_ids):
        if tag_ids is not None:
            instance.tags.set(Tag.objects.filter(id__in=tag_ids))
        if label_ids is not None:
            instance.labels.set(Label.objects.filter(id__in=label_ids))


    def create(self, validated_data):
        tag_ids = validated_data.pop("tag_ids", None)
        label_ids = validated_data.pop("label_ids", None)
        instance = super().create(validated_data)
        self._set_m2m(instance, tag_ids, label_ids)
        return instance

    def update(self, instance, validated_data):
        tag_ids = validated_data.pop("tag_ids", None)
        label_ids = validated_data.pop("label_ids", None)
        instance = super().update(instance, validated_data)
        self._set_m2m(instance, tag_ids, label_ids)
        return instance


    def get_sub_todos(self, obj):
        queryset = SubTodo.objects.filter(todo=obj).order_by("position")
        return SubTodoSerializer(queryset, many=True).data
