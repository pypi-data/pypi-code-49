import copy
import os

from unimatrix.lib import rdbms


ENGINE_MAPPING = {
    'postgresql': 'django.db.backends.postgresql_psycopg2',
    'mysql': 'django.db.backends.mysql',
    'sqlite': 'django.db.backends.sqlite3'
}


def setup(env=None):
    """Inspects environment variables to set up the ``default``
    database connection in a Django project.

    The following environment variables are supported:

    - ``DB_ENGINE`` (Required): specifies the database engine. Valid
      choices are ``postgresql``, ``mysql`` and ``sqlite``. If the
      ``DB_ENGINE`` environment variable is not specified, then all
      other ``DB_*`` variables are ignored and no database connection
      is configured.
    - ``DB_HOST`` (Optional): configures the hostname or IP address of
      the database server. This variable is ignored when ``DB_ENGINE`` is
      ``sqlite``.
    - ``DB_PORT`` (Optional): configures the port to which a connection
      is made by the database connector. If no value is specified, then
      this variable defaults to the well-known port for a given database
      engine, being ``5432`` for ``postgresql`` and ``3306`` for ``mysql``.
    - ``DB_NAME`` (Optional): specifies the name of the database for
      ``postgresql`` and ``mysql``. For ``sqlite``, the path on the local
      filesystem of the database; or ``:memory:`` for an in-memory
      database.
    - ``DB_USERNAME`` (Optional): the name of database user to connect
      with.
    - ``DB_PASSWORD`` (Optional): the password to authenticate as the
      database user.
    - ``DB_CONNECTION_MAX_AGE`` (Optional): the maximum age of a
      connection in the pool in seconds. Defaults to ``3600``.
    - ``DB_AUTOCOMMIT`` (Optional): indicates if the connection should
      operate in autocommit mode, if the engine supports it, where
      ``'1'`` evaluates to ``True`` and ``'0'`` evaluates to ``False``.

    Args:
        env: a dictionary holding the environment variables. If
            `env` is ``None``, then it defaults to :attr:`os.environ`.

    Returns:
        :class:`dict`
    """
    databases = {}
    connections = rdbms.load_config(
        env=copy.deepcopy(env or os.environ))
    if not connections:
        return {}

    # The 'self' connection is the default connection in
    # Django.
    if 'self' in connections:
        connections['default'] = connections.pop('self')

    # Construct the Django database connections from the parsed
    # configuration.
    for alias in dict.keys(connections):
        connection = connections[alias]
        databases[alias] = {
            'HOST': connection.host,
            'PORT': connection.port,
            'NAME': connection.name,
            'USER': connection.username,
            'PASSWORD': connection.password,
            'PORT': connection.port,
            'ENGINE': ENGINE_MAPPING[connection.engine],
            'CONN_MAX_AGE': connection.max_age,
            'AUTOCOMMIT': connection.autocommit
        }

        # Remove empty keys.
        for k in list(dict.keys(databases[alias])):
            if databases[alias].get(k) is not None:
                continue
            del databases[alias][k]

    return databases


#: Django ``DATABASES`` setting loaded from environment variables. This
#: module-level constant holds the result of :func:`setup`.
DATABASES = setup()
