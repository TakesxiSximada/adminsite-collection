from rest_framework import viewsets


from . import (
    models,
    serializers,
    )


class PushViewSet(viewsets.ModelViewSet):
    queryset = models.Push.objects.all()
    serializer_class = serializers.PushSerializer
