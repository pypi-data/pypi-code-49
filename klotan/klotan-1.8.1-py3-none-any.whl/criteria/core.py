from typing import Callable

from klotan.store import Storage


def args_to_string(*kargs, **kwargs):
    str_args = ""
    arg_size = len(kargs) + len(kwargs)
    i = 0
    for arg in kargs:
        varg = arg
        if isinstance(varg, str):
            varg = f'"{varg}"'
        str_args += str(varg) + (", " if i < arg_size - 1 else "")
        i += 1
    for arg in kwargs.items():
        varg = arg[1]
        if isinstance(varg, str):
            varg = f'"{varg}"'
        str_args += str(arg[0]) + "=" + str(varg) + (", " if i < arg_size - 1 else "")
        i += 1
    str_args = f"({str_args})" if i > 0 else ""
    return str_args


class Criteria:
    def __init__(self, name: str, fn: Callable[[], bool], *kargs, **kwargs):
        self.name = name
        self.fn = fn
        self.kargs = kargs
        self.kwargs = kwargs
        self.combined = False
        self.ref = None

    def __call__(self, *kargs, **kwargs):
        if self.ref:
            self.ref.store(self.fn, *kargs, **kwargs)
        return self.fn(*kargs, **kwargs)

    def __repr__(self):
        model = f"{self.name}" if self.combined else f"Criteria<{self.name}>"
        crit_repr = model + args_to_string(*self.kargs, **self.kwargs)
        return crit_repr

    def __or__(self, criteria):
        return Criteria(
            f"({str(self)} or {str(criteria)})",
            lambda *kargs, **kwargs: self.fn(*kargs, **kwargs)
            or criteria.fn(*kargs, **kwargs),
        ).set_combined()

    def __and__(self, criteria):
        return Criteria(
            f"({str(self)} and {str(criteria)})",
            lambda *kargs, **kwargs: self.fn(*kargs, **kwargs)
            and criteria.fn(*kargs, **kwargs),
        ).set_combined()

    def __rshift__(self, ref: Storage):
        self.ref = ref
        return self

    def __invert__(self):
        return Criteria(
            f"(not {str(self)})", lambda *kargs, **kwargs: not self.fn(*kargs, **kwargs)
        ).set_combined()

    def set_combined(self):
        self.combined = True
        return self


def fn_to_criteria(fn):
    def fn_to_criteria_wrapper(*kargs, **kwargs):
        return Criteria(fn.__name__, fn(*kargs, **kwargs), *kargs, **kwargs)

    return fn_to_criteria_wrapper

@fn_to_criteria
def expected(x, optional):
    return lambda y: optional