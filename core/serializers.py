from rest_framework import serializers

from core.models import Process, ProcessType


class ProcessTypeSerializer(serializers.ModelSerializer):
    # processes = ProcessSerializer(many=True, read_only=True)

    class Meta:
        model = ProcessType
        fields = (
            'id',
            'name',
            # 'processes'
        )


class ProcessSerializer(serializers.ModelSerializer):
    process_type = ProcessTypeSerializer()

    class Meta:
        model = Process
        fields = (
            'id',
            'name',
            'process_type'
        )
