from __future__ import annotations

from typing import Iterable, Mapping, Type, TypeVar

import sqlalchemy as sa
from databases.core import Transaction

from .connections import Connection
from .queries import (
    DeleteEntityQuery,
    DeleteQuery,
    InsertEntityQuery,
    InsertQuery,
    Query,
    RawQuery,
    SQLLike,
    UpdateEntityQuery,
    UpdateQuery,
)
from .schemas import Schema

E = TypeVar("E", bound=Schema)


class Store:
    def __init__(self, connection: Connection):
        self._connection = connection

    def raw(self, sql: SQLLike, params: Mapping = None) -> RawQuery[E]:
        return RawQuery(self._connection, sql, params)

    def transaction(self, force_rollback: bool = False) -> Transaction:
        return self._connection.transaction(force_rollback=force_rollback)

    def insert(self, entity: E) -> InsertEntityQuery[E]:
        return InsertEntityQuery(self._connection, entity)

    def insert_all(
        self, schema: Type[E], values: Iterable[Mapping], batch_size: int = None,
    ):
        return InsertQuery(
            connection=self._connection,
            schema=schema,
            values=values,
            batch_size=batch_size,
        )

    def update(self, entity: E, **values) -> UpdateEntityQuery:
        return UpdateEntityQuery(self._connection, entity, values)

    def update_all(
        self, schema: Type[E], values: Mapping, where: sa.sql.ClauseElement = None
    ) -> UpdateQuery:
        return UpdateQuery(self._connection, schema, values, where)

    def delete(self, entity: E) -> DeleteEntityQuery:
        return DeleteEntityQuery(self._connection, entity)

    def delete_all(
        self, schema: Type[E], where: sa.sql.ClauseElement = None
    ) -> DeleteQuery:
        return DeleteQuery(self._connection, schema, where)

    def query(self, schema: Type[E]) -> Query[E]:
        return Query(self._connection, schema, fields=schema.__meta__.fields.values())

    # def select(self,
    #       from_,
    #       select='*',
    #       join=None,
    #       where=None,
    #       having=None,
    #       group_by=None,
    #       ):
    #     store.select(
    #         from_=User,
    #         select=[User.id, User.name],
    #         join=[User.posts],
    #         where=[
    #             User.id > 1,
    #             Or(User.name.startswith('hui'), User.name.startswith('hui')),
    #         ],
    #         having=User.id < 10,
    #         group_by=[User.name],
    #     ).into(User).all()
