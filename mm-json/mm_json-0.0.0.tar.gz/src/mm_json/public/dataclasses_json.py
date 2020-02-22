import dataclasses
import functools
import typing

import marshmallow

from . import typing_json


class Converter(typing_json.Converter):
    def _handle_default(self, type_, type_info, metadata):
        if not issubclass(type_, DataclassesMixin):
            return super()._handle_default(type_, type_info, metadata)
        return marshmallow.fields.Nested(type_.schema(converter=self))


class DataclassesMixin:
    _default_converter = Converter()

    @classmethod
    @functools.lru_cache()
    def schema(cls, converter=None):
        if converter is None:
            converter = cls._default_converter

        schema = {}
        annotations = typing.get_type_hints(cls)
        for field in dataclasses.fields(cls):
            metadata = {"metadata": field.metadata.copy()}
            if field.default_factory is not dataclasses.MISSING:
                metadata["missing"] = field.default_factory
                metadata["metadata"]["default_factory"] = field.default_factory
            elif field.default is not dataclasses.MISSING:
                metadata["missing"] = field.default
            if field.default is not dataclasses.MISSING:
                metadata["metadata"]["default"] = field.default

            schema[field.name] = converter.convert(
                annotations[field.name], metadata=metadata
            )

        SchemaClass = marshmallow.Schema.from_dict(schema, name=cls.__name__)

        class Schema(SchemaClass):
            @marshmallow.post_load
            def __make_object(self, data, **kwargs):
                return cls(**data)

        return Schema()


def dataclass_json(obj=None, *, converter=None):
    def inner(obj):
        mapping = {}
        if converter is not None:
            mapping["_default_converter"] = converter
        return type(obj.__name__, (obj, DataclassesMixin), mapping)

    if obj is None:
        return inner
    return inner(obj)
