import time
from . import constant
from .context import ctx


class Span:

    # __slots__ = ['id', 'traceid', 'parentid', 'tags', 'timestamp', 'duration', 'endpoint', 'flag']
    fields = ['id', 'traceid', 'parentid', 'tags', 'timestamp', 'duration', 'endpoint', 'flag']

    def __init__(self, tracer, traceid, id, name, parent_id=0):
        self.tracer = tracer
        self.name = name
        self.traceid = traceid
        self.id = id
        self.parentid = parent_id
        self.tags = []
        self.flag = 0
        self.start_time = self.finish_time = self.timestamp = None

    @property
    def fields(self):
        return ["name", "id", "traceid", "parentid", "tags", "duration", "timestamp", "endpoint", "flag"]

    def set_flag(self, flag):
        self.flag = self.flag | flag

    def mark(self, span_type):
        self.flag = (self.flag & 0xffffffffffff00f) | span_type

    def set_tag(self, k, v):
        timestamp = int(round(time.time() * 1000 * 1000))
        tag = {"key": k,
               "value": v,
               "timestamp": timestamp}
        self.tags.append(tag)

    def start(self, start_time=None):
        self.start_time = start_time or int(round(time.time() * 1000 * 1000))

    def is_sampled(self):
        # if self.flag & constant.SAMPLED:
        # TODO use real flag
        if constant.SAMPLED:
            return True

    @property
    def duration(self):
        return int(self.finish_time - self.start_time)

    @property
    def endpoint(self):
        return self.tracer.endpoint.to_dict()

    def to_dict(self):
        ret = {}
        for key in self.fields:
            ret[key] = getattr(self, key)
        return ret

    def set_child_of(self, headers: dict()):
        try:
            headers.update({constant.PARENTID_KEY: str(self.id)})
            headers.update({constant.TRACEID_KEY: str(self.traceid)})
        except Exception:
            pass

    def clear(self):
        try:
            del ctx.trace_id
            del ctx.span_id
            del ctx.parent_id
            del ctx.span
        except KeyError:
            pass

    def finish(self):
        if self.is_sampled():
            self.finish_time = self.timestamp = int(round(time.time() * 1000 * 1000))
            self.tracer.report_span(self)
            self.clear()
