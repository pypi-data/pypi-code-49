# Copyright 2019 Bringing Data to Life Pty Ltd 
#
# Copyright 2013-2017 Lionheart Software LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Copyright (c) 2008, django-pyodbc developers (see README.rst).
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#     1. Redistributions of source code must retain the above copyright notice,
#        this list of conditions and the following disclaimer.
#
#     2. Redistributions in binary form must reproduce the above copyright
#        notice, this list of conditions and the following disclaimer in the
#        documentation and/or other materials provided with the distribution.
#
#     3. Neither the name of django-sql-server nor the names of its contributors
#        may be used to endorse or promote products derived from this software
#        without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

try:
    from django.db.backends.base.client import BaseDatabaseClient
except ImportError:
    # import location prior to Django 1.8
    from django.db.backends import BaseDatabaseClient

import os
import sys

class DatabaseClient(BaseDatabaseClient):
    executable_name = 'isql'

    def runshell(self):
        settings_dict = self.connection.settings_dict
        user = settings_dict['OPTIONS'].get('user', settings_dict['USER'])
        password = settings_dict['OPTIONS'].get('passwd', settings_dict['PASSWORD'])
        
        dsn = settings_dict['OPTIONS'].get('dsn', settings_dict.get('ODBC_DSN'))
        args = ['%s -v %s %s %s' % (self.executable_name, dsn, user, password)]

        import subprocess
        try:
            subprocess.call(args, shell=True)
        except KeyboardInterrupt:
            pass


import re
import sys
import datetime

from django.core.exceptions import ImproperlyConfigured
from django.db.backends.base.base import BaseDatabaseWrapper
from .client import DatabaseClient
from .compat import binary_type, text_type, timezone
from .creation import DatabaseCreation
from django.db.backends.base.introspection import BaseDatabaseIntrospection
from .operations import DatabaseOperations
from .features import FilemakerDatabaseFeatures


try:
    import pyodbc as Database
except ImportError:
    e = sys.exc_info()[1]
    raise ImproperlyConfigured("Error loading pyodbc module: %s" % e)

m = re.match(r'(\d+)\.(\d+)\.(\d+)(?:-beta(\d+))?', Database.version)
vlist = list(m.groups())
if vlist[3] is None: vlist[3] = '9999'
pyodbc_ver = tuple(map(int, vlist))
if pyodbc_ver < (2, 0, 38, 9999):
    raise ImproperlyConfigured("pyodbc 2.0.38 or newer is required; you have %s" % Database.version)

from django.conf import settings
from django import VERSION as DjangoVersion
if  DjangoVersion[:2] == (2, 2):
    _DJANGO_VERSION = 23
elif DjangoVersion[:2] == (2, 1):
    _DJANGO_VERSION = 22
elif DjangoVersion[:2] == (2, 0):
    _DJANGO_VERSION = 21
elif DjangoVersion[:2] == (1, 11):
    _DJANGO_VERSION = 20
elif DjangoVersion[:2] == (1, 10):
    _DJANGO_VERSION = 19
elif DjangoVersion[:2] == (1, 9):
    _DJANGO_VERSION = 19
elif DjangoVersion[:2] == (1, 8):
    _DJANGO_VERSION = 18
elif DjangoVersion[:2] == (1, 7):
    _DJANGO_VERSION = 17
elif DjangoVersion[:2] == (1, 6):
    _DJANGO_VERSION = 16
elif DjangoVersion[:2] == (1, 5):
    _DJANGO_VERSION = 15
elif DjangoVersion[:2] == (1, 4):
    _DJANGO_VERSION = 14
elif DjangoVersion[:2] == (1, 3):
    _DJANGO_VERSION = 13
elif DjangoVersion[:2] == (1, 2):
    _DJANGO_VERSION = 12
elif DjangoVersion[:2] == (1, 1):
    _DJANGO_VERSION = 11
else:
    raise ImproperlyConfigured("Django %d.%d is not supported." % DjangoVersion[:2])

from django.db import utils

DatabaseError = Database.Error
IntegrityError = Database.IntegrityError

def ignore(*args, **kwargs):
    pass

class DatabaseIntrospection(BaseDatabaseIntrospection):
    #get_table_list = complain
    #get_table_description = complain
    #get_relations = complain
    #get_indexes = complain
    #get_key_columns = complain
    pass 


