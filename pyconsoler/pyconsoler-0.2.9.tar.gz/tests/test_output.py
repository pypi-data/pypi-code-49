import logging

import pytest

from pyconsoler.output import print_waiting_countdown, prt

_LOGGER = logging.getLogger(__name__)


@pytest.mark.asyncio
async def test_print_waiting_countdown():
    await print_waiting_countdown(4)


@pytest.mark.parametrize("_input", [1, False, None, "test", {"test": 10}])
@pytest.mark.parametrize("_color", [None, "YELLOW"])
def test_prt_single(_input, capsys, _color):
    prt(_input, color=_color)
    _output = capsys.readouterr()

    lines = _output.out.split("\n")
    assert len(lines) == 2

    print(_output)


@pytest.mark.parametrize("_input", [(1, 2, 3), ["abc", 1, 2], ("abs", "abc")])
@pytest.mark.parametrize("_color", [None, "YELLOW"])
def test_prt_multiple(_input, capsys, _color):
    prt(*_input, color=_color)
    _output = capsys.readouterr()

    lines = _output.out.split("\n")
    assert len(lines) > 2
