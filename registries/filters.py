# coding: utf-8
from rest_framework.filters import FilterSet

from registries.models import Registry, ActivityPlace


class RegistryFilter(FilterSet):

    class Meta:
        model = Registry
        fields = {'id': ('exact', 'iexact', 'contains', 'icontains', 'gt', 'gte', 'lt', 'lte', 'in',
                         'startswith', 'istartswith', 'endswith', 'iendswith', 'range'
                         ),
                  'json_data': ()
                  }


class ActivityPlaceFilter(FilterSet):

    class Meta:
        model = ActivityPlace
        fields = {'id': ('exact', 'iexact', 'contains', 'icontains', 'gt', 'gte', 'lt', 'lte', 'in',
                         'startswith', 'istartswith', 'endswith', 'iendswith', 'range'
                         ),
                  'json_data': ()
                  }
