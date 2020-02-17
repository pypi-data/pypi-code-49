# -*- coding: utf-8 -*-
"""

    Контейнер с бегущим индексом, в который постоянно можно добавлять элементы

    На базе этого контейнера предполагается собирать структуры для вычисления динамических
    характеристик непрерывного потока входных данных в реальном времени.
    Например вычисление скользящего среднего.

    Пример работы с контейнером:
    c = Carousel(window=3)  # внутреннее хранилище: [NULL, NULL, NULL]
    c.push(1)               # внутреннее хранилище: [   1, NULL, NULL]
    c.push(2)               # внутреннее хранилище: [   1,    2, NULL]
    c.push(3)               # внутреннее хранилище: [   1,    2,    3]
    c.push(4)               # внутреннее хранилище: [   4,    2,    3]
    c.push(5)               # внутреннее хранилище: [   4,    5,    3]
    c.push(6)               # внутреннее хранилище: [   4,    5,    6]
    c.push(7)               # внутреннее хранилище: [   7,    5,    6]
    c.push(8)               # внутреннее хранилище: [   7,    8,    6]
    c.get_contents() --> [6, 7, 8]

    Почему не deque или другое подобие связного списка - очень медленно.
    Предполагается, что данная реализация будет работать намного быстрее
    и меньше загружать процессор при работе.

"""
# встроенные модули
from typing import Any, Optional, Collection, List, Generator, Union

# модули проекта
from trivial_tools.special.special import fail
from trivial_tools.formatters.base import s_type


class Carousel:
    """
    Контейнер с бегущим индексом на базе списка.
    Нужен для обработки непрерывного входного потока данных
    """
    __slots__ = ('_sentinel', '_data', '_len', '_index', 'window')

    def __init__(self, source: Optional[Collection] = None,
                 window: int = 0, sentinel: Any = object()):
        """
        Создание экземпляра. Можно задать базовую коллекцию, размер и объект для пустых слотов

        :param source: исходная коллекция элементов, на базе которой надо собрать экземпляр
        :param window: максимальное количество элементов (ширина окна вычисления)
        :param sentinel: элемент для заполнения пустых ячеек (можно добавить свой)
        """
        self._sentinel = sentinel
        self._data = []
        self._len = 0
        self._index = 0

        if source:
            # есть коллекция-прототип из которой можно взять данные
            if window:
                self.window = window
            else:
                self.window = len(source)
            self.restore()
            self.populate(source)

        elif window:
            # создаём пустую карусель
            self.window = window
            self.restore()

        else:
            fail(f'Для создания экземпляра {s_type(self)} необходимо либо указать длину и/или \n'
                 'дать коллекцию из которой будет собран экземпляр.', reason=ValueError)

    def __str__(self) -> str:
        """
        Текстовый вид
        """
        return self.make_str(with_null=False)

    def __repr__(self) -> str:
        """
        Текстовый вид
        """
        return self.make_str(with_null=True)

    def make_str(self, with_null: bool = False, sep: str = ', ') -> str:
        """
        Собрать текстовое представление
        """
        contents = []

        for element in self._internals():
            if element is self._sentinel:
                if with_null:
                    contents.append('NULL')
            else:
                contents.append(str(element))

        if len(contents) <= 5:
            string = sep.join(contents)
            result = f'{s_type(self)}([{string}], window={self.window})'

        else:
            string = sep.join([*contents[0:3], '...', *contents[-3:]])
            result = f'{s_type(self)}([{string}], len={len(self)}, window={self.window})'

        return result

    def populate(self, source: Collection[Any]) -> None:
        """
        Наполнить хранилище предоставленными данными

        :param source: некоторая коллекция, элементы которой надо последовательно переложить
        """
        self._index = 0
        for value in source:
            self.push(value)

    def __len__(self) -> int:
        """
        Длина показывает сколько ячеек у нас заполнено
        """
        return self._len

    def _step_right(self, index: int) -> int:
        """
        Увеличить индекс на единицу и вернуть его значение
        """
        if index < self.window - 1:
            index += 1
        else:
            index = 0
        return index

    def push(self, element: Any) -> Any:
        """
        Добавить элемент в карусель

        Мы замещаем элемент, выталкивая его из списка и возвращаем его. Его значение потом может
        быть использовано на вызывающей стороне

        :param element: Новый элемент любого типа
        :return: Старый элемент, который был вытолкнут при добавлении (может оказаться sentinel!)
        """
        old_value = self._data[self._index]
        self._data[self._index] = element
        self._index = self._step_right(self._index)

        self._len += 1
        if self._len > self.window:
            self._len = self.window

        return old_value

    def resize(self, new_window: int) -> None:
        """
        Изменить размер карусели

        :param new_window: новая предельная длина для внутреннего хранилища
        """
        if new_window == self.window:
            return

        old_data = self.get_contents()
        self.window = new_window
        self.restore()
        self.populate(old_data)

    def get_contents(self) -> List[Any]:
        """
        Получить копию внутреннего хранилища
        """
        result = [x for x in self._internals() if x is not self._sentinel]
        return result

    def extract(self) -> List[Any]:
        """
        Получить копию внутреннего хранилища и очистить его
        """
        result = self.get_contents()
        self.restore()
        return result

    def restore(self) -> None:
        """
        Сбросить индекс и длину, заполнить
        внутреннее хранилище пустыми объектами
        """
        self._len = 0
        self._index = 0
        self._data = [self._sentinel for _ in range(self.window)]

    def _internals(self) -> Generator[Any, None, None]:
        """
        Проитерироваться по элементам внутреннего хранилища (включая пустые элементы!)
        """
        if self._len == self.window:
            yield from self._data[self._index:]
            yield from self._data[:self._index]
        else:
            yield from self._data

    def __iter__(self) -> Any:
        """
        Проитерироваться по элементам внутреннего хранилища (без пустых элементов)
        Сохраняет порядок вставки элементов
        """
        for element in self._internals():
            if element is not self._sentinel:
                yield element

    def __getitem__(self, item: Union[int, slice]) -> Any:
        """
        Обратиться к элементу по индексу.
        Обеспечивается обычный доступ к внутреннему хранилищу, просто со смещением индекса

        :param item: ключ индексации
        :return: содержимое внутреннего хранилища
        """
        if isinstance(item, int):
            if not self._len:
                fail(f'Попытка получить элемент из пустого объекта {s_type(self)}',
                     reason=IndexError)

            result = self._data[self.get_real_index(item)]

            if result is self._sentinel:
                fail(f'В экземпляре {s_type(self)} нет элемента с индексом {item!r}',
                     reason=IndexError)

            return result

        if isinstance(item, slice):
            return self.get_contents()[item]

        fail(f"Тип {s_type(self)} поддерживает работу только с индексами int и slice!",
             reason=IndexError)

    def __setitem__(self, key: Union[int, slice], value: Any) -> None:
        """
        Записать элемент по индексу.
        Обеспечивается обычный доступ к внутреннему хранилищу, просто со смещением индекса

        :param key: ключ индексации, только int
        :param value: данные для записи (любой тип)
        """
        if not isinstance(key, int):
            fail(f"Тип {s_type(self)} поддерживает работу только с индексами типа int!",
                 reason=IndexError)

        if not self._len:
            fail(f'Попытка присвоить элемент по индексу {key} в пустой объект {s_type(self)}',
                 reason=IndexError)

        self._data[self.get_real_index(key)] = value
        return

    def get_real_index(self, key: int) -> int:
        """
        Настояшее положение ячеек, с учётом их сдвига
        """
        index = self._index + key
        if index > self._len - 1:
            index -= self._len
        return index
