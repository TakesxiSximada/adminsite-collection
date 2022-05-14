from rest_framework import serializers

from . import models


class PushSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Push
        fields = (
            'summary',
            'published_at',
            )
