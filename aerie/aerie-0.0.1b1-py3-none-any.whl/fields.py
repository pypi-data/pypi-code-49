import datetime
from typing import (
    Any,
    Generic,
    List,
    Mapping,
    Optional,
    Sequence,
    TYPE_CHECKING,
    Tuple,
    Type,
    TypeVar,
    Union,
    overload,
)

import sqlalchemy as sa

from aerie.mappers import entity_to_db_dict

if TYPE_CHECKING:
    from aerie import Schema

DT = TypeVar("DT")  # database type
PT = TypeVar("PT")  # python type


class ProvidesClauseElement:
    column: sa.Column

    @property
    def __clause_element__(self):
        return lambda: self.column


class OrderByExpr(ProvidesClauseElement):
    def __init__(self, column: sa.Column):
        self.column = column

    def nulls_first(self):
        return self.column.nullsfirst()

    def nulls_last(self):
        return self.column.nullslast()

    def __str__(self):
        return str(self.column)


class Lookups:
    column: sa.Column

    def concat(self, other):
        return self.column.concat(other)

    def like(self, other, escape=None):
        return self.column.like(other, escape)

    def not_like(self, other, escape=None):
        return self.column.notlike(other, escape)

    def ilike(self, other, escape=None):
        return self.column.ilike(other, escape)

    def not_ilike(self, other, escape=None):
        return self.column.notilike(other, escape)

    def in_(self, other):
        if hasattr(other, "get_query"):
            other = other.get_query()
        return self.column.in_(other)

    def not_in(self, other):
        if hasattr(other, "get_query"):
            other = other.get_query()
        return self.column.notin_(other)

    def is_(self, other):
        return self.column.is_(other)

    def is_not(self, other):
        return self.column.isnot(other)

    def startswith(self, other, **kwargs):
        return self.column.startswith(other, **kwargs)

    def not_startswith(self, other, **kwargs):
        return sa.sql.not_(self.startswith(other, **kwargs))

    def endswith(self, other, **kwargs):
        return self.column.endswith(other, **kwargs)

    def not_endswith(self, other, **kwargs):
        return sa.sql.not_(self.endswith(other, **kwargs))

    def contains(self, other, **kwargs):
        return self.column.contains(other, **kwargs)

    def not_contains(self, other, **kwargs):
        return sa.sql.not_(self.contains(other, **kwargs))

    def match(self, other, **kwargs):
        return self.column.match(other, **kwargs)

    def not_match(self, other, **kwargs):
        return sa.sql.not_(self.column.match(other, **kwargs))

    def between(self, cleft, cright, symmetric=False):
        return self.column.between(cleft, cright, symmetric=symmetric)

    def not_between(self, cleft, cright, symmetric=False):
        return sa.sql.not_(self.column.between(cleft, cright, symmetric=symmetric))

    def desc(self) -> OrderByExpr:
        return OrderByExpr(self.column.desc())

    def asc(self) -> OrderByExpr:
        return OrderByExpr(self.column.asc())

    def collate(self, collation):
        return self.column.collate(collation)

    def distinct(self):
        return self.column.distinct()

    def alias(self, name):
        return self.column.label(name)

    def __eq__(self, other):
        return self.column.__eq__(other)

    def __ne__(self, other):
        return self.column.__ne__(other)

    def __gt__(self, other):
        return self.column.__gt__(other)

    def __ge__(self, other):
        return self.column.__ge__(other)

    def __lt__(self, other):
        return self.column.__lt__(other)

    def __le__(self, other):
        return self.column.__le__(other)

    def __neg__(self):
        return self.column.__neg__()

    def __add__(self, other):
        return self.column.__add__(other)

    def __radd__(self, other):
        return self.column.__radd__(other)

    def __sub__(self, other):
        return self.column.__sub__(other)

    def __rsub__(self, other):
        return self.column.__rsub__(other)

    def __mul__(self, other):
        return self.column.__mul__(other)

    def __rmul__(self, other):
        return self.column.__rmul__(other)

    def __truediv__(self, other):
        return self.column.__truediv__(other)

    def __rtruediv__(self, other):
        return self.column.__rtruediv__(other)

    def __mod__(self, other):
        return self.column.__mod__(other)

    def __rmod__(self, other):
        return self.column.__rmod__(other)


class Field(Generic[DT, PT], Lookups, ProvidesClauseElement):
    _column: sa.Column
    type = None

    def __init__(
        self,
        *,
        name: str = None,
        default: PT = None,
        null: bool = False,
        index: bool = False,
        unique: bool = False,
        column: str = None,
    ):
        self.name = name
        self.index = index
        self.unique = unique
        self.null = null
        self.default = default
        self.column_name = column

    @property
    def column(self) -> sa.Column:
        if self._column is None:
            raise AttributeError("Field is not bound to schema.")
        return self._column

    def to_db_value(self, value: PT) -> DT:
        """Convert python object to database value."""
        if value is None or type(value) == self.type:
            return value
        return self.type(value)

    def to_python_value(self, value: DT) -> PT:
        """Convert database value to python object."""
        if value is None or isinstance(value, self.type):
            return value
        return self.type(value)

    def get_column_type(self) -> sa.types.TypeEngine:
        """Return SQLAlchemy column type."""
        raise NotImplementedError()

    def get_constraints(self, name: str) -> Sequence:
        """Return constraints for SQLAlchemy column."""
        return []

    def get_columns_kwargs(self) -> Mapping[str, Any]:
        """Return extra kwargs for SQLAlchemy column."""
        return {}

    def get_column(self, name: str, is_primary_key: bool = False) -> sa.Column:
        column_type = self.get_column_type()
        constraints = self.get_constraints(name)
        extra_kwargs = self.get_columns_kwargs()
        name = self.column_name or name or self.name

        self._column = sa.Column(
            name,
            column_type,
            *constraints,
            **extra_kwargs,
            default=self.default,
            primary_key=is_primary_key,
            nullable=self.null and not is_primary_key,
            index=self.index,
            unique=self.unique,
        )
        return self._column

    @property
    def _select_iterable(self) -> Tuple[sa.sql.ColumnElement]:
        return self.column._select_iterable

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self}>"

    def __str__(self):
        return self.name

    @overload
    def __get__(self, instance: None, owner: Type["Schema"]) -> Lookups:
        ...

    @overload
    def __get__(self, instance: "Schema", owner: Type["Schema"]) -> PT:
        ...

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class IntegerField(Field[int, int]):
    type = int

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_column_type(self) -> sa.types.TypeEngine:
        return sa.Integer()


