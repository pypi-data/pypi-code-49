# Check that the package version can be obtained and evalutes to 'True'

from filetrace import __version__
from filetrace.tracer import FileRunTracer


def test_something():
    assert __version__


def test_bin_true():
    FileRunTracer(["true"]).run()


def test_bin_true_fork():
    FileRunTracer(["bash", "-c", "/bin/true"]).run()


def test_bin_true_fork_new():
    FileRunTracer(["bash", "-c", '"/bin/true; cat /dev/null"']).run()
