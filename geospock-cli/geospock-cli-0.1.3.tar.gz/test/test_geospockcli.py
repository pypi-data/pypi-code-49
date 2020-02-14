# Copyright (c) 2014-2020 GeoSpock Ltd.

from geospock_cli.geospockcli import *
from click.testing import CliRunner


def test_get_user_list():
    runner = CliRunner()
    result = runner.invoke(run, ["account-list", "--profile", "local", "--pageSize", "10", "--pageIndex", "1"])
    jsonoutput = json.loads(result.output)
    items = jsonoutput["accounts"]
    assert len(items) > 0
    if len(items) > 0:
        assert items[0]["id"] is not None


def test_all_datasets():
    runner = CliRunner()
    result = runner.invoke(run,
                           ["dataset-list", "--profile", "local", "--pageSize", "10", "--pageIndex", "0"])
    jsonoutput = json.loads(result.output)
    items = jsonoutput["datasets"]
    assert len(items) > 0
    if len(items) > 0:
        assert items[0]["dataset"]["id"] is not None


def test_invite_and_delete_user():
    runner = CliRunner()
    result = runner.invoke(run,
                           ["account-invite", "--profile", "local", "--email", 'auth0.testuser+clivetest@geospock.com',
                            "--role", "USER"])
    jsonoutput = json.loads(result.output)
    test_user_id = jsonoutput["newAccount"]["id"]
    assert jsonoutput["newAccount"]["email"] == "auth0.testuser+clivetest@geospock.com"

    result = runner.invoke(run, ["account-delete", "--profile", "local", "--account-id", test_user_id])
    jsonoutput = json.loads(result.output)
    assert jsonoutput["deletedAccount"] == test_user_id
