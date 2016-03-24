# coding: utf-8
from rest_framework import filters

from registries.models import ViolationRegistry


class ViolationRegistryFilter(filters.FilterSet):

    class Meta:
        model = ViolationRegistry
        fields = ['id', 'violation', 'date', 'who', 'json_data']