class FloatField(Field[float, float]):
    type = float

    def get_column_type(self) -> sa.types.TypeEngine:
        return sa.Float()


class StringField(Field[str, str]):
    type = str

    def get_column_type(self) -> sa.types.TypeEngine:
        return sa.String()


class TextField(Field[str, str]):
    type = str

    def get_column_type(self) -> sa.types.TypeEngine:
        return sa.Text()


class BooleanField(Field[bool, bool]):
    type = bool

    def get_column_type(self) -> sa.types.TypeEngine:
        return sa.Boolean()

    def to_python_value(self, value: DT) -> PT:
        if isinstance(value, bool):
            return value
        return str(value).strip().lower() in ["yes", "1", "on", "true"]


class DateField(Field[str, datetime.date]):
    type = datetime.date

    def to_db_value(self, value: datetime.date) -> Optional[str]:
        if value is None:
            return value
        return value.isoformat()

    def to_python_value(self, value: Union[str, datetime.date]) -> datetime.date:
        if value is None or isinstance(value, self.type):
            return value

        return datetime.date.fromisoformat(value)

    def get_column_type(self):
        return sa.Date()


class DateTimeField(Field[str, datetime.datetime]):
    type = datetime.datetime

    def to_db_value(self, value: datetime.datetime) -> Optional[str]:
        if value is None:
            return value
        return value.isoformat()

    def to_python_value(
        self, value: Union[str, datetime.datetime]
    ) -> datetime.datetime:
        if value is None or isinstance(value, self.type):
            return value
        return datetime.datetime.fromisoformat(value)

    def get_column_type(self):
        return sa.DateTime()


class TimeField(Field[str, datetime.time]):
    type = datetime.time

    def to_db_value(self, value: datetime.time) -> Optional[str]:
        if value is None:
            return value
        return value.isoformat()

    def to_python_value(self, value: Union[str, datetime.time]) -> datetime.time:
        if value is None or isinstance(value, self.type):
            return value

        return datetime.time.fromisoformat(value)

    def get_column_type(self):
        return sa.Time()


class JsonField(Field[Any, Any]):
    type = dict

    def get_column_type(self) -> sa.types.TypeEngine:
        return sa.JSON()


class EmbedsOne(Field[dict, "Schema"]):
    type = dict

    def __init__(self, schema: Type["Schema"], *args, **kwargs):
        self.schema = schema
        super().__init__(*args, **kwargs)

    def to_db_value(self, value: PT) -> DT:
        if value is None:
            return value
        return entity_to_db_dict(value)

    def to_python_value(self, value: DT) -> PT:
        if value is None:
            return value
        return self.schema(**value)

    def get_column_type(self) -> sa.types.TypeEngine:
        return sa.JSON()


class EmbedsMany(Field[List[dict], List[dict]]):
    type = list

    def __init__(self, schema: Type["Schema"], *args, **kwargs):
        self.schema = schema
        super().__init__(*args, **kwargs)

    def to_db_value(self, value: PT) -> DT:
        if value is None:
            return value
        return [entity_to_db_dict(item) for item in value]

    def to_python_value(self, value: DT) -> PT:
        if value is None:
            return value
        return [self.schema(**item) for item in value]

    def get_column_type(self) -> sa.types.TypeEngine:
        return sa.JSON()


class PrimaryKey:
    def __init__(self, *fields: Field):
        self.fields = fields

    @property
    def is_composite(self) -> bool:
        return len(self.fields) > 1

    def asc(self):
        return [f.asc().nulls_last() for f in self.fields]

    def desc(self):
        return [f.desc().nulls_last() for f in self.fields]

    def __contains__(self, item: str) -> bool:
        for field in self.fields:
            if field.name == item:
                return True
        return False

    def __eq__(self, other):
        if isinstance(other, (str, int, float)):
            other = [other]
        return sa.and_(*[f == other[i] for i, f in enumerate(self.fields)])

    def __neq__(self, other):
        if isinstance(other, (str,)):
            other = [other]
        return sa.and_(*[f != other[i] for i, f in enumerate(self.fields)])

    def __getitem__(self, item):
        if item > len(self.fields) - 1:
            raise IndexError()
        return self.fields[item]

    # def __set__(self, instance, value):
    #     return super().__set__(instance, value)
    #
    # def __get__(self, instance, owner):
    #     return super().__get__(instance, owner)
    #


class HasOne(Field[DT, PT]):
    def __init__(self, schema: Type["Schema"], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schema = schema

    @property
    def _table(self) -> sa.Table:
        return self.schema.__meta__.table

    def get_column_type(self) -> sa.types.TypeEngine:
        return self.schema.pk.fields[0].get_column_type()

    def get_constraints(self, name: str) -> Sequence:
        table_name = self.schema.__meta__.table.name
        field_name = self.schema.pk.fields[0].name
        fk_name = table_name + "." + field_name
        return [sa.schema.ForeignKey(fk_name)]

    def to_python_value(self, value: DT) -> PT:
        return value
