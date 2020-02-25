import logging
from time import time

import pytest

from pyconsoler.output import get_time_stamp

_LOGGER = logging.getLogger(__name__)


def test_get_time_stamp():
    stmp = get_time_stamp()
    assert ":" in stmp
    assert "-" in stmp


def test_get_time_stamp_no_time():
    stmp = get_time_stamp(add_time=False)
    assert ":" not in stmp
    assert "-" in stmp


def test_get_time_stamp_other_separators():
    stmp = get_time_stamp(date_sep="*", time_sep="_", date_time_sep=" and ")
    assert ":" not in stmp
    assert "-" not in stmp

    assert "*" in stmp
    assert "_" in stmp
    assert " and " in stmp


def test_get_time_stamp_sec_input():
    secs = time()
    stmp = get_time_stamp(time_sec=secs)
    assert ":" in stmp
    assert "-" in stmp
