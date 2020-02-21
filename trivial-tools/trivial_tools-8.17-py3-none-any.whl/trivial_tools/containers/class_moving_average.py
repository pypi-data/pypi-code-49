# -*- coding: utf-8 -*-
"""

    Контейнер для вычисления скользящего среднего.
    В него можно постоянно можно добавлять элементы и быстро получать среднее

    Пример работы с контейнером:
    m = MovingAverage(maxlen=4)  # среднее равно 0
    m.push(1)   # среднее равно 1
    m.push(3)   # среднее равно 2
    m.push(5)   # среднее равно 3
    m.push(6)   # среднее равно 3,75
    m.push(8)   # среднее равно 5,5
    m.push(41)  # среднее равно 15
    m.push(9)   # среднее равно 16

"""
# встроенные модули
from typing import Union, Optional, Sequence, Any

# модули проекта
from trivial_tools.containers.class_moving_sum import MovingSum


class MovingAverage(MovingSum):
    """
    Контейнер для вычисления скользящего среднего.
    В него можно постоянно можно добавлять элементы и быстро получать среднее
    """
    __slots__ = ('_avg',)

    def __init__(self, source: Optional[Sequence] = None,
                 window: int = 0, sentinel: Any = object()):
        """
        Создание экземпляра

        :param source: исходная коллекция элементов, на базе которой надо собрать экземпляр
        :param window: максимальное киличество элементов (ширина окна вычисления)
        :param sentinel: элемент для заполнения пустых ячеек (можно добавить свой)
        """
        self._avg = 0.0
        super().__init__(source, window, sentinel)

    def push(self, value: Union[int, float]) -> None:
        """
        Добавить элемент в контейнер

        Мы выталкиваем предыдущий элемент и меняем сумму соответствующим образом. Причина
        для такого выполнения - избежать необходимости итерироваться по коллекции при
        попытке вычислить среднее значение

        :param value: новое число, которое соответствует сдвигу окна среднего на один элемент
        """
        super().push(value)
        self._avg = self._sum / len(self)

    def restore(self) -> None:
        """
        Сбросить параметры
        """
        self._avg = 0.0
        super().restore()

    @property
    def avg(self) -> float:
        """
        Среднее всех элементов
        """
        return self._avg

    def __setitem__(self, key: Union[int, slice], value: Union[int, float, Sequence]) -> Any:
        """
        Записать элемент по индексу.
        Обеспечивается обычный доступ к внутреннему хранилищу, просто со смещением индекса

        :param key: ключ индексации
        :param value: данные для записи (любой тип)
        """
        super().__setitem__(key, value)
        self._avg = self._sum / len(self)
