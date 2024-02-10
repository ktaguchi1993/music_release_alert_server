from rest_framework import serializers
from .models import NewRelease


class NewReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewRelease
        # json で出力するフィールド
        fields = ('id', 'title', 'artist', 'release_date', 'url', 'type', 'genre')
