# -*- coding: utf-8 -*-

import pytest
import tuxbuild.config

sample_token = "Q9qMlmkjkIuIGmEAw-Mf53i_qoJ8Z2eGYCmrNx16ZLLQGrXAHRiN2ce5DGlAebOmnJFp9Ggcq9l6quZdDTtrkw"
sample_url = "https://foo.bar.tuxbuild.com/v1"


def test_config_FileNotFoundError():
    with pytest.raises(FileNotFoundError):
        tuxbuild.config.Config(config_path="/nonexistent")


def test_config_token_from_env(monkeypatch):
    """ Set TUXBUILD_TOKEN in env and ensure it is used """
    monkeypatch.setenv("TUXBUILD_TOKEN", sample_token)
    c = tuxbuild.config.Config(config_path="/nonexistent")
    assert c.auth_token == sample_token
    assert c.kbapi_url == c.default_api_url
    assert c.get_auth_token() == c.auth_token
    assert c.get_kbapi_url() == c.kbapi_url
    assert c.get_tuxbuild_env() == c.tuxbuild_env


def test_config_token_and_url_from_env(monkeypatch):
    """ Set TUXBUILD_TOKEN in env and ensure it is used """
    monkeypatch.setenv("TUXBUILD_TOKEN", sample_token)
    monkeypatch.setenv("TUXBUILD_URL", sample_url)
    c = tuxbuild.config.Config(config_path="/nonexistent")
    assert c.auth_token == sample_token
    assert c.kbapi_url == sample_url
    assert c.get_auth_token() == c.auth_token
    assert c.get_kbapi_url() == c.kbapi_url
    assert c.get_tuxbuild_env() == c.tuxbuild_env


def test_config_file_minimum(tmp_path):
    contents = """
[default]
token={}
""".format(
        sample_token
    )
    config_file = tmp_path / "config.ini"
    config_file.write_text(contents)
    c = tuxbuild.config.Config(config_path=config_file)
    assert c.auth_token == sample_token
    assert c.kbapi_url == c.default_api_url
    assert c.get_auth_token() == c.auth_token
    assert c.get_kbapi_url() == c.kbapi_url
    assert c.get_tuxbuild_env() == c.tuxbuild_env


def test_config_file_default(tmp_path):
    contents = """
[default]
token={}
api_url={}
""".format(
        sample_token, sample_url
    )
    config_file = tmp_path / "config.ini"
    config_file.write_text(contents)
    c = tuxbuild.config.Config(config_path=config_file)
    assert c.auth_token == sample_token
    assert c.kbapi_url == sample_url
    assert c.get_auth_token() == c.auth_token
    assert c.get_kbapi_url() == c.kbapi_url
    assert c.get_tuxbuild_env() == c.tuxbuild_env


def test_config_file_non_default(monkeypatch, tmp_path):
    contents = """
[default]
token=foo
api_url=bar
[foobar]
token={}
api_url={}
""".format(
        sample_token, sample_url
    )
    monkeypatch.setenv("TUXBUILD_ENV", "foobar")
    config_file = tmp_path / "config.ini"
    config_file.write_text(contents)
    c = tuxbuild.config.Config(config_path=config_file)
    assert c.auth_token == sample_token
    assert c.kbapi_url == sample_url
    assert c.get_auth_token() == c.auth_token
    assert c.get_kbapi_url() == c.kbapi_url
    assert c.get_tuxbuild_env() == c.tuxbuild_env
