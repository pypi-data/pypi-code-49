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

import re
from itertools import count
from typing import List
from typing import Mapping
from typing import Union
from typing import Tuple

BindParams = Union[Tuple, Mapping]

DEFAULT_RESULT_TYPE = "cursor"

result_types = [
    ("one", ["one", "1"]),
    ("many", ["many", "*"]),
    ("affected", ["affected", "n"]),
    ("exactlyone", ["exactly-one", "=1"]),
    ("cursor", ["cursor", "raw"]),
    ("scalar", ["scalar"]),
    ("column", ["column"]),
]

result_type_pattern = rf"""
    :(?:
        {"|".join(
            f"(?P<{name}>{'|'.join(re.escape(t) for t in toks)})"
            for name, toks in result_types
        )}
    )
"""
name_pattern = re.compile(
    rf":name\s+(?P<name>\w+)(?:\s+{result_type_pattern})?$", re.X
)
result_pattern = re.compile(rf":result\s+{result_type_pattern}$", re.X)
param_pattern = re.compile(
    r"""
    # Don't match if preceded by backslash (an escape) or ':' (an SQL cast,
    # eg '::INT')
    (?<![:\\])

    # Optional parameter type
    (?:
        :(?P<param_type>
            value|v|value\*|v\*|tuple|t|tuple\*|t\*|identifier|i|raw|r
        )
    )?

    # An identifier
    :(?P<param>[a-zA-Z_]\w*)

    # followed by a non-word char, or end of string
    (?=\W|$)
    """,
    re.X,
)


def parse_comment_metadata(s: str) -> Mapping:

    lines = (re.sub(r"^\s*--", "", line).strip() for line in s.split("\n"))
    patterns = [name_pattern, result_pattern]
    result = {}
    for l in lines:
        for p in patterns:
            mo = p.match(l)
            if mo:
                for k, v in mo.groupdict().items():
                    if v is not None:
                        result[k] = v

    if result:
        return {
            "name": result.get("name", None),
            "result": next(
                (
                    rt
                    for rt in [name for name, _ in result_types]
                    if rt in result
                ),
                DEFAULT_RESULT_TYPE,
            ),
        }

    return None


def quote_ident_ansi(s):
    s = str(s)
    if "\x00" in s:
        raise ValueError(
            "Quoted identifiers can contain any character, "
            "except the character with code zero"
        )
    return f'''"{s.replace('"', '""')}"'''


def compile_bind_parameters(
    target_style: str, sql: str, bind_parameters: Mapping
) -> BindParams:
    """
    :param target_style: A DBAPI paramstyle value (eg 'qmark', 'format', etc)
    :param sql: An SQL str
    :bind_parameters: A dict of bind parameters for the query

    :return: tuple of `(sql, bind_parameters)`. ``sql`` will be rewritten with
             the target paramstyle; ``bind_parameters`` will be a tuple or
             dict as required.
    :raises: TypeError, if the bind_parameters do not match the query
    """

    positional, param_gen = {
        "qmark": (True, lambda name: "?"),
        "numeric": (True, lambda name, c=count(1): f":{next(c)}"),
        "format": (True, lambda name: "%s"),
        "pyformat": (False, lambda name: f"%({name})s"),
        "named": (False, lambda name: f":{name}"),
    }[target_style]

    if not bind_parameters:
        return (sql, (tuple() if positional else {}))

    if target_style[-6:] == "format":
        sql = sql.replace("%", "%%")

    positional_params = []
    named_params = {}

    def replace_placeholder(match):
        def make_sequence_placeholder(items: List, _c=count(1)) -> str:
            names = [f"_{next(_c)}" for _ in range(len(items))]
            if positional:
                positional_params.extend(items)
            else:
                named_params.update(zip(names, items))
            return ", ".join(param_gen(n) for n in names)

        group = match.groupdict().get
        pt = group("param_type")
        p = group("param")
        if pt in {None, "value", "v"}:
            if positional:
                positional_params.append(bind_parameters[p])
            else:
                named_params[p] = bind_parameters[p]
            return param_gen(p)
        elif pt in {"raw", "r"}:
            return str(bind_parameters.get(p))
        elif pt in {"identifier", "i"}:
            return quote_ident_ansi(bind_parameters.get(p))
        elif pt in {"value*", "v*", "tuple", "t"}:
            placeholder = make_sequence_placeholder(list(bind_parameters[p]))
            if pt in {"tuple", "t"}:
                return f"({placeholder})"
            return placeholder
        elif pt in {"tuple*", "t*"}:
            return ", ".join(
                f"({make_sequence_placeholder(list(items))})"
                for items in bind_parameters[p]
            )
        else:
            raise ValueError(f"Unsupported param_type {pt}")

    transformed_sql = param_pattern.sub(replace_placeholder, sql)
    if positional:
        return transformed_sql, tuple(positional_params)
    return transformed_sql, named_params
