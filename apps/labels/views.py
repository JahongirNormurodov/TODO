from rest_framework.viewsets import ModelViewSet

from apps.labels.models import Label
from apps.labels.serializers import LabelSerializer


class LabelViewSet(ModelViewSet):
    serializer_class = LabelSerializer
    pagination_class = None
    search_fields = ["name"]
    ordering_fields = ["name", "created_at", "updated_at"]

    def get_queryset(self):
        queryset = Label.objects.all().order_by("name")
        return LabelSerializer.with_counts(queryset)
