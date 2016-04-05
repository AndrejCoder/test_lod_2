# coding: utf-8
from rest_framework import filters

from jqgrid_django_rest_framework.filters import JqGridDjangoFilterBackend, JqGridOrderingFilter
from jqgrid_django_rest_framework.paginations import JqGridPageNumberPagination
from jqgrid_django_rest_framework.viewsets import JqGridModelViewSet
from registries.filters import RegistryFilter
from registries.models import Registry
from registries.serializers import RegistrySerializer


class RegistryViewset(JqGridModelViewSet):

    serializer_class = RegistrySerializer
    filter_backends = (filters.SearchFilter, JqGridDjangoFilterBackend, JqGridOrderingFilter)
    search_fields = ('id', 'json_data')
    ordering_fields = ('last_name', 'first_name', 'second_name', 'birthday', 'place', 'age')
    filter_class = RegistryFilter
    queryset = Registry.objects.all()

    pagination_class = JqGridPageNumberPagination
    pagination_class.page_size = 20
    pagination_class.page_size_query_param = 'rows'
