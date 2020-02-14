from typing import TypeVar, List, Any, Optional, Collection, Type

from django.core.paginator import Page
from django.forms import BaseForm
from django.utils.http import urlencode
from django_filters import FilterSet
from flex_forms.basic_mixins import TemplateObjectMixin, HttpRequestType
from flex_forms.components import BaseHtmlElement
from flex_forms.forms import StaticFieldset, StaticModelFieldset


class AbstractTableElementMetaclass(type):
    """
    Metaclass for verifying the existence of the render method in the class.
    """

    def __new__(mcs, name, bases, attrs):
        new_class = super().__new__(mcs, name, bases, attrs)
        if name != 'AbstractTableElement':
            method_for_check = 'render'
            method_exist = False
            method_exist |= bool(attrs.get(method_for_check))
            for base in reversed(new_class.__mro__):
                method_exist |= hasattr(base, method_for_check)
            if not method_exist:
                raise RuntimeError(f'Subclass "{name}" of "AbstractTableElement" must have a '
                                   f'"{method_for_check}" method.')
        return new_class


class AbstractTableElement(metaclass=AbstractTableElementMetaclass):
    """
    Render object template string when accessing it.
    """

    pass


AbstractTableElementType = TypeVar('AbstractTableElementType', bound=AbstractTableElement)


class BaseHtmlElementWithSlots(BaseHtmlElement):
    """
    Parent class for all table elements with __slots__ attribute to eliminate memory leak in case of a large
    number of cells.
    """

    __slots__ = ('data', 'css_classes', 'html_params')


class Td(AbstractTableElement, BaseHtmlElementWithSlots):
    """
    Class for implementing a table cell element (td).
    """

    tag = 'td'

    def __init__(self,
                 data: Any = None,
                 css_classes: list = None,
                 html_params: dict = None,
                 default_value: str = '-') -> None:

        cell_data = str(data or default_value)
        super().__init__(cell_data, css_classes, html_params)


class Th(AbstractTableElement, BaseHtmlElementWithSlots):
    """
    Class for implementing a table header cell element (th).
    """

    __slots__ = ('ordering', 'ordering_url', 'is_straight_order')

    order_classes = {
        True: 'asc',
        False: 'desc'
    }

    tag = 'th'
    order = '<%(tag)s %(html_params)s>%(data)s<a href="%(ordering_url)s" class="%(order_direction)s"></a></%(tag)s>'

    def __init__(self, data: str, css_classes: list = None, html_params: dict = None, ordering: str = None):
        self.ordering = ordering
        self.ordering_url = None
        self.is_straight_order = True
        if self.ordering:
            self.html_string = self.order
        super().__init__(data, css_classes, html_params)

    def get_format_kwargs(self, **kwargs) -> dict:
        order_direction = self.order_classes[self.is_straight_order]
        return super().get_format_kwargs(ordering_url=self.ordering_url, order_direction=order_direction, **kwargs)


class TableAdvancedCell(AbstractTableElement, TemplateObjectMixin):
    """
    Class for implementing a table cell element (td) rendered from the template.
    """

    __slots__ = ('data', 'css_classes', 'html_params')

    def __init__(self, data: str, css_classes: list = None, html_params: dict = None) -> None:
        self.data = data
        self.html_params = dict(**self.html_params, **(html_params or {}))
        self.css_classes = [*self.css_classes, *(css_classes or [])]


TableCellType = TypeVar('TableCellType', Td, TableAdvancedCell)
TableHeaderCellType = TypeVar('TableHeaderCellType', Th, TableAdvancedCell)


class Caption(AbstractTableElement, BaseHtmlElementWithSlots):
    """
    Class for implementing a table caption element (caption).
    """

    tag = 'caption'


TableCaptionType = TypeVar('TableCaptionType', bound=Caption)


class BaseTableWrappingElement(BaseHtmlElementWithSlots):
    """
    General class for describing wrappers - tr, thead, tbody, tfoot.
    """

    def __init__(self,
                 data: List[Optional[AbstractTableElementType]],
                 css_classes: list = None,
                 html_params: dict = None):

        super().__init__('', css_classes, html_params)
        self.data = data

    def get_format_kwargs(self, **kwargs) -> dict:
        format_kwargs = super().get_format_kwargs(**kwargs)
        format_kwargs.update(dict(data=self.render_internal()))
        return format_kwargs

    def add_element(self, element: AbstractTableElementType) -> None:
        self.data.append(element)

    def render_internal(self) -> str:
        return ''.join([internal.render() for internal in self.data])


class Tr(AbstractTableElement, BaseTableWrappingElement):
    """
    Class for implementing a table row element (tr).
    """

    tag = 'tr'


TableRowType = TypeVar('TableRowType', bound=Tr)


class Thead(AbstractTableElement, BaseTableWrappingElement):
    """
    Class for implementing a table header element (thead).
    """

    __slots__ = ('request',)

    tag = 'thead'

    def __init__(self,
                 request: HttpRequestType,
                 data: List[AbstractTableElementType],
                 css_classes: list = None,
                 html_params: dict = None):
        self.request = request
        super().__init__(data, css_classes, html_params)
        self._setup_table_ordering()

    def _setup_table_ordering(self) -> None:
        current_ordering = self.request.GET.get('ordering')
        for row in self.data:
            for th in row.data:
                if th.ordering:
                    query = self.request.GET.dict()
                    ordering = f'-{th.ordering}' if current_ordering == th.ordering else th.ordering
                    th.is_straight_order = True if ordering.startswith('-') else False
                    query.update({'ordering': ordering})
                    th.ordering_url = f'?{urlencode(query)}'


TableHeaderType = TypeVar('TableHeaderType', bound=Thead)


