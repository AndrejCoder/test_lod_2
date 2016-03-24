from django.conf import settings
from rest_framework import serializers

from registries.models import ViolationRegistry


class ViolationRegistrySerializer(serializers.ModelSerializer):
    date = serializers.DateField(format='%d.%m.%Y', input_formats=settings.DATE_INPUT_FORMATS)
    json_data = serializers.JSONField()

    class Meta:
        model = ViolationRegistry
        fields = '__all__'
