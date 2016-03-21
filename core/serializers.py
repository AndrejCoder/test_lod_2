from rest_framework import serializers

from core.models import Process, ProcessType


class ProcessTypeSerializer(serializers.ModelSerializer):
    # processes = ProcessSerializer(many=True, read_only=True)

    class Meta:
        model = ProcessType
        fields = '__all__'


class ProcessSerializer(serializers.ModelSerializer):
    # process_type = ProcessTypeSerializer(read_only=True)

    class Meta:
        model = Process
        fields = '__all__'
        depth = 2

    # def create(self, validated_data):
    #     process_type = ProcessType.objects.get(id=validated_data.pop('process_type'))
    #     process = Process.objects.create(process_type=process_type, **validated_data)
    #     return process
