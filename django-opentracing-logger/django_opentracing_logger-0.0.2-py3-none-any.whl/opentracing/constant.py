from enum import Enum

NO_TRACE_ID = "none"

SAMPLED = 1

TRACEID_KEY = "x-trace-id"
SPANID_KEY = "x-span-id"
PARENTID_KEY = "x-parent-id"
FLAG_KEY = "x-flag"
BAGGAGE_PREFIX = "x-baggage-"

class HEADER(Enum):
    TRACEID_KEY = "HTTP_X_TRACE_ID"
    SPANID_KEY = "HTTP_X_SPAN_ID"
    PARENTID_KEY = "HTTP_X_PARENT_ID"
    FLAG_KEY = "HTTP_X_FLAG"


class SPANKIND(Enum):
    NORMAL = 0
    API = 1 << 8
    METRICS = 2 << 8
    ERROR = 3 << 8
