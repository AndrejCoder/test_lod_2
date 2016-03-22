# coding: utf-8
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination

from registries.filters import ViolationRegistryFilter
from registries.models import ViolationRegistry
from registries.serializers import ViolationRegistrySerializer


class ViolationRegistryViewset(viewsets.ModelViewSet):

    serializer_class = ViolationRegistrySerializer
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)
    filter_class = ViolationRegistryFilter
    queryset = ViolationRegistry.objects.all()

    pagination_class = PageNumberPagination
    pagination_class.page_size_query_param = 'page_size'
