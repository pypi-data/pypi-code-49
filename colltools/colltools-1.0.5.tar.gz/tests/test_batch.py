import pytest
from colltools import batch


def test_empty_iterable():
    for i in batch([], 5):
        pytest.xfail('Batching empty list should not provide items')
    else:
        assert True


def test_step_over_iterable():
    results = []
    for i in batch(range(5), 10):
        results.append(i)
    assert results == [[0, 1, 2, 3, 4]]


def test_step_overflow():
    results = []
    for i in batch(range(10), 4):
        results.append(i)
    assert results == [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [8, 9]
    ]


def test_exact_batch_size_match():
    results = []
    for i in batch(range(10), 5):
        results.append(i)
    assert results == [
        [0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9]
    ]


def test_invalid_batch_size():
    with pytest.raises(TypeError, match='Step has to be an integer. <class \'str\'> given.'):
        next(batch(range(10), 'string'))


def test_negative_batch_size():
    with pytest.raises(IndexError, match='Step has to be larger than 0, -1 given.'):
        next(batch(range(10), -1))


def test_zero_batch_size():
    with pytest.raises(IndexError, match='Step has to be larger than 0, 0 given.'):
        next(batch(range(10), 0))


def test_not_iterable():
    with pytest.raises(TypeError, match='\'object\' object is not iterable'):
        next(batch(object(), 2))
