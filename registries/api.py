# coding: utf-8
from rest_framework import viewsets, filters

from registries.filters import RegistryFilter
from registries.models import Registry
from registries.paginations import PageNumberDataPagination
from registries.serializers import RegistrySerializer


class RegistryViewset(viewsets.ModelViewSet):

    serializer_class = RegistrySerializer
    filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend, filters.OrderingFilter)
    search_fields = ('id', 'json_data')
    filter_class = RegistryFilter
    queryset = Registry.objects.all()

    pagination_class = PageNumberDataPagination
    pagination_class.page_size_query_param = 'page_size'
