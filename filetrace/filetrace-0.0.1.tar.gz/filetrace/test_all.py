# Check that the package version can be obtained and evalutes to 'True'

from filetrace import __version__
from filetrace.tracer import FileRunTracer


def test_something():
    assert __version__


def test_bin_true():
    FileRunTracer(["true"]).run()
