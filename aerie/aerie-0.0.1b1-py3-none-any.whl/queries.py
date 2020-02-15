from __future__ import annotations

import sys
from functools import reduce
from typing import (
    Any,
    AsyncGenerator,
    Callable,
    Dict,
    Generic,
    IO,
    Iterable,
    List,
    Mapping,
    Optional,
    TYPE_CHECKING,
    Type,
    TypeVar,
    Union,
)

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import dialect as PgDialect

from aerie import functions as func
from aerie.collections import Collection
from aerie.connections import Connection
from aerie.exceptions import DoesNotExist
from aerie.fields import Field
from aerie.functions import BaseFunction
from aerie.mappers import entity_constructor, entity_to_db_dict

if TYPE_CHECKING:
    from aerie.schemas import Schema

SQLLike = Union[str, sa.sql.ClauseElement]
And = sa.sql.and_
Or = lambda *args: sa.sql.and_(sa.sql.or_(*args))
Not = sa.sql.not_

RE = TypeVar("RE")  # entity for RawQuery. does not need to be a Schema
E = TypeVar("E")
S = TypeVar("S", bound="Schema")
Factory = Callable[[Mapping, Type[E]], E]


class Row:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __data__(self):
        return {
            k: v if not isinstance(v, Row) else v.__data__()
            for k, v in self.__dict__.items()
            if not k.startswith("_")
        }

    def __str__(self):
        cols_limit = 5
        data = ", ".join(
            [
                f"{k}={v}"
                for k, v in list(self.__dict__.items())[:cols_limit]
                if not k.startswith("_") or not k.isupper()
            ]
        )
        total_keys = len(self.__dict__.keys())
        if total_keys > cols_limit:
            data += f" and {total_keys - cols_limit} columns more"
        return f"<Row: {data}>"


def _format_sql(sql: str) -> str:
    try:
        import pygments
        import pygments.lexers
        import pygments.formatters

        lexer = pygments.lexers.get_lexer_by_name("sql")
        formatter = pygments.formatters.get_formatter_by_name("console")
        sql = pygments.highlight(sql, lexer, formatter)
    except ImportError:
        pass
    return sql


class BaseQuery:
    sql: SQLLike
    dialect = PgDialect()
    _connection: Connection

    async def execute(self) -> int:
        expr = self._build_expr()
        return await self._connection.execute(expr)

    def dump(self, writer: IO = sys.stdout) -> BaseQuery:
        writer.write(_format_sql(str(self)))
        return self

    def _build_expr(self) -> sa.sql.ClauseElement:
        raise NotImplementedError()

    def __await__(self):
        return self.execute().__await__()

    def __str__(self):
        return str(
            self._build_expr().compile(
                dialect=self.dialect, compile_kwargs={"literal_binds": True}
            )
        )


class RawQuery(Generic[RE], BaseQuery):
    entity: Type[RE]
    constructor: Factory

    def __init__(
        self,
        connection: Connection,
        sql: SQLLike,
        values: Mapping = None,
        entity: Type[E] = Row,
    ):
        self.sql = sql
        self.connection = connection
        self.values = values
        self.entity = entity

    def to(self, entity: Type[RE] = None) -> RawQuery[RE]:
        if entity is not None:
            self.entity = entity
        return self.clone()

    def clone(self, **kwargs: dict) -> RawQuery[RE]:
        defaults = dict(
            connection=self.connection,
            sql=self.sql,
            values=self.values,
            entity=self.entity,
        )
        defaults.update(kwargs)
        return type(self)(**defaults)

    async def all(self) -> Collection[RE]:
        return Collection(
            [
                entity_constructor(row, self.entity)
                for row in await self.connection.fetch_all(self.sql, self.values)
            ]
        )

    async def one(self) -> RE:
        rows = await self.all()
        if len(rows) == 0:
            raise DoesNotExist("Exactly one row expected but zero found.")

        if len(rows) > 1:
            raise DoesNotExist(f"Exactly one row expected but zero {len(rows)} found.")
        return rows.first()

    async def one_or(self, fallback: Any) -> Union[RE, Any]:
        try:
            return await self.one()
        except DoesNotExist:
            return fallback

    async def one_or_none(self) -> Optional[RE]:
        return self.one_or(None)

    async def execute(self) -> Any:
        return await self.connection.execute(self.sql, self.values)

    async def iterate(self) -> AsyncGenerator[RE, None]:
        async for row in self.connection.iterate(self.sql):
            yield entity_constructor(row, self.entity)

    def __str__(self):
        return self.sql


