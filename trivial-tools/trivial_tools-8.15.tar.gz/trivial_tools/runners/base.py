# -*- coding: utf-8 -*-
"""

    Инструменты запуска

"""
# встроенные модули
import os
import time
from datetime import datetime
from functools import wraps
from typing import Callable, Union, Tuple, Any, Type, Optional, Dict

# сторонние модули
from loguru import logger

# модули проекта
from trivial_tools.special.special import fail
from trivial_tools.system.envs import get_full_path_from_env
from trivial_tools.config_handling.base_config import BaseConfig


def repeat_on_exceptions(repeats: int, case: Union[Exception, Tuple[Exception]],
                         delay: float = 1.0, verbose: bool = True) -> Callable:
    """Декоратор, заставляющий функцию повторить операцию при выбросе исключения.

    Инструмент добавлен для возможности повторной отправки HTTP запросов на серверах

    :param verbose: логгировать произошедшие исключения и выводить их на экран
    :param delay: время ожидания между попытками
    :param repeats: сколько раз повторить (0 - повторять бесконечно)
    :param case: при каком исключении вызывать повтор
    :return: возвращает фабрику декораторов
    """

    def decorator(func: Callable) -> Callable:
        """
        Декоратор
        """

        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            """
            Враппер
            """
            iteration = 0
            while True:
                try:
                    result = func(*args, **kwargs)
                    break
                except case as exc:
                    iteration += 1

                    if verbose:
                        logger.warning(f'{exc} в функции {func.__name__}'
                                       f' (итерация {iteration})')

                    if repeats and iteration > repeats:
                        fail(exc)

                    time.sleep(delay)

            return result

        return wrapper

    return decorator


def start_working(folder_name: str, config_name: Optional[str], func: Callable,
                  config_type: Type[BaseConfig],
                  config_filename: str = 'config.json', infinite: bool = True) -> None:
    """Стартовать скрипт с выбранными настройками.

    :param folder_name: имя суб-каталога со скриптом. Запуск предполагается из коневого каталога
    :param config_name: принудительный выбор конфигурации для скрипта при запуске из консоли
    :param func: рабочая функция скрпта, которая будет выполнять всю полезную работу
    :param config_type: класс конфигурации для выбранного скрипта
    :param config_filename: имя json файла в котором следует искать кофигурацию
    :param infinite: флаг бесконечного перезапуска скрипта при выбросе исключения
    """
    config = config_type.from_json(
        config_name=config_name,
        filename=os.path.join(folder_name, config_filename)
    )

    logger.add(
        sink=get_full_path_from_env(config.db_path, config.logger_filename),
        level=config.logger_level,
        rotation=config.logger_rotation
    )

    separator = '#' * 79

    logger.warning(separator)
    logger.warning(config.start_message)
    logger.info(f'Параметры скрипта:\n{config}')

    while True:
        # noinspection PyBroadException
        try:
            message = func(config)
            logger.warning(message)

            if message == 'stop':
                break

        except KeyboardInterrupt:
            logger.warning('\nОстановка по команде с клавиатуры!')
            break
        except Exception:
            logger.exception('\nКритический сбой!')

        if not infinite:
            break

    logger.warning(separator)


def capture_exception_output(title: str) -> Optional[str]:
    """
    Перехватить описание ошибки из loguru
    """
    storage = []
    sink_id = logger.add(sink=lambda msg: storage.append(msg))
    logger.exception(title)
    logger.remove(sink_id)
    return storage[0] if storage else None


def _execute(config, handler: Callable, separator: str) -> str:
    """
    Исполнить с логгированием
    """
    logger.add(
        config.LOGGER_FILENAME,
        level=config.LOGGER_LEVEL,
        rotation=config.LOGGER_ROTATION
    )
    logger.warning(separator)
    logger.info(config.START_MESSAGE)
    logger.info(config)

    # @@@@@@@@@@@@@@@@@@@@
    message = handler()
    # @@@@@@@@@@@@@@@@@@@@

    logger.info(message)
    return message


def init_daemon(config, handler: Callable, infinite: bool = False) -> None:
    """Стартовать скрипт с выбранными настройками.

    :param config: класс, атрибуты которого являются нашими настрояками
    :param handler: рабочая функция скрпта, которая будет выполнять всю полезную работу
    :param infinite: флаг бесконечного перезапуска скрипта при выбросе исключения
    """
    # избегаем циклической ссылки
    from trivial_tools.json_rpc.calls import call_api

    separator = '#' * 79

    while True:
        normal_stop = False
        time_start = datetime.now()

        payload: Dict[str, str] = {
            "service_name": config.SERVICE_NAME,
            "status": 'normal',
            "title": 'Успешное исполнение. Длительность - {} сек.'
        }

        # noinspection PyBroadException
        try:
            message = _execute(config, handler, separator)

            if message == '<stop>':
                logger.warning('Остановка по команде скрипта')
                normal_stop = True
                break

        except KeyboardInterrupt:
            logger.warning('Остановка по команде с клавиатуры')
            normal_stop = True
            break

        except Exception:
            description = capture_exception_output(f'Критический сбой {config.SERVICE_NAME}')
            payload['status'] = 'fail'
            payload['title'] = 'Остановка работы после {} сек. из-за критического сбоя'
            payload['text'] = description or 'Не удалось сохранить'

        else:
            payload['text'] = message

        finally:
            duration = int((datetime.now() - time_start).total_seconds())
            payload['title'] = payload['title'].format(duration)

            if config.in_production() and not normal_stop:
                # noinspection PyProtectedMember
                call_api(
                    url=config.API_URL,
                    method='register_report',
                    report=payload,
                    fingerprint=config._FINGERPRINT,
                    error_msg=f'Не удалось отправить отчёт о состоянии на {config.API_URL}!',
                    debug=config.in_debug()
                )

        if not infinite:
            break

    logger.warning(separator)
