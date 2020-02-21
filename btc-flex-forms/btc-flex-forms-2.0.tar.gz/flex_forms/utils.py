from typing import Any

from dev_tools.template.utils import Collector
from django.forms.renderers import get_default_renderer
from django.utils.safestring import mark_safe

from flex_forms.templatetags.flex_forms import complex_flex_field


# region template render features

class CollectorFieldNode:
    """
    A wrapper class over form field for getting field's html string.
    """

    def __init__(self, context: dict):
        self.context = context
        self.wrapper_template = context.pop('wrapper_template')

    def render(self) -> str:
        renderer = get_default_renderer()
        return mark_safe(renderer.render(self.wrapper_template, self.context))


class FlexFormObjectFieldCollector(Collector):
    """
    Collector and the main wrapper for flex fields.
    """

    row_str: str = None

    def __init__(self, form_object: Any, *args, **kwargs):
        self.form_object = form_object
        self.start_row = 0  # you can jump to any row of form grid and render only it.
        self.end_row = None
        super().__init__(self, *args, **kwargs)

    def get_row_str(self) -> str:
        # cache row string to prevent render in loop if it loading from template.
        if self.row_str is None:
            self.row_str = self.form_object.row_str
        return self.row_str

    def get_block_str(self) -> str:
        # cache block string.
        if self.block_str is None:
            self.block_str = self.form_object.block_str
        return self.block_str

    def parse_fields_map(self, grid: dict) -> str:
        result_str = ''
        for index, (row_title, row) in enumerate(grid.items()):
            if (self.start_row or 0) <= index <= (self.end_row or len(grid.keys())):
                if row_title.startswith('_'):
                    row_title = ''
                result_str += self.get_row_str() % {'title': row_title, 'row': self.parse_nested_list(row)}
        return result_str

    def prepare_node(self, node: str) -> str:
        # get BoundField or StaticFlexField
        field = self.form_object.static_fieldset.get(node) or self.form_object[node]
        context = complex_flex_field(field)
        return CollectorFieldNode(context).render()

    def get_template(self) -> str:
        return mark_safe(self.parse_fields_map(self.form_object.get_grid()))

# endregion
