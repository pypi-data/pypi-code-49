import time

import logging
from functools import wraps

log = logging.getLogger()


def trace_result(func):
    """Декоратор трассирующий вызываемую функцию. Показывет название
    функции и время ее выполнения
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func_result = func(*args, **kwargs)
        execution_time = time.time() - start
        log.debug(f'"{func.__name__}" exec_time: {execution_time} exec_result: {func_result}')
        return func_result

    return wrapper
