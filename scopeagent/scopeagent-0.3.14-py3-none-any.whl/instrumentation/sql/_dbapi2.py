# Copyright (c) 2015-2017 Uber Technologies, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
from __future__ import absolute_import

import opentracing
import wrapt
from opentracing.ext import tags as ext_tags

from .local_span import func_span, start_child_span
from scopeagent.tracer import tags as scope_tags

# Utils for instrumenting DB API v2 compatible drivers.
# PEP-249 - https://www.python.org/dev/peps/pep-0249/

_BEGIN = 'begin-trans'
_COMMIT = 'commit'
_ROLLBACK = 'rollback'
_TRANS_TAGS = [_BEGIN, _COMMIT, _ROLLBACK]

NO_ARG = object()

MODULE_TO_TECHNOLOGY = {'psycopg2': 'postgresql'}

MAXIMUM_DB_STATEMENT_LENGTH = 512


def format_version(module_name, version):
    version_str = str(version)
    if module_name != 'psycopg2':
        return version_str
    # server_version in psycopg is stored as int
    # https://github.com/psycopg/psycopg2/blob/4d10f1235fed1c0aa5958cc4a9248688c3345aad/psycopg/connection.h#L101
    # so the expected value is e.g. 120001. Here we transform it to 12.0.1
    if len(version_str) < 6:
        return version_str
    return '{major}.{minor}.{patch}'.format(
        major=int(version_str[0:2]), minor=int(version_str[2:4]), patch=int(version_str[4:6])
    )


def get_connection_string(module_name, parameters):
    technology = MODULE_TO_TECHNOLOGY.get(module_name, '')
    return '{technology}://{user}@{host}:{port}/{name}'.format(
        technology=technology,
        user=parameters.get('user'),
        host=parameters.get('host'),
        port=parameters.get('port'),
        name=parameters.get('dbname'),
    )


def db_span(
    sql_statement,
    module_name,
    sql_parameters=None,
    connect_params=None,
    cursor_params=None,
    tracer=None,
    dsn=None,
    server_version=None,
    driver_version=None,
    dsn_parameters={},
    active_db_statement_values=None,
):
    tracer = tracer or opentracing.tracer
    span = tracer.active_span

    statement = sql_statement.strip()

    add_sql_tag = True
    if sql_statement in _TRANS_TAGS:
        operation = sql_statement
        add_sql_tag = False
    else:
        space_idx = statement.find(' ')
        if space_idx == -1:
            operation = ''  # unrecognized format of the query
        else:
            operation = statement[0:space_idx]

    tags = {
        ext_tags.DATABASE_TYPE: 'sql',
        ext_tags.SPAN_KIND: ext_tags.SPAN_KIND_RPC_CLIENT,
        scope_tags.DB_PRODUCT_NAME: MODULE_TO_TECHNOLOGY[module_name],
        scope_tags.DB_DRIVER_NAME: module_name,
        scope_tags.PEER_SERVICE: MODULE_TO_TECHNOLOGY[module_name],
    }
    if driver_version:
        tags[scope_tags.DB_DRIVER_VERSION] = driver_version
    if server_version:
        tags[scope_tags.DB_PRODUCT_VERSION] = format_version(module_name, server_version)
    if add_sql_tag:
        tags[scope_tags.DB_PREPARE_STATEMENT] = statement[:MAXIMUM_DB_STATEMENT_LENGTH]
        if sql_parameters and active_db_statement_values:
            tags[ext_tags.DATABASE_STATEMENT] = (statement % sql_parameters)[:MAXIMUM_DB_STATEMENT_LENGTH]

    tags[scope_tags.DB_CONNECTION_STRING] = get_connection_string(module_name, dsn_parameters)

    # Non-standard tags
    if sql_parameters and active_db_statement_values:
        tags[scope_tags.DB_PARAMS] = sql_parameters

    tags[ext_tags.PEER_HOSTNAME] = dsn_parameters.get('host')
    tags[ext_tags.DATABASE_INSTANCE] = dsn_parameters.get('dbname')
    tags[ext_tags.DATABASE_USER] = dsn_parameters.get('user')
    tags[ext_tags.PEER_PORT] = dsn_parameters.get('port')

    if cursor_params:
        tags[scope_tags.DB_CURSOR] = cursor_params

    return start_child_span(operation_name='%s:%s' % (module_name, operation), parent=span, tags=tags, tracer=tracer)


