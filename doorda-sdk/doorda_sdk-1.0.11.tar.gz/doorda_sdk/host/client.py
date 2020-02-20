import requests
from requests.auth import HTTPBasicAuth
import atexit
from doorda_sdk.util.decorators import timeout
import logging
import doorda_sdk
from doorda_sdk.util import common
from doorda_sdk.util.exc import (
    ProgrammingError,
    DatabaseError,
    OperationalError,
    NotConnectedError,
)  # noqa
import base64
import signal
from doorda_sdk.util.permissions_tree import Node
import warnings

try:  # Python 3
    import urllib.parse as urlparse
except ImportError:  # Python 2
    import urlparse


# PEP 249 module globals
apilevel = "2.0"
threadsafety = 2  # Threads may share the module and connections.
paramstyle = (
    "pyformat"
)  # Python extended format codes, e.g. ...WHERE name=%(name)s

_logger = logging.getLogger(__name__)
_escaper = common.ParamEscaper()
__version__ = doorda_sdk.__version__


def connect(*args, **kwargs):
    return Connection(*args, **kwargs)


class Connection:
    def __init__(self, *args, **kwargs):

        self._args = args
        self._kwargs = kwargs

    def cursor(self):
        return Cursor(*self._args, **self._kwargs)

    def close(self):
        pass

    def commit(self):
        pass


