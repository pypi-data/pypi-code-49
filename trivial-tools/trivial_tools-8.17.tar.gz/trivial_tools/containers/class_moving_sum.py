# -*- coding: utf-8 -*-
"""

    Контейнер для вычисления скользящей суммы.
    В него можно постоянно можно добавлять элементы и быстро получать сумму

    Пример работы с контейнером:
    m = MovingSum(window=4)  # сумма равна 0
    m.push(8)    # сумма равна 8
    m.push(41)   # сумма равна 49
    m.push(9)    # сумма равна 58
    m.push(6)    # сумма равна 64
    m.push(32)   # сумма равна 88
    m.push(58)   # сумма равна 105
    m.push(8)    # сумма равна 104
    m.push(78)   # сумма равна 176
    m.push(3)    # сумма равна 147
    m.push(2)    # сумма равна 91

"""
# встроенные модули
from typing import Union, Optional, Sequence, Any

# модули проекта
from trivial_tools.containers.class_carousel import Carousel


class MovingSum(Carousel):
    """
    Контейнер для вычисления скользящей суммы.
    В него можно постоянно можно добавлять элементы и быстро получать сумму
    """
    __slots__ = ('_sum',)

    def __init__(self, source: Optional[Sequence] = None,
                 window: int = 0, sentinel: Any = object()):
        """
        Создание экземпляра

        :param source: исходная коллекция элементов, на базе которой надо собрать экземпляр
        :param window: максимальное киличество элементов (ширина окна вычисления)
        :param sentinel: элемент для заполнения пустых ячеек (можно добавить свой)
        """
        self._sum: Union[int, float] = 0
        super().__init__(source, window, sentinel)

    def push(self, value: Union[int, float]) -> None:
        """
        Добавить элемент в контейнер

        Мы выталкиваем предыдущий элемент и меняем сумму соответствующим образом. Причина
        для такого выполнения - избежать необходимости итерироваться по коллекции при
        попытке вычислить среднее значение

        :param value: новое число, которое соответствует сдвигу окна среднего на один элемент
        """
        old_value = super().push(value)

        if old_value is not self._sentinel:
            self._sum -= old_value

        self._sum += value

    def restore(self) -> None:
        """
        Сбросить параметры
        """
        self._sum = 0
        super().restore()

    @property
    def sum(self) -> float:
        """
        Сумма всех элементов
        """
        return self._sum

    def __setitem__(self, key: Union[int, slice], value: Union[int, float, Sequence]) -> None:
        """
        Записать элемент по индексу.
        Обеспечивается обычный доступ к внутреннему хранилищу, просто со смещением индекса

        :param key: ключ индексации
        :param value: данные для записи (любой тип)
        """
        if isinstance(key, int):
            self._sum -= self._data[self.get_real_index(key)]
            self._sum += value

        super().__setitem__(key, value)
