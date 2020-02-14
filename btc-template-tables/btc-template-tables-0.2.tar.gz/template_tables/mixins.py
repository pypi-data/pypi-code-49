import datetime
import logging
import re
from typing import Type

from django.db.models import Q
from django_filters import FilterSet, CharFilter

from template_tables.components import TemplateTableType, TemplateTablePaginationType, TemplateTablePagination

logger = logging.getLogger(__name__)


class TemplateTablePaginationMixin:
    """
    Mixin for adding pagination to the view.
    """

    pagination_class: Type[TemplateTablePaginationType] = TemplateTablePagination
    context_pagination_name: str = 'pagination'

    def get(self, request, *args, **kwargs):
        self.paginate_by = self.pagination_class.get_paginate_by_value(request, self.paginate_by)
        return super().get(request, *args, **kwargs)

    def get_pagination_kwargs(self, context: dict, **kwargs):
        return {'request': self.request, 'page_object': context.pop('page_obj'),
                'paginate_by': self.paginate_by, 'object_list': context.get('object_list'), **kwargs}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            self.context_pagination_name: self.pagination_class(**self.get_pagination_kwargs(context))
        })
        return context


class TemplateTableViewMixin:
    """
    Mixin for rendering a table with an auto-generated template.
    """

    table_class: Type[TemplateTableType] = None
    context_table_name: str = 'table'

    def get_table_kwargs(self, context: dict, **kwargs):
        return {'request': self.request, 'object_list': context.pop('object_list'), **kwargs}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            self.context_table_name: self.table_class(**self.get_table_kwargs(context))
        })
        return context


class SearchFieldMixin(FilterSet):
    """
    Mixin for adding search string to filterset.
    In the filter specify (example):
    1. search_field_placeholder = 'Начните вводить название для поиска'
    2. searching_fields = ['field', 'field__field']

    Authors: serwiz, franky_terra, petr_tikhonov - members of btc python dev team.
    """

    search_field_placeholder: str = 'Search...'
    label: str = ''
    searching_fields: list = []
    lookups: dict = {}  # icontains or exact
    default_lookup: str = 'icontains'

    q = CharFilter(method='filter_search')

    def filter_search(self, queryset, name, value):
        raw_value = value
        if value:
            value_date = self._parse_date(value)
            if value_date:
                value = value_date

            q_objects = Q()

            try:
                if '__str__' in self.searching_fields:
                    self.searching_fields = [field for field in self.searching_fields if field != '__str__']
                    pk_list = []
                    for obj in queryset:
                        obj_string = str(obj)
                        if raw_value in obj_string or obj_string in raw_value:
                            pk_list.append(obj.pk)
                    q_objects |= Q(pk__in=pk_list)

                for field in self.searching_fields:
                    lookup = self.lookups.get(field, self.default_lookup)
                    q_objects |= Q(**{'{0}__{1}'.format(field, lookup): value})

                queryset = queryset.filter(q_objects).distinct()
            except Exception as e:
                logger.error(f'An error occurred while filtering with SearchFieldMixin: {e}')
                queryset = queryset.none()

        return queryset

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form.fields['q'].label = self.label
        self.form.fields['q'].widget.attrs.update({'placeholder': self.search_field_placeholder})

    def _parse_date(self, value):
        """
        Returned datetime.date if a string of the form dd.mm.yyyy is entered.
        """

        date_re = re.compile(r'(?P<day>\d{1,2}).(?P<month>\d{1,2}).(?P<year>\d{4})$')
        date_match = date_re.match(value)
        if date_match:
            kw = {k: int(v) for k, v in date_match.groupdict().items()}
            try:
                return datetime.date(**kw)
            except ValueError:
                return None
