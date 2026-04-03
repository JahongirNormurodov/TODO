from django.contrib import admin
from django.urls import include, path

from apps.common.views import ApiRootView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", ApiRootView.as_view()),
    path("api/v1/", include("config.api_urls")),
]
