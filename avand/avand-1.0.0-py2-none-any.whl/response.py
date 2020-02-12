import json


class Response:
    __slots__ = ("error_code", "message", "page_num", "page_size", "total_count", "reference_id", "result", "raw")

    def __init__(self, **kwargs):
        self.raw = json.dumps(kwargs)
        self.error_code = kwargs.pop("errorCode", 0)
        self.message = kwargs.pop("message", 0)
        self.page_num = kwargs.pop("pageNum", 0)
        self.page_size = kwargs.pop("pageSize", 0)
        self.total_count = kwargs.pop("totalCount", 0)
        self.reference_id = kwargs.pop("referenceId", 0)
        self.result = kwargs.pop("result", 0)
