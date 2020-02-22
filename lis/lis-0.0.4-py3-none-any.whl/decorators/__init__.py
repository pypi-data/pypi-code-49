import logging
from functools import wraps, partial
from time import time


logger = logging.getLogger(__name__)


def safe_or(default=None, swallows=[AssertionError]):
    def _safe_or(func):
        @wraps(func)
        def _safe(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if next((True for s in swallows if isinstance(e, s)), False):
                    logger.warning(str(e))
                else:
                    func_name = func.func.__name__ if isinstance(func, partial) else func.__name__
                    logger.exception('ignore exception when run func:%s', func_name)

                return default
        return _safe
    return _safe_or


def timeit(func):
    @wraps(func)
    def _timeit(*args, **kwargs):
        tstart = time()
        res = func(*args, **kwargs)
        logger.info(f'func={func.__name__} takes {time() - tstart} seconds to run.')
        return res
    return _timeit
