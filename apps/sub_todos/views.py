from rest_framework.viewsets import ModelViewSet

from apps.sub_todos.models import SubTodo
from apps.sub_todos.serializers import SubTodoSerializer


class SubTodoViewSet(ModelViewSet):
    serializer_class = SubTodoSerializer
    search_fields = ["title"]
    ordering_fields = ["position", "created_at", "updated_at"]

    def get_queryset(self):
        todo_pk = self.kwargs.get("todo_pk")
        queryset = SubTodo.objects.all().order_by("position")
        if todo_pk:
            queryset = queryset.filter(todo_id=todo_pk)
        return queryset

    def perform_create(self, serializer):
        todo_pk = self.kwargs.get("todo_pk")
        if todo_pk:
            serializer.save(todo_id=todo_pk)
            return
        serializer.save()
