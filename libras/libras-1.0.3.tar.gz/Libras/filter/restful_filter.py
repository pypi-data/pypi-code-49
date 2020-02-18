from . import Filter
import json


class RestfulFilter(Filter):
    @classmethod
    def do_filter(cls, rv, status):
        if isinstance(rv, tuple):
            len_rv = len(rv)
            if len_rv == 3:
                rv, status, headers = rv
            elif len_rv == 2:
                rv, status = rv
            else:
                rv = None
            rv = json.loads(rv) if rv else {}
        return rv, status

