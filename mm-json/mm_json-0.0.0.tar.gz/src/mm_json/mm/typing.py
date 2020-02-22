import abc
import typing

_T = typing.TypeVar("_T")


class _GenericMeta(abc.ABCMeta):
    def __repr__(self):
        return self.__module__ + "." + self.__name__

    def __call__(cls):
        raise TypeError(f"Type {cls!r} cannot be instantiated.")


class Constant(typing.Generic[_T], metaclass=_GenericMeta):
    pass


class DateTime(typing.Generic[_T], metaclass=_GenericMeta):
    pass


class NaiveDateTime(typing.Generic[_T], metaclass=_GenericMeta):
    pass


class AwareDateTime(typing.Generic[_T], metaclass=_GenericMeta):
    pass


class Pluck(typing.Generic[_T], metaclass=_GenericMeta):
    pass


Number = typing._SpecialForm("Number", doc="")
Url = typing._SpecialForm("Url", doc="")
Email = typing._SpecialForm("Email", doc="")

# Not implemented:
# marshmallow.Method
