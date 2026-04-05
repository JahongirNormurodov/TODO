import django_filters

from apps.todos.models import Todo
from django.db.models import Count, Q




class TodoFilter(django_filters.FilterSet):
    due_date_before = django_filters.DateTimeFilter(field_name="due_date", lookup_expr="lte")
    due_date_after = django_filters.DateTimeFilter(field_name="due_date", lookup_expr="gte")
    tags = django_filters.CharFilter(method="filter_tags")
    labels = django_filters.CharFilter(method="filter_labels")

    class Meta:
        model = Todo
        fields = ["folder", "category", "status", "priority"]

    def filter_tags(self, queryset, _name, value):
        for tag_id in self._split_uuid_csv(value):
            queryset = queryset.filter(tags__id=tag_id)
        return queryset.distinct()
    def filter_by_tags(queryset, tag_ids):
        return queryset.filter(tags__id__in=tag_ids).annotate(
        matched_tags=Count(
            "tags",
            filter=Q(tags__id__in=tag_ids),
            distinct=True
        )
    ).filter(matched_tags=len(tag_ids))

    def filter_labels(self, queryset, _name, value):
        for label_id in self._split_uuid_csv(value):
            queryset = queryset.filter(labels__id=label_id)
        return queryset.distinct()
