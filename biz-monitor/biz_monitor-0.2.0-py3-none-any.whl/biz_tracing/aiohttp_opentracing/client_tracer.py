import aiohttp
import opentracing
from opentracing import tags

from biz_monitor.biz_tracing.tracer import inc_level


async def on_request_start(session, trace_config_ctx, params: aiohttp.TraceRequestStartParams):
    tracer = opentracing.tracer
    span = tracer.start_span(params.method)
    inc_level(span)
    span.set_tag(tags.COMPONENT, 'aiohttp')
    span.set_tag(tags.SPAN_KIND, tags.SPAN_KIND_RPC_CLIENT)
    span.set_tag(tags.HTTP_URL, params.url.path)
    span.set_tag(tags.HTTP_METHOD, params.method)
    carrier_headers = {}
    tracer.inject(span.context,
                  opentracing.Format.HTTP_HEADERS,
                  carrier_headers)
    params.headers.update(carrier_headers)

    trace_config_ctx.span = span


async def on_request_end(session, trace_config_ctx, params: aiohttp.TraceRequestEndParams):
    span = trace_config_ctx.span
    span.set_tag(tags.HTTP_STATUS_CODE, params.response.status)
    span.finish()


async def on_request_exception(session, trace_config_ctx, params: aiohttp.TraceRequestExceptionParams):
    span = trace_config_ctx.span
    span.set_tag(tags.ERROR, True)
    span.set_tag("error.object", params.exception)
    span.finish()


trace_config = aiohttp.TraceConfig()
trace_config.on_request_start.append(on_request_start)
trace_config.on_request_end.append(on_request_end)
trace_config.on_request_exception.append(on_request_exception)
