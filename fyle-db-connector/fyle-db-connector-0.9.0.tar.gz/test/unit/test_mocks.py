import pytest

import sqlite3
import logging
from test.common.utilities import dict_compare_keys, dbconn_table_num_rows

logger = logging.getLogger(__name__)


def test_fyle_mock_setup(fyle):
    """
    Testing mock data
    """
    logger.info('Testing mock data')

    assert fyle.Expenses.get_all()[0]['id'] == 'txNx96Gutp1X', 'fyle mock setup is broken'


def test_dbconn_mock_setup(dbconn):
    """
    Testing mock dbconn
    """
    logger.info('Testing mock dbconn')

    with pytest.raises(sqlite3.OperationalError) as e:
        rows = dbconn_table_num_rows(dbconn, 'fyle_extract_employees')


def test_fec_mock_setup(fec):
    """
    Testing Extract connector with mock instance
    """
    logger.info('Testing Extract connector with mock instance')

    # python magic to access private variable for testing db state
    dbconn = fec._FyleExtractConnector__dbconn
    assert dbconn_table_num_rows(dbconn, 'fyle_extract_employees') == 0, 'Unclean db'


def test_flc_mock_setup(flc, dbconn):
    """
    Testing Load Connector with mock instance
    """
    logger.info('Testing Load Connector with mock instance')

    flc.create_tables()
    sqlpath = './test/common/mock_db_load.sql'
    sql = open(sqlpath, 'r').read()
    dbconn.executescript(sql)

    assert dbconn_table_num_rows(dbconn, 'fyle_load_tpa_export_batches') == 2, 'Unclean db'
    assert dbconn_table_num_rows(dbconn, 'fyle_load_tpa_export_batch_lineitems') == 4, 'Unclean db'


def test_dict_compare():
    """
    Testing dict compare function
    """
    logger.info('Testing dict compare function')

    d1 = {
        'k1': 'xxx', 'k2': 2, 'k3': [1, 2], 'k4': {'k41': [2], 'k42': {'k421': 20}}
    }
    d2 = {
        'k1': 'xyx', 'k3': [1, 2], 'k4': {'k42': {'k421': 20}}
    }
    d3 = {
        'k1': 'xyz', 'k3': [3, 2], 'k4': {'k42': {'k421': 40}}
    }
    assert dict_compare_keys(d1, d2) == ['->k2', '->k4->k41'], 'not identifying diff properly'
    assert dict_compare_keys(d2, d3) == [], 'should return no diff'