class Cursor(common.DBAPICursor):
    def __init__(
        self,
        username,
        password,
        catalog="default",
        schema="default",
        session_props=None,
    ):
        super(Cursor, self).__init__()
        self._host = "host.doorda.com"
        self.__port = 443
        self.username = username
        self.catalog = catalog
        self.schema = schema
        self.password = password
        self.__protocol = "https"
        self.__source = "doorda-python-client %s" % __version__
        self._requests_kwargs = {
            "auth": HTTPBasicAuth(self.username, self.password)
        }
        self._session_props = (
            session_props if session_props is not None else {}
        )
        self._arraysize = 1
        self._state = self._STATE_NONE
        self._requests_session = requests

        def exit_handler():

            """
            Safely cancel query on exit

            """
            if self._state == self._STATE_RUNNING:
                try:
                    self.cancel()
                    _logger.info("Exiting")
                except ProgrammingError:
                    pass

        signal.signal(signal.SIGTERM, exit_handler)
        signal.signal(signal.SIGINT, exit_handler)
        atexit.register(exit_handler)

    def _reset_state(self):
        """Reset state about the previous query in
        preparation for running another query"""
        super(Cursor, self)._reset_state()
        if self._state == 1:
            self.cancel()
        self._nextUri = None
        self._columns = None
        self._state = self._STATE_NONE

    @property
    def description(self):
        """This read-only attribute is a sequence of 7-item sequences.
        Each of these sequences contains
        information describing one result column:
        - name
        - type_code
        - display_size (None in current implementation)
        - internal_size (None in current implementation)
        - precision (None in current implementation)
        - scale (None in current implementation)
        - null_ok (always True in current implementation)
        The ``type_code`` can be interpreted by comparing it
        to the Type Objects specified in the section below.
        """
        # Sleep until we're done or we got the columns
        self._fetch_while(
            lambda: self._columns is None
            and self._state not in (self._STATE_NONE, self._STATE_FINISHED)
        )
        if self._columns is None:
            return None
        return [
            # name, type_code, display_size, internal_size,
            # precision, scale, null_ok
            (col["name"], col["type"], None, None, None, None, True)
            for col in self._columns
        ]

    def execute(self, operation, parameters=None):
        """Prepare and execute a database operation (query or command).
                Return values are not defined.
        """
        headers = {
            "X-Presto-Catalog": self.catalog,
            "X-Presto-Schema": self.schema,
            "X-Presto-Source": self.__source,
            "X-Presto-User": self.username,
        }

        if self._session_props:
            headers["X-Presto-Session"] = ",".join(
                "{}={}".format(propname, propval)
                for propname, propval in self._session_props.items()
            )
        # Prepare statement
        if parameters is None:
            sql = operation
        else:
            sql = operation % _escaper.escape_args(parameters)
        sql = sql.strip()
        sql = sql.replace(";", "") if sql.endswith(";") else sql
        self._reset_state()

        self._state = self._STATE_RUNNING
        url = urlparse.urlunparse(
            (
                self.__protocol,
                "{}:{}".format(self._host, self.__port),
                "/v1/statement",
                None,
                None,
                None,
            )
        )
        _logger.info("%s", sql)
        _logger.debug("Headers: %s", headers)
        response = self._requests_session.post(
            url,
            data=sql.encode("utf-8"),
            headers=headers,
            **self._requests_kwargs
        )
        self._process_response(response)

    def cancel(self):
        if self._state == self._STATE_NONE:
            raise ProgrammingError("No query yet")
        if self._nextUri is None:
            assert (
                self._state == self._STATE_FINISHED
            ), "Should be finished if nextUri is None"
            return

        response = self._requests_session.delete(
            self._nextUri, **self._requests_kwargs
        )
        if response.status_code != requests.codes.no_content:
            fmt = "Unexpected status code after cancel {}\n{}"
            raise OperationalError(
                fmt.format(response.status_code, response.content)
            )

        self._state = self._STATE_FINISHED

    def poll(self):
        """Poll for and return the raw status data
        provided by the Presto REST API.
        :returns: dict -- JSON status information
                  or `None` if the query is done
        :raises: ``ProgrammingError`` when no query has been started
        .. note::
            This is not a part of DB-API.
        """
        if self._state == self._STATE_NONE:
            raise ProgrammingError("No query yet")
        if self._nextUri is None:
            assert (
                self._state == self._STATE_FINISHED
            ), "Should be finished if nextUri is None"
            return None
        response = self._requests_session.get(
            self._nextUri, **self._requests_kwargs
        )
        self._process_response(response)
        return response.json()

    def _fetch_more(self):
        """Fetch the next URI and update state"""
        self._process_response(
            self._requests_session.get(self._nextUri, **self._requests_kwargs)
        )

    def _decode_binary(self, rows):
        # As of Presto 0.69, binary data is returned as the
        # varbinary type in base64 format
        # This function decodes base64 data in place
        for i, col in enumerate(self.description):
            if col[1] == "varbinary":
                for row in rows:
                    if row[i] is not None:
                        row[i] = base64.b64decode(row[i])

    def _process_response(self, response):
        """Given the JSON response from Presto's REST API,
        update the internal state with the next
        URI and any data from the response
        """
        # TODO handle HTTP 503
        if response.status_code != requests.codes.ok:
            fmt = "Unexpected status code {}\n{}"
            raise OperationalError(
                fmt.format(response.status_code, response.content)
            )

        response_json = response.json()
        _logger.debug("Got response %s", response_json)
        assert (
            self._state == self._STATE_RUNNING
        ), "Should be running if processing response"
        self._nextUri = response_json.get("nextUri")
        self._columns = response_json.get("columns")
        if "X-Presto-Clear-Session" in response.headers:
            propname = response.headers["X-Presto-Clear-Session"]
            self._session_props.pop(propname, None)
        if "X-Presto-Set-Session" in response.headers:
            propname, propval = response.headers["X-Presto-Set-Session"].split(
                "=", 1
            )
            self._session_props[propname] = propval
        if "data" in response_json:
            assert self._columns
            new_data = response_json["data"]
            self._decode_binary(new_data)
            self._data += map(tuple, new_data)
        if "nextUri" not in response_json:
            self._state = self._STATE_FINISHED
        if "error" in response_json:
            raise DatabaseError(response_json["error"])

    def show_catalogs(self):
        """
        Returns a list of catalogs that user has access to.

        """
        self.execute("SHOW CATALOGS")
        return self.fetchall()

    def show_schema(self, catalog=""):
        if catalog:
            pass
        elif not catalog and self.catalog:
            catalog = self.catalog
        else:
            raise ProgrammingError("Catalog not valid")
        self.execute("SHOW SCHEMAS FROM {catalog}".format(catalog=catalog))
        return self.fetchall()

    def show_tables(self, catalog="", schema=""):
        query = "SHOW TABLES FROM {catalog}.{schema}"
        if catalog and schema:
            self.execute(query.format(catalog=catalog, schema=schema))
            return self.fetchall()
        elif self.catalog and self.schema:
            self.execute(
                query.format(catalog=self.catalog, schema=self.schema)
            )
            return self.fetchall()
        else:
            raise ProgrammingError("Catalog/Schema not valid")

    @property
    def col_names(self):
        """
        Returns a list of column names IF a query has been executed

        """
        assert self.description, "Column names not available"
        if self.description:
            return [col[0] for col in self.description]

    @property
    def col_types(self):
        """
        Returns a list of column names mapped to
        column types IF a query has been executed
        """
        assert self.description, "Column types not available"
        if self.description:
            return {col[0]: col[1] for col in self.description}

    def table_stats(self, catalog, schema, table):
        """
        Returns number of rows in a table

        """
        if catalog and schema and table:
            fmt = "SHOW STATS FOR {catalog_name}.{schema_name}.{table_name}"
            self.execute(
                fmt.format(
                    catalog_name=catalog, schema_name=schema, table_name=table
                )
            )
            results = self.fetchall()
            return {"number_of_rows": results[-1][-3]}

    @timeout(5, "Cursor not connected")
    def is_connected(self):
        """
        Checks connection with DoordaHost.

        """
        headers = {
            "X-Presto-Catalog": self.catalog,
            "X-Presto-Schema": self.schema,
            "X-Presto-Source": self.__source,
            "X-Presto-User": self.username,
        }

        url = urlparse.urlunparse(
            (
                self.__protocol,
                "{}:{}".format(self._host, self.__port),
                "/v1/statement",
                None,
                None,
                None,
            )
        )
        response = self._requests_session.post(
            url,
            data="SELECT 1".encode("utf-8"),
            headers=headers,
            **self._requests_kwargs
        )
        if response.status_code != requests.codes.ok:
            raise NotConnectedError("Cursor not connected")
        return True

    def permissions(self):
        """
        Example:

        |Catalogs   | Schemas   | Table Names
        __________________________________________
        |-- DoordaBiz_Snapshot
        |           |-- DoordaBiz_Snapshot
        |           |           |-- register_company_profile
        |-- DoordaBiz_Ledger
        |           |-- DoordaBiz_Ledger
        |           |           |-- register_company_profile_ledger

        :return:
        """
        warnings.warn("Experimental Function", UserWarning)
        catalogs = self.show_catalogs()
        root = Node("")
        root.children = [
            Node(str(catalog[0]))
            for catalog in catalogs
            if catalog[0] != "system"
        ]

        for cat in root.children:
            schemas = self.show_schema(cat.value)
            cat.children = [
                Node(schema[0])
                for schema in schemas
                if schema[0] != "information_schema"
            ]
            for sche in cat.children:
                tables = self.show_tables(cat.value, sche.value)
                sche.children = [Node(str(table[0])) for table in tables]
        return root