class ConnectionFactory(object):
    """
    Wraps connect_func of the DB API v2 module by creating a wrapper object
    for the actual connection.
    """

    def __init__(
        self,
        connect_func,
        module_name,
        conn_wrapper_ctor=None,
        tracer=None,
        version=None,
        active_db_statement_values=None,
    ):
        self._tracer = tracer
        self._connect_func = connect_func
        self._module_name = module_name
        self._version = version
        self._active_db_statement_values = active_db_statement_values
        if hasattr(connect_func, '__name__'):
            self._connect_func_name = '%s:%s' % (module_name, connect_func.__name__)
        else:
            self._connect_func_name = '%s:%s' % (module_name, connect_func)
        self._wrapper_ctor = conn_wrapper_ctor if conn_wrapper_ctor is not None else ConnectionWrapper

    def __call__(self, *args, **kwargs):
        safe_kwargs = kwargs
        if 'passwd' in kwargs or 'password' in kwargs or 'conv' in kwargs:
            safe_kwargs = dict(kwargs)
            if 'passwd' in safe_kwargs:
                del safe_kwargs['passwd']
            if 'password' in safe_kwargs:
                del safe_kwargs['password']
            if 'conv' in safe_kwargs:  # don't log conversion functions
                del safe_kwargs['conv']
        connect_params = (args, safe_kwargs) if args or safe_kwargs else None
        tags = {
            ext_tags.DATABASE_TYPE: 'sql',
            ext_tags.SPAN_KIND: ext_tags.SPAN_KIND_RPC_CLIENT,
            scope_tags.PEER_SERVICE: MODULE_TO_TECHNOLOGY[self._module_name],
            scope_tags.DB_PRODUCT_NAME: MODULE_TO_TECHNOLOGY[self._module_name],
            scope_tags.DB_DRIVER_NAME: self._module_name,
            scope_tags.DB_DRIVER_VERSION: self._version,
            scope_tags.DB_PARAMS: connect_params,
            ext_tags.PEER_HOSTNAME: safe_kwargs.get('host'),
            ext_tags.DATABASE_INSTANCE: safe_kwargs.get('database'),
            ext_tags.PEER_PORT: safe_kwargs.get('port'),
        }
        with func_span(self._connect_func_name, tags=tags, tracer=self._tracer):
            return self._wrapper_ctor(
                connection=self._connect_func(*args, **kwargs),
                module_name=self._module_name,
                connect_params=connect_params,
                tracer=self._tracer,
                version=self._version,
                active_db_statement_values=self._active_db_statement_values,
            )


class ConnectionWrapper(wrapt.ObjectProxy):
    __slots__ = ('_module_name', '_connect_params', '_tracer', '_version', '_active_db_statement_values')

    def __init__(self, connection, module_name, connect_params, tracer, version, active_db_statement_values):
        super(ConnectionWrapper, self).__init__(wrapped=connection)
        self._module_name = module_name
        self._connect_params = connect_params
        self._tracer = tracer
        self._version = version
        self._active_db_statement_values = active_db_statement_values

    def cursor(self, *args, **kwargs):
        return CursorWrapper(
            cursor=self.__wrapped__.cursor(*args, **kwargs),
            module_name=self._module_name,
            connect_params=self._connect_params,
            cursor_params=(args, kwargs) if args or kwargs else None,
            tracer=self._tracer,
            version=self._version,
            active_db_statement_values=self._active_db_statement_values,
        )

    def begin(self):
        with db_span(sql_statement=_BEGIN, module_name=self._module_name, tracer=self._tracer):
            return self.__wrapped__.begin()

    def commit(self):
        with db_span(sql_statement=_COMMIT, module_name=self._module_name, tracer=self._tracer):
            return self.__wrapped__.commit()

    def rollback(self):
        with db_span(sql_statement=_ROLLBACK, module_name=self._module_name, tracer=self._tracer):
            return self.__wrapped__.rollback()


