import pytest
from scheduler_tools.PrefectPreferences import PrefectPreferences


def test_user_pref():
    pp = PrefectPreferences()


def test_given(data_dir):
    pp = PrefectPreferences(path=data_dir/"ssh.json")


def test_url(data_dir):
    pp = PrefectPreferences(path=data_dir/"ssh.json")
    assert pp.gateway_url == "slurm-master.corp.alleninstitute.org"


def test_username(data_dir):
    pp = PrefectPreferences(path=data_dir / "ssh.json")
    assert pp.username == "jamies"


def test_identity_file(data_dir):
    pp = PrefectPreferences(path=data_dir/"ssh.json")
    assert pp.identity_file

