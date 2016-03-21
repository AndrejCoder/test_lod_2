from rest_framework import serializers

from registries.models import ViolationRegistry


class ViolationRegistrySerializer(serializers.ModelSerializer):
    date = serializers.DateField(format='%d.%m.%Y')

    class Meta:
        model = ViolationRegistry
        fields = '__all__'
