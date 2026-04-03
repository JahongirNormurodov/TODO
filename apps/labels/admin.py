from django.contrib import admin

from apps.labels.models import Label


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "color", "created_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("name",)
