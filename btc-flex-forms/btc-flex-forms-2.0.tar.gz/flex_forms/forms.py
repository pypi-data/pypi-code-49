from collections import OrderedDict
from copy import deepcopy
from typing import Any, Type, Iterable, TypeVar, Optional

from dev_tools.template.mixins import FlexWrapperMixin, TemplateFlexObjectMixin
from dev_tools.template.utils import Collector
from dev_tools.utils import safety_get_attribute, camel_to_snake, format_date
from django.db.models import Model
from django.forms import Form, ModelForm, Field, Widget, BaseFormSet
from django.forms.forms import DeclarativeFieldsMetaclass, BaseForm
from django.forms.models import ModelFormMetaclass, BaseInlineFormSet, BaseModelFormSet

from flex_forms.components import StaticFlexField, FlexDataArrayType, FormError, FormErrorType, BaseStaticFlexField

ModelType = TypeVar('ModelType', bound=Model)
ModelFieldType = TypeVar('ModelFieldType', bound=Field)


# Service classes

class FlexFormParameters:
    """
    Flex form additional parameters collection.
    """

    REQUIRED_TEXT = 'required_text'
    ICON = 'icon'
    ADDITIONAL_ICON = 'additional_icon'
    SHOW_ERRORS = 'show_errors'
    WRAPPER_TEMPLATE = 'wrapper_template'
    FIELD_GROUP_CLASS = 'field_group_class'
    READONLY = 'readonly'
    DISABLED = 'disabled'

# endregion


# region Mixins

