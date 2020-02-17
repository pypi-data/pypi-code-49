import json
from typing import Any

from aio_pika.patterns import RPC


class JsonRPC(RPC):
    SERIALIZER = json
    CONTENT_TYPE = 'application/json'

    def serialize(self, data: Any) -> bytes:
        return self.SERIALIZER.dumps(data, ensure_ascii=False).encode()

    def serialize_exception(self, exception: Exception) -> bytes:
        return self.serialize({
            'error': {
                'type': exception.__class__.__name__,
                'message': repr(exception),
                'args': exception.args,
            }
        })
