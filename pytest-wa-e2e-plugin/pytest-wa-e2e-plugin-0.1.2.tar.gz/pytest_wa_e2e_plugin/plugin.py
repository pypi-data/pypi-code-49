
import pytest
import logging
import time

from pytest_wa_e2e_plugin.utils import WAEndToEnd, parse_yaml_data_file


logging.basicConfig(level=logging.INFO)


def pytest_addoption(parser):
    parser.addoption(
        "--data-file", required=True, action="store",
        help="File System Path to the file containing the input data for the test run."
    )


@pytest.fixture(scope="session")
def wa_e2e_yaml_data(request):
    """ Returns the yaml parsed data from the input data-file
    """
    data_file_path = request.config.getoption("--data-file")
    yield parse_yaml_data_file(data_file_path)


@pytest.fixture
def test_run_instance(wa_e2e_yaml_data):
    """ Creates a WhatsApp EndToEnd instance based on the yaml input data file
    """
    yield WAEndToEnd(wa_e2e_yaml_data["wa_e2e"]["whatsapp_bot_number"])

