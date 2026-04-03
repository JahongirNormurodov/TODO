from rest_framework.viewsets import ModelViewSet

from apps.folders.models import Folder
from apps.folders.serializers import FolderSerializer


class FolderViewSet(ModelViewSet):
    serializer_class = FolderSerializer
    pagination_class = None
    search_fields = ["name"]
    ordering_fields = ["position", "created_at", "updated_at"]

    def get_queryset(self):
        queryset = Folder.objects.all().order_by("position", "created_at")
        return FolderSerializer.with_counts(queryset)