class DatabaseWrapper(BaseDatabaseWrapper):
    
    _DJANGO_VERSION = _DJANGO_VERSION
    Database = Database
    driver_supports_utf8 = None
    encoding = 'utf-8'
    autocommit = True

    operators = {
        # Since '=' is used not only for string comparision there is no way
        # to make it case (in)sensitive. It will simply fallback to the
        # database collation.
        'exact': '= %s',
        'iexact': "= UPPER(%s)",
        'contains': "LIKE %s ESCAPE '\\'",
        'icontains': "LIKE UPPER(%s) ESCAPE '\\'",
        'gt': '> %s',
        'gte': '>= %s',
        'lt': '< %s',
        'lte': '<= %s',
        'startswith': "LIKE %s ESCAPE '\\'",
        'endswith': "LIKE %s ESCAPE '\\'",
        'istartswith': "LIKE UPPER(%s) ESCAPE '\\'",
        'iendswith': "LIKE UPPER(%s) ESCAPE '\\'",

        # TODO: remove, keep native T-SQL LIKE wildcards support
        # or use a "compatibility layer" and replace '*' with '%'
        # and '.' with '_'
        'regex': 'LIKE %s',
        'iregex': 'LIKE %s',

        # TODO: freetext, full-text contains...
    }
    
    # Override the base class implementations with null
    # implementations. Anything that tries to actually
    # do something raises complain; anything that tries
    # to rollback or undo something raises ignore.
    #ensure_connection = complain
    #_commit = complain
    #_rollback = ignore
    #_close = ignore
    #_savepoint = ignore
    #_savepoint_commit = complain
    #_savepoint_rollback = ignore
    # Classes instantiated in __init__().
    client_class = DatabaseClient
    creation_class = DatabaseCreation
    features_class = FilemakerDatabaseFeatures
    introspection_class = DatabaseIntrospection
    ops_class = DatabaseOperations

    data_types = DatabaseCreation.data_types

    def __init__(self, *args, **kwargs):
        super(DatabaseWrapper, self).__init__(*args, **kwargs)
        options = self.settings_dict.get('OPTIONS', None)
        self.client = DatabaseClient(self)
        if options:
            self.datefirst = options.get('datefirst', 1)
            self.unicode_results = options.get('unicode_results', False)
            self.encoding = options.get('encoding', 'utf-8')
        
        self.ops = DatabaseOperations(self)
        self.client = DatabaseClient(self)
        self.creation = DatabaseCreation(self)
        self.introspection = DatabaseIntrospection(self)
        #self.validation = BaseDatabaseValidation(self)
        self.data_types = DatabaseCreation.data_types
        self.connection = None
        self.autocommit = True

    def get_connection_params(self):
        settings_dict = self.settings_dict
        if not settings_dict['NAME']:
            from django.core.exceptions import ImproperlyConfigured
            raise ImproperlyConfigured(
                "settings.DATABASES is improperly configured. "
                "Please supply the NAME value.")
        conn_params = {
            'database': settings_dict['NAME'],
        }
        conn_params.update(settings_dict['OPTIONS'])
        if 'autocommit' in conn_params:
            self.autocommit = conn_params['autocommit']
            del conn_params['autocommit']
        if settings_dict['USER']:
            conn_params['user'] = settings_dict['USER']
        if settings_dict['PASSWORD']:
            conn_params['password'] = settings_dict['PASSWORD']
        if settings_dict['HOST']:
            conn_params['host'] = settings_dict['HOST']
        if settings_dict['PORT']:
            conn_params['port'] = settings_dict['PORT']
        return conn_params

    def get_new_connection(self, conn_params):
        connection = Database.connect(**conn_params,autocommit=self.autocommit)
        connection.setdecoding(Database.SQL_CHAR, encoding='unicode_escape')
        connection.setdecoding(Database.SQL_WCHAR, encoding='unicode_escape')
        connection.setencoding(encoding='unicode_escape',ctype=Database.SQL_WCHAR)
        self.connection = connection
        return self.connection
    
    def init_connection_state(self):
        pass

    def _set_autocommit(self, autocommit):
        pass

    def create_cursor(self,name):
        cursor = None
        if self.connection:
            cursor = self.connection.cursor()
        return CursorWrapper(cursor, self.driver_supports_utf8, self.encoding)

    def is_usable(self):
        return True

