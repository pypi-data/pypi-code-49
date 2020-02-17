from . import timework as tw


def assert_timer(e):
    assert e[:10] == 'time used:'


@tw.timer(out=assert_timer)
def timer_demo():
    i = 0
    while i < 5000:
        i += 1


@tw.limit(1.5)
def limit_demo():
    i = 0
    while True:
        i += 1


@tw.progressive(2)
def progressive_demo(i, max_depth):
    for _ in range(max_depth):
        i += 1
    return i


def test_timer():
    timer_demo()


def test_limit():
    try:
        limit_demo()
    except Exception as e:
        assert str(e)[:10] == 'limit_demo'


def test_progressive1():
    try:
        progressive_demo(5, max_depth=100)
    except Exception as e:
        rc = str(e)
        assert int(rc) == 105


def test_progressive2():
    try:
        progressive_demo(0, max_depth=10**9)
    except Exception as e:
        rc = str(e)
        assert rc.isdigit()


def test_progressive3():
    try:
        progressive_demo(0, max_depth='i')
    except Exception as e:
        assert isinstance(e, BaseException)
