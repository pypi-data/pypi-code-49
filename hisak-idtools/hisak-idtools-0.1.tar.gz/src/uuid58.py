import uuid
from .base58 import Base58

_base58 = Base58()


def uuid1(node=None, clock_seq=None):
    # type: (int, int) -> UUID58
    return UUID58(uuid.uuid1(node, clock_seq).hex)


def uuid3(namespace, name):
    # type: (uuid.UUID, str) -> UUID58
    return UUID58(uuid.uuid3(namespace, name).hex)


def uuid4():
    # type: () -> UUID58
    return UUID58(uuid.uuid4().hex)


def uuid5(namespace, name):
    # type: (uuid.UUID, str) -> UUID58
    return UUID58(uuid.uuid5(namespace, name).hex)


class UUID58(uuid.UUID):
    @property
    def base58(self):
        # type: () -> str
        return _base58.encode(self.bytes).decode('ascii')

    @property
    def base58check(self):
        # type: () -> str
        return _base58.encode_check(self.bytes).decode('ascii')

    @classmethod
    def from_base58(cls, s):
        # type: (str) -> 'UUID58'
        return UUID58(bytes=_base58.decode(s.encode('ascii')))

    @classmethod
    def from_base58check(cls, s):
        # type: (str) -> 'UUID58'
        return UUID58(bytes=_base58.decode_check(s.encode('ascii')))
