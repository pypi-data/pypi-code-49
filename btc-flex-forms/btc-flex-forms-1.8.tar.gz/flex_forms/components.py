from typing import Any, TypeVar, List, Type

from dev_tools.template.components import BaseHTMLElement, BaseButtonType, HTMLElementType, BaseButton
from django.forms import BoundField
from django.utils.html import format_html


class FormError(BaseHTMLElement):
    """
    Class as a wrapper for displaying forms errors.
    """

    tag = 'div'
    common_css_classes = ['error']


FormErrorType = TypeVar('FormErrorType', bound=FormError)


class BaseStaticFlexField:
    """
    Class that provides wrapping static html as field in flex form layout.
    """

    wrapper_template: str = None

    def __init__(self,
                 data: Any = '',
                 label: str = '',
                 icon: str = None,
                 field_group_class: str = '',
                 help_text: str = ''):

        self._data = data
        self.label = label
        self.icon = icon
        self.field_group_class = field_group_class
        self.help_text = help_text

    @property
    def data(self) -> str:
        return self.prepare_data()

    def prepare_data(self) -> str:
        return str(self._data)


class StaticFlexField(BaseStaticFlexField):
    """
    StaticFlexField interface class.
    """

    wrapper_template: str = 'flex_forms/fields/static.html'

    @property
    def data(self) -> str:
        return self.prepare_data()

    @data.setter
    def data(self, value: Any) -> None:
        self._data = value


class FlexButton(BaseStaticFlexField):
    """
    Class for adding button to the form layout.
    """

    wrapper_template: str = 'flex_forms/fields/static_button.html'

    def __init__(self,
                 data: str = '',
                 css_classes: list = None,
                 html_params: dict = None,
                 icon: HTMLElementType = None,
                 field_group_class: str = '',
                 button_class: Type[BaseButtonType] = BaseButton):

        button = button_class(data, css_classes, html_params, icon)
        super().__init__(button, field_group_class=field_group_class)

    @property
    def button(self) -> BaseButtonType:
        return self._data

    @button.setter
    def button(self, value: Any) -> None:
        self._data = value

    def prepare_data(self) -> str:
        return self._data.render()


class FlexDataArray(BaseStaticFlexField):
    """
    Provides adding mix of types of data-elements to the layout of the form.
    """

    wrapper_template: str = 'flex_forms/fields/data_array.html'

    def __init__(self,
                 array: List[HTMLElementType] = None,
                 label: str = '',
                 icon: str = None,
                 field_group_class: str = '',
                 help_text: str = ''):

        super().__init__(array or [], label, icon, field_group_class, help_text)

    @property
    def array(self) -> List[HTMLElementType]:
        return self._data

    @array.setter
    def array(self, value: List[HTMLElementType]) -> None:
        self._data = value

    def add_data(self, new_data: HTMLElementType) -> None:
        self._data += [new_data]

    def prepare_data(self) -> str:
        return format_html(''.join([item.render() for item in self._data]))


FlexFieldType = TypeVar('FlexFieldType', BoundField, StaticFlexField, FlexDataArray)
StaticFlexFieldType = TypeVar('StaticFlexFieldType', bound=BaseStaticFlexField)
FlexDataArrayType = TypeVar('FlexDataArrayType', bound=FlexDataArray)
