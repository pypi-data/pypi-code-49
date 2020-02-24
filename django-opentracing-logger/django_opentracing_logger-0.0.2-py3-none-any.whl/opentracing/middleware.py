import logging

from django.http import HttpRequest, HttpResponse
from .context import ctx
from .tracer import get_tracer
from . import constant, tags
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


logger = logging.getLogger(__name__)


class DDTracerMiddleware(MiddlewareMixin):

    @staticmethod
    def start_span(request: HttpRequest):
        match = request.resolver_match
        if not match or request.path in ("/ping/", "/ping", "/favicon.ico", "/", "/static") or request.method == "HEAD":
            return
        mapping = {
            constant.TRACEID_KEY: "trace_id",
            constant.SPANID_KEY: "span_id",
            constant.PARENTID_KEY: "parent_id",
            constant.FLAG_KEY: "flag"
        }
        header_mapping = {
            constant.TRACEID_KEY: constant.HEADER.TRACEID_KEY.value,
            constant.SPANID_KEY: constant.HEADER.SPANID_KEY.value,
            constant.PARENTID_KEY: constant.HEADER.PARENTID_KEY.value,
            constant.FLAG_KEY: constant.HEADER.FLAG_KEY.value
        }
        for key in mapping:
            if header_mapping[key] in request.META:
                try:
                    setattr(ctx, mapping[key], int(request.META[header_mapping[key]]))
                except Exception:
                    pass

        tracer = get_tracer()
        span = tracer.start_span(
            match.view_name,
            ctx.get_or_generate('trace_id'),
            ctx.get_or_generate('span_id'),
            getattr(ctx, 'parent_id', 0)
        )
        span.set_tag(, request.build_absolute_uri())
        span.set_tag("http.request.method", request.method)

        setattr(ctx, 'span', span)

    @staticmethod
    def finish_span(request: HttpRequest, response: HttpResponse):
        try:
            if request.path in ("/ping/", "/ping", "/favicon.ico", "/") or request.method == "HEAD":
                return
            span = getattr(ctx, 'span', None)
            if not span:
                return
            span.set_tag("http.response.code", str(response.status_code))
            if response.status_code == 500:
                span.mark(constant.SPANKIND.ERROR.value)
            span.finish()

        except Exception as e:
            # logger.warning(e)
            pass

    def process_view(self, request, callback, callback_args, callback_kwargs):
        enable = getattr(settings, "APM_ENABLE", False)
        if enable:
            self.start_span(request)

    def process_response(self, request, response):
        enable = getattr(settings, "APM_ENABLE", False)
        if enable:
            self.finish_span(request, response)
        return response
