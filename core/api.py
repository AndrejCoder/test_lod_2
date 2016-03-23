from rest_framework import viewsets
from rest_framework.response import Response

from rest_framework import status

from core.models import Process, ProcessType
from core.serializers import ProcessSerializer, ProcessTypeSerializer


class ProcessViewset(viewsets.ModelViewSet):

    serializer_class = ProcessSerializer

    def get_queryset(self):
        filters = {}
        for key, value in iter(self.request.query_params.dict().items()):
            if key in self.get_serializer(data=self.request.data).get_fields().keys():
                filters[key] = value
        return Process.objects.filter(**filters)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ProcessTypeViewset(viewsets.ModelViewSet):

    serializer_class = ProcessTypeSerializer

    def get_queryset(self):
        return ProcessType.objects.filter(**self.request.query_params.dict())
