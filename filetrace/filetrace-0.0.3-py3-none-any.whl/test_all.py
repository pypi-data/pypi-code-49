# Check that the package version can be obtained and evalutes to 'True'

from filetrace import __version__
from filetrace.tracer import FileRunTracer


class OPTIONS:
    live = False
    output = None
    exclude = ""


def test_something():
    assert __version__


def test_bin_true():
    FileRunTracer(OPTIONS, ["true"]).run()


def test_bin_true_fork():
    FileRunTracer(OPTIONS, ["bash", "-c", "/bin/true"]).run()


def test_bin_true_fork_new():
    FileRunTracer(OPTIONS, ["bash", "-c", '"/bin/true; cat /dev/null"']).run()
