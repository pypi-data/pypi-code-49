from typing import Any, TypeVar, List

from django.forms import BoundField
from django.utils.html import format_html


class TemplateElement:
    """
    Class with some methods to prepare template elements before render.
    """

    @staticmethod
    def prepare_html_params(html_params: dict) -> str:
        return ' '.join([f'{key}="{str(value)}"' for key, value in html_params.items()])

    @staticmethod
    def prepare_css_classes(css_classes: list) -> str:
        return ' '.join(css_classes)


class RenderedSimpleHTMLElement:
    """
    Class for elements that need render as string.
    """

    html_string: str = None

    def get_format_kwargs(self, **kwargs) -> dict:
        return kwargs

    @property
    def raw_string(self) -> str:
        string = self.html_string % self.get_format_kwargs()
        return self._prepare_string(string)

    def _prepare_string(self, raw_string: str) -> str:
        return raw_string

    def render(self) -> str:
        return format_html(self.raw_string)


class BaseHtmlElement(RenderedSimpleHTMLElement, TemplateElement):
    """
    Base class for all html elements.
    """

    html_string: str = '<%(tag)s %(html_params)s>%(data)s</%(tag)s>'
    common_css_classes: list = []
    common_html_params: dict = {}
    tag: str = 'span'

    def __init__(self, data: str, css_classes: list = None, html_params: dict = None) -> None:
        self.data = self.format_data(data) or data
        self.html_params = dict(**self.common_html_params, **(html_params or {}))
        self.css_classes = [*self.common_css_classes, *(css_classes or [])]

    def get_format_kwargs(self, **kwargs) -> dict:
        format_kwargs = dict(
            data=self.data,
            html_params=self.prepare_html_params(self.html_params),
            tag=self.tag,
            **kwargs
        )
        return super().get_format_kwargs(**format_kwargs)

    def prepare_html_params(self, html_params: dict) -> str:
        prepared_css_classes = self.prepare_css_classes(self.css_classes)
        if prepared_css_classes:
            html_params.update({'class': prepared_css_classes})
        return super().prepare_html_params(html_params)

    def _prepare_string(self, raw_string: str) -> str:
        return raw_string.replace(' >', '>')

    def format_data(self, data: str) -> str:
        pass


HTMLElementType = TypeVar('HTMLElementType', bound=BaseHtmlElement)


class BaseButton(BaseHtmlElement):
    """
    Generic button class.
    """

    html_string: str = '<%(tag)s %(html_params)s>%(icon)s %(data)s</%(tag)s>'
    tag: str = 'button'

    def __init__(self,
                 data: str,
                 css_classes: list = None,
                 html_params: dict = None,
                 icon: HTMLElementType = None) -> None:

        self.icon = icon.raw_string if icon else ''
        super().__init__(data, css_classes, html_params)

    def get_format_kwargs(self, **kwargs) -> dict:
        return super().get_format_kwargs(icon=self.icon, **kwargs)


BaseButtonType = TypeVar('BaseButtonType', bound=BaseButton)


class MaterialIcon(BaseHtmlElement):
    """
    A class for "material-icon" icon
    """

    tag = 'i'
    common_css_classes = ['material-icons']


class FormError(BaseHtmlElement):
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

    def __init__(self, button: BaseButtonType, field_group_class: str = ''):
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
