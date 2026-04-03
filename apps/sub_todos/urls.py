from django.urls import include, path
from rest_framework_nested.routers import NestedDefaultRouter

from apps.sub_todos.views import SubTodoViewSet
from apps.todos.urls import router as todos_router

nested_router = NestedDefaultRouter(todos_router, r"todos", lookup="todo")
nested_router.register(r"sub-todos", SubTodoViewSet, basename="todo-sub-todos")

urlpatterns = [
    path("", include(nested_router.urls)),
]
