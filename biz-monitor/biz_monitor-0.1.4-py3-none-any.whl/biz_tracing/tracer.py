from typing import Tuple

import opentracing
from jaeger_client import Config
from jaeger_client.span import Span

HTTP_URI = "http.uri"
START_TIME = "start_time"
TREE_LEVEL_KEY = "treeLevel"


def extract_uri(uri) -> Tuple[str, int]:
    assert ":" in uri, f"Incorrect URI format: {uri}"
    host, port = uri.split(":")
    assert port.isdigit(), f"Incorrect port format: {port}"
    return host, int(port)


def init_tracer(tracing_uri, service, scope_manager=None):
    host, port = extract_uri(tracing_uri)
    config = Config(
        config={
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'local_agent': {
                'reporting_host': host,
                'reporting_port': port
            },
            'biz_logging': True,
        },
        service_name=service,
        scope_manager=scope_manager
    )
    opentracing.tracer = config.initialize_tracer()
    return opentracing.tracer


def inc_level(span: Span):
    """ Increment span's tree level
    """
    # NOTE: jaeger will make the baggage header lowercase
    level = span.get_baggage_item(TREE_LEVEL_KEY) or span.get_baggage_item(TREE_LEVEL_KEY.lower())
    if not level:
        level = "0"
    else:
        level = str(int(level) + 1)
    span.set_baggage_item(TREE_LEVEL_KEY, level)
