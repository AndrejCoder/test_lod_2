from rest_framework import serializers

from core.models import Process


class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = (
            'id',
            'name',
            'process_type'
        )
