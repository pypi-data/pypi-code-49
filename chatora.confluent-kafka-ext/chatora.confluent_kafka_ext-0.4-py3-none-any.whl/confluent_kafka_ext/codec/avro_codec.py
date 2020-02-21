__all__ = (
    'AvroCodec',
)

from collections import deque
import contextlib
import functools
from io import (
    BytesIO,
    SEEK_CUR,
)
import struct
import time
import typing

from fastavro import (
    reader as fastavro_reader,
    schemaless_reader as fastavro_schemaless_reader,
    writer as fastavro_writer,
    schemaless_writer as fastavro_schemaless_writer,
)

from fasteners import ReaderWriterLock
import structlog

from chatora.confluent_kafka_ext.exception import (
    AvroEncodeException,
    AvroRecordEncodeException,
    AvroDecodeException,
    AvroRecordDecodeException,
)
from chatora.confluent_kafka_ext.schema.base import BaseAvroSchema
from chatora.confluent_kafka_ext.codec.base import BaseAvroCodec
from chatora.confluent_kafka_ext.schema_registry.client import SchemaRegistryClient


logger = structlog.get_logger(__name__)

MAGIC_NUM: int = 0
MAGIC_BYTES: bytes = struct.pack('b', MAGIC_NUM)
struct_record_header: struct.Struct = struct.Struct('>bI')
schema_record_header_pack: typing.Callable[
    [int, int], bytes
] = struct_record_header.pack
schema_record_header_unpack_from: typing.Callable[
    [typing.ByteString, typing.Optional[int]], typing.Tuple[int, int]
] = struct_record_header.unpack_from


