from django.contrib import admin

from apps.sub_todos.models import SubTodo


@admin.register(SubTodo)
class SubTodoAdmin(admin.ModelAdmin):
    list_display = ("id", "todo", "title", "is_completed", "position", "created_at")
    list_filter = ("is_completed", "created_at", "updated_at")
    search_fields = ("title", "todo__title")
