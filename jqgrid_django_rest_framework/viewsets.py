# coding: utf-8
import json

from django.http import QueryDict
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class JqGridGenericViewSet(GenericViewSet):

    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        if kwargs.get('data'):
            kwargs['data'] = self.modify_request_data(kwargs.get('data'))
        return super().get_serializer(*args, **kwargs)


class JqGridListModelMixin(mixins.ListModelMixin):

    ORDER_DIRECTION = {
        'asc': '%s',
        'desc': '-%s'
    }

    def formatted_order(self, request):
        request.query_params._mutable = True
        request.query_params.update({"ordering": self.ORDER_DIRECTION.get(request.query_params.get("sord")) % request.query_params.get("sidx")})
        request.query_params._mutable = False
        return request

    def list(self, request, *args, **kwargs):
        # request = self.formatted_order(request)
        return super().list(request, *args, **kwargs)


class JqGridModelViewSet(mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         JqGridListModelMixin,
                         JqGridGenericViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    JSON_FIELD = 'json_data'
    NO_JSON_FIELDS = ['id', ]

    def modify_request_data(self, req_data):
        request_data = req_data.dict()
        data_querydict = QueryDict('', mutable=True)
        data_dict = {self.JSON_FIELD: {}}
        for no_json_field in self.NO_JSON_FIELDS:
            request_data.pop(no_json_field)

        if request_data.get('oper'):
            request_data.pop('oper')
        data_dict[self.JSON_FIELD] = json.dumps(request_data)

        data_querydict.update(data_dict)

        return data_querydict