class Tbody(AbstractTableElement, BaseTableWrappingElement):
    """
    Class for implementing a table body element (tbody).
    """

    tag = 'tbody'


TableBodyType = TypeVar('TableBodyType', bound=Tbody)


class Tfoot(AbstractTableElement, BaseTableWrappingElement):
    """
    Class for implementing a table footer element (tfoot).
    """

    tag = 'tfoot'


TableFooterType = TypeVar('TableFooterType', bound=Tfoot)
TableFormObjectType = TypeVar('TableFormObjectType', FilterSet, BaseForm, StaticFieldset, StaticModelFieldset)


class BaseTemplateTable(TemplateObjectMixin):
    """
    Base class for describing tables with an auto-generated template.
    """

    css_classes = ['template-tables']
    template = 'template_tables/tables/default.html'
    context_object_name = 'table'
    caption: str = ''
    empty_table_text: str = 'No data'

    _elements: list = ['table_caption', 'table_header', 'table_body', 'table_footer']
    exclude: list = []

    def __init__(self, request: HttpRequestType, object_list: Collection):
        self.request = request
        self.object_list = object_list

        self.table_caption = self.get_caption()
        self.table_header = self.get_header(self.get_header_rows())
        self.table_body = self.get_body(self.get_body_rows())
        self.table_footer = self.get_footer(self.get_footer_rows())

    def __iter__(self):
        to_render = [el for el in self._elements if el not in self.exclude]
        for element in to_render:
            yield getattr(self, element).render()

    def _get_request(self) -> Optional[HttpRequestType]:
        return self.request

    def get_caption(self) -> TableCaptionType:
        return Caption(self.caption)

    def get_header(self, header_rows: List[TableRowType]) -> TableHeaderType:
        return Thead(request=self.request, data=header_rows)

    def get_body(self, body_rows: List[TableRowType]) -> TableBodyType:
        return Tbody(body_rows)

    def get_footer(self, footer_rows: List[TableRowType]) -> TableFooterType:
        return Tfoot(footer_rows)

    def get_header_rows(self) -> List[TableRowType]:
        return [Tr([])]

    def get_footer_rows(self) -> List[TableRowType]:
        return [Tr([])]

    def get_body_rows(self) -> List[TableRowType]:
        rows = []
        if self.object_list:
            for index, data_item in enumerate(self.object_list):
                row = self.get_body_row(index, data_item)
                rows.append(row)
        else:
            rows.append(self.get_row_for_empty_table())
        return rows

    def get_body_row(self, index: int, data_item: Any) -> TableRowType:
        cells = []
        return Tr(cells)

    def get_context_data(self, **kwargs) -> dict:
        return super().get_context_data(
            **{self.context_object_name: self}, **kwargs
        )

    def get_row_for_empty_table(self) -> TableRowType:
        th_first_tr = self.table_header.data[:1]
        colspan = len(th_first_tr[0].data) if th_first_tr else 1
        return Tr([Td(self.empty_table_text, html_params=dict(colspan=colspan))])


TemplateTableType = TypeVar('TemplateTableType', bound=BaseTemplateTable)


class TemplateTablePagination(TemplateObjectMixin):
    """
    Table pagination class.
    """

    css_classes = ['template-tables-pagination']
    template = 'template_tables/pagination.html'
    context_object_name = 'pagination'

    page_ranges = [10, 30, 50]
    default_page_range = 10

    paginate_by_parameter_name: str = 'paginate_by'
    page_parameter_name: str = 'page'

    def __init__(self, request: HttpRequestType, page_object: Page, object_list: Collection, paginate_by: int):
        self.request = request
        self.page_object = page_object
        self.paginator = page_object.paginator
        self.object_list = object_list
        self.paginate_by = int(paginate_by)

        self._objects_count = None

    @property
    def objects_count(self) -> int:
        if not self._objects_count:
            self._objects_count = len(self.object_list)
        return self._objects_count

    @property
    def items_range(self) -> str:
        page_number = self.page_object.number
        if page_number and self.objects_count is not None and self.paginate_by:
            floor = (int(page_number) - 1) * int(self.paginate_by)
            items_range = f'{floor + 1} - {floor + int(self.objects_count)}'
        else:
            items_range = '0'

        return f'{items_range} / Всего записей: {self.paginator.count}'

    @property
    def next_page(self) -> str:
        if self.page_object.has_next():
            return f'?{self._get_page_query_string(1)}'

    @property
    def previous_page(self) -> str:
        if self.page_object.has_previous():
            return f'?{self._get_page_query_string(-1)}'

    @property
    def page_range_urls(self) -> dict:
        urls = dict()
        for page_range in self.page_ranges:
            query = self.request.GET.dict()
            query.update({self.paginate_by_parameter_name: page_range})
            urls[page_range] = f'?{urlencode(query)}'

        return urls

    @classmethod
    def get_paginate_by_value(cls, request: HttpRequestType, default: int = None) -> int:
        # redirecting the user to the first page when changing the range of pages.
        saved_page_range = request.session.get('user_page_range')
        page_range = request.GET.get(cls.paginate_by_parameter_name, default or cls.default_page_range)
        if page_range != saved_page_range:
            request.GET._mutable = True
            request.GET[cls.page_parameter_name] = 1
            request.GET._mutable = False
        request.session.update({'user_page_range': page_range})
        return page_range

    def _get_page_query_string(self, page_increment: int) -> str:
        query = self.request.GET.dict()
        query.update({self.page_parameter_name: self.page_object.number + page_increment})
        return urlencode(query)

    def _get_request(self) -> Optional[HttpRequestType]:
        return self.request


TemplateTablePaginationType = TypeVar('TemplateTablePaginationType', bound=TemplateTablePagination)
