__all__ = (
    'BaseCodec',
    'BaseAvroCodec',
)

import abc


class BaseCodec(metaclass=abc.ABCMeta):

    __slots__ = ()

    @abc.abstractmethod
    def encode(self, *args, **kwargs):
        raise NotImplementedError()

    @abc.abstractmethod
    def iter_encode(self, *args, **kwargs):
        raise NotImplementedError()

    @abc.abstractmethod
    def decode(self, *args, **kwargs):
        raise NotImplementedError()

    @abc.abstractmethod
    def iter_decode(self, *args, **kwargs):
        raise NotImplementedError()


class BaseAvroCodec(BaseCodec):

    __slots__ = ()

    @abc.abstractmethod
    def encode_with_schema_id(self, *args, **kwargs):
        raise NotImplementedError()

    @abc.abstractmethod
    def iter_encode_with_schema_id(self, *args, **kwargs):
        raise NotImplementedError()

    @abc.abstractmethod
    def encode_with_schema_registry(self, *args, **kwargs):
        raise NotImplementedError()

    @abc.abstractmethod
    def iter_encode_with_schema_registry(self, *args, **kwargs):
        raise NotImplementedError()

    @abc.abstractmethod
    def decode_with_schema_registry(self, *args, **kwargs):
        raise NotImplementedError

    @abc.abstractmethod
    def iter_decode_with_schema_registry(self, *args, **kwargs):
        raise NotImplementedError()