class InsertQuery(Generic[E], BaseQuery):
    def __init__(
        self,
        connection: Connection,
        schema: Type[E],
        values: Union[Mapping, Iterable[Mapping]],
        batch_size: int = None,
    ):
        self._schema = schema
        self._table = self._schema.__meta__.table
        self._connection = connection
        self._batch_size = batch_size
        if isinstance(values, Dict):
            values = [values]
        self._values = Collection(values)

    async def execute(self) -> None:
        batch_size = self._batch_size or 999_999_999_999
        for to_insert in self._values.chunk(batch_size):
            await self._connection.execute(self._table.insert().values(to_insert))

    def _build_expr(self) -> sa.sql.Insert:
        return (
            self._table.insert()
            .values(self._values.as_list())
            .returning(*self._schema.pk)
        )


class InsertEntityQuery(Generic[E], BaseQuery):
    __slots__ = ["_table", "_schema", "_connection", "_entity"]

    def __init__(self, connection: Connection, entity: E):
        self._schema = type(entity)
        self._table = self._schema.__meta__.table
        self._connection = connection
        self._entity = entity

    async def execute(self) -> E:
        identity = await self._connection.fetch_one(self._build_expr())
        for pk_field, value in zip(self._schema.pk, identity.values()):
            setattr(self._entity, pk_field.name, value)
        return self._entity

    def _build_expr(self) -> sa.sql.Insert:
        values = entity_to_db_dict(self._entity)

        # remove PK fields if their value is None and they are not nullable
        for pk_field in self._schema.pk:
            if values[pk_field.column_name] is None:
                del values[pk_field.column_name]

        return self._table.insert().values(values).returning(*self._schema.pk)

    def __await__(self):
        return self.execute().__await__()

    def __str__(self):
        return str(self._build_expr().compile(compile_kwargs={"literal_binds": True}))


class UpdateEntityQuery(Generic[E], BaseQuery):
    def __init__(self, connection: Connection, entity: E, values: Dict):
        self._connection = connection
        self._schema = type(entity)
        self._entity = entity
        self._values = values
        self._table = self._schema.__meta__.table

    async def execute(self) -> E:
        await self._connection.execute(self._build_expr())
        for column, value in self._values.items():
            setattr(self._entity, column, value)
        return self._entity

    def _build_expr(self) -> sa.sql.Update:
        changeset = self._values.copy()
        for column, value in changeset.items():
            if value == getattr(self._entity, column):
                del changeset[column]

        where = reduce(
            sa.sql.and_,
            [
                field == getattr(self._entity, field.name)
                for field in self._schema.__meta__.primary_key.fields
            ],
        )
        return self._table.update().values(changeset).where(where)

    def __await__(self):
        return self.execute().__await__()

    def __str__(self):
        return str(self._build_expr().compile(compile_kwargs={"literal_binds": True}))


