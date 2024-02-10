from rest_framework.viewsets import ModelViewSet

from music_release_alert_portal_app.models import NewRelease
from music_release_alert_portal_app.serializer import NewReleaseSerializer


class NewReleaseViewSet(ModelViewSet):
    serializer_class = NewReleaseSerializer
    queryset = NewRelease.objects.all()

