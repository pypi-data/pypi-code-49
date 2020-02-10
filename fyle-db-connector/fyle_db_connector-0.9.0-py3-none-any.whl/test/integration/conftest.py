import logging
import os
import sqlite3

import pytest

from test.common.utilities import get_mock_fyle, fyle_connect

from fyle_db_connector import FyleExtractConnector

logger = logging.getLogger(__name__)


@pytest.fixture
def mock_fyle():
    """
    make mock_fyle connection
    :return: mock_fyle
    """
    return get_mock_fyle()


@pytest.fixture(scope='module')
def fyle():
    """
    make fyle_connection
    :return: fyle_connection
    """
    return fyle_connect()


@pytest.fixture
def dbconn():
    """
    connect to a database
    :return: database connection
    """
    SQLITE_DB_FILE = '/tmp/test_fyle.db'
    if os.path.exists(SQLITE_DB_FILE):
        os.remove(SQLITE_DB_FILE)
    return sqlite3.connect(SQLITE_DB_FILE, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)


@pytest.fixture
def fec(fyle, dbconn):
    """
    make FyleExtractConnection
    :param fyle: fyle_connection
    :param dbconn: database_connection
    :return: FyleExtractConnector response
    """
    res = FyleExtractConnector(fyle_sdk_connection=fyle, dbconn=dbconn)
    res.create_tables()
    return res