class DeleteEntityQuery(Generic[E], BaseQuery):
    def __init__(self, connection: Connection, entity: E):
        self._connection = connection
        self._schema = type(entity)
        self._entity = entity
        self._table = self._schema.__meta__.table

    async def execute(self) -> E:
        await self._connection.execute(self._build_expr())
        for pk_field in self._schema.__meta__.primary_key:
            setattr(self._entity, pk_field.name, None)
        return self._entity

    def _build_expr(self) -> sa.sql.Delete:
        where = reduce(
            sa.sql.and_,
            [
                field == getattr(self._entity, field.name)
                for field in self._schema.__meta__.primary_key.fields
            ],
        )
        return self._table.delete().where(where)

    def __await__(self):
        return self.execute().__await__()

    def __str__(self):
        return str(self._build_expr().compile(compile_kwargs={"literal_binds": True}))


class UpdateQuery(BaseQuery):
    def __init__(
        self,
        connection: Connection,
        schema: Type[Schema],
        values: Mapping,
        where: sa.sql.ClauseElement = None,
    ):
        self._table = schema.__meta__.table
        self._schema = schema
        self._connection = connection
        self._values = values
        self._where = where

    def _build_expr(self):
        expr = self._table.update().values(self._values)
        if self._where is not None:
            expr = expr.where(self._where)
        return expr


class DeleteQuery(BaseQuery):
    def __init__(
        self,
        connection: Connection,
        schema: Type[Schema],
        where: sa.sql.ClauseElement = None,
    ):
        self._table = schema.__meta__.table
        self._schema = schema
        self._connection = connection
        self._where = where

    def _build_expr(self):
        expr = self._table.delete()
        if self._where is not None:
            expr = expr.where(self._where)
        return expr


class CompoundQuery:
    def __init__(
        self,
        schema: Type[Schema],
        connection: Connection,
        left_qs: Query,
        right_qs: Query,
        order_by: List[Field] = None,
        group_by: List[Field] = None,
        limit: int = None,
        offset: int = None,
        all: bool = None,
    ):
        self._schema = schema
        self._connection = connection
        self._left_qs = left_qs
        self._right_qs = right_qs
        self._order_by = order_by or []
        self._group_by = group_by or []
        self._limit = limit
        self._offset = offset
        self._all = all

    def order_by(self, *fields: Field) -> CompoundQuery:
        if not len(fields):
            self._order_by = []
        else:
            self._order_by = fields
        return self.clone()

    def group_by(self, *fields: Field) -> CompoundQuery:
        if not len(fields):
            self._group_by = []
        else:
            self._group_by = fields
        return self.clone()

    def limit(self, size: int) -> CompoundQuery:
        self._limit = size
        return self.clone()

    def offset(self, offset: int) -> CompoundQuery:
        self._offset = offset
        return self.clone()

    def page(self, page: int = 1, page_size: int = 50) -> CompoundQuery:
        page = max(page - 1, 0)
        start_offset = page * page_size
        return self.limit(page_size).offset(start_offset)

    def clone(self) -> CompoundQuery:
        return CompoundQuery(
            schema=self._schema,
            connection=self._connection,
            left_qs=self._left_qs,
            right_qs=self._right_qs,
            order_by=list(self._order_by).copy(),
            group_by=list(self._group_by).copy(),
            limit=self._limit,
            offset=self._offset,
            all=self._all,
        )

    def get_compound_select(self):
        raise NotImplementedError()

    def get_query(self) -> sa.sql.CompoundSelect:
        select = self.get_compound_select()
        select = select.limit(self._limit)
        select = select.offset(self._offset)
        select = select.group_by(*self._group_by)
        return select.order_by(*self._order_by)

    async def all(self) -> Collection[E]:
        expr = self.get_query()
        return Collection(
            [self._schema(**row) for row in await self._connection.fetch_all(expr)]
        )


class UnionQuery(CompoundQuery):
    def get_compound_select(self) -> sa.sql.CompoundSelect:
        if self._all:
            return self._left_qs.get_query().union_all(self._right_qs.get_query())
        return self._left_qs.get_query().union(self._right_qs.get_query())


