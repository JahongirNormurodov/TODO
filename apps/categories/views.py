from rest_framework.viewsets import ModelViewSet

from apps.categories.models import Category
from apps.categories.serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    pagination_class = None
    search_fields = ["name"]
    ordering_fields = ["created_at", "updated_at"]

    def get_queryset(self):
        queryset = Category.objects.all().order_by("created_at")
        return CategorySerializer.with_counts(queryset)
