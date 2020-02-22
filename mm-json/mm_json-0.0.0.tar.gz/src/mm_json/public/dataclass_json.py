import dataclasses
import typing

import marshmallow

from .typing_json import Converter


def dataclass_json(obj=None, *, converter=Converter()):
    def inner(obj):
        schema = {}
        annotations = typing.get_type_hints(obj)
        for field in dataclasses.fields(obj):
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

        SchemaClass = marshmallow.Schema.from_dict(schema, name=obj.__name__)

        class Schema(SchemaClass):
            @marshmallow.post_load
            def __make_object(self, data, **kwargs):
                return obj(**data)

        obj.schema = Schema()
        return obj

    if obj is not None:
        return inner(obj)
    return inner
