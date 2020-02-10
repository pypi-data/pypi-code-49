# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from avatica import errors, types
from avatica.client import AvaticaClient
from avatica.connection import Connection
from avatica.errors import *  # noqa: F401,F403
from avatica.types import *  # noqa: F401,F403

__all__ = ['connect', 'apilevel', 'threadsafety', 'paramstyle'] + types.__all__ + errors.__all__


apilevel = "2.0"
"""
This module supports the `DB API 2.0 interface <https://www.python.org/dev/peps/pep-0249/>`_.
"""

threadsafety = 1
"""
Multiple threads can share the module, but neither connections nor cursors.
"""

paramstyle = 'qmark'
"""
Parmetrized queries should use the question mark as a parameter placeholder.
For example::
 cursor.execute("SELECT * FROM table WHERE id = ?", [my_id])
"""


def connect(url, max_retries=None, auth=None, **kwargs):
    """Connects to a Phoenix query server.
    :param url:
        URL to the Phoenix query server, e.g. ``http://localhost:8765/``
    :param autocommit:
        Switch the connection to autocommit mode.
    :param readonly:
        Switch the connection to readonly mode.
    :param max_retries:
        The maximum number of retries in case there is a connection error.
    :param cursor_factory:
        If specified, the connection's :attr:`~phoenixdb.connection.Connection.cursor_factory` is set to it.
    :param auth
        If specified a specific auth type will be used, otherwise connection will be unauthenticated
        Currently only HTTPDigestAuth is supported
    :returns:
        :class:`~phoenixdb.connection.Connection` object.
    """
    client = AvaticaClient(url, max_retries=max_retries, auth=auth)
    client.connect()
    return Connection(client, **kwargs)
