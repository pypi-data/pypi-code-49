from . import timework as tw

from random import randint


@tw.timer()
def timer_demo_a(m):
    i = 0
    while i < 2 ** m:
        i += 1
    return i


@tw.timer(timeout=1)
def timer_demo_b(m):
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


@tw.iterative(3)
def iterative_demo_a(max_depth):
    i = 0
    while i < 2 ** max_depth:
        i += 1
    return i


@tw.iterative(3, history=5, key='depth')
def iterative_demo_b(depth):
    i = 0
    while i < 2 ** depth:
        i += 1
    return depth, i


def test_timer_a():
    for _ in range(10):
        d = randint(10, 25)
        x = timer_demo_a(d)
        assert x == 2 ** d


def test_timer_b():
    for _ in range(10):
        d = randint(10, 25)
        try:
            c = timer_demo_b(d)
        except tw.TimeError as e:
            assert e.message[:12] == 'timer_demo_b'
            assert e.result == 2 ** d
        else:
            assert c == 2 ** d


def test_limit():
    for _ in range(10):
        d = randint(15, 35)
        try:
            s = limit_demo(d)
        except tw.TimeError as e:
            assert isinstance(e, tw.TimeError)
        else:
            assert s == 2 ** d


def test_iterative_a():
    for _ in range(5):
        d = randint(10, 20)
        try:
            s = iterative_demo_a(max_depth=d)
        except tw.TimeError as e:
            assert e.result <= 2 ** d
            assert len(e.detail) == 1
            assert e.result == e.detail[-1]
        else:
            assert s == 2 ** d


def test_iterative_b():
    for _ in range(5):
        d = randint(10, 30)
        try:
            s = iterative_demo_b(depth=d)
        except tw.TimeError as e:
            assert e.result <= (d, 2 ** d)
            assert len(e.detail) == 5
            assert e.result == e.detail[-1]
        else:
            assert s == (d, 2 ** d)


def test_errors():
    try:
        timer_demo_b('2')
    except Exception as e:
        assert isinstance(e, TypeError)

    try:
        limit_demo('2')
    except Exception as e:
        assert isinstance(e, TypeError)

    try:
        iterative_demo_a('2')
    except Exception as e:
        assert isinstance(e, KeyError)

    try:
        limit_demo(max_depth='2')
    except Exception as e:
        assert isinstance(e, TypeError)
