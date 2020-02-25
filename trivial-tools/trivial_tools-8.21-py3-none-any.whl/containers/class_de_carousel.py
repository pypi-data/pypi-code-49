# -*- coding: utf-8 -*-
"""

    Двусторонная карусель.
    В работе подобна deque, но не меняет размера при добавлении и извлечении элементов.

"""
# встроенные модули
from typing import Any, Optional, Collection, Generator, List

# модули проекта
from trivial_tools.special.special import fail
from trivial_tools.formatters.base import s_type
from trivial_tools.containers.class_carousel import Carousel


class DeCarousel(Carousel):
    """
    Двусторонная карусель.
    В работе подобна deque, но не меняет размера при добавлении и извлечении элементов.
    """
    __slots__ = ('_head', '_tail')

    def __init__(self, source: Optional[Collection] = None,
                 window: int = 0, sentinel: Any = object()):
        """
        Создание экземпляра. Можно задать базовую коллекцию, размер и объект для пустых слотов

        :param source: исходная коллекция элементов, на базе которой надо собрать экземпляр
        :param window: максимальное количество элементов (ширина окна вычисления)
        :param sentinel: элемент для заполнения пустых ячеек (можно добавить свой)
        """
        self._head = -1
        self._tail = -1
        super().__init__(source, window, sentinel)

    def __contains__(self, item: Any) -> bool:
        """
        Проверка наличия элемента
        """
        return item in self._data

    def _step_right(self, index: int) -> int:
        """
        Шагнуть вправо
        """
        if index < self.window - 1:
            index += 1
        else:
            index = 0
        return index

    def _step_left(self, index: int) -> int:
        """
        Шагнуть влево
        """
        if index > 0:
            index -= 1
        else:
            index = self.window - 1
        return index

    @property
    def left(self) -> Optional[Any]:
        """
        Крайний элемент слева
        """
        if len(self):
            return self._data[self._head]
        return None

    @property
    def right(self) -> Optional[Any]:
        """
        Крайний элемент справа
        """
        if len(self):
            return self._data[self._tail]
        return None

    def restore(self) -> None:
        """
        Сбросить индекс и длину, заполнить
        внутреннее хранилище пустыми объектами
        """
        self._len = 0
        self._index = 0
        self._head = -1
        self._tail = -1
        self._data = [self._sentinel for _ in range(self.window)]

    def _internals(self) -> Generator[Any, None, None]:
        """
        Проитерироваться по элементам внутреннего хранилища (включая пустые элементы!)
        """
        if self._head == -1 and self._tail == -1:
            yield from self._data

        else:
            i = self._head
            while True:
                if i == self._tail:
                    break
                yield self._data[i]
                i = self._step_right(i)
            yield self._data[self._tail]

    def update_len(self) -> None:
        """
        Пересчитать длину коллекции
        """
        if self._head < self._tail:
            self._len = self._tail - self._head + 1

        elif self._head > self._tail:
            self._len = self._tail - self._head + 1 + self.window

        elif self._head == self._tail:
            self._len = 1

    def push(self, item: Any) -> Any:
        """
        Добавить элемент в карусель

        Мы замещаем элемент, выталкивая его из списка и возвращаем его. Его значение потом может
        быть использовано на вызывающей стороне

        :param item: Новый элемент любого типа
        :return: Старый элемент, который был вытолкнут при добавлении (может оказаться sentinel!)
        """
        old_value = self._data[self._index]
        self._data[self._index] = item

        if self._head == self._tail == -1:
            # первая вставка элемента
            self._index = self._step_right(self._index)
            self._head = self._step_right(self._head)
            self._tail = self._step_right(self._tail)

        else:
            # обычная конфигурация
            if self._index == self._head:
                # затираем голову
                self._head = self._step_right(self._head)

            self._index = self._step_right(self._index)
            self._tail = self._step_right(self._tail)

        self.update_len()
        return old_value

    def append(self, item: Any) -> None:
        """
        Добавить элемент справа
        """
        self.push(item)
        return None

    def pop(self) -> Any:
        """
        Извлечь элемент справа
        """
        if self._len == 0:
            fail(f'Попытка извлечь элемент из пустой коллекции: {self}', reason=IndexError)

        value = self._data[self._tail]
        self._data[self._tail] = self._sentinel
        self._tail = self._step_left(self._tail)
        self._index = self._step_left(self._index)
        self._len -= 1
        return value

    def appendleft(self, item: Any) -> None:
        """
        Добавить элемент слева
        """
        if self._head == self._tail == -1:
            # первая вставка элемента
            self._data[-1] = item
            self._index = 0
            self._head = len(self._data) - 1
            self._tail = len(self._data) - 1

        else:
            # обычная конфигурация
            self._head = self._step_left(self._head)
            if self._head == self._tail:
                self._tail = self._step_left(self._tail)

            self._data[self._head] = item

        self.update_len()

    def popleft(self) -> Any:
        """
        Извлечь элемент слева
        """
        if self._len == 0:
            fail(f'Попытка извлечь элемент из пустой коллекции: {self}', reason=IndexError)

        value = self._data[self._head]
        self._data[self._head] = self._sentinel
        self._head = self._step_right(self._head)
        self._index = self._step_right(self._tail)
        self._len -= 1

        if self._len == 0:
            self.restore()
        return value
