# -*- coding: utf-8 -*-
"""

    Простой конфиг

"""
# встроенные модули
from typing import Any, Optional, List

# сторонние модули
from trivial_tools.runners.base import fail
from trivial_tools.formatters.base import s_type


class SimpleConfig:
    """
    Базовый класс для хранения настроек. Хранит все значения в пространстве имён класса,
    экземпляры не подразумевают наличие атрибутов.

    Особенности именования:
        АТРИБУТ - постоянное значение, не допускает изменения
        атрибут - не инициализированное значение, должно быть установлено сразу после запуска
    """
    def __setattr__(self, key: str, value: Any):
        """
        Объект неизменяемый
        """
        if key.islower():
            old_value = getattr(type(self), key)
            if isinstance(old_value, DeferredInitField):
                super().__setattr__(key, value)
                return

        fail(f'Экземпляры типа {s_type(self)} не позволяют менять атрибуты!')

    @classmethod
    def in_debug(cls) -> bool:
        """
        Находимся ли мы в режиме дебага?
        """
        return getattr(cls, 'DEBUG')

    @classmethod
    def in_production(cls) -> bool:
        """
        Находимся ли мы на продакшене?
        """
        return getattr(cls, 'APP_CONFIG') == 'production'

    def _get_attributes(self):
        """
        Получить перечень атрибутов объекта
        """
        for key in dir(self):
            if not key.startswith('__') and not callable(getattr(type(self), key)):
                yield key

    def _get_values(self):
        """
        Получить перечень значений атрибутов объекта
        """
        values = []
        for key in sorted(self._get_attributes()):
            attr = getattr(type(self), key)

            if isinstance(attr, DeferredInitField):
                if attr.already_set:
                    value = getattr(self, key)
                else:
                    value = '<Не инициализировано>'
            else:
                value = attr

            # прячем логины/пароли, которые могут попасть в конфиг
            if key.startswith('_'):
                value = '< hidden >'

            values.append((key, value))

        return values

    def _render_short(self, values: List[Any]) -> str:
        """
        Собрать текстовое представление для варианта с коротким списком аргументов
        """
        strings = [f'{key}={value}' for key, value in values]
        return f'{s_type(self)}(' + ', '.join(strings) + ')'

    def _render_long(self, values: List[Any]) -> str:
        """
        Собрать текстовое представление для варианта с длинным списком аргументов
        """
        longest = max([len(x[0]) for x in values])
        offset = '    '

        result = []
        for i, (key, value) in enumerate(values, start=1):
            if isinstance(value, (list, tuple)):
                if len(value) > 5:
                    # длинная последовательность
                    # 05. par_5 = [
                    #               1,
                    #               2,
                    string = ('{0:02d}. {1:' + str(longest) + '} = [').format(i, key)
                    result.append(offset + string)

                    for j, sub_element in enumerate(value, start=1):
                        line = offset + len(string) * ' ' + f'{sub_element}'
                        if j != len(value):
                            line += ','
                        result.append(line)

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

    def __str__(self) -> str:
        """
        Текстовое представление
        """
        values = self._get_values()

        if len(values) <= 3:
            return self._render_short(values)
        return self._render_long(values)

    def __repr__(self) -> str:
        """
        Этот класс не имеет аргументов для конструктора
        """
        return f'{s_type(self)}()'


class DeferredInitField:
    """
    Дескриптор для описания атрибутов, которые устанавливаются после запуска приложения
    """
    def __init__(self):
        """
        Инициация
        """
        self.name = None
        self.already_set = False

    def __set_name__(self, owner: SimpleConfig, name: str):
        """
        Запомнить имя дескриптора
        """
        self.name = name

    def __get__(self, instance: Optional[SimpleConfig], owner: SimpleConfig):
        """
        Получить значение атрибута
        """
        if instance is None:
            return self

        if not self.already_set:
            fail(f'Атрибут {s_type(instance)}.{self.name} ещё не был инициализирован!')

        return getattr(owner, self.name)

    def __set__(self, instance: SimpleConfig, value: Any) -> None:
        """
        Установить значение атрибута
        """
        if self.already_set:
            old_value = getattr(instance, self.name)
            fail(f'Атрибут {s_type(instance)}.{self.name} уже установлен в "{old_value!r}"!')

        # атрибут сохраняется в классе, а не в экземпляре
        setattr(type(instance), self.name, value)
        self.already_set = True
