from unittest.mock import mock_open

from ayda_tools.client import run_client


def test_key_file_is_set_to_prod_key_file(mocker):
    open_mock = mock_open(read_data="data\ndata2\nMULTIPLE_JOB\ndata4\ndata5")
    mocker.patch("builtins.open", open_mock)
    mocker.patch.object(run_client, "AnalyticToolClient")
    mocker.patch.object(run_client, "ServerConnection")

    run_client.run()

    open_mock.assert_called_once_with("/home/cboden/.ayda/clientkey", "r")
