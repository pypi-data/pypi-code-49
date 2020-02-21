__all__ = (
    'BaseAvroSchema',
    'avro_loads',
    'avro_load',
    'iter_load_avro_schema',
)

from types import MappingProxyType
import abc
import codecs
import inspect
import io
import pathlib
import typing

from avro import schema as _avro_schema
from fastavro.schema import parse_schema as fastavro_parse_schema
from simplejson import (
    dumps as _simplejson_dumps,
    load as _simplejson_load,
    loads as _simplejson_loads,
    JSONEncoder,
)

from chatora.util.functional import reify


class MappingProxyJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, MappingProxyType):
            return obj.copy()
        return super().default(obj)


@reify
def x_py_obj(self) -> typing.Any:
    return self.to_json()


@reify
def x_json_str(self) -> str:
    return _simplejson_dumps(self.x_py_obj, ensure_ascii=False, separators=(',',':'), cls=MappingProxyJSONEncoder)


@reify
def x_fastavro_parsed_schema(self) -> typing.Any:
    return fastavro_parse_schema(_simplejson_loads(self.x_json_str))


def x__hash__(self) -> str:
    return hash(self.x_json_str)


class BaseAvroSchema(abc.ABC):
    __hash__ = x__hash__
    x_py_obj = x_py_obj
    x_json_str = x_json_str
    x_fastavro_parsed_schema = x_fastavro_parsed_schema


for n, v in _avro_schema.__dict__.items():
    if inspect.isclass(v) is True and issubclass(v, _avro_schema.Schema) is True:
        BaseAvroSchema.register(v)
        if '__hash__' not in v.__dict__ or v.__hash__ is None:
            v.__hash__ = x__hash__
        v.x_py_obj = x_py_obj
        v.x_json_str = x_json_str
        v.x_fastavro_parsed_schema = x_fastavro_parsed_schema
        if n.startswith('_') is False:
            if n not in globals():
                globals()[n] = v
            # __all__.append(n)


def avro_loads(schema_str: str) -> BaseAvroSchema:
    return _avro_schema.Parse(schema_str)


def avro_load(fp: typing.Union[typing.TextIO, pathlib.Path, str]) -> BaseAvroSchema:
    if isinstance(fp, io.TextIOBase) is True:
        return avro_loads(schema_str=fp.read())
    elif isinstance(fp, pathlib.Path) is True:
        return avro_loads(schema_str=fp.read_text(encoding='utf-8'))
    elif isinstance(fp, str) is True:
        with codecs.open(fp, mode='rt', encoding='utf-8') as f:
            return avro_loads(schema_str=f.read())
    else:
        raise ValueError(f'unknown src type [{fp!r}')


def iter_load_avro_schema(
    schema_data_iter: typing.Iterable[typing.Union[typing.Any]],
) -> typing.Iterator[BaseAvroSchema]:
    known_schema_names = _avro_schema.Names()

    for schema_data in schema_data_iter:
        if isinstance(schema_data, io.TextIOBase) is True:
            py_obj = _simplejson_load(schema_data)
        elif isinstance(schema_data, pathlib.Path) is True:
            with schema_data.open(mode='rt', encoding='utf-8') as f:
                py_obj = _simplejson_load(f)
        elif isinstance(schema_data, str) is True:
            py_obj = _simplejson_loads(schema_data)
        else:
            py_obj = schema_data
        yield _avro_schema.SchemaFromJSONData(py_obj, names=known_schema_names)


# __all__ = tuple(__all__)
