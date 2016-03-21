from rest_framework import viewsets

from registries.models import ViolationRegistry
from registries.serializers import ViolationRegistrySerializer


class ViolationRegistryViewset(viewsets.ModelViewSet):

    serializer_class = ViolationRegistrySerializer

    def get_queryset(self):
        filters = {}
        for key, value in self.request.query_params.dict().iteritems():
            if key in self.get_serializer(data=self.request.data).get_fields().keys():
                filters[key] = value
        return ViolationRegistry.objects.filter(**filters)
