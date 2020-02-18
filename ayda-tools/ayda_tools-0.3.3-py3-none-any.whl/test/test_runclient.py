from ayda_tools.client import run_client


def test_key_file_is_set_to_prod_key_file(mocker):
    mocker.patch.object(run_client, "AnalyticToolClient")
    mocker.patch.object(run_client, "ServerConnection")

    run_client.run()
