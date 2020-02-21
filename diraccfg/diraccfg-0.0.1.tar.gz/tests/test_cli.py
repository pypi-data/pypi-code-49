from __future__ import unicode_literals

import io
import json
import os
import random
import subprocess

import pytest

import diraccfg.__main__


EXAMPLE_CFG_FILE = os.path.join(os.path.dirname(__file__), 'releases.cfg')


@pytest.fixture
def argparse_test(monkeypatch, capsys):
  def run_command(args, expected_code=0, stdin=None):
    monkeypatch.setattr("sys.argv", args)
    if stdin is not None:
      try:
        stdin = io.StringIO(stdin)
      except TypeError:
        # stdin needs decoding to unicode in Python 2
        stdin = io.StringIO(stdin.decode())
      monkeypatch.setattr('sys.stdin', stdin)
    with pytest.raises(SystemExit) as excinfo:
      diraccfg.__main__.parseArgs()
    assert excinfo.value.code == expected_code
    captured = capsys.readouterr()
    return captured.out, captured.err

  return run_command


@pytest.mark.parametrize("args,expected_code", [(["diraccfg", "-h"], 0), (["diraccfg", "--help"], 0)])
def test_help(args, expected_code, argparse_test):
  stdout, stderr = argparse_test(args, expected_code)
  assert "usage:" in stdout
  assert stderr == ""
  subprocess_output = subprocess.check_output(args, stderr=subprocess.STDOUT)
  assert subprocess_output.decode() == stdout


def test_as_json_no_fn(argparse_test):
  args = ["diraccfg", "as-json"]
  stdout, stderr = argparse_test(args, 2)
  assert stdout == ""
  assert "usage:" in stderr


def test_as_json_bad_fn(argparse_test):
  args = ["diraccfg", "as-json", "this file doesn't exist!!!"]
  stdout, stderr = argparse_test(args, 1)
  assert stdout == ""
  assert "ERROR:" in stderr
  assert "does not exist" in stderr


def test_as_json(argparse_test):
  args = ["diraccfg", "as-json", EXAMPLE_CFG_FILE]
  stdout, stderr = argparse_test(args, 0)
  assert stderr == ""
  with open(EXAMPLE_CFG_FILE, 'rt') as fp:
    assert "Here is where the releases go:" in fp.read()
  assert "Here is where the releases go:" not in stdout
  result = json.loads(stdout)
  assert result['Releases']['v6r22']['DIRACOS'] == 'v1r2'  # pylint: disable=unsubscriptable-object


def test_sort_versions_with_fn(argparse_test):
  args = ["diraccfg", "sort-versions", EXAMPLE_CFG_FILE]
  stdout, stderr = argparse_test(args, 2)
  assert stdout == ""
  assert "usage:" in stderr


def test_sort_versions_with_bad_input(argparse_test):
  args = ["diraccfg", "sort-versions"]
  stdout, stderr = argparse_test(args, 3, stdin='sadasdsa')
  assert stdout == ""
  assert "Failed to parse" in stderr


@pytest.mark.parametrize("releases", [
    [],
    ["v1r2"],
    ["v2r0", "v1r10", "v1r2"],
    ["v2r0", "v1r10", "v1r10-pre10", "v1r2"],
    ["v2r0", "v1r10p0", "v1r10-pre10", "v1r2"],
    ["v2r0", "v1r10", "v1r10p0-pre10", "v1r2"],
    ["v2r0", "v1r10p0", "v1r10p0-pre10", "v1r2"],
    ["v2r0", "v1r10p1-pre10", "v1r10", "v1r10p0-pre10", "v1r2"],
    ["v200r100", "v200r1", "v1r200"],
])
def test_sort_versions(releases, argparse_test):
  expected_releases = [r for r in releases if "pre" not in r]
  for i in range(100):
    random.seed(i)
    cmd_input = releases[:]
    random.shuffle(cmd_input)
    stdout, stderr = argparse_test(["diraccfg", "sort-versions"],
                                   stdin=json.dumps(cmd_input))
    assert stdout == json.dumps(expected_releases) + "\n"
    assert json.loads(stdout) == expected_releases
    assert stderr == ""


@pytest.mark.parametrize("releases,expected_out,expected_errs", [
    (["integration"], [], []),
    (["bad-name"], [], ["bad-name"]),
    (["devel"], [], []),
    (["integration", "devel"], [], []),
    (["integration", "devel", "master"], [], []),
    (["v1r2", "integration", "master", "v1r3"], ["v1r3", "v1r2"], []),
    (["v1r3", "devel", "bad-name", "v1r2"], ["v1r3", "v1r2"], ["bad-name"]),
    (["bad-name", "v1r2", "other-name"], ["v1r2"], ["bad-name", "other-name"]),
])
def test_sort_unexpected(releases, expected_out, expected_errs, argparse_test):
  for i in range(100):
    random.seed(i)
    cmd_input = releases[:]
    random.shuffle(cmd_input)
    stdout, stderr = argparse_test(["diraccfg", "sort-versions"],
                                   stdin=json.dumps(cmd_input))
    assert stdout == json.dumps(expected_out) + "\n"
    assert json.loads(stdout) == expected_out
    if expected_errs:
      for expected_err in expected_errs:
        assert expected_err in stderr
    else:
      assert stderr == ""


@pytest.mark.parametrize("releases", [
    [],
    ["v1r2"],
    ["v2r0", "v1r10", "v1r2"],
    ["v2r0", "v1r10", "v1r10-pre10", "v1r2"],
    ["v2r0", "v1r10p0", "v1r10-pre10", "v1r2"],
    ["v2r0", "v1r10", "v1r10p0-pre10", "v1r2"],
    ["v2r0", "v1r10p0", "v1r10p0-pre10", "v1r2"],
    ["v2r0", "v1r10p1-pre10", "v1r10", "v1r10p0-pre10", "v1r2"],
    ["v200r100", "v200r1", "v1r200"],
])
def test_sort_versions_pre_releases(releases, argparse_test):
  for i in range(100):
    random.seed(i)
    cmd_input = releases[:]
    random.shuffle(cmd_input)
    stdout, stderr = argparse_test(
        ["diraccfg", "sort-versions", "--allow-pre-releases"],
        stdin=json.dumps(cmd_input)
    )
    assert stdout == json.dumps(releases) + "\n"
    assert json.loads(stdout) == releases
    assert stderr == ""
