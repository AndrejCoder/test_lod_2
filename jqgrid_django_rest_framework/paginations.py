from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class JqGridPageNumberPagination(PageNumberPagination):

    JSON_FIELD = 'json_data'

    def get_paginated_response(self, data):
        rows = list()
        for data_ordered_dict in data:
            json_dict = data_ordered_dict.get(self.JSON_FIELD)
            data_ordered_dict_rows = data_ordered_dict.copy()
            data_ordered_dict_rows.update(json_dict)
            data_ordered_dict_rows.pop(self.JSON_FIELD)
            rows.append(data_ordered_dict_rows)

        return Response(OrderedDict([
            ('records', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('rows', rows),
            ('results', data),
            ('page', self.page.number),
            ('total', self.page.paginator.num_pages)
        ]))
