from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Process
from core.serializers import ProcessSerializer


class ProcessList(APIView):

    def get(self, request, format=None):
        processes = Process.objects.all()
        serialized_licenses = ProcessSerializer(processes, many=True)
        return Response(serialized_licenses.data)


class ProcessDetail(APIView):

    def get_object(self, pk):
        try:
            return Process.objects.get(pk=pk)
        except Process.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        _process = self.get_object(pk)
        serialized_license = ProcessSerializer(_process)
        return Response(serialized_license.data)