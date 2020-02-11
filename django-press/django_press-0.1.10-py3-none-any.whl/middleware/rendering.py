from django.http import HttpRequest
from django.template.response import TemplateResponse
from django_press.models import Context


class RenderingMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        return response

    @staticmethod
    def process_template_response(request: HttpRequest, response: TemplateResponse):
        response.context_data.update(dict(core=dict(Context.objects.values_list('key', 'value'))))
        return response
