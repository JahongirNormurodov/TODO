from rest_framework.viewsets import ModelViewSet

from apps.todos.filters import TodoFilter
from apps.todos.models import Todo
from apps.todos.serializers import TodoDetailSerializer, TodoListSerializer


class TodoViewSet(ModelViewSet):
    filterset_class = TodoFilter
    search_fields = ["title", "description"]
    ordering_fields = ["created_at", "updated_at", "due_date", "priority", "position"]

    def get_queryset(self):
        queryset = Todo.objects.select_related("folder", "category").prefetch_related("tags", "labels", "sub_todos")
        
    def get_serializer_class(self):
        if self.action == "retrieve":
            return TodoDetailSerializer
        return TodoListSerializer