class ContextManagerConnectionWrapper(ConnectionWrapper):
    """
    Extends ConnectionWrapper by implementing `__enter__` and `__exit__`
    methods of the context manager API, for connections that can be used
    in as context managers to control the transactions, e.g.

    .. code-block:: python

        with MySQLdb.connect(...) as cursor:
            cursor.execute(...)
    """

    def __init__(self, connection, module_name, connect_params, tracer, version, active_db_statement_values):
        super(ContextManagerConnectionWrapper, self).__init__(
            connection=connection,
            module_name=module_name,
            connect_params=connect_params,
            tracer=tracer,
            version=version,
            active_db_statement_values=active_db_statement_values,
        )

    def __getattr__(self, name):
        # Tip suggested here:
        # https://gist.github.com/mjallday/3d4c92e7e6805af1e024.
        if name == '_sqla_unwrap':
            return self.__wrapped__
        return super(ContextManagerConnectionWrapper, self).__getattr__(name)

    def __enter__(self):
        with func_span('%s:begin_transaction' % self._module_name, self._tracer):
            cursor = self.__wrapped__.__enter__()

        return CursorWrapper(cursor=cursor, module_name=self._module_name, connect_params=self._connect_params)

    def __exit__(self, exc, value, tb):
        outcome = _COMMIT if exc is None else _ROLLBACK
        with db_span(sql_statement=outcome, module_name=self._module_name, tracer=self._tracer):
            return self.__wrapped__.__exit__(exc, value, tb)


class CursorWrapper(wrapt.ObjectProxy):
    __slots__ = (
        '_module_name',
        '_connect_params',
        '_cursor_params',
        '_tracer',
        '_version',
        '_active_db_statement_values',
    )

    def __init__(
        self,
        cursor,
        module_name,
        connect_params=None,
        cursor_params=None,
        tracer=None,
        version=None,
        active_db_statement_values=None,
    ):
        super(CursorWrapper, self).__init__(wrapped=cursor)
        self._module_name = module_name
        self._connect_params = connect_params
        self._cursor_params = cursor_params
        self._tracer = tracer
        self._version = version
        self._active_db_statement_values = active_db_statement_values
        # We could also start a span now and then override close() to capture
        # the life time of the cursor

    def execute(self, sql, params=NO_ARG):
        with db_span(
            sql_statement=sql,
            sql_parameters=params if params is not NO_ARG else None,
            module_name=self._module_name,
            connect_params=self._connect_params,
            cursor_params=self._cursor_params,
            tracer=self._tracer,
            dsn=self.__wrapped__.connection.dsn,
            server_version=self.__wrapped__.connection.server_version,
            driver_version=self._version,
            dsn_parameters=self.__wrapped__.connection.get_dsn_parameters(),
            active_db_statement_values=self._active_db_statement_values,
        ):
            if params is NO_ARG:
                return self.__wrapped__.execute(sql)
            else:
                return self.__wrapped__.execute(sql, params)

    def executemany(self, sql, seq_of_parameters):
        with db_span(
            sql_statement=sql,
            sql_parameters=seq_of_parameters,
            module_name=self._module_name,
            connect_params=self._connect_params,
            cursor_params=self._cursor_params,
            tracer=self._tracer,
        ):
            return self.__wrapped__.executemany(sql, seq_of_parameters)

    def callproc(self, proc_name, params=NO_ARG):
        with db_span(
            sql_statement='sproc:%s' % proc_name,
            sql_parameters=params if params is not NO_ARG else None,
            module_name=self._module_name,
            connect_params=self._connect_params,
            cursor_params=self._cursor_params,
            tracer=self._tracer,
        ):
            if params is NO_ARG:
                return self.__wrapped__.callproc(proc_name)
            else:
                return self.__wrapped__.callproc(proc_name, params)
