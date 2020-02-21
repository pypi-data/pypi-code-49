import os
import traceback
from typing import Callable, Union

from .utils import get_list_values, get_values, ColorPrint, _check_lambda_args
from .event import Event

__all__ = ('event', 'list_value_event')


class __Executor(object):
    def __init__(self, function: Callable, keys=None, description_key=None, list_value=None, iter_key=None,
                 custom_description=None, *args, **kwargs):
        self.function = function
        self.keys = keys
        self.description_key = description_key
        self.list_value = list_value
        self.iter_key = iter_key
        self.custom_description = custom_description
        self.args = args
        self.kwargs = kwargs

    def execution(self, name: str, description: str, *args, **kwargs) -> any:
        init_kwargs = {
            "system_name": os.environ.get("SYSTEM_EVENT_NAME", ""),
            "system_url": os.environ.get("SYSTEM_EVENT_URL", ""),
            "execute_token": os.environ.get("SYSTEM_EVENT_TOKEN", ""),
            "em_notifier": os.environ.get("SYSTEM_EM_NOTIFIER", False),
            "debug": os.environ.get("SYSTEM_EM_NOTIFIER", False),
        }
        event = Event(**init_kwargs)
        event.push_to_event(name=name, description=description, status=False)
        # print(pushed)
        try:
            args = _check_lambda_args(args)
            if args or kwargs:
                func_result = self.function(*args, **kwargs)
            else:
                func_result = self.function()
        except Exception as exc_description:
            t = traceback.format_exc()
            t = t.replace("func_result = function", function.__name__)
            return event.log_exception(name, description=str(exc_description), trb=t)
        event.push_to_event(name=name, description=description, status=True)
        return func_result

    def push(self, list_: bool = False, *args, **kwargs):
        exception = False
        name = ""
        description = ""
        var_names = self.function.__code__.co_varnames
        try:
            if self.keys is not None and not list_:
                values = get_values(self.keys, var_names, description_key=self.description_key, *args, **kwargs)
                name = values["name"]
                description = values['description']
            if list_:
                list_values = get_list_values(
                    self.keys, self.description_key, self.list_value, self.iter_key, var_names, *args, **kwargs
                )
                name = list_values["name"]
                description = list_values["description"]

            if not description and self.custom_description:
                description = self.custom_description
        except IndexError:
            exception = True
        if not exception:
            return self.execution(name, description, *args, **kwargs)


def event(keys=None, description_key=None, custom_description=None):
    def decorator(function, *args, **kwargs):
        def push_function_results(*args, **kwargs):
            executor = __Executor(function=function, keys=keys,
                                  description_key=description_key,
                                  custom_description=custom_description)
            return executor.push(False, *args, **kwargs)

        return push_function_results

    return decorator


def list_value_event(keys: Union[str, list], list_value: str, iter_key: str, description_key=None,
                     custom_description=None) -> any:
    def decorator(function, *args, **kwargs):
        def push_function_results(*args, **kwargs):
            executor = __Executor(function=function, keys=keys,
                                  description_key=description_key,
                                  custom_description=custom_description,
                                  list_value=list_value,
                                  iter_key=iter_key)
            return executor.pusher(True, *args, **kwargs)

        return push_function_results

    return decorator
