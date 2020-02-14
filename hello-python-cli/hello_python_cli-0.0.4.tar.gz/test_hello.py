import subprocess
import re

import pytest


@pytest.mark.int
def test_version():
    rc, out = subprocess.getstatusoutput('hello --version')
    assert out == '0.0.1'
    assert re.match(r'[0-9]+\.[0-9]+\.[0-9]', out)
    assert rc == 0


@pytest.mark.int
def test_help():
    rc, out = subprocess.getstatusoutput('hello --help')
    assert re.match('Usage', out)
    assert rc == 0


@pytest.mark.int
def test_noname():
    rc, out = subprocess.getstatusoutput('hello')
    assert rc == 0
    assert out == 'Hello world'


@pytest.mark.int
def test_lower():
    rc, out = subprocess.getstatusoutput('hello --lower Bob')
    assert rc == 0
    assert out == 'hello bob'
