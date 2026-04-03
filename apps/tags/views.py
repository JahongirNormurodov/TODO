from rest_framework.viewsets import ModelViewSet

from apps.tags.models import Tag
from apps.tags.serializers import TagSerializer


class TagViewSet(ModelViewSet):
    serializer_class = TagSerializer
    pagination_class = None
    search_fields = ["name"]
    ordering_fields = ["name", "created_at", "updated_at"]

    def get_queryset(self):
        queryset = Tag.objects.all().order_by("name")
        return TagSerializer.with_counts(queryset)
