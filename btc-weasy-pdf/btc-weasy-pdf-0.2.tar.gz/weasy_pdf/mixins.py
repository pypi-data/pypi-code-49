from typing import Any

from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views import View
from django.views.generic.base import ContextMixin
from weasyprint import HTML


class WeasyPDFView(ContextMixin, View):
    """
    Миксин для рендеринга pdf с помощью библиотеки WeasyPrint.
    """

    file_name: str = None
    base_url: str = None

    template_name: str = None
    context_object_name: str = 'data_object'

    def get(self, *args, **kwargs):
        return self.render_to_response(
            self.get_base_url(),
            self.template_name,
            self.get_context_data(),
            file_name=self.file_name
        )

    def get_base_url(self) -> str:
        return self.base_url or self.request.build_absolute_uri('/')

    def get_object(self) -> Any:
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            self.context_object_name: self.get_object()
        })
        return context

    def render_to_response(self,
                           base_url,
                           template_name: str,
                           context: dict,
                           disposition_type='inline',
                           file_name='example.pdf') -> HttpResponse:
        """
        Render a WeasyPrint PDF and return it as HttpResponse.
        """

        html_string = render_to_string(template_name, context, self.request)
        html = HTML(string=html_string, base_url=base_url)
        pdf_file = html.write_pdf()
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = f'{disposition_type}; filename="{file_name}"'

        return response

    def render_to_file(self, base_url, template_name: str, context: dict, file_path: str) -> str:
        """
        Render a WeasyPrint PDF and save it to a file.
        """

        html_string = render_to_string(template_name, context, self.request)
        html = HTML(string=html_string, base_url=base_url)
        html.write_pdf(target=file_path)

        return file_path
