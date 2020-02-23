import re

import opentracing
from aiohttp.web import middleware
from opentracing import tags
from opentracing.scope_managers.contextvars import ContextVarsScopeManager

from biz_monitor.biz_metrics import KafkaMetricsCollector
from biz_monitor.biz_tracing.tracer import init_tracer, inc_level, HTTP_URI

biz_code_reg = re.compile(r'"code": "?(\d+)"?')


def init_tracing(service_name, tracing_uri, kafka_uri, idc_name, set_name, instance_id):
    tracer = init_tracer(tracing_uri, service_name, scope_manager=ContextVarsScopeManager())
    metrics_collector = KafkaMetricsCollector(kafka_uri, service_name, idc_name, set_name, instance_id)

    @middleware
    async def tracing_middleware(request, handler):
        operation_name = handler.__name__
        headers = request.headers
        # start new span from trace info
        try:
            span_ctx = tracer.extract(opentracing.Format.HTTP_HEADERS,
                                      headers)
            scope = tracer.start_active_span(operation_name,
                                             child_of=span_ctx)
        except (opentracing.InvalidCarrierException,
                opentracing.SpanContextCorruptedException):
            scope = tracer.start_active_span(operation_name)

        inc_level(scope.span)
        # biz_logging extra needs some traced attributes
        scope.span.set_tag(tags.COMPONENT, 'aiohttp')
        scope.span.set_tag(tags.SPAN_KIND, tags.SPAN_KIND_RPC_SERVER)
        scope.span.set_tag(tags.HTTP_METHOD, request.method)
        scope.span.set_tag(tags.HTTP_URL, request.path)
        scope.span.set_tag(HTTP_URI, request.path)

        try:
            resp = await handler(request)
        except Exception as e:
            scope.span.set_tag(tags.ERROR, True)
            scope.span.log_kv({
                'event': tags.ERROR,
                'error.object': e,
            })
            raise
        else:
            scope.span.set_tag(tags.HTTP_STATUS_CODE, resp.status)
            try:
                biz_code = biz_code_reg.search(resp.text).group(1)
            except AttributeError:
                biz_code = None
            metrics_collector.report_span(scope.span, biz_code=biz_code)
        finally:
            scope.close()

        return resp

    return tracing_middleware
