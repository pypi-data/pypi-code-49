import zlib

from .rg_exceptions import RGLZMAException


class ZLib:

    @classmethod
    def compress_string(cls, _str_data: str) -> bytes:
        if isinstance(_str_data, str):
            _bytes = _str_data.encode()
            _out_bytes = zlib.compress(_bytes)
            return _out_bytes
        else:
            raise RGLZMAException("data is not in string format")

    @classmethod
    def decompress(cls, _str_data: bytes) -> str:
        if isinstance(_str_data, bytes):
            _out_bytes = zlib.decompress(_str_data)
            return _out_bytes.decode()
        else:
            raise RGLZMAException("data is not in bytes format")

