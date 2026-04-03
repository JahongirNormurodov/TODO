from django.contrib import admin

from apps.categories.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "icon", "created_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("name",)
