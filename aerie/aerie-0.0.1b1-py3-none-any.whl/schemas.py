from __future__ import annotations

import re
from functools import wraps
from typing import Any, Dict, Generic, List, Type, TypeVar, cast

import sqlalchemy as sa

from aerie.connections import Connection
from aerie.exceptions import DoesNotExist, ImproperlyConfigured, MultipleResults
from aerie.fields import Field, PrimaryKey

E = TypeVar("E")

default_metadata = sa.MetaData()

schema_registry = {}
table_registry = {}


def make_table_name(name: str) -> str:
    name = name.strip("_")
    if name.endswith("x"):
        name += "es"

    if not name.endswith("s"):
        name += "s"

    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


class Metadata:
    def __init__(
        self,
        *,
        schema: Type[Schema],
        fields: Dict[str, Field],
        metadata: sa.MetaData,
        primary_key: PrimaryKey,
        table: sa.Table,
        abstract: bool = False,
        connection: Connection = None,
        entity_class: Type = None,
    ):
        self.schema = schema
        self.metadata = metadata
        self.fields = fields
        self.table = table
        self.primary_key = primary_key
        self.connection = connection
        self.entity_class = entity_class
        self.abstract = abstract

    @property
    def table_name(self) -> str:
        return self.table.name


class SchemaBase(type):
    def __new__(mcs, name: str, bases, attrs: dict):
        meta_options = {}
        meta = attrs.pop("Meta", None)
        if getattr(meta, "abstract", False) is True:
            return super().__new__(mcs, name, bases, attrs)

        if meta:
            for key, value in meta.__dict__.items():
                if not key.startswith("_"):
                    meta_options[key] = value

        pk = getattr(meta, "primary_key", None)
        if pk is None:
            pk = "id"  # default pk name is ID
            if pk not in attrs or not isinstance(attrs[pk], Field):
                raise ImproperlyConfigured(
                    f"Could not infer primary key for schema {name}. "
                    f"Define a {name}.Meta.primary_key attribute "
                    'or add a field with name "id".'
                )

        if isinstance(pk, str):
            pk = [pk]

        fields: Dict[str, Field] = {}
        columns: List[sa.Column] = []
        for key, value in attrs.items():
            if isinstance(value, Field):
                value.name = key
                value.column_name = value.column_name or key
                fields[key] = value
                columns.append(value.get_column(key, is_primary_key=key in pk))

        primary_key = PrimaryKey(
            *[field for field_name, field in fields.items() if field_name in pk]
        )

        # remove duplicate or unnecessary fields from meta options
        meta_options.pop("primary_key", None)  # replaced by PrimaryKey
        meta_options.pop("table_name", None)  # replaced by sa.Table:name

        table_name = getattr(meta, "table_name", make_table_name(name))
        metadata = getattr(meta, "metadata", default_metadata)
        connection = getattr(meta, "connection", None)

        new_class = super().__new__(mcs, name, bases, attrs)
        new_class.__meta__ = Metadata(
            schema=cast(Type[Schema], new_class),
            fields=fields,
            metadata=metadata,
            primary_key=primary_key,
            table=sa.Table(table_name, metadata, *columns),
            connection=connection,
            **meta_options,
        )
        new_class.pk = primary_key
        new_class.DoesNotExist = type(f"{name}.DoesNotExist", (DoesNotExist,), {})
        new_class.MultipleResults = type(
            f"{name}.MultipleResults", (MultipleResults,), {}
        )
        return new_class


class Schema(Generic[E], metaclass=SchemaBase):
    __meta__: Metadata
    pk: PrimaryKey
    DoesNotExist: Type[DoesNotExist]
    MultipleResults: Type[MultipleResults]

    class Meta:
        abstract = True

    def __init__(self, **kwargs):
        super().__init__()
        for name, value in kwargs.items():
            if name in self.__meta__.fields:
                value = self.__meta__.fields[name].to_python_value(value)
            setattr(self, name, value)
