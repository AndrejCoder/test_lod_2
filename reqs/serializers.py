from rest_framework import serializers

from jqgrid_django_rest_framework.fields import CustomJSONField
from reqs.models import Request, ActivityPlace


class RequestSerializer(serializers.ModelSerializer):
    STATUS_FIELD = 'status'


    json_data = CustomJSONField()

    class Meta:
        model = Request
        fields = '__all__'

    def change_status(self):
        a = self.data
        return a


class ActivityPlaceSerializer(serializers.ModelSerializer):
    json_data = CustomJSONField()

    class Meta:
        model = ActivityPlace
        fields = '__all__'

