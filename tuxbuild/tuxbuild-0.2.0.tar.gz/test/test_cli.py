# -*- coding: utf-8 -*-

import click
from click.testing import CliRunner
import os
import pytest
import tuxbuild.cli

sample_token = "Q9qMlmkjkIuIGmEAw-Mf53i_qoJ8Z2eGYCmrNx16ZLLQGrXAHRiN2ce5DGlAebOmnJFp9Ggcq9l6quZdDTtrkw"
sample_url = "https://foo.bar.tuxbuild.com/v1"


def test_get_config_happy_path(tmp_path):
    """ Test calling get_config with a working config file """
    contents = """
[default]
token={}
api_url={}
""".format(
        sample_token, sample_url
    )
    config_file = tmp_path / "config.ini"
    config_file.write_text(contents)
    c = tuxbuild.cli.get_config(config_path=config_file)
    assert c.get_auth_token() == sample_token
    assert c.get_kbapi_url() == sample_url


def test_get_config_FileNotFoundError(tmp_path):
    """ Test calling get_config with a missing file """
    with pytest.raises(click.exceptions.ClickException):
        tuxbuild.cli.get_config(config_path="/nonexistent")


def test_get_config_PermissionError(tmp_path):
    """ Test calling get_config with an unreadable file """
    contents = """
[default]
token={}
api_url={}
""".format(
        sample_token, sample_url
    )
    config_file = tmp_path / "config.ini"
    config_file.write_text(contents)
    # Make config_file unreadable
    os.chmod(config_file, 0o000)

    uid = os.geteuid()
    if uid == 0:
        # Uh oh, we are running as root
        # Change to some user so that PermissionError will be raised
        os.seteuid(12345)
    with pytest.raises(click.exceptions.ClickException):
        tuxbuild.cli.get_config(config_path=config_file)
    if os.geteuid() != uid:
        # If we changed our uid, change it back
        os.seteuid(uid)


def test_get_config_NoSectionError(tmp_path):
    """ Test calling get_config with no default section """
    contents = """
[XYZ]
token={}
api_url={}
""".format(
        sample_token, sample_url
    )
    config_file = tmp_path / "config.ini"
    config_file.write_text(contents)
    with pytest.raises(click.exceptions.ClickException):
        tuxbuild.cli.get_config(config_path=config_file)


def test_get_config_TokenNotFound(tmp_path):
    """ Test calling get_config with a missing token """
    contents = """
[default]
api_url={}
""".format(
        sample_token, sample_url
    )
    config_file = tmp_path / "config.ini"
    config_file.write_text(contents)
    with pytest.raises(click.exceptions.ClickException):
        tuxbuild.cli.get_config(config_path=config_file)


def test_usage():
    """ Test running cli() with no arguments """
    runner = CliRunner()
    result = runner.invoke(tuxbuild.cli.cli, [])
    assert result.exit_code == 0
    assert "Usage" in result.output
    assert "Commands" in result.output


def test_build_no_args():
    """ Test calling build() with no options """
    runner = CliRunner()
    result = runner.invoke(tuxbuild.cli.build, [])
    assert result.exit_code == 2
    assert "Usage" in result.output
    assert "help" in result.output


def test_build_usage():
    """ Test calling build() with --help """
    runner = CliRunner()
    result = runner.invoke(tuxbuild.cli.build, ["--help"])
    assert result.exit_code == 0
    assert "Usage" in result.output
    assert "--toolchain" in result.output
    assert "--git-repo TEXT" in result.output
