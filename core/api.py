from rest_framework import viewsets

from core.models import Process, ProcessType
from core.serializers import ProcessSerializer, ProcessTypeSerializer


class ProcessViewset(viewsets.ModelViewSet):

    serializer_class = ProcessSerializer

    def get_queryset(self):
        return Process.objects.filter(**self.request.query_params.dict())


class ProcessTypeViewset(viewsets.ModelViewSet):

    serializer_class = ProcessTypeSerializer

    def get_queryset(self):
        return ProcessType.objects.filter(**self.request.query_params.dict())
