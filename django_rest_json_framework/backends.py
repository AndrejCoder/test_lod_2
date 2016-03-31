import django_filters
from django.template import loader
from rest_framework.compat import template_render
from rest_framework.filters import BaseFilterBackend, FilterSet, filter_template

from registries.models import Registry


class JqGridDjangoFilterBackend(BaseFilterBackend):
    """
    A filter backend that uses django-filter.
    """
    LOOKUPS_JQGRID_DJANGO = {
        'eq': 'iexact',
        'bw': 'istartswith',
        'ew': 'iendswith',
        'cn': 'icontains',
        'nu': 'isnull'
    }

    default_filter_set = FilterSet
    template = filter_template

    def __init__(self):
        assert django_filters, 'Using DjangoFilterBackend, but django-filter is not installed'

    def get_filter_class(self, view, queryset=None):
        """
        Return the django-filters `FilterSet` used to filter the queryset.
        """
        filter_class = getattr(view, 'filter_class', None)
        filter_fields = getattr(view, 'filter_fields', None)

        if filter_class:
            filter_model = filter_class.Meta.model

            assert issubclass(queryset.model, filter_model), \
                'FilterSet model %s does not match queryset model %s' % \
                (filter_model, queryset.model)

            return filter_class

        if filter_fields:
            class AutoFilterSet(self.default_filter_set):
                class Meta:
                    model = queryset.model
                    fields = filter_fields

            return AutoFilterSet

        return None

    def filter_queryset(self, request, queryset, view):
        filter_class = self.get_filter_class(view, queryset)

        qs1 = Registry.objects.filter(json_data__kvcontains={'first_name': 'Пе'})
        qs2 = Registry.objects.filter(id__icontains=2)

        print(qs1)

        if filter_class:
            return filter_class(request.query_params, queryset=queryset).qs

        return queryset

    def to_html(self, request, queryset, view):
        filter_class = self.get_filter_class(view, queryset)
        if not filter_class:
            return None
        filter_instance = filter_class(request.query_params, queryset=queryset)
        context = {
            'filter': filter_instance
        }
        template = loader.get_template(self.template)
        return template_render(template, context)