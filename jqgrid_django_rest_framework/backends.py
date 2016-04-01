import json

from rest_framework.filters import DjangoFilterBackend


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
        'ni': {'op': ' NOT IN ', 'value': '%s'}
    }

    UPPER_OPS = ('eq', 'ne')

    def left_where_query(self, filter_rule, view):
        lwq = view.JSON_FIELD + '::json->>\'' + filter_rule.get('field') + '\''
        if filter_rule.get('op') in self.UPPER_OPS:
            lwq = 'UPPER(' + lwq + ')'
        return lwq

    def op_where_query(self, filter_rule):
        return self.LOOKUPS_JQGRID.get(filter_rule.get('op')).get('op')

    def right_where_query(self, filter_rule):
        rwq = filter_rule.get('data')
        if filter_rule.get('op') in ('nu', 'nn'):
            rwq = ''
        rwq = self.LOOKUPS_JQGRID.get(filter_rule.get('op')).get('value') % rwq
        if filter_rule.get('op') not in ('nu', 'nn'):
            rwq = '\'' + rwq + '\''
        if filter_rule.get('op') in self.UPPER_OPS:
            rwq = 'UPPER(' + rwq + ')'
        return rwq

    def sql_where_query(self, filter_rule, view):
        return self.left_where_query(filter_rule, view) + self.op_where_query(filter_rule) + self.right_where_query(
            filter_rule)

    def filter_queryset(self, request, queryset, view):
        filter_list = list()

        filters = request.query_params.dict().get('filters')
        if filters:
            filters_dict = json.loads(request.query_params.dict().get('filters'))
            filter_rules = filters_dict.get('rules')
            for filter_rule in filter_rules:
                filter_list.append(self.sql_where_query(filter_rule, view))
            group_op = ' ' + filters_dict.get('groupOp') + ' '
            sql_query = group_op.join(filter_list)
            queryset = queryset.extra(where=[sql_query])

        return super().filter_queryset(request, queryset, view)
