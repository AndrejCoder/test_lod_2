# coding: utf-8
from django.db.models import Lookup


class PostgresSimpleJsonLookup(Lookup):

    def as_sql(self, qn, connection):
        lhs, lhs_params = self.process_lhs(qn, connection)
        rhs, rhs_params = self.process_rhs(qn, connection)
        params = lhs_params + rhs_params
        return '%s %s %s' % (lhs, self.json_operator, rhs), params


class KeyValueContains(Lookup):
    lookup_name = 'kvcontains'

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params
        return '%s ->> %s LIKE %s' % (lhs, rhs), params
