import logging

from test.common.utilities import (dbconn_table_num_rows, dbconn_table_row_dict, dict_compare_keys, get_mock_fyle_empty)
from fyle_db_connector.extract import FyleExtractConnector

logger = logging.getLogger(__name__)


def test_employees(fec):
    """
    Test Extract Employees
    :param fec: fyle extract connection
    :return: None
    """
    dbconn = fec._FyleExtractConnector__dbconn
    fyle = fec._FyleExtractConnector__connection
    ids = fec.extract_employees()
    fyle_data = fyle.Employees.get_all()
    db_data = dbconn_table_row_dict(dbconn, 'fyle_extract_employees')
    assert dict_compare_keys(db_data, fyle_data[0]) == [], 'db table has some columns that fyle doesnt'
    assert dbconn_table_num_rows(dbconn, 'fyle_extract_employees') == len(fyle_data), 'row count mismatch'
    assert len(ids) == 3, 'return value messed up'


def test_settlements(fec):
    """
    Test Extract Settlements
    :param fec: fyle extract connection
    :return: None
    """
    dbconn = fec._FyleExtractConnector__dbconn
    fyle = fec._FyleExtractConnector__connection
    ids = fec.extract_settlements()
    fyle_data = fyle.Settlements.get_all()
    db_data = dbconn_table_row_dict(dbconn, 'fyle_extract_settlements')
    assert dict_compare_keys(db_data, fyle_data[0]) == [], 'db table has some columns that fyle doesnt'
    assert dbconn_table_num_rows(dbconn, 'fyle_extract_settlements') == len(fyle_data), 'row count mismatch'
    assert len(ids) == 5, 'return value messed up'


def test_reimbursements(fec):
    """
    Test Extract Reimbursements
    :param fec: fyle extract connection
    :return: None
    """
    dbconn = fec._FyleExtractConnector__dbconn
    fyle = fec._FyleExtractConnector__connection
    ids = fec.extract_reimbursements()
    fyle_data = fyle.Reimbursements.get_all()
    db_data = dbconn_table_row_dict(dbconn, 'fyle_extract_reimbursements')
    assert dict_compare_keys(db_data, fyle_data[0]) == [], 'db table has some columns that fyle doesnt'
    assert dbconn_table_num_rows(dbconn, 'fyle_extract_reimbursements') == len(fyle_data), 'row count mismatch'
    assert len(ids) == 3, 'return value messed up'


def test_expenses(fec):
    """
    Test Extract Expenses
    :param fec: fyle extract connection
    :return: None
    """
    dbconn = fec._FyleExtractConnector__dbconn
    fyle = fec._FyleExtractConnector__connection
    ids = fec.extract_expenses(extract_custom_fields=False)
    fyle_data = fyle.Expenses.get_all()
    db_data = dbconn_table_row_dict(dbconn, 'fyle_extract_expenses')
    assert dict_compare_keys(db_data, fyle_data[0]) == [], 'db table has some columns that fyle doesnt'
    assert dbconn_table_num_rows(dbconn, 'fyle_extract_expenses') == len(fyle_data), 'row count mismatch'
    assert len(ids) == 3, 'return value messed up'


def test_corporate_credit_card_expenses(fec):
    """
    Test Extract CorporateCreditCardExpenses
    :param fec: fyle extract connection
    :return: None
    """
    dbconn = fec._FyleExtractConnector__dbconn
    fyle = fec._FyleExtractConnector__connection
    ids = fec.extract_corporate_credit_card_expenses()
    fyle_data = fyle.CorporateCreditCardExpenses.get_all()
    db_data = dbconn_table_row_dict(dbconn, 'fyle_extract_corporate_credit_card_expenses')
    assert dict_compare_keys(db_data, fyle_data[0]) == [], 'db table has some columns that fyle doesnt'
    assert dbconn_table_num_rows(dbconn, 'fyle_extract_corporate_credit_card_expenses') == len(
        fyle_data), 'row count mismatch'
    assert len(ids) == 3, 'return value messed up'


