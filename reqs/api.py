# coding: utf-8
from rest_framework import filters

from jqgrid_django_rest_framework.filters import JqGridDjangoFilterBackend
from jqgrid_django_rest_framework.paginations import JqGridPageNumberPagination
from jqgrid_django_rest_framework.viewsets import JqGridModelViewSet
from registries.filters import ActivityPlaceFilter
from registries.models import ActivityPlace
from registries.serializers import ActivityPlaceSerializer
from reqs.filters import RequestFilter
from reqs.models import Request
from reqs.serializers import RequestSerializer


class RequestViewset(JqGridModelViewSet):

    no_json_fields = ['id', ]

    serializer_class = RequestSerializer
    filter_backends = (filters.SearchFilter, JqGridDjangoFilterBackend, filters.OrderingFilter)
    search_fields = ('id', 'json_data')
    # ordering_fields = ('last_name', 'first_name', 'second_name', 'birthday', 'place', 'age')
    filter_class = RequestFilter
    queryset = Request.objects.all()

    pagination_class = JqGridPageNumberPagination
    pagination_class.page_size = 20
    pagination_class.page_size_query_param = 'rows'


class ActivityPlaceViewset(JqGridModelViewSet):
    no_json_fields = ['id', 'request']
    serializer_class = ActivityPlaceSerializer
    filter_backends = (filters.SearchFilter, JqGridDjangoFilterBackend, filters.OrderingFilter)
    search_fields = ('id', 'json_data')
    # ordering_fields = ('last_name', 'first_name', 'second_name', 'birthday', 'place', 'age')
    filter_class = ActivityPlaceFilter
    queryset = ActivityPlace.objects.all()

    pagination_class = JqGridPageNumberPagination
    pagination_class.page_size = 20
    pagination_class.page_size_query_param = 'rows'
