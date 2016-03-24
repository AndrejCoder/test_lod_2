# coding: utf-8
from rest_framework import filters

from registries.models import Registry


class RegistryFilter(filters.FilterSet):

    class Meta:
        model = Registry
        fields = ['id', 'json_data']
