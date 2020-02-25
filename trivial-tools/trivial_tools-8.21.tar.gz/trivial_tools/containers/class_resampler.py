# -*- coding: utf-8 -*-
"""

    Класс для ресемплирования данных с неоднородными метками времени в посекундный формат

    Пример работы с контейнером:

    r = Resampler()
    result = r.push((datetime(2019, 12, 1, 12, 0, 0), 'A'))  # result будет []
    result = r.push((datetime(2019, 12, 1, 12, 0, 4), 'B'))

    В result будет лежать:
    [
        [datetime(2019, 12, 1, 12, 0, 0), 'A'],
        [datetime(2019, 12, 1, 12, 0, 1), 'A'],
        [datetime(2019, 12, 1, 12, 0, 2), 'A'],
        [datetime(2019, 12, 1, 12, 0, 3), 'A'],
        [datetime(2019, 12, 1, 12, 0, 4), 'B']
    ]

"""
# встроенные модули
from datetime import timedelta
from typing import Generator, Any

# модули проекта
from trivial_tools.formatters.base import s_type
from trivial_tools.datetime_tools.text import datetime_to_text_s


class Resampler:
    """
    Выдаёт данные в посекундном виде.
    Создаётся по одному экземпляру на источник данных
    Сами данные не хранит, работает по двум меткам времени
    """
    __slots__ = ('max_gap', 'datetime_index', 'previous', 'placeholder', '_full_on')

    def __init__(self, max_gap: int = 30, datetime_index: int = 0, placeholder: Any = None):
        """
        Создание экземпляра

        :param max_gap: предельно допустимое количество секунд между временными метками. Периоды
        больше этого времени считаются периодом сбоя связи и забиваются nan

        :param datetime_index: объект ожидает получать некоторые данные в виде кортежа,
        соответственно datetime_index это индекс в этом кортеже,
        по которому можно найти метку времени.
        :param placeholder: заполнитель для случая, когда у нас не нашлось значения для подстановки
        :param _full_on: флаг, показывающий, что ресемплер вошёл в рабочий режим. Без него
        будет съедено первое значение в списке
        """
        self.max_gap = max_gap
        self.datetime_index = datetime_index
        self.placeholder = placeholder
        self.previous = None
        self._full_on = False

    def __repr__(self) -> str:
        """
        Текстовое представление
        """
        result = (
            f'{s_type(self)}('
            f'max_gap={self.max_gap}, '
            f'datetime_index={self.datetime_index}, '
            f'placeholder={self.placeholder!r})'
        )
        return result

    def __str__(self) -> str:
        """
        Текстовое представление
        """
        if self.previous:
            previous = datetime_to_text_s(self.previous[self.datetime_index])
        else:
            previous = 'None'

        result = f'{s_type(self)}[{previous}]'
        return result

    def iter_push(self, payload: tuple) -> Generator[tuple, None, None]:
        """
        Добавить новый кусочек данных с меткой времени и получить обратно итератор по
        ресемплированным данным

        Подразумевается, что данные уже округлены до целых секунд

        :param payload: кортеж данных с временной меткой
        :return: последовательность кортежей с ресемплированными данными
        """
        # ----------------- Первичная инициализация, мы пока не можем считать
        if not payload:
            return None

        payload = list(payload)

        # у нас нет старого значения, берём это без проверки
        if self.previous is None:
            self.previous = payload
            return None

        new_seconds = self.get_seconds(payload)
        old_seconds = self.get_seconds(self.previous)

        if new_seconds == old_seconds:
            # при равенстве мы всё-равно замещаем старые показания новыми
            self.previous = payload
            return None

        if new_seconds < old_seconds:
            # это значение слишком старое
            return None

        old_moment = self.previous[self.datetime_index]
        delta = new_seconds - old_seconds

        if delta > self.max_gap:
            # забиваем пустыми значениями т.к. превышен предельный интервал
            body = [self.placeholder if i != self.datetime_index else x
                    for i, x in enumerate(self.previous)]
        else:
            # вытаскиваем значения (идут после индекса времени)
            body = list(self.previous)

        # первое значение в списке требует особого отношения
        if not self._full_on:
            yield self.previous
            self._full_on = True

        # генерируем серию промежуточных значений
        for i in range(1, delta):
            moment = old_moment + timedelta(seconds=i)
            body[self.datetime_index] = moment
            yield list(body)

        yield payload

        self.previous = payload

    def push(self, payload: tuple) -> list:
        """
        Аналогично итеративному варианту, только получить сразу список

        :param payload: кортеж данных с временной меткой
        :return: список кортежей с ресемплированными данными
        """
        result = []
        for each in self.iter_push(payload):
            result.append(each)
        return result

    def get_seconds(self, payload: list) -> int:
        """
        Выделить число секунд для datetime
        """
        return int(payload[self.datetime_index].timestamp())

    def clear(self):
        """
        Сбросить в исходное состояние
        """
        self.previous = None
        self._full_on = False
