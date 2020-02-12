from typing import Any

from django import template
from django.forms import BoundField
from django.template import Template
from django.utils.safestring import mark_safe

from flex_forms.components import FlexFieldType, BaseStaticFlexField, StaticFlexFieldType
from flex_forms.forms import FlexFormParameters
from flex_forms.utils import CollectorFieldNode, Collector

register = template.Library()

dummy = Template("""{% extends wrapper_template %}""")


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


@register.inclusion_tag(dummy)
def flex_field(bound_field: BoundField, label: str = None, required: bool = None, **kwargs):
    """
    Takes context and render field in specified template.
    Expected params:

    - required_text
    - icon
    - show_errors
    - wrapper_template
    - field_group_class
    """

    if bound_field:
        widget = bound_field.field.widget
        field_type = type(widget).__name__
        label = label if label is not None else bound_field.label
        required = required if required is not None else bound_field.field.required
        readonly = bound_field.field.widget.attrs.get(FlexFormParameters.READONLY, False)
        disabled = bound_field.field.disabled
        icon = kwargs.get(FlexFormParameters.ICON) or widget.attrs.pop(FlexFormParameters.ICON, None)
        required_text = widget.attrs.pop(FlexFormParameters.REQUIRED_TEXT, '')
        show_errors = widget.attrs.pop(FlexFormParameters.SHOW_ERRORS, True)
        wrapper_template = \
            kwargs.get(FlexFormParameters.WRAPPER_TEMPLATE) or widget.attrs.get(FlexFormParameters.WRAPPER_TEMPLATE)
        field_group_class = \
            kwargs.get(FlexFormParameters.FIELD_GROUP_CLASS) or \
            widget.attrs.pop(FlexFormParameters.FIELD_GROUP_CLASS, '')

        context = dict(
            field=bound_field,
            field_group_class=field_group_class,
            wrapper_template=wrapper_template,
            label=label,
            required=required,
            required_text=required_text,
            field_type=field_type,
            icon=icon,
            show_errors=show_errors,
            readonly=FlexFormParameters.READONLY if readonly else '',
            disabled=FlexFormParameters.DISABLED if disabled else ''
        )
        context.update(kwargs)

        return context


@register.inclusion_tag(dummy)
def static_flex_field(static_field: StaticFlexFieldType, label: str = None, **kwargs):
    """
    Render static html as a ordinary field.
    Expected params:

    - icon
    - wrapper_template
    - field_group_class
    """

    if static_field:
        label = label if label is not None else static_field.label
        icon = kwargs.get(FlexFormParameters.ICON) or static_field.icon
        wrapper_template = kwargs.get(FlexFormParameters.WRAPPER_TEMPLATE) or static_field.wrapper_template
        field_group_class = kwargs.get(FlexFormParameters.FIELD_GROUP_CLASS) or static_field.field_group_class
        help_text = static_field.help_text
        data = static_field.data

        context = dict(
            field_group_class=field_group_class,
            wrapper_template=wrapper_template,
            label=label,
            icon=icon,
            help_text=help_text,
            data=data
        )
        context.update(kwargs)

        return context


@register.inclusion_tag(dummy)
def complex_flex_field(field: FlexFieldType, **kwargs):
    """
    Complex field context handler.
    """

    context = {}
    if isinstance(field, BoundField):
        context = flex_field(field, **kwargs)
    elif isinstance(field, BaseStaticFlexField):
        context = static_flex_field(field, **kwargs)

    return context


@register.simple_tag
def flex_form_grid(form_object: Any, start_row: int = 0, end_row: int = None) -> str:
    """
    Render form fields from map specified in the form.
    """

    collector = FlexFormObjectFieldCollector(form_object)
    collector.start_row = start_row
    collector.end_row = end_row
    return collector.get_template()


@register.simple_tag(takes_context=True)
def as_flex(context, form_object: Any) -> str:
    """
    Render form objects with csrf_token in the context.
    """

    form_object.extra_context.update(dict(csrf_token=context.get('csrf_token')))
    return form_object.as_flex()
