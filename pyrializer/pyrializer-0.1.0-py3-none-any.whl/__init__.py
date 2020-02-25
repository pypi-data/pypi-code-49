from .decode import decode
from .encode import encode


__all__ = [
    'serializable'
]


@classmethod
def _decode(cls, context):
    return decode(cls, context)


def _encode(self):
    return encode(self.__class__, self)


def serializable(cls):
    setattr(cls, 'decode', _decode)
    setattr(cls, 'encode', _encode)
    return cls
