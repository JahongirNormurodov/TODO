from django.urls import include, path

urlpatterns = [
    path("", include("apps.folders.urls")),
    path("", include("apps.categories.urls")),
    path("", include("apps.tags.urls")),
    path("", include("apps.labels.urls")),
    path("", include("apps.todos.urls")),
    path("", include("apps.sub_todos.urls")),
]
