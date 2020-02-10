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

from typing import Any
from typing import Mapping
from typing import List
from typing import Tuple
import sys

from .parsing import BindParams, compile_bind_parameters


def get_param_style(conn: Any) -> str:

    modname = conn.__class__.__module__
    while modname:
        try:
            return sys.modules[modname].paramstyle
        except AttributeError:
            if "." in modname:
                modname = modname.rsplit(".", 1)[0]
            else:
                raise TypeError(
                    f"Can't find paramstyle for connection {conn!r}"
                )


class Query:

    metadata: Mapping
    sql: str
    source: str

    def __init__(self, metadata, sql, source):
        self.statements = sql
        self.metadata = metadata
        self.source = source

    def bind(self, conn):
        return BoundQuery(self.metadata, self.statements, self.source, conn)


class BoundQuery(Query):
    def __init__(self, metadata, sql, source, conn):
        self._conn = conn
        self._paramstyle = get_param_style(conn)
        super().__init__(metadata, sql, source)

    def prepare(self, kw: Mapping) -> List[Tuple[str, BindParams]]:
        return [
            compile_bind_parameters(self._paramstyle, s, kw)
            for s in self.statements
        ]

    def __call__(self, **kw):
        rt = self.metadata["result"]

        cursor = self._conn.cursor()
        affected = None

        for sqltext, bind_params in self.prepare(kw):
            affected = cursor.execute(sqltext, bind_params)

        if rt == "many":
            return iter(cursor.fetchone, None)

        if rt == "column":
            return (row[0] for row in iter(cursor.fetchone, None))

        if rt == "affected":
            return affected

        if rt == "cursor":
            return cursor

        raise ValueError(f"Unsupported result type: {rt}")
