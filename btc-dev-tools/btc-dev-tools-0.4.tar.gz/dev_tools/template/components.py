from typing import TypeVar

from django.utils.html import format_html


class HTMLAttributesHandlerMixin:
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


class BaseHTMLElement(RenderedSimpleHTMLElement, HTMLAttributesHandlerMixin):
    """
    Base class for all html elements.
    """

    html_string: str = '<%(tag)s %(html_params)s>%(data)s</%(tag)s>'
    default_css_classes: list = []
    default_html_params: dict = {}
    tag: str = 'span'

    def __init__(self, data: str, css_classes: list = None, html_params: dict = None) -> None:
        self.data = self.format_data(data) or data
        self.html_params = dict(**self.default_html_params, **(html_params or {}))
        self.css_classes = [*self.default_css_classes, *(css_classes or [])]

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


HTMLElementType = TypeVar('HTMLElementType', bound=BaseHTMLElement)


class BaseButton(BaseHTMLElement):
    """
    Generic button class.
    """

    html_string: str = '<%(tag)s %(html_params)s>%(icon)s %(data)s</%(tag)s>'
    tag: str = 'button'

    def __init__(self,
                 data: str = '',
                 css_classes: list = None,
                 html_params: dict = None,
                 icon: HTMLElementType = None) -> None:

        self.icon = icon.raw_string if icon else ''
        super().__init__(data, css_classes, html_params)

    def get_format_kwargs(self, **kwargs) -> dict:
        return super().get_format_kwargs(icon=self.icon, **kwargs)


BaseButtonType = TypeVar('BaseButtonType', bound=BaseButton)
