from django.http import Http404
from rest_framework import viewsets
from rest_framework.response import Response

from core.models import Process, ProcessType
from core.serializers import ProcessSerializer, ProcessTypeSerializer


class ProcessViewset(viewsets.ViewSet):

    queryset = Process.objects.all()

    def list(self, request, format=None):
        processes = Process.objects.filter(**request.query_params.dict())
        serialized_licenses = ProcessSerializer(processes, many=True)
        return Response(serialized_licenses.data)

    def get_object(self, pk):
        try:
            return Process.objects.get(pk=pk)
        except Process.DoesNotExist:
            return Http404

    def detail(self, request, pk, format=None):
        _process = self.get_object(pk)
        serialized_license = ProcessSerializer(_process)
        return Response(serialized_license.data)


class ProcessTypeViewset(viewsets.ViewSet):

    queryset = ProcessType.objects.all()

    def list(self, request, format=None):
        process_types = ProcessType.objects.all()
        serialized_process_types = ProcessTypeSerializer(process_types, many=True)
        return Response(serialized_process_types.data)

    def get_object(self, pk):
        try:
            return ProcessType.objects.get(pk=pk)
        except ProcessType.DoesNotExist:
            return Http404

    def detail(self, request, pk, format=None):
        _process_type = self.get_object(pk)
        serialized_process_type = ProcessTypeSerializer(_process_type)
        return Response(serialized_process_type.data)