class IntersectQuery(CompoundQuery):
    def get_compound_select(self) -> sa.sql.CompoundSelect:
        if self._all:
            return self._left_qs.get_query().intersect_all(self._right_qs.get_query())
        return self._left_qs.get_query().intersect(self._right_qs.get_query())


class ExceptionQuery(CompoundQuery):
    def get_compound_select(self) -> sa.sql.CompoundSelect:
        if self._all:
            return self._left_qs.get_query().except_all(self._right_qs.get_query())
        return self._left_qs.get_query().except_(self._right_qs.get_query())


def dumps(fn):
    def wrapper(self: Query, *args, **kwargs):
        if self._dump:
            self._dump_writer.write(_format_sql(str(self)))
        return fn(self, *args, **kwargs)

    return wrapper


class Query(Generic[E]):
    def __init__(
        self,
        connection: Connection,
        schema: Type[E],
        *,
        fields: List[Field] = None,
        where_clauses=None,
        having_clauses=None,
        order_by=None,
        group_by=None,
        limit=None,
        offset=None,
        preload=None,
        dump=False,
        dump_writer=None,
    ):
        self._schema = schema
        self._table = schema.__meta__.table
        self._fields = (
            fields if fields is not None else list(schema.__meta__.fields.values())
        )
        self._connection = connection
        self._where_clauses = where_clauses or []
        self._having_clauses = having_clauses or []
        self._order_by = order_by or []
        self._group_by = group_by or []
        self._limit = limit
        self._offset = offset
        self._dump = dump
        self._dump_writer = dump_writer
        self._preload: List[Field] = preload or []

    def clone(self) -> Query[E]:
        return Query(
            schema=self._schema,
            connection=self._connection,
            fields=self._fields.copy(),
            where_clauses=self._where_clauses.copy(),
            having_clauses=self._having_clauses.copy(),
            order_by=list(self._order_by).copy(),
            group_by=list(self._group_by).copy(),
            limit=self._limit,
            offset=self._offset,
            dump=self._dump,
            dump_writer=self._dump_writer,
            preload=self._preload,
        )

    def dump(self, writer: IO = sys.stdout) -> Query[E]:
        self._dump = True
        self._dump_writer = writer
        return self.clone()

    def select(self, *fields: Union[Field, sa.sql.ClauseElement]) -> Query[E]:
        """Set columns to select."""
        self._fields = list(fields)
        return self.clone()

    def add_select(self, field: Union[Field, sa.sql.ClauseElement]) -> Query[E]:
        """Add a column to select."""
        self._fields.append(field)
        return self.clone()

    def filter(self, **kwargs) -> Query[E]:
        query = self
        for k, v in kwargs.items():
            field = self._schema.__meta__.fields[k]
            query = self.where(field == v)
        return query

    def where(self, *criteria: sa.sql.ClauseElement) -> Query[E]:
        if not len(criteria):
            self._where_clauses = []
        else:
            self._where_clauses.extend(criteria)
        return self.clone()

    def where_raw(self, sql: str) -> Query[E]:
        return self.where(sa.sql.text(sql))

    def where_when(self, condition: Any, *criteria) -> Query[E]:
        """Add where statement only when condition is truthy."""
        condition = condition() if callable(condition) else condition
        if condition:
            return self.where(*criteria)
        return self.clone()

    def exclude(self, *criteria: sa.sql.ClauseElement) -> Query[E]:
        return self.where(Not(*criteria))

    def having(self, *criteria: sa.sql.ClauseElement) -> Query[E]:
        if not len(criteria):
            self._having_clauses = []
        else:
            self._having_clauses.extend(criteria)
        return self.clone()

    def having_raw(self, sql: str) -> Query[E]:
        return self.having(sa.sql.text(sql))

    def limit(self, size: int) -> Query[E]:
        self._limit = size
        return self.clone()

    def offset(self, offset: int) -> Query[E]:
        self._offset = offset
        return self.clone()

    def page(self, page: int = 1, page_size: int = 20) -> Query[E]:
        page = max(page - 1, 0)
        start_offset = page * page_size
        return self.limit(page_size).offset(start_offset)

    def order_by(self, *fields: Field) -> Query[E]:
        if not len(fields):
            self._order_by = []
        else:
            self._order_by = fields
        return self.clone()

    def group_by(self, *fields: Field) -> Query[E]:
        if not len(fields):
            self._group_by = []
        else:
            self._group_by = fields
        return self.clone()

    def hide(self, *fields: Field):
        """Remove fields from the result rows."""
        self._fields = [f for f in self._fields if f not in fields]
        return self.clone()

    def reverse(self):
        """Returns rows in reverse order ordered by primary key."""
        return self.order_by(*self._schema.__meta__.primary_key.desc())

    def aggregate(self, **kwargs: BaseFunction) -> Query[E]:
        qs = self
        for name, fn in kwargs.items():
            qs = self.add_select(fn().label(name))
        return qs

    def union(self, qs: Query, all: bool = False) -> CompoundQuery:
        return UnionQuery(self._schema, self._connection, self, qs, all=all)

    def union_all(self, qs: Query) -> CompoundQuery:
        return self.union(qs, all=True)

    def intersection(self, qs: Query, all: bool = False) -> CompoundQuery:
        """Return the rows that are common to all the queries."""
        return IntersectQuery(self._schema, self._connection, self, qs, all=all)

    def intersection_all(self, qs: Query) -> CompoundQuery:
        """Return the rows that are common to all the queries."""
        return self.intersection(qs, all=True)

    def difference(self, qs: Query, all: bool = False) -> CompoundQuery:
        """List the rows in the first that are not in the second."""
        return ExceptionQuery(self._schema, self._connection, self, qs, all=all)

    def difference_all(self, qs: Query) -> CompoundQuery:
        """List the rows in the first that are not in the second."""
        return self.difference(qs, all=True)

    def get_query(self) -> sa.sql.Select:
        tables = [self._table]
        select_from = self._table
        all_schema_fields = list(self._schema.__meta__.fields.values())
        fields = self._fields if self._fields is not None else all_schema_fields

        # for index, preload in enumerate(self._preload):
        #     for f in preload.schema.__meta__.fields.values():
        #         fields.append(f.alias(f"p{index}.{f.name}"))
        #
        #     select_from = select_from.outerjoin(preload._table)
        #     tables.append(preload._table)

        select: sa.sql.Select = sa.sql.select(tables)
        select = select.select_from(select_from)

        select = select.with_only_columns(fields)
        select = select.where(sa.sql.and_(*self._where_clauses))
        select = select.having(sa.sql.and_(*self._having_clauses))

        if self._limit:
            select = select.limit(self._limit)

        if self._offset:
            select = select.offset(self._offset)

        if self._order_by:
            select = select.order_by(*self._order_by)

        if self._group_by:
            select = select.group_by(*self._group_by)

        return select

    def get_sql(self) -> str:
        return str(self.get_query().compile(compile_kwargs={"literal_binds": True}))

    def raw(self, sql: SQLLike, params: Dict[str, Any] = None,) -> RawQuery[E]:
        return RawQuery(self._connection, sql, params, self._schema)

    def preload(self, *fields: Field) -> Query[E]:
        self._preload.extend(fields)
        return self.clone()

    # todo: not implemented
    async def chunk(self, size: int) -> AsyncGenerator[E, None]:
        """Chunk results by `size` items."""
        raise NotImplementedError()

    @dumps
    async def scalar(self):
        """Returns a single scalar value.
        If more that one field is in SELECT it will raise."""

        if len(self._fields) > 1:
            raise RuntimeError(
                '"scalar" query requires a single column in SELECT statement. '
                f"{len(self._fields)} found ({self._fields})."
            )
        expr = self.get_query()
        value = await self._connection.fetch_val(expr)
        return value

    @dumps
    async def one(self) -> E:
        expr = self.get_query().limit(2)
        rows = Collection(
            [self._schema(**row) for row in await self._connection.fetch_all(expr)]
        )
        if len(rows) == 0:
            raise self._schema.DoesNotExist("Query returned no results.")

        if len(rows) > 1:
            raise self._schema.MultipleResults("Query matched multiple rows.")

        return rows.first()

    async def one_or(self, fallback: Any) -> Union[E, Any]:
        try:
            return await self.one()
        except self._schema.DoesNotExist:
            return fallback

    async def one_or_none(self) -> Optional[E]:
        return await self.one_or(None)

    @dumps
    async def column(self, field: Field) -> Collection[Any]:
        """Fetch only single column as a list."""
        rows = await self.select(field).all()
        return rows.pluck(field)

    @dumps
    async def all(self) -> Collection[E]:
        expr = self.get_query()
        return Collection(
            [self._schema(**row) for row in await self._connection.fetch_all(expr)]
        )

    @dumps
    async def iterate(self) -> AsyncGenerator[E, None, None]:
        expr = self.get_query()
        if self._dump:
            self._print_query(expr)

        async for row in self._connection.iterate(expr):
            yield self._schema(**row)

    @dumps
    async def exists(self) -> bool:
        expr = self.get_query()
        return await self._connection.fetch_val(sa.exists(expr).select())

    @dumps
    async def unique(self):
        return await self.exists() is False

    @dumps
    async def count(self) -> int:
        expr = self.get_query().alias("__count")
        return await self._connection.fetch_val(
            sa.func.count().select().select_from(expr)
        )

    @dumps
    async def first(self, order_by: Field = None) -> Optional[E]:
        order_by = order_by or self._schema.__meta__.primary_key
        rule = order_by.asc()
        if not isinstance(rule, Iterable):
            rule = [rule]

        rows = await self.order_by(*rule).limit(1).all()
        if len(rows) > 0:
            return rows.first()
        return None

    @dumps
    async def last(self, order_by: Field = None) -> Optional[E]:
        order_by = order_by or self._schema.__meta__.primary_key
        rule = order_by.desc()
        if not isinstance(rule, Iterable):
            rule = [rule]

        rows = await self.order_by(*rule).limit(1).all()
        if len(rows) > 0:
            return rows.first()
        return None

    @dumps
    async def avg(self, field: Field) -> float:
        return await self.select().aggregate(_avg=func.Avg(field)).scalar()

    @dumps
    async def min(self, field: Field) -> float:
        return await self.select().aggregate(_min=func.Min(field)).scalar()

    @dumps
    async def max(self, field: Field) -> float:
        return await self.select().aggregate(_max=func.Max(field)).scalar()

    @dumps
    async def sum(self, field: Field) -> float:
        return await self.select().aggregate(_sum=func.Sum(field)).scalar()

    @dumps
    async def increment(self, column: Field, amount: Union[int, float]):
        kwargs = {column.name: column + amount}
        expr = self._table.update().values(**kwargs)
        if len(self._where_clauses):
            expr = expr.where(*self._where_clauses)
        await self._connection.execute(expr)

    @dumps
    async def decrement(self, column: Field, amount: Union[int, float]):
        kwargs = {column.name: column - amount}
        expr = self._table.update().values(**kwargs)
        if len(self._where_clauses):
            expr = expr.where(*self._where_clauses)
        await self._connection.execute(expr)

    def _print_query(self, expr: Union[sa.sql.ClauseElement, str]) -> None:
        if isinstance(expr, sa.sql.ClauseElement):
            expr = expr.compile(compile_kwargs={"literal_binds": True})
        print(expr)

    def __str__(self) -> str:
        return self.get_sql()


def query(schema: Type[S], connection: Connection) -> Query[S]:
    return Query(
        connection=connection, schema=schema, fields=schema.__meta__.fields.values(),
    )
