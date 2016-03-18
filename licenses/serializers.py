# coding: utf-8
from rest_framework import serializers

from licenses.models import License


class LicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = '__all__'
