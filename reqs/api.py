# coding: utf-8
from rest_framework.decorators import detail_route
from rest_framework.filters import DjangoFilterBackend, OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from jqgrid_django_rest_framework.filters import JqGridDjangoFilterBackend
from jqgrid_django_rest_framework.paginations import JqGridPageNumberPagination
from jqgrid_django_rest_framework.viewsets import JqGridModelViewSet
from reqs.filters import RequestFilter, ActivityPlaceFilter
from reqs.models import Request, ActivityPlace
from reqs.serializers import RequestSerializer, ActivityPlaceSerializer


class RequestViewset(ModelViewSet):

    no_json_fields = ['id', ]
    json_field = 'json_data'

    serializer_class = RequestSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    search_fields = ('id', 'json_data')
    filter_class = RequestFilter
    queryset = Request.objects.all()

    pagination_class = PageNumberPagination
    pagination_class.page_size = 20
    pagination_class.page_size_query_param = 'rows'

    @detail_route(methods=['get'])
    def activity_places(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.activity_places(instance))

    @detail_route(methods=['get'])
    def change_status(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        # serializer.is_valid(raise_exception=True)
        serializer.change_status(instance)
        return Response(serializer.data)


class JqGridRequestViewset(JqGridModelViewSet):
    no_json_fields = ['id', ]

    serializer_class = RequestSerializer
    filter_backends = (SearchFilter, JqGridDjangoFilterBackend, OrderingFilter)
    search_fields = ('id', 'json_data')
    filter_class = RequestFilter
    queryset = Request.objects.all()

    pagination_class = JqGridPageNumberPagination
    pagination_class.page_size = 20
    pagination_class.page_size_query_param = 'rows'


class ActivityPlaceViewset(JqGridModelViewSet):
    no_json_fields = ['id', 'request']
    serializer_class = ActivityPlaceSerializer
    filter_backends = (SearchFilter, JqGridDjangoFilterBackend, OrderingFilter)
    search_fields = ('id', 'json_data')
    # ordering_fields = ('last_name', 'first_name', 'second_name', 'birthday', 'place', 'age')
    filter_class = ActivityPlaceFilter
    queryset = ActivityPlace.objects.all()

    pagination_class = JqGridPageNumberPagination
    pagination_class.page_size = 20
    pagination_class.page_size_query_param = 'rows'
