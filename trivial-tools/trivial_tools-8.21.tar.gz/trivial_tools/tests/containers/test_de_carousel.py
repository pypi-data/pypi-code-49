# -*- coding: utf-8 -*-
"""

    Тесты двусторонней карусели

"""
# сторонние модули
import pytest

# модули проекта
from trivial_tools.containers.class_de_carousel import DeCarousel


def test_creation():
    """
    Проверка создания
    """
    with pytest.raises(ValueError):
        DeCarousel()

    d = DeCarousel(window=2)
    assert d.window == 2
    assert len(d) == 0
    assert d.get_contents() == []
    assert d.extract() == []

    d = DeCarousel([1, 2, 3])
    assert len(d) == 3
    assert d.window == 3
    assert d.get_contents() == [1, 2, 3]
    assert d.extract() == [1, 2, 3]
    assert d.extract() == []

    d = DeCarousel([1, 2, 3], window=2)
    assert len(d) == 2
    assert d.window == 2
    assert d.get_contents() == [2, 3]
    assert d.extract() == [2, 3]
    assert d.extract() == []


def test_contains():
    """
    Проверка наличия элемента
    """
    d = DeCarousel(window=2)
    assert 0 not in d
    assert 4 not in d

    d.populate([1, 2, 3])
    assert d.get_contents() == [2, 3]

    assert 0 not in d
    assert 1 not in d
    assert 2 in d
    assert 3 in d
    assert 4 not in d


def test_len():
    """
    Проверка измерения длины
    """
    maxlen = 5
    d = DeCarousel(window=maxlen)
    for i in range(1, 10):
        d.push(i)
        assert len(d) == i if i < maxlen else maxlen
    assert len(d) == maxlen


def test_get_contents():
    """
    Не должно влиять на внутренности
    """
    d = DeCarousel([1, 2, 3])
    assert d.get_contents() == [1, 2, 3]
    assert d._data == [1, 2, 3]
    assert d._data == d.get_contents()

    d = DeCarousel([1, 2, 3], window=2)
    assert d.get_contents() == [2, 3]
    assert d._data == [3, 2]
    assert d._data != d.get_contents()


def test_str():
    """
    Проверка текстового представления
    """
    d = DeCarousel(window=4)
    assert str(d) == 'DeCarousel([], window=4)'

    d = DeCarousel([1, 2, 3])
    assert str(d) == 'DeCarousel([1, 2, 3], window=3)'

    d = DeCarousel([1, 2, 3], window=2)
    assert str(d) == 'DeCarousel([2, 3], window=2)'


def test_str_long():
    """
    Проверка текстового представления
    """
    d = DeCarousel(window=40)
    assert str(d) == 'DeCarousel([], window=40)'

    d = DeCarousel(range(100), window=40)
    assert str(d) == 'DeCarousel([60, 61, 62, ..., 97, 98, 99], len=40, window=40)'


def test_repr():
    """
    Проверка текстового представления
    """
    d = DeCarousel(window=3)
    assert repr(d) == 'DeCarousel([NULL, NULL, NULL], window=3)'

    d = DeCarousel(range(100), window=3)
    assert repr(d) == 'DeCarousel([97, 98, 99], window=3)'


def test_repr_long():
    """
    Проверка текстового представления
    """
    d = DeCarousel(window=40)
    assert repr(d) == 'DeCarousel([NULL, NULL, NULL, ..., NULL, NULL, NULL], len=0, window=40)'

    d = DeCarousel(range(100), window=40)
    assert repr(d) == 'DeCarousel([60, 61, 62, ..., 97, 98, 99], len=40, window=40)'


def test_push():
    """
    Проверка добавления элемента
    """
    d = DeCarousel(window=3, sentinel=None)
    assert d.get_contents() == []
    assert len(d) == 0

    x = d.push(1)
    assert d.get_contents() == [1]
    assert x is None
    assert len(d) == 1

    x = d.push(2)
    assert d.get_contents() == [1, 2]
    assert x is None
    assert len(d) == 2

    x = d.push(3)
    assert d.get_contents() == [1, 2, 3]
    assert x is None
    assert len(d) == 3

    x = d.push(4)
    assert d.get_contents() == [2, 3, 4]
    assert x == 1
    assert len(d) == 3

    x = d.push(5)
    assert d.get_contents() == [3, 4, 5]
    assert x == 2
    assert len(d) == 3

    x = d.push(6)
    assert d.get_contents() == [4, 5, 6]
    assert x == 3
    assert len(d) == 3


