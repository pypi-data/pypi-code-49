import logging
import os
import sqlite3
from os import path

import pytest

from test.common.utilities import get_mock_fyle
from fyle_db_connector.extract import FyleExtractConnector
from fyle_db_connector.load import FyleLoadConnector

logger = logging.getLogger(__name__)


@pytest.fixture
def fyle():
    return get_mock_fyle()


@pytest.fixture
def dbconn():
    SQLITE_DB_FILE = '/tmp/test_fyle.db'
    if os.path.exists(SQLITE_DB_FILE):
        os.remove(SQLITE_DB_FILE)
    conn = sqlite3.connect(SQLITE_DB_FILE, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    return conn


@pytest.fixture
def fec(fyle, dbconn):
    res = FyleExtractConnector(fyle_sdk_connection=fyle, dbconn=dbconn)
    res.create_tables()
    return res


@pytest.fixture
def flc(fyle, dbconn):
    res = FyleLoadConnector(fyle_sdk_connection=fyle, dbconn=dbconn)
    res.create_tables()
    basepath = path.dirname(__file__)
    sqlpath = path.join(basepath, '../common/mock_db_load.sql')
    sql = open(sqlpath, 'r').read()
    dbconn.executescript(sql)
    return res
