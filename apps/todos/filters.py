import django_filters

from apps.todos.models import Todo


class TodoFilter(django_filters.FilterSet):
    due_date_before = django_filters.DateTimeFilter(field_name="due_date", lookup_expr="lte")
    due_date_after = django_filters.DateTimeFilter(field_name="due_date", lookup_expr="gte")
    tags = django_filters.CharFilter(method="filter_tags")
    labels = django_filters.CharFilter(method="filter_labels")

    class Meta:
        model = Todo
        fields = ["folder", "category", "status", "priority"]

    def _split_uuid_csv(self, value: str):
        return [item.strip() for item in value.split(",") if item.strip()]

    def filter_tags(self, queryset, _name, value):
        for tag_id in self._split_uuid_csv(value):
            queryset = queryset.filter(tags__id=tag_id)
        return queryset.distinct()

    def filter_labels(self, queryset, _name, value):
        for label_id in self._split_uuid_csv(value):
            queryset = queryset.filter(labels__id=label_id)
        return queryset.distinct()
