# -*- coding: utf-8 -*-
"""

    Класс с динамически генерируемыми атрибутами

"""
# модули проекта
from trivial_tools.special.special import fail
from trivial_tools.formatters.base import s_type


class Fluid:
    """
    Класс с динамически генерируемыми атрибутами
    """
    def __init__(self, *args, **kwargs):
        """
        Автоматическая инициация
        """
        if args:
            fail(f'{s_type(self)} подразумевает создание только из именованных атрибутов',
                 reason=ValueError)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self) -> dict:
        """
        Преобразовать в словарь
        """
        return {key: value for key, value in vars(self).items()}

    def alter(self, **kwargs):
        """
        Получить аналогичный экземпляр, но с другими параметрами
        """
        values = {**self.to_dict(), **kwargs}
        return self.from_dict(values)

    @classmethod
    def from_dict(cls, parameters: dict):
        """
        Создать экземпляр из словаря
        """
        return cls(**parameters)

    def __str__(self) -> str:
        """
        Текстовое представление
        """
        fields = []
        for key in vars(self):
            value = getattr(self, key)
            fields.append((key, value))

        if len(fields) <= 3:
            strings = [f'{key}={value}' for key, value in fields]
            return f'{s_type(self)}(' + ', '.join(strings) + ')'

        longest = max([len(x[0]) for x in fields])
        offset = '    '

        result = []
        for i, (key, value) in enumerate(fields, start=1):
            if isinstance(value, (list, tuple)):
                if len(value) > 5:
                    # длинная последовательность
                    # 05. par_5 = [
                    #               1,
                    #               2,
                    string = ('{0:02d}. {1:' + str(longest) + '} = [').format(i, key)
                    result.append(offset + string)
                    for j, sub_element in enumerate(value, start=1):
                        if j == len(value):
                            result.append(offset + len(string) * ' ' + f'{sub_element}')
                        else:
                            result.append(offset + len(string) * ' ' + f'{sub_element},')
                    result.append(offset + (len(string) - 1) * ' ' + ']')
                else:
                    # короткая последовательность
                    # \t01. par_1 = [1, 2, 3]
                    string = ('{0:02d}. {1:' + str(longest) + '} = ').format(i, key)
                    result.append(offset + string + str(value))
            else:
                string = ('{0:02d}. {1:' + str(longest) + '} = {2}').format(i, key, value)
                result.append(offset + string)
        return s_type(self) + '(\n' + '\n'.join(result) + '\n)'

    def __repr__(self) -> str:
        """
        Текстовое представление
        """
        result = []
        for key in vars(self):
            value = getattr(self, key)
            result.append(f'{key}={value!r}')

        return f'{s_type(self)}(' + ', '.join(result) + ')'

    def __eq__(self, other) -> bool:
        """
        Равенство
        """
        if isinstance(other, type(self)):
            return self.to_dict() == other.to_dict()
        return False
