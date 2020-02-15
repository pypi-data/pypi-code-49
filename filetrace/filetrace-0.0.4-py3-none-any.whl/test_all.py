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
    RESULT = ["/etc/ld.so.cache", "/usr/bin/true", "/usr/lib/libc.so.6"]
    assert RESULT == FileRunTracer(OPTIONS, ["true"]).run()
