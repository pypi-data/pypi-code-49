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
from . import exceptions


known_styles = {}


def get_param_style(conn: Any) -> str:

    conncls = conn.__class__
    try:
        return known_styles[conncls]
    except KeyError:
        modname = conncls.__module__
        while modname:
            try:
                style = sys.modules[modname].paramstyle
                known_styles[conncls] = style
                return style
            except AttributeError:
                if "." in modname:
                    modname = modname.rsplit(".", 1)[0]
                else:
                    raise TypeError(
                        f"Can't find paramstyle for connection {conn!r}"
                    )


class Query:

    name: str
    metadata: Mapping
    sql: str
    source: str

    def __init__(self, name, metadata, statements, source):
        self.name = name
        self.metadata = metadata
        self.statements = statements
        self.source = source
        self._conn = None

    def prepare(self, paramstyle, kw: Mapping) -> List[Tuple[str, BindParams]]:
        return [
            compile_bind_parameters(paramstyle, s, kw) for s in self.statements
        ]

    def bind(self, conn) -> "Query":
        """
        Return a copy of the query bound to a database connection
        """
        cls = self.__class__
        bound = cls.__new__(cls)
        bound.__dict__ = self.__dict__.copy()
        bound._conn = conn
        return bound

    def __call__(self, conn=None, *, debug=False, **kw):
        if conn is None:
            conn = self._conn
            if conn is None:
                raise TypeError(
                    "Query must be called with a connection argument"
                )
        rt = self.metadata["result"]

        paramstyle = get_param_style(conn)
        cursor = conn.cursor()
        affected = None

        for sqltext, bind_params in self.prepare(paramstyle, kw):
            if debug:
                import textwrap

                print(
                    f"Executing \n{textwrap.indent(sqltext, '    ')} with {bind_params!r}",
                    file=sys.stderr,
                )
            affected = cursor.execute(sqltext, bind_params)

        if rt == "one":
            return cursor.fetchone()

        if rt == "many":
            return iter(cursor.fetchone, None)

        if rt == "exactlyone":
            row = cursor.fetchone()
            if row is None:
                raise exceptions.NoResultFound()
            if cursor.fetchone() is not None:
                raise exceptions.MultipleResultsFound()
            return row

        if rt == "scalar":
            result = cursor.fetchone()
            if result is None:
                raise exceptions.NoResultFound()
            if isinstance(result, dict):
                return result[next(result)]
            return result[0]

        if rt == "column":
            return (row[0] for row in iter(cursor.fetchone, None))

        if rt == "affected":
            return affected

        if rt == "cursor":
            return cursor

        raise ValueError(f"Unsupported result type: {rt}")
