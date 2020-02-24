import time
import random
from .utils import generate_random_id, get_local_ip
from .reporter import NoopReporter, LogReporter
from .sampler import NoopSampler, AlwaysSampler
from .endpoint import Endpoint
from .span import Span
from .constant import SPANKIND


class Tracer:
    """global uniform tracer"""
    def __init__(self, name="noop", **kwargs):
        self.reporter = kwargs.get("reporter", NoopReporter())
        self.sampler = kwargs.get("sampler", NoopSampler())
        self.endpoint = Endpoint(name, get_local_ip())

    def start_span(self, name, trace_id=0, span_id=0, parent_id=0, span_type=SPANKIND.API):

        # span_id, trace_id, parent_id
        span = Span(self, trace_id, span_id, name, parent_id)
        span.start(start_time=int(round(time.time() * 1000 * 1000)))
        # 采样率设为 1
        span.set_flag(1 << 16)

        # 开启采样并采样 110b
        span.set_flag(6)
        # 默认为 API 类型
        span.mark(span_type.value)

        return span

    def report_span(self, span):
        self.reporter.report(span)


def reset_tracer():
    global tracer, is_tracer_registered
    is_tracer_registered = False
    tracer = Tracer()


def set_log_tracer(name, **kwargs):
    global tracer, is_tracer_registered
    is_tracer_registered = True
    if "reporter" not in kwargs:
        kwargs["reporter"] = LogReporter()
    if "sampler" not in kwargs:
        kwargs["sampler"] = AlwaysSampler()
    tracer = Tracer(name, **kwargs)


def set_tracer(name, **kwargs):
    global tracer, is_tracer_registered
    is_tracer_registered = True
    tracer = Tracer(name, **kwargs)


def get_tracer():
    global tracer
    return tracer


tracer = Tracer()
is_tracer_registered = False
