# coding: utf-8
from rest_framework import filters

from jqgrid_django_rest_framework.backends import JqGridDjangoFilterBackend
from jqgrid_django_rest_framework.paginations import JqGridPageNumberPagination
from jqgrid_django_rest_framework.viewsets import JqGridModelViewSet
from registries.filters import RegistryFilter
from registries.models import Registry
from registries.serializers import RegistrySerializer


class RegistryViewset(JqGridModelViewSet):

    serializer_class = RegistrySerializer
    filter_backends = (filters.SearchFilter, JqGridDjangoFilterBackend, filters.OrderingFilter)
    search_fields = ('id', 'json_data')
    filter_class = RegistryFilter
    queryset = Registry.objects.all()

    pagination_class = JqGridPageNumberPagination
    pagination_class.page_size = 20
    pagination_class.page_size_query_param = 'rows'
