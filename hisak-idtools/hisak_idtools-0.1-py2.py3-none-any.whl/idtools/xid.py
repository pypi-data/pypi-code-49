import os
import sys
import time
import struct
import hashlib
import platform
from threading import Lock
from datetime import datetime
from .base32 import Base32


class InvalidId(Exception):
    pass


def _real_machine_id():
    # type: () -> bytes
    hid = ''
    system = platform.system()
    if system == 'Linux':
        try:
            with open('/sys/class/dmi/id/product_uuid') as f:
                hid = f.read()
        except IOError:
            pass
    # TODO: readPlatformMachineID is Linux only implementation. Implement other OS if needed
    if not hid:
        hid = platform.node()
    if hid:
        md5 = hashlib.md5()
        md5.update(hid.encode('latin-1'))
        return md5.digest()[:3]
    # Fallback to rand number if machine id can't be gathered
    return os.urandom(3)


def _count_generator():
    def rand_int():
        # type: () -> int
        buf = struct.unpack('BBB', os.urandom(3))
        return buf[0] << 16 | buf[1] << 8 | buf[2]
    count = rand_int()
    while True:
        # reset 3-byte counter
        if count < 0xffffff:
            count += 1
        else:
            count = 0
        yield count


_py3k = sys.version_info.major > 2
_encoded_len = 20
_raw_len = 12
_lock = Lock()
_base32hex = Base32(base32hex=True)
_machine_id = _real_machine_id()
_object_id_counter = _count_generator()


def new_xid():
    # type: () -> Xid
    now = int(time.time())
    pid = os.getpid()
    id_ = b''
    # Timestamp, 4 bytes, big endian
    id_ += struct.pack('>I', now & 0xffffffff)
    # Machine, first 3 bytes of md5(hostname)
    id_ += _machine_id
    # Pid, 2 bytes, specs don't specify endianness, but we use big endian.
    id_ += struct.pack('>H', pid & 0xffff)
    # Increment, 3 bytes, big endian
    _lock.acquire()
    count = next(_object_id_counter)
    _lock.release()
    id_ += struct.pack('>I', count & 0xffffff)[-3:]
    return Xid(id_)


class Xid:
    def __init__(self, id_):
        # type: (bytes) -> None
        if len(id_) != _raw_len:
            raise InvalidId('Xid length is {} bytes'.format(_raw_len))
        self._value = id_

    @property
    def time(self):
        # type: () -> datetime
        time_, = struct.unpack('>I', self._value[:4])
        return datetime.fromtimestamp(time_)

    @property
    def machine(self):
        # type: () -> bytes
        return self._value[4:7]

    @property
    def pid(self):
        # type: () -> int
        pid, = struct.unpack('>H', self._value[7:9])
        return pid

    @property
    def counter(self):
        # type: () -> int
        count, = struct.unpack('>I', b'\x00' + self._value[9:12])
        return count

    @property
    def string(self):
        # type: () -> str
        str_ = _base32hex.encode(self._value).lower()[:_encoded_len]
        return str_.decode() if _py3k else str_

    @property
    def bytes(self):
        # type: () -> bytes
        return self._value

    def __repr__(self):
        return '<Xid at {}>'.format(self.string)

    def __str__(self):
        return self.string

    def __eq__(self, other):
        # type: ('Xid') -> bool
        return self._value == other._value

    def __ne__(self, other):
        # type: ('Xid') -> bool
        return self._value != other._value

    def __lt__(self, other):
        # type: ('Xid') -> bool
        return self._value < other._value

    def __le__(self, other):
        # type: ('Xid') -> bool
        return self._value <= other._value

    def __gt__(self, arg):
        # type: ('Xid') -> bool
        return self._value > arg._value

    def __ge__(self, other):
        # type: ('Xid') -> bool
        return self._value >= other._value

    @classmethod
    def from_string(cls, s):
        # type: (str) -> 'Xid'
        if len(s) != _encoded_len:
            raise InvalidId('Xid string is {} characters'.format(_encoded_len))
        val = _base32hex.decode(s.upper().encode('ascii'))
        return cls(val)