def test_append():
    """
    Проверка добавления элемента
    """
    d = DeCarousel(window=4)
    assert len(d) == 0

    d.append(1)
    assert d.get_contents() == [1]
    assert len(d) == 1
    assert d.left == 1
    assert d.right == 1

    d.append(2)
    assert d.get_contents() == [1, 2]
    assert len(d) == 2
    assert d.left == 1
    assert d.right == 2

    d.append(3)
    assert d.get_contents() == [1, 2, 3]
    assert len(d) == 3
    assert d.left == 1
    assert d.right == 3

    d.append(4)
    assert d.get_contents() == [1, 2, 3, 4]
    assert len(d) == 4
    assert d.left == 1
    assert d.right == 4

    d.append(5)
    assert d.get_contents() == [2, 3, 4, 5]
    assert len(d) == 4
    assert d.left == 2
    assert d.right == 5

    d.append(6)
    assert d.get_contents() == [3, 4, 5, 6]
    assert len(d) == 4
    assert d.left == 3
    assert d.right == 6

    d.append(7)
    assert d.get_contents() == [4, 5, 6, 7]
    assert len(d) == 4
    assert d.left == 4
    assert d.right == 7

    d.append(8)
    assert d.get_contents() == [5, 6, 7, 8]
    assert len(d) == 4
    assert d.left == 5
    assert d.right == 8

    d.append(9)
    assert d.get_contents() == [6, 7, 8, 9]
    assert len(d) == 4
    assert d.left == 6
    assert d.right == 9


def test_appendleft():
    """
    Проверка добавления элемента
    """
    d = DeCarousel(window=4, sentinel=None)
    assert len(d) == 0

    d.appendleft(1)
    assert d.get_contents() == [1]
    assert d.left == 1
    assert d.right == 1

    d.appendleft(2)
    assert d.get_contents() == [2, 1]
    assert d.left == 2
    assert d.right == 1

    d.appendleft(3)
    assert d.get_contents() == [3, 2, 1]
    assert d.left == 3
    assert d.right == 1

    d.appendleft(4)
    assert d.get_contents() == [4, 3, 2, 1]
    assert d.left == 4
    assert d.right == 1

    d.appendleft(5)
    assert d.get_contents() == [5, 4, 3, 2]
    assert d.left == 5
    assert d.right == 2

    d.appendleft(6)
    assert d.get_contents() == [6, 5, 4, 3]
    assert d.left == 6
    assert d.right == 3

    d.appendleft(7)
    assert d.get_contents() == [7, 6, 5, 4]
    assert d.left == 7
    assert d.right == 4

    d.appendleft(8)
    assert d.get_contents() == [8, 7, 6, 5]
    assert d.left == 8
    assert d.right == 5

    d.appendleft(9)
    assert d.get_contents() == [9, 8, 7, 6]
    assert d.left == 9
    assert d.right == 6


def test_pop():
    """
    Проверка извлечения элемента
    """
    d = DeCarousel([1, 2, 3, 4, 5, 6, 7, 8, 9], window=4)
    assert d.get_contents() == [6, 7, 8, 9]
    assert d.left == 6
    assert d.right == 9

    x = d.pop()
    assert x == 9
    assert d.left == 6
    assert d.right == 8

    x = d.pop()
    assert x == 8
    assert d.left == 6
    assert d.right == 7

    x = d.pop()
    assert x == 7
    assert d.left == 6
    assert d.right == 6

    x = d.pop()
    assert x == 6
    assert d.left is None
    assert d.right is None

    with pytest.raises(IndexError):
        d.pop()

    assert len(d) == 0


def test_popleft():
    """
    Проверка извлечения элемента
    """
    d = DeCarousel([1, 2, 3, 4, 5, 6, 7, 8, 9], window=4)
    assert d.get_contents() == [6, 7, 8, 9]
    assert d.left == 6
    assert d.right == 9

    x = d.popleft()
    assert x == 6
    assert d.left == 7
    assert d.right == 9

    x = d.popleft()
    assert x == 7
    assert d.left == 8
    assert d.right == 9

    x = d.popleft()
    assert x == 8
    assert d.left == 9
    assert d.right == 9

    x = d.popleft()
    assert x == 9
    assert d.left is None
    assert d.right is None

    with pytest.raises(IndexError):
        d.popleft()

    assert len(d) == 0


def test_resize():
    """
    Проверка изменения размера
    """
    d = DeCarousel([1, 2, 3], window=2)
    assert len(d) == 2
    assert d.window == 2
    assert d.get_contents() == [2, 3]

    d.resize(5)

    d.push(4)
    d.push(5)

    assert len(d) == 4
    assert d.window == 5
    assert d.get_contents() == [2, 3, 4, 5]

    d.push(6)

    assert len(d) == 5
    assert d.window == 5
    assert d.get_contents() == [2, 3, 4, 5, 6]

    d.resize(2)

    assert len(d) == 2
    assert d.window == 2
    assert d.get_contents() == [5, 6]