def test_advances(fec):
    """
    Test Extract Advances
    :param fec: fyle extract connection
    :return: None
    """
    dbconn = fec._FyleExtractConnector__dbconn
    fyle = fec._FyleExtractConnector__connection
    ids = fec.extract_advances()
    fyle_data = fyle.Advances.get_all()
    db_data = dbconn_table_row_dict(dbconn, 'fyle_extract_advances')
    assert dict_compare_keys(db_data, fyle_data[0]) == [], 'db table has some columns that fyle doesnt'
    assert dbconn_table_num_rows(dbconn, 'fyle_extract_advances') == len(
        fyle_data), 'row count mismatch'
    assert len(ids) == 4, 'return value messed up'


def test_advance_requests(fec):
    """
    Test Extract AdvanceRequests
    :param fec: fyle extract connection
    :return: None
    """
    dbconn = fec._FyleExtractConnector__dbconn
    fyle = fec._FyleExtractConnector__connection
    ids = fec.extract_advance_requests()
    fyle_data = fyle.AdvanceRequests.get_all()
    db_data = dbconn_table_row_dict(dbconn, 'fyle_extract_advance_requests')
    assert dict_compare_keys(db_data, fyle_data[0]) == [], 'db table has some columns that fyle doesnt'
    assert dbconn_table_num_rows(dbconn, 'fyle_extract_advance_requests') == len(
        fyle_data), 'row count mismatch'
    assert len(ids) == 4, 'return value messed up'


def test_categories(fec):
    """
    Test Extract Categories
    :param fec: fyle extract connection
    :return: None
    """
    dbconn = fec._FyleExtractConnector__dbconn
    fyle = fec._FyleExtractConnector__connection
    ids = fec.extract_categories()
    fyle_data = fyle.Categories.get()['data']
    db_data = dbconn_table_row_dict(dbconn, 'fyle_extract_categories')
    assert dict_compare_keys(db_data, fyle_data[0]) == [], 'db table has some columns that fyle doesnt'
    assert dbconn_table_num_rows(dbconn, 'fyle_extract_categories') == len(fyle_data), 'row count mismatch'
    assert len(ids) == 26, 'return value messed up'


def test_projects(fec):
    """
    Test Extract Projects
    :param fec: fyle extract connection
    :return: None
    """
    dbconn = fec._FyleExtractConnector__dbconn
    fyle = fec._FyleExtractConnector__connection
    ids = fec.extract_projects()
    fyle_data = fyle.Projects.get()['data']
    db_data = dbconn_table_row_dict(dbconn, 'fyle_extract_projects')
    assert dict_compare_keys(db_data, fyle_data[0]) == [], 'db table has some columns that fyle doesnt'
    assert dbconn_table_num_rows(dbconn, 'fyle_extract_projects') == len(fyle_data), 'row count mismatch'
    assert len(ids) == 4, 'return value messed up'


def test_cost_centers(fec):
    """
    Test Extract CostCenters
    :param fec: fyle extract connection
    :return: None
    """
    dbconn = fec._FyleExtractConnector__dbconn
    fyle = fec._FyleExtractConnector__connection
    fyle_extract = FyleExtractConnector(fyle_sdk_connection=fyle, dbconn=dbconn)
    ids = fyle_extract.extract_cost_centers()
    fyle_data = fyle.CostCenters.get()['data']
    db_data = dbconn_table_row_dict(dbconn, 'fyle_extract_cost_centers')
    assert dict_compare_keys(db_data, fyle_data[0]) == [], 'db table has some columns that fyle doesnt'
    assert dbconn_table_num_rows(dbconn, 'fyle_extract_cost_centers') == len(fyle_data), 'row count mismatch'
    assert len(ids) == 11, 'return value messed up'


def test_empty(dbconn):
    """
    Test Extract Empty
    :param dbconn: sqlite db connection
    :return: None
    """
    fyle = get_mock_fyle_empty()
    res = FyleExtractConnector(fyle_sdk_connection=fyle, dbconn=dbconn)
    res.create_tables()
    assert res.extract_expenses() == []
