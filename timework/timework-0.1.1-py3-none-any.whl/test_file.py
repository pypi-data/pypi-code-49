from . import timework as tw

r = tw.ResultHandler()


@tw.timer(r)
def timer_demo(m):
    i = 0
    while i < 2 ** m:
        i += 1
    return i


@tw.limit(3)
def limit_demo(m):
    i = 0
    while i < 2 ** m:
        i += 1
    return i


@tw.iterative(r, 3)
def iterative_demo(max_depth):
    i = 0
    while i < 2 ** max_depth:
        i += 1
    return max_depth, i


def test_timer():
    r.clean()
    timer_demo(10)
    timer_demo(25)
    assert len(r.value) == 2
    assert r.value[0] < r.value[1]


def test_limit_a():
    try:
        s = limit_demo(4)
    except Exception as e:
        assert isinstance(e, BaseException)
    else:
        assert s == 16


def test_limit_b():
    try:
        s = limit_demo(30)
    except Exception as e:
        assert isinstance(e, BaseException)
    else:
        assert s == 2 ** 30


def test_iterative_a():
    try:
        r.clean()
        iterative_demo(max_depth=4)
    except Exception as e:
        assert isinstance(e, BaseException)
    finally:
        assert len(r.value) == 4
        assert r.value[0] == (1, 2)
        assert r.value[-1][0] == 4


def test_iterative_b():
    try:
        r.clean()
        iterative_demo(max_depth=30)
    except Exception as e:
        assert isinstance(e, BaseException)
    finally:
        assert len(r.value) < 30
        assert r.value[0] == (1, 2)
        assert r.value[2] == (3, 8)
