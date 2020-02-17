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
from itertools import chain
from typing import Callable
from typing import Dict
from typing import Iterable
from typing import Mapping
from typing import Optional
from typing import Tuple
from typing import Union

from .query import Query
from .exceptions import InvalidStatement
from .parsing import parse_comment_metadata
from .parsing import DEFAULT_RESULT_TYPE

SQL_FILE_GLOB = "**/*.sql"


class Module:

    reloader: Optional[Callable] = None
    _conn = None
    queries: Dict = {}

    def __init__(self):
        self.queries = {}

    def __getattr__(self, name):
        if self.reloader:
            self.reloader()
        try:
            return self.queries[name]
        except KeyError:
            raise AttributeError(name)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        return

    def set_reloader(self, fn):
        self.reloader = fn

    def clear(self):
        self.queries.clear()

    def add_query(self, name, query):
        if name in self.queries:
            raise InvalidStatement(
                f"Can't add query {name!r} in {query.source}: "
                f"{self!r} already has an attribute named {name!r} "
                f"(loaded from {getattr(self, name).source})"
            )
        if self._conn:
            query = query.bind(self._conn)
        self.queries[name] = query

    def add_queries(
        self, qs: Union[Iterable[Tuple[str, Query]], Mapping[str, Query]]
    ):
        if isinstance(qs, Mapping):
            qs = qs.items()
        for name, query in qs:
            self.add_query(name, query)

    def load_dir(self, path: Union[str, pathlib.Path]):
        for p in pathlib.Path(path).glob(SQL_FILE_GLOB):
            self.load_file(p)

        return self

    def load_file(self, path: pathlib.Path):
        queries = list(load_queries(path))
        for query in queries:
            self.add_query(query.name, query)

    def execute(self, conn, sql=None, result="many", **kw):
        if sql is None:
            conn, sql = self._conn, conn
        query = Query(
            name=None,
            metadata={"result": result},
            statements=[sql],
            source="<string>",
        )
        return query(conn, **kw)

    def one(self, *args, **kwargs):
        return self.execute(result="one", *args, **kwargs)

    def many(self, *args, **kwargs):
        return self.execute(result="many", *args, **kwargs)

    def scalar(self, *args, **kwargs):
        return self.execute(result="scalar", *args, **kwargs)

    def affected(self, *args, **kwargs):
        return self.execute(result="affected", *args, **kwargs)

    def column(self, *args, **kwargs):
        return self.execute(result="column", *args, **kwargs)

    def cursor(self, *args, **kwargs):
        return self.execute(result="cursor", *args, **kwargs)

    def bind(self, conn) -> "Module":
        """
        Return a copy of the module bound to a database connection
        """
        cls = self.__class__
        bound = cls.__new__(cls)
        bound.__dict__ = {
            "_conn": conn,
            "reloader": self.reloader,
            "queries": {
                name: q.bind(conn) for name, q in self.queries.items()
            },
        }
        return bound

    def transaction(self, conn) -> "Transaction":
        return Transaction(self, conn)


class Transaction:
    def __init__(self, module, conn):
        self.conn = conn
        self.module = module.bind(conn)

    def __enter__(self):
        return self.module

    def __exit__(self, type, value, traceback):
        if type:
            self.conn.rollback()
        else:
            self.conn.commit()

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()


def module(path, auto_reload=False):
    path = pathlib.Path(path)
    module = Module()
    module.load_dir(path)
    if auto_reload:

        def get_all_mtimes(path):
            return chain(
                [path.stat().st_mtime],
                (p.stat().st_mtime for p in path.glob(SQL_FILE_GLOB)),
            )

        module_mtime = [max(get_all_mtimes(path))]

        def reload_module():
            if any(m > module_mtime[0] for m in get_all_mtimes(path)):
                module_mtime[:] = [max(get_all_mtimes(path))]
                module.clear()
                module.load_dir(path)

        module.set_reloader(reload_module)
    return module


def _break_up_statements(
    path, sql
) -> Iterable[Tuple[Mapping, sqlparse.sql.Statement]]:
    statements = (s for s in sqlparse.parse(sql) if str(s).strip())
    current = ({}, [])
    for statement in statements:
        metadata = {}
        for token in statement.tokens[:]:
            if isinstance(token, sqlparse.sql.Comment):
                metadata = parse_comment_metadata(str(token))
                statement.tokens.remove(token)
                break

        if metadata:
            if current != ({}, []):
                yield current
            current = metadata, [str(statement)]

        else:
            current[1].append(str(statement))

    yield current


def load_queries(path: pathlib.Path) -> Iterable[Query]:
    with path.open("r", encoding="UTF-8") as f:
        sql = f.read()
        for ix, (metadata, statements) in enumerate(
            _break_up_statements(path, sql)
        ):
            if "result" not in metadata:
                metadata["result"] = DEFAULT_RESULT_TYPE
            if "name" not in metadata:
                if ix == 0:
                    metadata["name"] = path.stem
                else:
                    raise InvalidStatement(
                        f"{path!s}: no name specified (eg `-- :name my_query_name`)"
                    )
            if "result" not in metadata:
                raise InvalidStatement(
                    f"{path!s}: no result type specified (eg `-- :result :many`)"
                )
            yield Query(
                metadata["name"], metadata, statements, source=str(path)
            )
