from rest_framework import serializers

from jqgrid_django_rest_framework.fields import CustomJSONField
from registries.models import Registry


class RegistrySerializer(serializers.ModelSerializer):
    json_data = CustomJSONField()

    class Meta:
        model = Registry
        fields = '__all__'
