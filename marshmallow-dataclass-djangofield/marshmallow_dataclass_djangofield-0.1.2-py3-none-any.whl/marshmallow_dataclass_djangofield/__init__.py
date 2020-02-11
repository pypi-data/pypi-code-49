"""Django Fields from marshmallow-dataclass."""
__version__ = "0.1.1-1"

from django.contrib.postgres.fields import JSONField
from django.db import migrations
from marshmallow import Schema

__all__ = (
    "MarshmallowField",
    "marshmallow_dataclass_djangofield",
)


class MarshmallowField(JSONField):
    def __init__(self, *args, many: bool = False, schema: Schema, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.schema = schema
        self.many = many

    def deconstruct(self, *args, **kwargs):
        name, path, args, kwargs = super().deconstruct()
        kwargs["many"] = self.many
        kwargs["schema"] = self.schema
        return name, path, args, kwargs

    def get_prep_value(self, value):
        return super().get_prep_value(list(map(self.schema.dump, value)))

    def from_db_value(self, value, *_, **__):
        return self.to_python(value)

    def to_python(self, *args, **kwargs):
        python = super().to_python(*args, **kwargs)
        if self.many:
            return map(self.schema.load, python)
        return self.schema.load(python)


def marshmallow_dataclass_djangofield(*, model_name: str):
    def wrapper(cls):
        class Serializer(migrations.serializer.BaseSerializer):
            def serialize(self):
                return (
                    f"{cls.__module__}.{model_name}.{cls.__name__}.Schema()",
                    {f"import {cls.__module__}"},
                )

        setattr(
            cls.Schema,
            "__eq__",
            lambda s, o: s.Schema().dumps(s) == o.Schema().dumps(o),
        )
        migrations.writer.MigrationWriter.register_serializer(cls.Schema, Serializer)
        return cls

    return wrapper
