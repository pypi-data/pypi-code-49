import logging
from functools import wraps

import opentracing
import six
from six.moves.urllib.parse import urlunparse

from ...tracer import tags

logger = logging.getLogger(__name__)


class ASGIMiddleware:
    def __init__(self, app, tracer):
        self.tracer = tracer
        self.app = app

    async def __call__(self, scope, receive, send):  # noqa: E999
        if scope["type"] not in {"http", "websocket"}:
            return await self.app(scope, receive, send)

        logger.debug("ASGI request intercepted scope=%s", scope)

        span_tags = {
            tags.COMPONENT: "asgi",
            tags.SPAN_KIND: tags.SPAN_KIND_RPC_SERVER,
            tags.HTTP_URL: get_url_from_scope(scope),
        }

        if scope["type"] == "http":
            operation_name = "HTTP %s" % scope["method"]
            span_tags[tags.HTTP_METHOD] = scope["method"]
        else:
            operation_name = scope["type"].upper()

        try:
            context = self.tracer.extract(
                format=opentracing.Format.HTTP_HEADERS,
                carrier={six.ensure_str(name): six.ensure_str(value) for name, value in scope["headers"]}
            )
        except opentracing.SpanContextCorruptedException:
            context = None

        with self.tracer.start_active_span(
            child_of=context,
            operation_name=operation_name,
            tags=span_tags,
        ) as tracing_scope:
            span = tracing_scope.span
            return await self.app(scope, receive, wrap_send(send, span))


def wrap_send(send, span):
    @wraps(send)
    async def send_middleware(event):
        if event["type"] == "http.response.start":
            span.set_tag(tags.HTTP_STATUS_CODE, event["status"])
        return await send(event)
    return send_middleware


def get_url_from_scope(scope):
    host, port = scope["server"]
    return urlunparse(
        (
            six.ensure_str(scope["scheme"]),
            "%s:%s" % (six.ensure_str(host), port),
            six.ensure_str(scope["path"]),
            "",
            six.ensure_str(scope["query_string"]),
            "",
        )
    )
