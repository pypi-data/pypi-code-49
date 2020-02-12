from typing import Optional, TypeVar

from django.http import HttpRequest
from django.template.loader import render_to_string

from flex_forms.components import TemplateElement


class ObjectContextMixin:
    """
    An extra context mixin that passes the keyword arguments received by
    get_context_data() as the form context.
    """

    extra_context: dict = {}

    def get_context_data(self, **kwargs) -> dict:
        if self.extra_context:
            kwargs.update(self.extra_context)
        return kwargs


class TemplateObjectContextMixin(ObjectContextMixin, TemplateElement):
    """
    Adds html attributes to class and template context.
    """

    css_classes: list = []
    html_params: dict = {}

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context.update({
            'html_params': self.prepare_html_params(self.get_html_params())
        })
        return context

    def get_html_params(self) -> dict:
        # add a class as an HTML parameter, if one exists.
        html_params = self.html_params
        if self.css_classes:
            prepared_css_classes = self.prepare_css_classes(self.get_css_classes())
            html_params.update({'class': prepared_css_classes})
        return html_params

    def get_css_classes(self) -> list:
        return self.css_classes


HttpRequestType = TypeVar('HttpRequestType', bound=HttpRequest)


class TemplateObjectMixin(TemplateObjectContextMixin):
    """
    Adds support for rendering objects with a custom template.
    """

    template: str = None
    context_object_name: str = None

    def render(self) -> str:
        return self._get_template_or_string(self.template, self.get_context_data())

    def _get_template_or_string(self, template_name_or_string: str, context_data: dict = None) -> str:
        ctx = context_data or {}
        if template_name_or_string.endswith('.html'):
            return render_to_string(template_name_or_string, ctx, request=self._get_request())
        return (template_name_or_string % ctx) if ctx else template_name_or_string

    def get_template(self) -> str:
        return self.template

    def get_context_data(self, **kwargs) -> dict:
        return super().get_context_data(**{self.context_object_name: self, **kwargs})

    def _get_request(self) -> Optional[HttpRequestType]:
        return None
