# coding: utf-8
from django.utils import six
from django_filters.fields import Lookup
from django_filters.filters import Filter
from rest_framework.filters import FilterSet

from registries.models import Registry


class JSONFilter(Filter):

    def filter(self, qs, value):
        values_list = value.split(',')
        val = values_list.pop()
        if isinstance(value, Lookup):
            lookup = six.text_type(value.lookup_type)
            value = value.value
        else:
            lookup = self.lookup_expr
        if value in ([], (), {}, None, ''):
            return qs
        _filter = {'{0}__{1}__{2}'.format(self.name, '__'.join(values_list), lookup): int(val)}
        return qs.filter(**_filter)


class RegistryFilter(FilterSet):
    # json_data = JSONFilter()
    # json_data = JSONFilter(lookup_expr='gte')

    class Meta:
        model = Registry
        fields = {'id': ('exact', 'iexact', 'contains', 'icontains', 'gt', 'gte', 'lt', 'lte', 'in',
                         'startswith', 'istartswith', 'endswith', 'iendswith', 'range'
                         ),
                  'json_data': ()
                  }
