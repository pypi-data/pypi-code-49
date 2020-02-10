import logging
from test.common.utilities import (dict_compare_keys, get_mock_fyle_empty)
from fyle_db_connector.extract import FyleExtractConnector

logger = logging.getLogger(__name__)


def test_employees(fyle, mock_fyle):
    """
    Test fyle_db_connector Extract employees
    :param fyle: fyle_extract instance
    :param mock_fyle: mock instance
    :return: None
    """
    data = fyle.Employees.get_all()
    mock_data = mock_fyle.Employees.get_all()

    assert dict_compare_keys(data[0], mock_data[0]) == [], 'real fyle has stuff that mock_fyle doesnt'
    assert dict_compare_keys(mock_data[0], data[0]) == [], 'mock_fyle has stuff that real fyle doesnt'


def test_settlements(fyle, mock_fyle):
    """
    Test fyle_db_connector Extract settlements
    :param fyle: fyle_extract instance
    :param mock_fyle: mock instance
    :return: None
    """
    data = fyle.Settlements.get_all()
    mock_data = mock_fyle.Settlements.get_all()

    assert dict_compare_keys(data[0], mock_data[0]) == [], 'real fyle has stuff that mock_fyle doesnt'
    assert dict_compare_keys(mock_data[0], data[0]) == [], 'mock_fyle has stuff that real fyle doesnt'


def test_reimbursements(fyle, mock_fyle):
    """
    Test fyle_db_connector Extract reimbursements
    :param fyle: fyle_extract instance
    :param mock_fyle: mock instance
    :return: None
    """
    data = fyle.Reimbursements.get_all()
    mock_data = mock_fyle.Reimbursements.get_all()

    assert dict_compare_keys(data[0], mock_data[0]) == [], 'real fyle has stuff that mock_fyle doesnt'
    assert dict_compare_keys(mock_data[0], data[0]) == [], 'mock_fyle has stuff that real fyle doesnt'


def test_expenses(fyle, mock_fyle):
    """
    Test fyle_db_connector Extract expenses
    :param fyle: fyle_extract instance
    :param mock_fyle: mock instance
    :return: None
    """
    data = fyle.Expenses.get_all()
    mock_data = mock_fyle.Expenses.get_all()

    assert dict_compare_keys(data[0], mock_data[0]) == [], 'real fyle has stuff that mock_fyle doesnt'
    assert dict_compare_keys(mock_data[0], data[0]) == [], 'mock_fyle has stuff that real fyle doesnt'


def test_advances(fyle, mock_fyle):
    """
    Test fyle_db_connector Extract advances
    :param fyle: fyle_extract instance
    :param mock_fyle: mock instance
    :return: None
    """
    data = fyle.Advances.get_all()
    mock_data = mock_fyle.Advances.get_all()
    assert dict_compare_keys(data[0], mock_data[0]) == [], 'real fyle has stuff that mock_fyle doesnt'
    assert dict_compare_keys(mock_data[0], data[0]) == [], 'mock_fyle has stuff that real fyle doesnt'


def test_advance_requests(fyle, mock_fyle):
    """
    Test fyle_db_connector Extract advance_requests
    :param fyle: fyle_extract instance
    :param mock_fyle: mock instance
    :return: None
    """
    data = fyle.AdvanceRequests.get_all()
    mock_data = mock_fyle.AdvanceRequests.get_all()
    assert dict_compare_keys(data[0], mock_data[0]) == [], 'real fyle has stuff that mock_fyle doesnt'
    assert dict_compare_keys(mock_data[0], data[0]) == [], 'mock_fyle has stuff that real fyle doesnt'


def test_projects(fyle, mock_fyle):
    """
    Test fyle_db_connector Extract projects
    :param fyle: fyle_extract instance
    :param mock_fyle: mock instance
    :return: None
    """
    data = fyle.Projects.get()['data']
    mock_data = mock_fyle.Projects.get()['data']
    assert dict_compare_keys(data[0], mock_data[0]) == [], 'real fyle has stuff that mock_fyle doesnt'
    assert dict_compare_keys(mock_data[0], data[0]) == [], 'mock_fyle has stuff that real fyle doesnt'


def test_cost_centers(fyle, mock_fyle):
    """
    Test fyle_db_connector Extract cost_centers
    :param fyle: fyle_extract instance
    :param mock_fyle: mock instance
    :return: None
    """
    data = fyle.CostCenters.get()['data']
    mock_data = mock_fyle.CostCenters.get()['data']
    assert dict_compare_keys(data[0], mock_data[0]) == [], 'real fyle has stuff that mock_fyle doesnt'
    assert dict_compare_keys(mock_data[0], data[0]) == [], 'mock_fyle has stuff that real fyle doesnt'


def test_categories(fyle, mock_fyle):
    """
    Test fyle_db_connector Extract categories
    :param fyle: fyle_extract instance
    :param mock_fyle: mock instance
    :return: None
    """
    data = fyle.Categories.get()['data']
    mock_data = mock_fyle.Categories.get()['data']
    assert dict_compare_keys(data[0], mock_data[0]) == [], 'real fyle has stuff that mock_fyle doesnt'
    assert dict_compare_keys(mock_data[0], data[0]) == [], 'mock_fyle has stuff that real fyle doesnt'


def test_corporate_card_expenses(fyle, mock_fyle):
    """
    Test fyle_db_connector Extract corporate_credit_card_expenses
    :param fyle: fyle_extract instance
    :param mock_fyle: mock instance
    :return: None
    """
    data = fyle.CorporateCreditCardExpenses.get_all()
    mock_data = mock_fyle.CorporateCreditCardExpenses.get_all()
    assert dict_compare_keys(data[0], mock_data[0]) == [], 'real fyle has stuff that mock_fyle doesnt'
    assert dict_compare_keys(mock_data[0], data[0]) == [], 'mock_fyle has stuff that real fyle doesnt'


def test_empty(dbconn):
    """
    Test fyle_db_connector Extract empty_test
    :param dbconn: database connection
    :return: None
    """
    fyle = get_mock_fyle_empty()
    res = FyleExtractConnector(fyle_sdk_connection=fyle, dbconn=dbconn)
    res.create_tables()
    assert res.extract_expenses() == []
