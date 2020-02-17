from typing import Type

from template_tables.components import TemplateTableType, TemplateTablePaginationType, TemplateTablePagination


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
