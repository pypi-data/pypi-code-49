"""
Load Unit Tests
"""
import logging

from test.common.utilities import dbconn_get_load_object_by_id, dbconn_get_load_object_by_batch_id

logger = logging.getLogger(__name__)


def test_fyle_load_tpa_export_batches(flc, dbconn):
    """
    tpa_export_batches load Unit Test
    """
    assert dbconn_get_load_object_by_id(dbconn, 'fyle_load_tpa_export_batches',
                                        'exbtCGWmKieHip'), 'fyle load_tpa_export id should not exist'
    sql = open('./test/common/mock_db_load.sql').read()
    dbconn.executescript(sql)

    response = flc.load_tpa_exports()
    assert response == ['exbtCGWmKieHip', 'exbt0EdBt3ojED', 'exbtCGWmKieHip', 'exbt0EdBt3ojED'], 'fyle load_tpa_export id not matching'


def test_fyle_load_tpa_export_batch_lineitems(flc, dbconn):
    """
    tpa_export_batch_lineitems load Unit Test
    """
    assert dbconn_get_load_object_by_batch_id(dbconn, 'fyle_load_tpa_export_batch_lineitems',
                                              'exbtCGWmKieHip'), 'fyle load_tpa_export_batch_lineitems  id should not exist'

    sql = open('./test/common/mock_db_load.sql').read()
    dbconn.executescript(sql)

    response = flc.load_tpa_export_batch(batch_id='exbtCGWmKieHip')
    assert response == ['exbtCGWmKieHip'], 'fyle load_tpa_export_batch_lineitems not matching'
