from django.urls import path, include
from rest_framework import routers

from .api_views.new_release_views import NewReleaseViewSet

router = routers.DefaultRouter()
router.register(r"new_release", NewReleaseViewSet)

urlpatterns = [
    path(r"", include(router.urls)),
]