class AvroCodec(BaseAvroCodec):

    __slots__ = (
        '_schema_info_rw_lock',
        '_cached_schema_info_map',
        '_cached_id_schema_map',
        'schema_entry_expire_sec',
        'schema_registry_client',
    )

    # {schema: (schema, id, cached_posix_time_in_sec)}
    _cached_schema_info_map: typing.MutableMapping[BaseAvroSchema, typing.Tuple[BaseAvroSchema, int, int]]

    # {id: schema}
    _cached_id_schema_map: typing.MutableMapping[int, BaseAvroSchema]

    def __init__(
        self,
        schema_registry_client: typing.Optional[SchemaRegistryClient] = None,
        schema_info_rw_lock: typing.Optional[ReaderWriterLock] = None,
        schema_entry_expire_sec: int = 60 * 7,
        *args, **kwargs,
    ) -> None:
        self.schema_registry_client = schema_registry_client
        self._schema_info_rw_lock = schema_info_rw_lock or ReaderWriterLock()
        self._cached_schema_info_map = {}
        self._cached_id_schema_map = {}
        self.schema_entry_expire_sec = schema_entry_expire_sec
        super().__init__(*args, **kwargs)
        return

    @staticmethod
    def write_fastavro(
        buf: BytesIO,
        fastavro_parsed_schema: typing.Any,
        value: typing.Any,
    ) -> None:
        fastavro_writer(buf, fastavro_parsed_schema, (value,))
        return

    @staticmethod
    def write_fastavro_schemaless(
        buf: BytesIO,
        fastavro_parsed_schema: typing.Any,
        value: typing.Any,
    ):
        fastavro_schemaless_writer(buf, fastavro_parsed_schema, value)
        return

    @staticmethod
    def read_fastavro(
        buf: BytesIO,
    ):
        return next(fastavro_reader(buf))

    @staticmethod
    def read_fastavro_schemaless(
        buf: BytesIO,
        fastavro_parsed_schema: typing.Any = None,
    ):
        return fastavro_schemaless_reader(buf, writer_schema=fastavro_parsed_schema)

    def _cleanup_expired_schema_info(
        self,
        base_time: typing.Union[int, float],
    ) -> None:
        cached_schema_info_map = self._cached_schema_info_map
        cached_id_schema_map = self._cached_id_schema_map
        schema_entry_expire_sec = self.schema_entry_expire_sec

        for schema, (_, schema_id, cached_time) in tuple(cached_schema_info_map.items()):
            if (base_time - cached_time) > schema_entry_expire_sec:
                del cached_schema_info_map[schema]
                del cached_id_schema_map[schema_id]
                logger.debug(
                    'cleanupped avro schema from cache',
                    callee=self.__class__._cleanup_expired_schema_info,
                    schame_fullname=schema.fullname,
                )
        return

    def get_schema_id(
        self,
        schema: BaseAvroSchema,
        subject_name: str,
        auto_register_schema: bool = False,
    ) -> typing.Tuple[BaseAvroSchema, int, int]:
        blogger = logger.bind(
            callee=self.__class__.get_schema_id,
            schame_fullname=schema.fullname,
            subject_name=subject_name,
            auto_register_schema=auto_register_schema,
        )
        blogger.debug(f'[start]')
        try:
            with self._schema_info_rw_lock.read_lock(), contextlib.suppress(KeyError):
                schema_info = self._cached_schema_info_map[schema]
                schema = self._cached_id_schema_map[schema_info[1]]
                if (time.time() - schema_info[2]) < self.schema_entry_expire_sec:
                    blogger.debug(f'[end]', schema_id=schema_info[1])
                    return schema_info

            with self._schema_info_rw_lock.write_lock():
                if auto_register_schema is True:
                    schema_id = self.schema_registry_client.put_schema_under_subject(
                        subject_name=subject_name,
                        schema=schema,
                    )['id']
                else:
                    schema_id = self.schema_registry_client.get_schema_info_under_subject(
                        subject_name=subject_name,
                        schema=schema,
                    )['id']
                current_time = int(time.time())
                self._cleanup_expired_schema_info(base_time=current_time)
                self._cached_schema_info_map[schema] = schema_info = (schema, schema_id, current_time)
                self._cached_id_schema_map[schema_id] = schema
        except:
            blogger.exception('[error]')
            raise

        blogger.debug(f'[end]', schema_id=schema_info[1])
        return schema_info

    def get_schema(
        self,
        schema_id: int,
    ) -> typing.Tuple[BaseAvroSchema, int, int]:
        blogger = logger.bind(
            callee=self.__class__.get_schema,
            schema_id=schema_id,
        )
        blogger.debug(f'[start]')
        try:
            with self._schema_info_rw_lock.read_lock(), contextlib.suppress(KeyError):
                schema = self._cached_id_schema_map[schema_id]
                schema_info = self._cached_schema_info_map[schema]
                if (time.time() - schema_info[2]) < self.schema_entry_expire_sec:
                    blogger.debug(f'[end]', schame_fullname=schema_info[0].fullname)
                    return schema_info

            with self._schema_info_rw_lock.write_lock():
                schema = self.schema_registry_client.get_schema(schema_id=schema_id)
                current_time = int(time.time())
                self._cleanup_expired_schema_info(base_time=current_time)
                self._cached_schema_info_map[schema] = schema_info = (schema, schema_id, current_time)
                self._cached_id_schema_map[schema_id] = schema
        except:
            blogger.exception('[error]')
            raise
        blogger.debug(f'[end]', schame_fullname=schema_info[0].fullname)
        return schema_info

    def encode(
        self,
        value: typing.Any,
        schema: BaseAvroSchema,
        with_schema: bool = False,
        exc_handler_func: typing.Optional[typing.Callable[
            [Exception, typing.Any, typing.Optional[BaseAvroSchema]], None
        ]] = None,
    ) -> typing.Optional[bytes]:
        if value is None:
            return None
        with BytesIO() as buf:
            try:
                (
                    self.write_fastavro if with_schema is True else self.write_fastavro_schemaless
                )(buf, schema.x_fastavro_parsed_schema, value)
                return buf.getvalue()
            except Exception as _exc:
                exc = AvroEncodeException('encode failed', value=value, schema=schema)
                exc.__cause__ = _exc
                if exc_handler_func:
                    return exc_handler_func(exc=exc, value=value, schema=schema)
                else:
                    logger.exception(
                        '[error]',
                        callee=self.__class__.encode,
                        value=repr(value)[:100],
                        schema_fullname=schema.fullname,
                        exc_info=exc,
                    )
                    raise exc

    def iter_encode(
        self,
        key_value_pair_iter: typing.Iterable[typing.Sequence[typing.Any]],
        key_schema: BaseAvroSchema,
        value_schema: BaseAvroSchema,
        with_key_schema: bool = False,
        with_value_schema: bool = False,
        exc_handler_func: typing.Optional[typing.Callable[[
            Exception, typing.Any, typing.Any, typing.Optional[BaseAvroSchema],
            typing.Optional[BaseAvroSchema], typing.Tuple[typing.Any, ...]
        ], None]] = None,
    ) -> typing.Iterator[typing.Union[typing.Tuple[
        typing.Any, typing.Any, typing.Optional[bytes], typing.Optional[bytes], typing.Tuple[typing.Any, ...],
    ], Exception]]:
        key_fastavro_parsed_schema = key_schema.x_fastavro_parsed_schema
        value_fastavro_parsed_schema = value_schema.x_fastavro_parsed_schema
        key_write_func = self.write_fastavro if with_key_schema is True else self.write_fastavro_schemaless
        value_write_func = self.write_fastavro if with_value_schema is True else self.write_fastavro_schemaless

        with BytesIO() as buf:
            tell_buf, seek_buf, read_buf, truncate_buf = \
                buf.tell, buf.seek, buf.read, buf.truncate
            for key, value, *others in key_value_pair_iter:
                offset = 0
                try:
                    if with_key_schema is False:
                        if key is not None:
                            key_write_func(
                                buf=buf,
                                fastavro_parsed_schema=key_fastavro_parsed_schema,
                                value=key,
                            )
                            offset = tell_buf()
                        if value is not None:
                            value_write_func(
                                buf=buf,
                                fastavro_parsed_schema=value_fastavro_parsed_schema,
                                value=value,
                            )
                        seek_buf(0)
                        yield (
                            key, value,
                            None if key is None else read_buf(offset),
                            None if value is None else read_buf(),
                            others,
                        )
                    else:
                        if key is not None:
                            key_write_func(
                                buf=buf,
                                fastavro_parsed_schema=key_fastavro_parsed_schema,
                                value=key,
                            )
                            encoded_key = buf.getvalue()
                            seek_buf(0)
                            truncate_buf()
                        else:
                            encoded_key = None
                        if value is not None:
                            value_write_func(
                                buf=buf,
                                fastavro_parsed_schema=value_fastavro_parsed_schema,
                                value=value,
                            )
                        seek_buf(0)
                        yield (
                            key, value,
                            encoded_key,
                            None if value is None else read_buf(),
                            others,
                        )
                except Exception as _exc:
                    exc = AvroRecordEncodeException(
                        'encode failed', key=key, value=value, key_schema=key_schema, value_schema=value_schema,
                    )
                    exc.__cause__ = _exc
                    if exc_handler_func:
                        yield exc_handler_func(
                            exc=exc, key=key, value=value,
                            key_schema=key_schema, value_schema=value_schema, others=others,
                        )
                    else:
                        logger.exception(
                            '[error]',
                            callee=self.__class__.iter_encode,
                            key=repr(key)[:100], value=repr(value)[:100],
                            key_schema_fullname=key_schema.fullname, value_schema_fullname=value_schema.fullname,
                            exc_info=exc,
                        )
                        raise exc
                seek_buf(0)
                truncate_buf()
        return

    def encode_with_schema_id(
        self,
        value: typing.Any,
        schema: BaseAvroSchema,
        schema_id: int,
        exc_handler_func: typing.Optional[typing.Callable[
            [Exception, typing.Any, typing.Optional[BaseAvroSchema]], None
        ]] = None,
    ) -> typing.Optional[bytes]:
        if value is None:
            return None
        with BytesIO() as buf:
            try:
                buf.write(schema_record_header_pack(MAGIC_NUM, schema_id))
                self.write_fastavro_schemaless(buf, schema.x_fastavro_parsed_schema, value)
                return buf.getvalue()
            except Exception as _exc:
                exc = AvroEncodeException('encode failed', value=value, schema=schema)
                exc.__cause__ = _exc
                if exc_handler_func:
                    return exc_handler_func(exc=exc, value=value, schema=schema)
                else:
                    logger.exception(
                        '[error]',
                        callee=self.__class__.encode_with_schema_id,
                        value=repr(value)[:100],
                        schema_fullname=schema.fullname,
                        exc_info=exc,
                    )
                    raise exc

    def iter_encode_with_schema_id(
        self,
        key_value_pair_iter: typing.Iterable[typing.Sequence[typing.Any]],
        key_schema: BaseAvroSchema,
        value_schema: BaseAvroSchema,
        key_schema_id: int,
        value_schema_id: int,
        exc_handler_func: typing.Optional[typing.Callable[[
            Exception, typing.Any, typing.Any, typing.Optional[BaseAvroSchema],
            typing.Optional[BaseAvroSchema], typing.Tuple[typing.Any, ...]
        ], None]] = None,
    ) -> typing.Iterator[typing.Union[typing.Tuple[
        typing.Any, typing.Any, typing.Optional[bytes], typing.Optional[bytes], typing.Tuple[typing.Any, ...]
    ], Exception]]:
        key_fastavro_parsed_schema = key_schema.x_fastavro_parsed_schema
        value_fastavro_parsed_schema = value_schema.x_fastavro_parsed_schema
        write_func = self.write_fastavro_schemaless
        with BytesIO() as buf:
            tell_buf, seek_buf, read_buf, truncate_buf, write_buf = \
                buf.tell, buf.seek, buf.read, buf.truncate, buf.write
            for key, value, *others in key_value_pair_iter:
                offset = 0
                try:
                    if key is not None:
                        write_buf(schema_record_header_pack(MAGIC_NUM, key_schema_id))
                        write_func(buf, key_fastavro_parsed_schema, key)
                        offset = tell_buf()
                    if value is not None:
                        write_buf(schema_record_header_pack(MAGIC_NUM, value_schema_id))
                        write_func(buf, value_fastavro_parsed_schema, value)
                    seek_buf(0)
                    yield (
                        key, value,
                        None if key is None else read_buf(offset),
                        None if value is None else read_buf(),
                        others,
                    )
                except Exception as _exc:
                    exc = AvroRecordEncodeException(
                        'encode failed', key=key, value=value, key_schema=key_schema, value_schema=value_schema,
                    )
                    exc.__cause__ = _exc
                    if exc_handler_func:
                        yield exc_handler_func(
                            exc=exc, key=key, value=value,
                            key_schema=key_schema, value_schema=value_schema, others=others,
                        )
                    else:
                        logger.exception(
                            '[error]',
                            callee=self.__class__.iter_encode_with_schema_id,
                            key=repr(key)[:100], value=repr(value)[:100],
                            key_schema_fullname=key_schema.fullname, value_schema_fullname=value_schema.fullname,
                            exc_info=exc,
                        )
                        raise exc
                seek_buf(0)
                truncate_buf()
        return

    def encode_with_schema_registry(
        self,
        value: typing.Any,
        schema: BaseAvroSchema,
        topic: str,
        subject_name: typing.Optional[str] = None,
        auto_register_schema: bool = False,
        subject_name_resolver_func: typing.Optional[typing.Callable[[str, BaseAvroSchema], str]] = None,
        exc_handler_func: typing.Optional[typing.Callable[
            [Exception, typing.Any, typing.Optional[BaseAvroSchema]], None
        ]] = None,
    ) -> typing.Optional[bytes]:
        try:
            schema, schema_id, _ = self.get_schema_id(
                schema=schema,
                subject_name=subject_name or subject_name_resolver_func(topic=topic, schema=schema),
                auto_register_schema=auto_register_schema,
            )
            return self.encode_with_schema_id(
                value=value,
                schema=schema,
                schema_id=schema_id,
                exc_handler_func=exc_handler_func,
            )
        except Exception as _exc:
            exc = AvroEncodeException('encode failed', value=value, schema=schema)
            exc.__cause__ = _exc
            if exc_handler_func:
                return exc_handler_func(exc=exc, value=value, schema=schema)
            else:
                logger.exception(
                    '[error]',
                    callee=self.__class__.encode_with_schema_registry,
                    value=repr(value)[:100],
                    schema_fullname=schema.fullname,
                    exc_info=exc,
                )
                raise exc

    def iter_encode_with_schema_registry(
        self,
        topic: str,
        key_value_pair_iter: typing.Iterable[typing.Sequence[typing.Any]],
        key_schema: BaseAvroSchema,
        value_schema: BaseAvroSchema,
        key_subject_name: typing.Optional[str] = None,
        value_subject_name: typing.Optional[str] = None,
        key_subject_name_resolver_func: typing.Optional[typing.Callable[[str, BaseAvroSchema], str]] = None,
        value_subject_name_resolver_func: typing.Optional[typing.Callable[[str, BaseAvroSchema], str]] = None,
        auto_register_schema: bool = False,
        exc_handler_func: typing.Optional[typing.Callable[[
            Exception, typing.Any, typing.Any, typing.Optional[BaseAvroSchema],
            typing.Optional[BaseAvroSchema], typing.Tuple[typing.Any, ...]
        ], None]] = None,
    ) -> typing.Iterator[typing.Union[typing.Tuple[
        typing.Any, typing.Any, typing.Optional[bytes], typing.Optional[bytes], typing.Tuple[typing.Any, ...]
    ], Exception]]:
        key_subject_name = key_subject_name or key_subject_name_resolver_func(topic=topic, schema=key_schema)
        value_subject_name = value_subject_name or value_subject_name_resolver_func(topic=topic, schema=value_schema)
        schema_entry_expire_sec = self.schema_entry_expire_sec
        get_schema_id = self.get_schema_id
        write_func = self.write_fastavro_schemaless
        key_schame_cached_time = 0
        value_schame_cached_time = 0
        with BytesIO() as buf:
            tell_buf, seek_buf, read_buf, truncate_buf, write_buf = \
                buf.tell, buf.seek, buf.read, buf.truncate, buf.write
            for key, value, *others in key_value_pair_iter:
                offset = 0
                try:
                    if key is not None:
                        if (time.time() - key_schame_cached_time) >= schema_entry_expire_sec:
                            key_schema, key_schema_id, key_schame_cached_time = get_schema_id(
                                schema=key_schema,
                                subject_name=key_subject_name,
                                auto_register_schema=auto_register_schema,
                            )
                        write_buf(schema_record_header_pack(MAGIC_NUM, key_schema_id))
                        write_func(buf, key_schema.x_fastavro_parsed_schema, key)
                        offset = tell_buf()
                    if value is not None:
                        if (time.time() - value_schame_cached_time) >= schema_entry_expire_sec:
                            value_schema, value_schema_id, value_schame_cached_time = get_schema_id(
                                schema=value_schema,
                                subject_name=value_subject_name,
                                auto_register_schema=auto_register_schema,
                            )
                        write_buf(schema_record_header_pack(MAGIC_NUM, value_schema_id))
                        write_func(buf, value_schema.x_fastavro_parsed_schema, value)
                    seek_buf(0)
                    yield (
                        key, value,
                        None if key is None else read_buf(offset),
                        None if value is None else read_buf(),
                        others,
                    )
                except Exception as _exc:
                    exc = AvroRecordEncodeException(
                        'encode failed', key=key, value=value, key_schema=key_schema, value_schema=value_schema,
                    )
                    exc.__cause__ = _exc
                    if exc_handler_func:
                        yield exc_handler_func(
                            exc=exc, key=key, value=value,
                            key_schema=key_schema, value_schema=value_schema, others=others,
                        )
                    else:
                        logger.exception(
                            '[error]',
                            callee=self.__class__.iter_encode_with_schema_registry,
                            key=repr(key)[:100], value=repr(value)[:100],
                            key_schema_fullname=key_schema.fullname, value_schema_fullname=value_schema.fullname,
                            exc_info=exc,
                        )
                        raise exc
                seek_buf(0)
                truncate_buf()

    def decode(
        self,
        value: typing.Optional[bytes],
        schema: typing.Optional[BaseAvroSchema] = None,
        exc_handler_func: typing.Optional[typing.Callable[
            [Exception, typing.Optional[bytes], typing.Optional[BaseAvroSchema]], None
        ]] = None,
    ) -> typing.Any:
        if value is None:
            return None
        with BytesIO(value) as buf:
            try:
                if schema is None:
                    return self.read_fastavro(buf=buf)
                else:
                    return self.read_fastavro_schemaless(
                        buf=buf, fastavro_parsed_schema=schema.x_fastavro_parsed_schema,
                    )
            except Exception as _exc:
                exc = AvroDecodeException('decode failed', value=value, schema=schema)
                exc.__cause__ = _exc
                if exc_handler_func:
                    return exc_handler_func(exc=exc, value=value, schema=schema)
                else:
                    logger.exception(
                        '[error]',
                        callee=self.__class__.decode,
                        value=repr(value)[:100],
                        schema_fullname=schema.fullname if schema else None,
                        exc_info=exc,
                    )
                    raise exc

    def iter_decode(
        self,
        key_value_pair_iter: typing.Iterable,
        is_chunked: bool = False,
        key_schema: typing.Optional[BaseAvroSchema] = None,
        value_schema: typing.Optional[BaseAvroSchema] = None,
        exc_handler_func: typing.Optional[typing.Callable[[
            Exception, typing.Optional[bytes], typing.Optional[bytes],
            typing.Optional[BaseAvroSchema], typing.Optional[BaseAvroSchema], typing.Tuple[typing.Any, ...],
        ], None]] = None,
    ) -> typing.Iterator[typing.Union[typing.Iterable, Exception]]:
        key_read_func = self.read_fastavro if key_schema is None else functools.partial(
            self.read_fastavro_schemaless,
            fastavro_parsed_schema=key_schema.x_fastavro_parsed_schema,
        )
        value_read_func = self.read_fastavro if value_schema is None else functools.partial(
            self.read_fastavro_schemaless,
            fastavro_parsed_schema=value_schema.x_fastavro_parsed_schema,
        )

        with BytesIO() as buf:
            write_buf, seek_buf, truncate_buf = buf.write, buf.seek, buf.truncate

            for _v in key_value_pair_iter:
                if is_chunked:
                    chunked_response_container = deque()

                for key, value, *others in _v if is_chunked else (_v,):
                    try:
                        if key is not None:
                            write_buf(key)
                        if value is not None:
                            write_buf(value)
                        seek_buf(0)
                        response = (
                            key, value,
                            None if key is None else key_read_func(buf),
                            None if value is None else value_read_func(buf),
                            others,
                        )

                        if is_chunked:
                            chunked_response_container.append(response)
                        else:
                            yield response
                    except Exception as _exc:
                        exc = AvroRecordDecodeException(
                            'decode failed', key=key, value=value, key_schema=key_schema, value_schema=value_schema,
                        )
                        exc.__cause__ = _exc
                        if exc_handler_func:
                            _handled_obj = exc_handler_func(
                                exc=exc, key=key, value=value,
                                key_schema=key_schema, value_schema=value_schema, others=others,
                            )
                            if is_chunked:
                                chunked_response_container.append(_handled_obj)
                            else:
                                yield _handled_obj
                        else:
                            logger.exception(
                                '[error]',
                                callee=self.__class__.iter_decode,
                                key=repr(key)[:100], value=repr(value)[:100],
                                key_schema_fullname=key_schema.fullname if key_schema else None,
                                value_schema_fullname=value_schema.fullname if value_schema else None,
                                exc_info=exc,
                            )
                            raise exc
                    seek_buf(0)
                    truncate_buf()
                if is_chunked:
                    yield chunked_response_container
                    del chunked_response_container
        return

    def decode_with_schema_registry(
        self,
        value: typing.Optional[bytes],
        exc_handler_func: typing.Optional[typing.Callable[
            [Exception, typing.Optional[bytes], typing.Optional[BaseAvroSchema]], None
        ]] = None,
    ) -> typing.Union[
        typing.Tuple[typing.Any, typing.Optional[BaseAvroSchema], typing.Optional[int]],
        Exception,
    ]:
        if value is None:
            return (None, None, None)
        schema = None
        with BytesIO(value) as buf:
            try:
                magic_num, schema_id = schema_record_header_unpack_from(buf.getbuffer())
                buf.seek(5, SEEK_CUR)
                if magic_num != MAGIC_NUM:
                    raise ValueError()
                schema = self.get_schema(schema_id=schema_id)[0]
                return (
                    self.read_fastavro_schemaless(
                        buf, fastavro_parsed_schema=schema.x_fastavro_parsed_schema,
                    ),
                    schema,
                    schema_id,
                )
            except Exception as _exc:
                exc = AvroDecodeException('decode failed', value=value, schema=schema)
                exc.__cause__ = _exc
                if exc_handler_func:
                    return exc_handler_func(exc=exc, value=value, schema=schema)
                else:
                    logger.exception(
                        '[error]',
                        callee=self.__class__.decode_with_schema_registry,
                        value=repr(value)[:100],
                        schema_fullname=schema.fullname if schema else None,
                        exc_info=exc,
                    )
                    raise exc

    def iter_decode_with_schema_registry(
        self,
        key_value_pair_iter: typing.Iterable,
        is_chunked: bool = False,
        exc_handler_func: typing.Optional[typing.Callable[[
            Exception, typing.Optional[bytes], typing.Optional[bytes],
            typing.Optional[BaseAvroSchema], typing.Optional[BaseAvroSchema], typing.Tuple[typing.Any, ...]
        ], None]] = None,
    ) -> typing.Iterator[typing.Union[typing.Iterable, Exception]]:
        get_schema = self.get_schema
        read_func = self.read_fastavro_schemaless

        with BytesIO() as buf:
            write_buf, read_buf, seek_buf, truncate_buf = buf.write, buf.read, buf.seek, buf.truncate

            for _v in key_value_pair_iter:
                if is_chunked:
                    chunked_response_container = deque()

                for key, value, *others in _v if is_chunked else (_v,):
                    key_schema, value_schema, key_schema_id, value_schema_id = None, None, None, None
                    try:
                        if key is not None:
                            m = memoryview(key)
                            magic_num, key_schema_id = schema_record_header_unpack_from(m[:5])
                            if magic_num != MAGIC_NUM:
                                raise ValueError(f'invalid magic number [{magic_num}]')
                            key_schema = get_schema(schema_id=key_schema_id)[0]
                            write_buf(m[5:])
                        if value is not None:
                            m = memoryview(value)
                            magic_num, value_schema_id = schema_record_header_unpack_from(m[:5])
                            if magic_num != MAGIC_NUM:
                                raise ValueError(f'invalid magic number [{magic_num}]')
                            value_schema = get_schema(schema_id=value_schema_id)[0]
                            write_buf(m[5:])
                        seek_buf(0)
                        response = (
                            key, value,
                            None if key is None else read_func(
                                buf=buf, fastavro_parsed_schema=key_schema.x_fastavro_parsed_schema,
                            ),
                            None if value is None else read_func(
                                buf=buf, fastavro_parsed_schema=value_schema.x_fastavro_parsed_schema,
                            ),
                            key_schema, value_schema,
                            key_schema_id, value_schema_id,
                            others,
                        )

                        if is_chunked:
                            chunked_response_container.append(response)
                        else:
                            yield response
                    except Exception as _exc:
                        exc = AvroRecordDecodeException(
                            'decode failed', key=key, value=value, key_schema=key_schema, value_schema=value_schema,
                        )
                        exc.__cause__ = _exc
                        if exc_handler_func:
                            _handled_obj = exc_handler_func(
                                exc=exc, key=key, value=value,
                                key_schema=key_schema, value_schema=value_schema, others=others,
                            )
                            if is_chunked:
                                chunked_response_container.append(_handled_obj)
                            else:
                                yield _handled_obj
                        else:
                            logger.exception(
                                '[error]',
                                callee=self.__class__.iter_decode,
                                key=repr(key)[:100], value=repr(value)[:100],
                                key_schema_fullname=key_schema.fullname if key_schema else None,
                                value_schema_fullname=value_schema.fullname if value_schema else None,
                                exc_info=exc,
                            )
                            raise exc
                    seek_buf(0)
                    truncate_buf()
                if is_chunked:
                    yield chunked_response_container
                    del chunked_response_container
        return