def test_resize_empty():
    """
    Проверка изменения размера пустой карусели
    """
    d = DeCarousel(window=2)
    assert d.window == 2
    assert repr(d) == 'DeCarousel([NULL, NULL], window=2)'

    d.resize(5)
    assert d.window == 5
    assert repr(d) == 'DeCarousel([NULL, NULL, NULL, NULL, NULL], window=5)'

    d.resize(3)
    assert d.window == 3
    assert repr(d) == 'DeCarousel([NULL, NULL, NULL], window=3)'


def test_no_resize():
    """
    Проверка изменения размера при том же значении
    """
    d = DeCarousel(window=2)
    assert d.window == 2

    d.resize(d.window)
    assert d.window == 2


def test_iter():
    """
    Проверка итерирования по карусели
    """
    base = [1, 2, 3]
    d = DeCarousel(base, window=4)
    for ref, value in zip(base, d):
        assert ref == value

    # убедимся, что не сломали список
    assert base == [1, 2, 3]


def test_getitem_int():
    """
    Проверка обращения к элементу (целое как индекс)
    """
    d = DeCarousel(window=4)

    with pytest.raises(IndexError):
        assert d[0]

    with pytest.raises(IndexError):
        # noinspection PyTypeChecker
        assert d['test']

    d.push(1)
    assert d[0] == 1
    assert d[-1] == 1

    with pytest.raises(IndexError):
        assert d[2]

    d.push(2)
    assert d[0] == 1
    assert d[1] == 2
    assert d[-1] == 2
    assert d[-2] == 1

    d.push(3)
    assert d[0] == 1
    assert d[1] == 2
    assert d[2] == 3
    assert d[-1] == 3
    assert d[-2] == 2
    assert d[-3] == 1

    d.push(4)
    assert d[0] == 1
    assert d[1] == 2
    assert d[2] == 3
    assert d[3] == 4
    assert d[-1] == 4
    assert d[-2] == 3
    assert d[-3] == 2
    assert d[-4] == 1

    d.push(5)
    assert d[0] == 2
    assert d[1] == 3
    assert d[2] == 4
    assert d[3] == 5
    assert d[-1] == 5
    assert d[-2] == 4
    assert d[-3] == 3
    assert d[-4] == 2

    d.push(6)
    assert d[0] == 3
    assert d[1] == 4
    assert d[2] == 5
    assert d[3] == 6
    assert d[-1] == 6
    assert d[-2] == 5
    assert d[-3] == 4
    assert d[-4] == 3

    d.push(7)
    assert d[0] == 4
    assert d[1] == 5
    assert d[2] == 6
    assert d[3] == 7
    assert d[-1] == 7
    assert d[-2] == 6
    assert d[-3] == 5
    assert d[-4] == 4

    d.push(8)
    assert d[0] == 5
    assert d[1] == 6
    assert d[2] == 7
    assert d[3] == 8
    assert d[-1] == 8
    assert d[-2] == 7
    assert d[-3] == 6
    assert d[-4] == 5


def test_getitem_slice():
    """
    Проверка обращения к элементу (срез как индекс)
    """
    d = DeCarousel(window=4)

    assert d[:] == []

    for i in range(1, 9):
        d.push(i)

    assert d[0] == 5
    assert d[1] == 6
    assert d[2] == 7
    assert d[3] == 8

    assert d[:] == [5, 6, 7, 8]

    assert d[:4] == [5, 6, 7, 8]
    assert d[:3] == [5, 6, 7]
    assert d[:2] == [5, 6]
    assert d[:1] == [5]

    assert d[1:] == [6, 7, 8]
    assert d[2:] == [7, 8]
    assert d[3:] == [8]
    assert d[4:] == []

    d.push(9)

    assert d[:] == [6, 7, 8, 9]

    assert d[:4] == [6, 7, 8, 9]
    assert d[:3] == [6, 7, 8]
    assert d[:2] == [6, 7]
    assert d[:1] == [6]

    assert d[1:] == [7, 8, 9]
    assert d[2:] == [8, 9]
    assert d[3:] == [9]
    assert d[4:] == []

    d.push(10)

    assert d[:] == [7, 8, 9, 10]

    assert d[1:] == [8, 9, 10]
    assert d[2:] == [9, 10]
    assert d[3:] == [10]
    assert d[4:] == []

    assert d[0:3:2] == [7, 9]


