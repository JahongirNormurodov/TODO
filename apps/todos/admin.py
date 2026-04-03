from django.contrib import admin

from apps.todos.models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ("id", "folder", "title", "status", "priority", "due_date", "created_at")
    list_filter = ("status", "priority", "created_at")
    search_fields = ("title", "description")
