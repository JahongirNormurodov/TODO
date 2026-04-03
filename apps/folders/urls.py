from rest_framework.routers import DefaultRouter

from apps.folders.views import FolderViewSet

router = DefaultRouter()
router.register(r"folders", FolderViewSet, basename="folder")

urlpatterns = router.urls
