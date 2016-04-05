import json

from rest_framework.filters import DjangoFilterBackend, OrderingFilter


class JqGridDjangoFilterBackend(DjangoFilterBackend):
    """
    Адаптер фильтрации JqGrid для Django REST Framework
    """
    LOOKUPS_JQGRID = {
        'eq': {'op': ' = ', 'value': '%s'},
        'ne': {'op': ' != ', 'value': '%s'},
        'bw': {'op': ' ILIKE ', 'value': '%s%%%%'},
        'bn': {'op': ' NOT ILIKE ', 'value': '%s%%%%'},
        'ew': {'op': ' ILIKE ', 'value': '%%%%%s'},
        'en': {'op': ' NOT ILIKE ', 'value': '%%%%%s'},
        'cn': {'op': ' ILIKE ', 'value': '%%%%%s%%%%'},
        'nc': {'op': ' NOT ILIKE ', 'value': '%%%%%s%%%%'},
        'nu': {'op': ' IS NULL', 'value': '%s'},
        'nn': {'op': ' IS NOT NULL', 'value': '%s'},
        'in': {'op': ' IN ', 'value': '%s'},
        'ni': {'op': ' NOT IN ', 'value': '%s'},
        'lt': {'op': ' < ', 'value': '%s'},
        'le': {'op': ' <= ', 'value': '%s'},
        'gt': {'op': ' > ', 'value': '%s'},
        'ge': {'op': ' >= ', 'value': '%s'}
    }

    TYPE_FORMAT = {
        'string': '%s',
        'date': 'TO_DATE(%s, \'dd.mm.yyyy\')',
        'integer': 'TO_NUMBER(%s, \'9999999999999999999\')'
    }

    UPPER_OPS = ('eq', 'ne')

    def formatted_wq(self, parameter, field, col_model, op=None):
        if op and op in self.UPPER_OPS and col_model.get(field) == 'string':
            parameter = 'UPPER(' + parameter + ')'
        return self.TYPE_FORMAT.get(col_model.get(field)) % parameter

    def left_where_query(self, filter_rule, view, col_model):
        lwq = view.JSON_FIELD + '::json->>\'' + filter_rule.get('field') + '\''
        lwq = self.formatted_wq(lwq, filter_rule.get('field'), col_model, filter_rule.get('op'))
        return lwq

    def op_where_query(self, filter_rule):
        return self.LOOKUPS_JQGRID.get(filter_rule.get('op')).get('op')

    def right_where_query(self, filter_rule, col_model):
        rwq = filter_rule.get('data')
        if filter_rule.get('op') in ('nu', 'nn'):
            rwq = ''
        rwq = self.LOOKUPS_JQGRID.get(filter_rule.get('op')).get('value') % rwq
        if filter_rule.get('op') not in ('nu', 'nn'):
            rwq = '\'' + rwq + '\''
        rwq = self.formatted_wq(rwq, filter_rule.get('field'), col_model, filter_rule.get('op'))
        return rwq

    def sql_where_query(self, filter_rule, view, col_model):
        return self.left_where_query(filter_rule, view, col_model) + self.op_where_query(filter_rule) + self.right_where_query(
            filter_rule, col_model)

    def filter_queryset(self, request, queryset, view):
        filter_list = list()

        filters = request.query_params.dict().get('filters')
        if filters:
            filters_dict = json.loads(request.query_params.dict().get('filters'))
            col_model = json.loads(request.query_params.dict().get('colModel'))
            filter_rules = filters_dict.get('rules')
            for filter_rule in filter_rules:
                filter_list.append(self.sql_where_query(filter_rule, view, col_model))
            group_op = ' ' + filters_dict.get('groupOp') + ' '
            sql_query = group_op.join(filter_list)
            queryset = queryset.extra(where=[sql_query])

        return super().filter_queryset(request, queryset, view)


class JqGridOrderingFilter(OrderingFilter):

    def filter_queryset(self, request, queryset, view):
        ordering = self.get_ordering(request, queryset, view)
        if ordering:
            ordering_sql = list()
            for order_field in ordering:
                direction = ''
                if order_field.startswith('-'):
                    direction = 'DESC'
                if list(order_field)[0] == '-':
                    order_field = order_field[1:]
                ordering_sql.append(view.JSON_FIELD + '::json->>\'' + order_field + '\' ' + direction)
            return queryset.extra(order_by=tuple(ordering_sql))

        return queryset


