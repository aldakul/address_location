from django.db.models import Q
from django_filters import CharFilter
from django_filters.constants import EMPTY_VALUES


class SearchFilterField(CharFilter):
    def filter(self, qs, value):
        if value in EMPTY_VALUES:
            return qs
        if self.distinct:
            qs = qs.distinct()
        lookups = (
            '%s__%s' % (self.field_name, lookup_expr)
            for lookup_expr in ('contains', 'icontains')
        )
        qs_lookup_expression = Q()
        for lookup in lookups:
            qs_lookup_expression |= Q(**{lookup: value})
        qs = self.get_method(qs)(qs_lookup_expression)
        return qs