class FlexWidgetWrapperMixin:
    """
    Mixin which provides some methods for wrapping field widget templates by custom html-wrappers.
    """

    _DEFAULT = 'default'
    _CHECKBOX_INPUT = 'CheckboxInput'
    _CHECKBOX_MULTI = 'CheckboxSelectMultiple'
    _RADIO_SELECT = 'RadioSelect'

    _EXTRA_WIDGETS = (
        _CHECKBOX_INPUT,
        _CHECKBOX_MULTI,
        _RADIO_SELECT
    )

    _fields_wrapper_templates: dict = {
        _DEFAULT: 'flex_forms/fields/generic.html',
        _CHECKBOX_INPUT: 'flex_forms/fields/checkbox.html',
        _CHECKBOX_MULTI: 'flex_forms/fields/checkbox_multi.html',
        _RADIO_SELECT: 'flex_forms/fields/radio.html'
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._set_fields_wrapper_template_name()

    @classmethod
    def _get_widget_base_class(cls, field_widget: Widget) -> str:
        base_class = None
        if field_widget:
            base_classes = [fidget_class.__name__ for fidget_class in field_widget.__class__.__mro__]
            classes_intersection = set(cls._EXTRA_WIDGETS) & set(base_classes)
            if classes_intersection:
                base_class = classes_intersection.pop()
        return base_class

    def _set_fields_wrapper_template_name(self) -> None:
        # set wrapper_template to every form field in according to widget class.
        for field_name, field in getattr(self, 'fields', {}).items():
            widget = field.widget
            if FlexFormParameters.WRAPPER_TEMPLATE not in widget.attrs.keys():
                widget.attrs[FlexFormParameters.WRAPPER_TEMPLATE] = self.get_field_wrapper_template(field)

    def get_field_wrapper_template(self, field: Type[Field]) -> str:
        widget_class = self._get_widget_base_class(field.widget) or self._DEFAULT
        return self._fields_wrapper_templates.get(widget_class)


class StaticFieldsSupportMixin:
    """
    Adds static fields support to object.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.static_fieldset = deepcopy(self.static_class_fields)


class CommonFlexWrapperMixin(FlexWrapperMixin):
    """
    Setting field wrappers for core classes in separate mixin.
    """

    _row_str: str = 'flex_forms/blocks/row.html'
    _block_str: str = 'flex_forms/blocks/block.html'


class FlexFormMixin(CommonFlexWrapperMixin, FlexWidgetWrapperMixin, StaticFieldsSupportMixin):
    """
    The main mixin for converting a normal form / model form into a flex form.
    """

    flex_type = 'form'
    css_classes = ['flex-object']
    template = 'flex_forms/forms/generic_form.html'
    context_object_name = 'form'
    html_params = {'method': 'POST', 'action': '/'}


class FlexFormsetMixin(TemplateFlexObjectMixin):
    """
    Mixin such as FlexFormMixin - converts formset into a flex formset.
    """

    flex_type = 'formset'
    css_classes = ['flex-object']
    template = 'flex_forms/forms/generic_formset.html'
    context_object_name = 'formset'
    html_params = {'method': 'POST', 'action': '/'}


class StaticFieldsetMixin(CommonFlexWrapperMixin, StaticFieldsSupportMixin):
    """
    Converts object to StaticFieldset.
    """

    flex_type = 'fieldset'
    css_classes = ['flex-object']
    html_params = {}
    template = 'flex_forms/fieldsets/generic_fieldset.html'
    context_object_name = 'fieldset'


class StaticModelFieldsetMethodsMixin:
    """
    Mixin, which provides methods for obtaining data of model objects.
    """

    default_value: Optional[str] = '-'
    defaults: dict = {}
    defaults_if_none: dict = {}
    date_format: str = 'd.m.Y'
    time_format: str = 'H:i'
    date_time_format: str = 'd.m.Y H:i'

    def _prepare_expressions(self, expression: str) -> str:
        # remove method's parentheses.
        # it's ok to use parentheses to indicate methods.
        return expression.replace('()', '')

    def get_data(self, instance: Optional[ModelType], field_name: str) -> tuple:
        expression = self._prepare_expressions(field_name)
        last_instance, expression_part = safety_get_attribute(instance, expression, get_last_object=True)
        field = last_instance._meta.get_field(expression_part) if last_instance else None
        value = self.get_field_display_value(last_instance, field)
        return last_instance, field, value

    def get_defaults(self, field_name: str, value: Optional[str]) -> str:
        default = value
        if default is None:
            default = self.defaults_if_none.get(field_name)
        if not default:
            default = self.defaults.get(field_name)
        return default or self.default_value or value

    def get_value(self, instance: Optional[ModelType], field_name: str) -> Any:
        value = self.get_data(instance, field_name)[2]
        return value or self.get_defaults(field_name, value)

    def get_field_display_value(self, instance: Optional[ModelType], field: Optional[ModelFieldType]) -> Optional[str]:
        # check field type and get the value.
        display_value = None
        if instance and field:
            method_name = 'get_%s_display'
            internal_type = field.get_internal_type()
            field_value = getattr(instance, field.name, None)
            if field_value:
                display_value = getattr(self, method_name % camel_to_snake(internal_type),
                                        self.get_default_display)(field, field_value)
        return display_value

    def get_default_display(self, field: ModelFieldType, field_value: Any) -> str:
        if getattr(field, 'choices'):
            display_value = self.get_choice_field_display(field, field_value)
        else:
            display_value = str(field_value)
        return display_value

    def get_foreign_key_display(self, field: ModelFieldType, field_value: Any) -> str:
        return str(field_value)

    def get_many_to_many_field_display(self, field: ModelFieldType, field_value: Any) -> str:
        return ', '.join([str(related) for related in field_value.iterator()])

    def get_time_field_display(self, field: ModelFieldType, field_value: Any) -> str:
        return format_date(field_value, self.time_format)

    def get_date_field_display(self, field: ModelFieldType, field_value: Any) -> str:
        return format_date(field_value, self.date_format)

    def get_date_time_field_display(self, field: ModelFieldType, field_value: Any) -> str:
        return format_date(field_value, self.date_time_format)

    def get_choice_field_display(self, field: ModelFieldType, field_value: Any) -> str:
        choices = dict(field.choices)
        if isinstance(field_value, (int, str, bool)):
            display_value = choices.get(field_value, field_value)
        elif isinstance(field_value, list):  # ArrayField
            display_value = ', '.join([str(choices.get(value_item, value_item)) for value_item in field_value])
        else:
            display_value = field_value
        return display_value


class StaticModelFieldsetMixin(StaticModelFieldsetMethodsMixin, StaticFieldsetMixin):
    """
    Adds support for rendering static model data.
    """

    labels: dict = {}

    def __init__(self, instance, *args, **kwargs):
        self.instance = instance
        super().__init__(*args, **kwargs)
        self.prepare_static_fieldset()
        self._update_static_fields()

    def prepare_static_fieldset(self) -> None:
        pass

    def _update_static_fields(self):
        collector = Collector()
        static_fields = collector.get_all_nodes_from_dict(self.get_grid())
        for field_name in static_fields:
            if field_name not in self.static_class_fields and field_name not in self.static_fieldset:
                last_instance, field, value = self.get_data(self.instance, field_name)
                field_verbose_name = getattr(field, 'verbose_name', '').capitalize()
                verbose_name = self.labels.get(field_name) or field_verbose_name
                filed_value = value or self.get_defaults(field_name, value)
                self.static_fieldset.update({field_name: StaticFlexField(data=filed_value, label=verbose_name)})


class MixedFlexFormMixin(CommonFlexWrapperMixin, StaticFieldsSupportMixin):
    """
    Allows render mixed groups of flex objects - forms / model forms / formsets.
    """

    flex_type = 'flex_group'
    css_classes = ['flex-object']
    template = 'flex_forms/forms/group_template.html'
    context_object_name = 'group'
    html_params = {'method': 'POST', 'action': '/'}

    def __init__(self, form_objects, *args, **kwargs):
        self.form_objects = form_objects
        self.fields = OrderedDict()
        self.forms = []
        self.bound_fields = OrderedDict()
        super().__init__(*args, **kwargs)
        self._collect_fields(form_objects)

    def _update_fields(self, form_object: Any) -> None:
        # get bound fields from the form.
        form_fields = getattr(form_object, 'fields', None)
        if form_fields:
            self.fields.update(form_object.fields)
            prefix = form_object.prefix
            self.bound_fields.update({
                f'{prefix + "-" if prefix else ""}{field_name}': form_object[field_name]
                for field_name in form_object.fields.keys()
            })
        self.static_fieldset.update(form_object.static_fieldset)

    def _collect_fields(self, form_objects: Iterable) -> None:
        for item in form_objects:
            if isinstance(item, BaseForm):
                self._update_fields(item)
                self.forms.append(item)
            elif isinstance(item, BaseFormSet):
                self._collect_fields(item)

    def __getitem__(self, name):
        return self.bound_fields[name]

    def __iter__(self):
        for item in self.form_objects:
            yield item


class FlexFormErrorsMixin:
    """
    Adds a static field to the form with array of collected form errors.
    """

    errors_field_name: str = 'form_errors'
    __has_errors: bool = False

    def full_clean(self):
        super().full_clean()
        self.set_form_errors_to_field()

    def set_form_errors_to_field(self) -> None:
        form_errors = self.get_form_errors()
        form_field = self.get_form_errors_static_field()
        for error in form_errors:
            form_field.add_data(self.get_form_error_element(error))

    def get_form_errors(self) -> Iterable:
        form_errors = []
        if hasattr(self, 'non_field_errors'):
            form_errors = self.non_field_errors()
        if form_errors:
            self.__has_errors = True
        return form_errors

    def get_form_errors_static_field(self) -> FlexDataArrayType:
        return self.static_fieldset[self.errors_field_name]

    def get_form_error_element(self, data: Any) -> FormErrorType:
        return FormError(data)

    def get_grid_with_errors(self, grid: dict) -> dict:
        new_grid = deepcopy(grid)
        if not self.__has_errors:
            for key, value in new_grid.items():
                if self.errors_field_name in value:
                    new_grid[key].remove(self.errors_field_name)
                    break
        return new_grid

    def get_grid(self) -> dict:
        grid = super().get_grid()
        return self.get_grid_with_errors(grid)

# endregion


# region Meta classes

class StaticFlexFieldsMetaclass(type):
    """
    Metaclass for collecting StaticFlexField fields from parent classes and assigning them to
    static_fields class variable.
    """

    def __new__(mcs, name, bases, attrs):
        static_fields = []
        for key, value in list(attrs.items()):
            if isinstance(value, BaseStaticFlexField):
                static_fields.append((key, value))
                attrs.pop(key)
        attrs['static_fields'] = OrderedDict(static_fields)

        new_class = super().__new__(mcs, name, bases, attrs)

        # Walk through the MRO.
        static_fields = OrderedDict()
        for base in reversed(new_class.__mro__):
            # Collect fields from base class.
            if hasattr(base, 'static_fields'):
                static_fields.update(base.static_fields)
            # Field shadowing.
            for attr, value in base.__dict__.items():
                if value is None and attr in static_fields:
                    static_fields.pop(attr)

        new_class.static_class_fields = static_fields

        return new_class


class FlexFormObjectMetaclass(StaticFlexFieldsMetaclass, DeclarativeFieldsMetaclass):
    """
    Provides static fields collect from mro.
    """

    pass


class FlexModelFormMetaclass(StaticFlexFieldsMetaclass, ModelFormMetaclass):
    """
    A metaclass, such as for FlexForm, but a subclass of ModelFormMetaclass.
    """

    pass


# endregion


# region Main classes


class StaticFieldset(StaticFieldsetMixin, metaclass=StaticFlexFieldsMetaclass):
    """
    Usage: when you need to display arbitrary static information on the page.
    For example:

    In view:
    static_data = StaticFieldset(model_1=some_model, model_2=another_model)

    In form:
    grid = {
        ['field_1', 'field_2'],  # etc.
        ...
    }
    field_1 = StaticFlexField(label='Data 1', help_text='Field 1')
    field_2 = StaticFlexField(data='Some data', label='Data 2')

    def __init__(*args, **kwargs)
        self.model_1 = kwargs.pop('model_1', None)
        self.model_2 = kwargs.pop('model_2', None)
        super().__init__(*args, **kwargs)
        self.static_fieldset['field_1'].data = self.model_1.field_1 + self.model_2.field_1
        ...
    """

    pass


class StaticModelFieldset(StaticModelFieldsetMixin, metaclass=FlexFormObjectMetaclass):
    """
    Usage: when you need to display static information on a page based on model data.
    For example:

    # In view:
    my_model = get_object_or_404(MyModel, pk=self.kwargs.get('pk'))
    static_model_data = StaticModelFieldset(instance=my_model)

    # In form:
    # Support is for StaticFlexField only.
    grid = {
        '_1': ['model_field_1', 'model_field_2'],
        '_2': ['separate_static_field'],  # etc.
        ...
    }
    separate_field = StaticFlexField('This is a static field')  # only static fields can be defined.
    """

    pass


class MixedFlexForm(MixedFlexFormMixin, metaclass=StaticFlexFieldsMetaclass):
    """
    Usage: when you need to display multiple forms on a page with a mixed arrangement of fields.
    For example:

    # In view:
    mix = MixedFlexForm([form_1, form_2, formset_1])  # form_1, form_2, formset_1 - must be are flex too!

    # In form:                  static field from the form_2
    grid = {                               /
        '_1': ['form_1_field_2', 'form_2_static_field_1', [formset_1_field_1, form_1_field_1]],
        '_2': ['separate_field', 'form_1_field_3', 'separate_static_field'],  # etc.
        ...                                                \
    }                                        field defined below (non-forms field)

    # You can define separate non-forms fields and specify them in grid.
    separate_field = forms.CharField()
    separate_static_field = StaticFlexField('This is a static field')

    # If you use prefixes for forms (this will be needed if the forms have the same field names (formset)),
    # you must specify fields with prefixes:
    grid = {
        ['form_1_prefix-form_1_field_2', 'form_2_prefix-form_2_field_1'],  # etc.
        ...
    }
    """

    pass


class FlexForm(FlexFormMixin, Form, metaclass=FlexFormObjectMetaclass):
    pass


class FlexModelForm(FlexFormMixin, ModelForm, metaclass=FlexModelFormMetaclass):
    pass


class FlexFormset(FlexFormsetMixin, BaseFormSet):
    pass


class FlexModelFormset(FlexFormsetMixin, BaseModelFormSet):
    pass


class FlexInlineFormset(FlexFormsetMixin, BaseInlineFormSet):
    pass

# endregion
