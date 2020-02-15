import functools
import inspect
import sys
import types

from IQCommon import const, exception, utils
from IQCommon.exception import get_traceback_message


def decorate_api_exc(func):
    """
    api运行装饰器，该装饰器会对需要处理异常的方法增加异常处理
    :param func: function 待装饰的函数
    :return:function 装饰后函数
    """
    f = func
    while f:
        if getattr(f, const.NEED_EXCEPTION_HANDLE, False):
            break
        f = getattr(f, '__wrapped__', None)
    else:
        func = api_exec_patcher(func)
    return func


def api_exec_patcher(func):
    """
    为函数进行异常捕获处理
    :param func: function 待处理函数
    :return: function 处理后的函数
    """
    if isinstance(func, types.FunctionType):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception.IQInvalidArgument:
                raise
            except Exception as e:
                print(get_traceback_message(),flush=True)
                if isinstance(e, TypeError):
                    exc_info = sys.exc_info()
                    try:
                        inspect.signature(utils.get_original_function(
                            func)).bind(*args, **kwargs)
                    except TypeError:
                        t, v, tb = exc_info
                        raise exception.user_exc(v.with_traceback(tb))

                if exception.get_func_exc_ext_name_value(e) == const.ExcType.NOTSET:
                    raise exception.system_exc(e)
        return wrapper
    return func