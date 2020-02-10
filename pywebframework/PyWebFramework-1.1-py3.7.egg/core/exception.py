# coding: utf-8
import traceback
import io
from pyWebFramework.dll.IeWebFramework import RunJsException, ErrorCode
from .module import TaskManager


class FailureException(BaseException):
    def __init__(self, desc, code=ErrorCode.ExcuteFailed):
        self.desc = desc
        self.code = code


class SuccessException(BaseException):
    def __init__(self, desc='', code=ErrorCode.ExcuteSuccess):
        self.desc = desc
        self.code = code


def dispatch_task_func(task, func, *args):
    try:
        return func(*args)
    except RunJsException as e:
        traceback.print_exc()

        sio = io.StringIO()
        traceback.print_exc(file=sio)
        tb = sio.getvalue()

        task.Failure('执行js异常: \n' + tb, ErrorCode.RunJScriptFailed)
    except FailureException as e:
        task.Failure(e.desc, e.code)
    except SuccessException as e:
        task.Success(e.desc, e.code)
    except BaseException as e:
        traceback.print_exc()

        sio = io.StringIO()
        traceback.print_exc(file=sio)
        tb = sio.getvalue()

        task.Failure('未知python异常: \n' + tb)


def dispatch_page_func(func, *args):
    task = TaskManager.current_task
    if task:
        return dispatch_task_func(task, func, *args)


def wrap_callback(func):
    def wrapper(*args):
        task = TaskManager.current_task
        if task:
            dispatch_task_func(task, func, *args)

    if not func:
        return None

    return wrapper
