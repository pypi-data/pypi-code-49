import pytest

from todo_extractor import todo_extractor


class MockedSubprocessReturn:
    def __init__(self, returncode):
        self.returncode = returncode


def test_get_grep(mocker):
    process = mocker.patch("subprocess.run")
    process.return_value = MockedSubprocessReturn(1)

    assert todo_extractor.grep_cmd("search")[0] == "grep"


def test_get_ripgrep(mocker):
    process = mocker.patch("subprocess.run")
    process.return_value = MockedSubprocessReturn(0)

    assert todo_extractor.grep_cmd("search")[0] == "rg"
