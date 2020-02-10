#  Copyright 2020 Oliver Cope
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import sqlparse
import pathlib
from typing import Mapping
from typing import Tuple
from typing import Iterable
from typing import Union

from .query import Query
from .exceptions import InvalidStatement
from .parsing import parse_comment_metadata


class Module:

    statements: Mapping[str, Query]

    def __init__(self):
        self.statements = {}

    def add_query(self, name, query):
        _marker = object()
        self.statements[name] = query
        if getattr(self, name, _marker) is _marker:
            setattr(self, name, query)
        else:
            raise InvalidStatement(
                f"Can't add query {name!r} in {query.source}: "
                f"{self!r} already has an attribute named {name!r} "
                f"(loaded from {getattr(self, name).source})"
            )

    def add_queries(
        self, qs: Union[Iterable[Tuple[str, Query]], Mapping[str, Query]]
    ):
        if isinstance(qs, Mapping):
            qs = qs.items()
        for name, query in qs:
            self.add_query(name, query)

    def bind(self, conn):
        bound = BoundModule(conn)
        bound.add_queries(self.statements)
        return bound

    def load_dir(self, path: Union[str, pathlib.Path]):
        def break_up_statements(
            path, sql
        ) -> Iterable[Tuple[Mapping, sqlparse.sql.Statement]]:
            current = ({}, [])
            for statement in sqlparse.parse(sql):
                if not str(statement).strip():
                    continue
                metadata = None
                for token in statement.tokens[:]:
                    if isinstance(token, sqlparse.sql.Comment):
                        metadata = parse_comment_metadata(str(token))
                        statement.tokens.remove(token)
                        break

                if metadata:
                    if current != ({}, []):
                        yield current
                    current = metadata, [str(statement)]

                if metadata is None:
                    if current:
                        current[1].append(str(statement))
                    else:
                        raise InvalidStatement(
                            f"{path!s}: no metadata comment found"
                        )

            yield current

        for p in pathlib.Path(path).glob("**/*.sql"):
            with open(p, "r") as f:
                sql = f.read()
                for metadata, statements in break_up_statements(p, sql):
                    if "name" not in metadata:
                        raise InvalidStatement(
                            f"{path!s}: no name specified (eg `-- :name my_query_name`)"
                        )
                    if "result" not in metadata:
                        raise InvalidStatement(
                            f"{path!s}: no result type specified (eg `-- :result :many`)"
                        )
                    self.add_query(
                        metadata["name"],
                        Query(metadata, statements, source=str(p)),
                    )

        return self


class BoundModule(Module):
    def __init__(self, conn):
        super().__init__()
        self._conn = conn

    def add_query(self, name, query):
        super().add_query(name, query.bind(self._conn))


def module(path, conn=None):
    module = Module()
    module.load_dir(path)
    if conn:
        module = module.bind(conn)
    return module