def test_setitem_int():
    """
    Проверка подмены элемента
    """
    d = DeCarousel(window=3)

    with pytest.raises(IndexError):
        d[0] = 1

    d.push(1)
    d.push(2)
    d.push(3)
    d.push(4)
    d.push(5)
    d.push(6)

    assert d[0] == 4
    assert d[1] == 5
    assert d[2] == 6

    assert d[-1] == 6
    assert d[-2] == 5
    assert d[-3] == 4

    assert d[:] == [4, 5, 6]

    d[0] = 9
    assert d[0] == 9
    assert d[1] == 5
    assert d[2] == 6

    d[1] = 7
    assert d[0] == 9
    assert d[1] == 7
    assert d[2] == 6

    d[2] = 4
    assert d[0] == 9
    assert d[1] == 7
    assert d[2] == 4

    d[-1] = 78
    assert d[0] == 9
    assert d[1] == 7
    assert d[2] == 78

    with pytest.raises(IndexError):
        d[75] = 6


def test_setitem_slice():
    """
    Проверка подмены элемента
    """
    d = DeCarousel(window=4)

    with pytest.raises(IndexError):
        d[:] = [9, 8, 7, 6]


def test_no_element():
    """
    Проверка выдачи пустого элемента
    """
    d = DeCarousel(window=2)

    with pytest.raises(IndexError):
        _ = d[0]


def test_push_and_pop():
    """
    Проверка добавления с извлечением
    """
    d = DeCarousel(window=4, sentinel=None)
    assert len(d) == 0
    assert d._index == 0
    assert d._head == -1
    assert d._tail == -1
    assert d.get_contents() == []
    assert d._data == [None, None, None, None]
    assert d.left is None
    assert d.right is None

    d.push(1)
    assert d._index == 1
    assert d._head == 0
    assert d._tail == 0
    assert d.get_contents() == [1]
    assert d._data == [1, None, None, None]
    assert d.left == 1
    assert d.right == 1

    d.push(2)
    assert d._index == 2
    assert d._head == 0
    assert d._tail == 1
    assert d.get_contents() == [1, 2]
    assert d._data == [1, 2, None, None]
    assert d.left == 1
    assert d.right == 2

    d.push(3)
    assert d._index == 3
    assert d._head == 0
    assert d._tail == 2
    assert d.get_contents() == [1, 2, 3]
    assert d._data == [1, 2, 3, None]
    assert d.left == 1
    assert d.right == 3

    d.push(4)
    assert d._index == 0
    assert d._head == 0
    assert d._tail == 3
    assert d.get_contents() == [1, 2, 3, 4]
    assert d._data == [1, 2, 3, 4]
    assert d.left == 1
    assert d.right == 4

    d.push(5)
    assert d._index == 1
    assert d._head == 1
    assert d._tail == 0
    assert d.get_contents() == [2, 3, 4, 5]
    assert d._data == [5, 2, 3, 4]
    assert d.left == 2
    assert d.right == 5

    d.push(6)
    assert d._index == 2
    assert d._head == 2
    assert d._tail == 1
    assert d.get_contents() == [3, 4, 5, 6]
    assert d._data == [5, 6, 3, 4]
    assert d.left == 3
    assert d.right == 6

    assert d.popleft() == 3
    assert d._index == 2
    assert d._head == 3
    assert d._tail == 1
    assert d.get_contents() == [4, 5, 6]
    assert d._data == [5, 6, None, 4]
    assert d.left == 4
    assert d.right == 6
    assert len(d) == 3

    assert d.popleft() == 4
    assert d._index == 2
    assert d._head == 0
    assert d._tail == 1
    assert d.get_contents() == [5, 6]
    assert d._data == [5, 6, None, None]
    assert d.left == 5
    assert d.right == 6
    assert len(d) == 2

    assert d.popleft() == 5
    assert d._index == 2
    assert d._head == 1
    assert d._tail == 1
    assert d.get_contents() == [6]
    assert d._data == [None, 6, None, None]
    assert d.left == 6
    assert d.right == 6
    assert len(d) == 1

    assert d.popleft() == 6
    assert d._index == 0
    assert d._head == -1
    assert d._tail == -1
    assert d.get_contents() == []
    assert d._data == [None, None, None, None]
    assert d.left is None
    assert d.right is None
    assert len(d) == 0

    d.push(7)
    assert d._index == 1
    assert d._head == 0
    assert d._tail == 0
    assert d.get_contents() == [7]
    assert d._data == [7, None, None, None]
    assert d.left == 7
    assert d.right == 7
    assert len(d) == 1
