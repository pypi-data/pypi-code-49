import zlib


class ZLib:

    @classmethod
    def compress_string(cls, _data: str) -> bytes:
        return cls.compress(_data.encode())

    @classmethod
    def compress(cls, _data: bytes) -> bytes:
        return zlib.compress(_data)

    @classmethod
    def decompress(cls, _data: bytes) -> bytes:
        return zlib.decompress(_data)
