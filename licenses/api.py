# coding: utf-8
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from licenses.models import License
from licenses.serializers import LicenseSerializer


class LicenseList(APIView):

    def get(self, request, format=None):
        licenses = License.objects.all()
        serialized_licenses = LicenseSerializer(licenses, many=True)
        return Response(serialized_licenses.data)


class LicenseDetail(APIView):

    def get_object(self, pk):
        try:
            return License.objects.get(pk=pk)
        except License.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        _license = self.get_object(pk)
        serialized_license = LicenseSerializer(_license)
        return Response(serialized_license.data)