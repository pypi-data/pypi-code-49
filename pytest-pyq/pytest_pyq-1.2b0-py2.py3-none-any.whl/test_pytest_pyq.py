import pytest
import pytest_pyq
from pyq import q as _q


def test_q1(q):
    assert q.get('.').count == 0
    q.foo = 42
    assert q.get('.').count == 1


def test_q2(q):
    assert q.get('.').count == 0


def test_console_size(testdir):
    test_code = r"""
    console = []

    def test_console_1(q):
        dim = q(r'\c')
        console.append(dim)
        assert list(dim) == [25, 80]


    def test_console_2(q):
        q(r'\c 123 321')


    def test_console_3(q):
        assert q(r'\c') == console[0]
    """

    testdir.makepyfile(test_code)
    result = testdir.runpytest('-v')
    result.stdout.fnmatch_lines([
        "*::test_console_1 PASSED*",
        "*::test_console_2 PASSED*",
        "*::test_console_3 PASSED*",
    ])
    assert result.ret == 0


def test_float_precision(testdir):
    test_code = r"""
    precision = []

    def test_precision_1(q):
        p = q(r'\P')
        precision.append(p)
        assert int(p) == 7


    def test_precision_2(q):
        q(r'\P 11')


    def test_precision_3(q):
        assert q(r'\P') == precision[0]
    """

    testdir.makepyfile(test_code)
    result = testdir.runpytest('-v')
    result.stdout.fnmatch_lines([
        "*::test_precision_1 PASSED*",
        "*::test_precision_2 PASSED*",
        "*::test_precision_3 PASSED*",
    ])
    assert result.ret == 0


@pytest.fixture(scope="module")
def a(q_module):
    return 'a'


def test_a(a):
    assert a == 'a'


@pytest.fixture(scope="session")
def b(q_session):
    return 'b'


def test_b(b):
    assert b == 'b'
