import timework as tw


def assert_timer(e):
    assert e[:10] == 'time used:'


@tw.timer(out=assert_timer)
def timer_demo():
    i = 0
    while True:
        i += 1


@tw.limit(1.5)
def limit_demo():
    i = 0
    while True:
        i += 1


@tw.progressive(2)
def progressive_demo(i, max_depth):
    while i < max_depth:
        i += 1
    return max_depth + i


def test_timer():
    timer_demo()


def test_limit():
    try:
        limit_demo()
    except Exception as e:
        assert str(e)[:10] == 'limit_demo'


def test_progressive1():
    try:
        progressive_demo(max_depth=10)
    except Exception as e:
        rc = str(e)
        assert int(rc) == 20


def test_progressive2():
    try:
        progressive_demo(max_depth=10 ** 6)
    except Exception as e:
        rc = str(e)
        assert int(rc) > 10 ** 6


def test_progressive3():
    try:
        progressive_demo(max_depth='i')
    except Exception as e:
        assert isinstance(e, BaseException)
