from rest_framework import serializers

from jqgrid_django_rest_framework.fields import CustomJSONField
from reqs.models import Request, ActivityPlace


class ActivityPlaceSerializer(serializers.Serializer):
    json_data = CustomJSONField()

    class Meta:
        model = ActivityPlace
        fields = '__all__'

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class RequestSerializer(serializers.ModelSerializer):
    status_field = 'status'
    activity_places_field = 'aps'

    json_data = CustomJSONField()
    aps = ActivityPlaceSerializer(many=True)

    class Meta:
        model = Request
        fields = ('json_data', 'aps')

    def activity_places(self, instance):
        return instance.json_data.get(self.activity_places_field)

    def change_status(self, instance):
        instance.json_data[self.status_field] = 'old'
        instance.save()
        return instance