class CursorWrapper(object):
    """
    A wrapper around the pyodbc's cursor that takes in account a) some pyodbc
    DB-API 2.0 implementation and b) some common ODBC driver particularities.
    """
    binary_type = binary_type
    text_type = text_type

    def __init__(self, cursor, driver_supports_utf8, encoding=""):
        self.cursor = cursor
        self.driver_supports_utf8 = driver_supports_utf8
        self.last_sql = ''
        self.last_params = ()
        self.encoding = encoding

    def close(self):
        try:
            self.cursor.close()
        except Database.ProgrammingError:
            pass

    def format_sql(self, sql, n_params=None):

        # pyodbc uses '?' instead of '%s' as parameter placeholder.
        if n_params is not None:
            try:
                sql = sql % tuple('?' * n_params)
            except:
                #Todo checkout whats happening here
                pass
        else:
            if '%s' in sql:
                sql = sql.replace('%s', '?')
        if sys.version.startswith('3') and type(sql) is not str:
            #sql = sql.decode(self.encoding or sys.stdout.encoding)
            pass

        sql = sql.replace('%s', '?')
        return sql

    def format_params(self, params):
        fp = []

        for p in params:
            print(type(p))
            if isinstance(p, text_type):
                if p.endswith('+00:00') and len(p) == 25:
                    fp.append(p.replace('+00:00',''))
                else:
                    fp.append(p)
            elif isinstance(p, binary_type):
                if not self.driver_supports_utf8:
                    fp.append(p.decode(self.encoding).encode('utf-8'))
                else:
                    fp.append(p)
            elif isinstance(p, datetime.datetime):
                if not p:
                    fp.append(None)
                else:
                    fp.append(p.isoformat().replace('T',' '))
            elif isinstance(p, type(True)):
                if p:
                    fp.append(1)
                else:
                    fp.append(0)
            else:
                fp.append(p)
        return tuple(fp)

    def execute(self, sql, params=()):

        self.last_sql = sql
        sql = self.format_sql(sql, len(params))
        params = self.format_params(params)
        self.last_params = params

        try:
            return self.cursor.execute(sql, params)
        except IntegrityError:
            e = sys.exc_info()[1]
            raise utils.IntegrityError(*e.args)
        except DatabaseError:
            e = sys.exc_info()[1]
            raise utils.DatabaseError(*e.args)

    def executemany(self, sql, params_list):
        sql = self.format_sql(sql)
        # pyodbc's cursor.executemany() doesn't support an empty param_list
        if not params_list:
            if '?' in sql:
                return
        else:
            raw_pll = params_list
            params_list = [self.format_params(p) for p in raw_pll]

        try:
            return self.cursor.executemany(sql, params_list)
        except IntegrityError:
            e = sys.exc_info()[1]
            raise utils.IntegrityError(*e.args)
        except DatabaseError:
            e = sys.exc_info()[1]
            raise utils.DatabaseError(*e.args)

    def format_results(self, rows):
        """
        Decode data coming from the database if needed and convert rows to tuples
        (pyodbc Rows are not sliceable).
        """
        needs_utc = _DJANGO_VERSION >= 14 and settings.USE_TZ
        if not (needs_utc or not self.driver_supports_utf8):
            return tuple(rows)
        # FreeTDS (and other ODBC drivers?) don't support Unicode yet, so we
        # need to decode UTF-8 data coming from the DB
        fr = []
        for row in rows:
            if not self.driver_supports_utf8 and isinstance(row, binary_type):
                row = row.decode(self.encoding)

            elif needs_utc and isinstance(row, datetime.datetime):
                row = row.replace(tzinfo=timezone.utc)
            fr.append(row)
        return tuple(fr)

    def fetchone(self):
        row = self.cursor.fetchone()
        if row is not None:
            return self.format_results(row)
        return []

    def fetchmany(self, chunk):
        return [self.format_results(row) for row in self.cursor.fetchmany(chunk)]

    def fetchall(self):
        return [self.format_results(row) for row in self.cursor.fetchall()]

    def __getattr__(self, attr):
        if attr in self.__dict__:
            return self.__dict__[attr]
        return getattr(self.cursor, attr)

    def __iter__(self):
        return iter(self.cursor)


    # # MS SQL Server doesn't support explicit savepoint commits; savepoints are
    # # implicitly committed with the transaction.
    # # Ignore them.
    def savepoint_commit(self, sid):
        # if something is populating self.queries, include a fake entry to avoid
        # issues with tests that use assertNumQueries.
        if self.queries:
            self.queries.append({
                'sql': '-- RELEASE SAVEPOINT %s -- (because assertNumQueries)' % self.ops.quote_name(sid),
                'time': '0.000',
            })