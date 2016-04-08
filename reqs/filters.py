# coding: utf-8
from rest_framework.filters import FilterSet

from registries.models import ActivityPlace
from reqs.models import Request


class RequestFilter(FilterSet):

    class Meta:
        model = Request
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
