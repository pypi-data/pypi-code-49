from _contextvars import ContextVar

name = 'kode_rpc'

request_trace_id: ContextVar[str] = ContextVar('request_trace_id')
