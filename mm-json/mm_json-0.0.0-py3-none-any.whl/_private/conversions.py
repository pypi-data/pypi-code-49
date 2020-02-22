import collections
import datetime
import decimal
import enum
import inspect
import typing
import uuid
import warnings

import marshmallow
import typing_inspect_lib

from .. import mm

NoneType = type(None)

_LITERAL_CONVERT = {
    dict: typing.Dict,
    list: typing.List,
    tuple: typing.Tuple,
}


def _to_internal_conversions(conversions):
    output = {}
    for key, value in conversions.items():
        value = mm.fields._base_conversions.get(value, value)
        if not hasattr(value, "from_typing"):
            warnings.warn(f"Marshmallow type {value} doesn't expose `from_typing`.")

        type_, *t_args = key if isinstance(key, tuple) else (key,)
        unwrapped, origin = typing_inspect_lib.get_typing(type_)
        if unwrapped is None:
            unwrapped = type_
        unwrapped = _LITERAL_CONVERT.get(unwrapped, unwrapped)
        new_key = (unwrapped, *t_args) if t_args else unwrapped

        if new_key not in output:
            output[new_key] = value
        elif output[new_key] is not value:
            raise ValueError(
                f"Two keys map to the same unwrapped type, {new_key}, "
                f"but have different marshmallow types - "
                f"{output[new_key]} != {value}"
            )
    return output


class ConversionType(enum.Flag):
    PLAIN = 1
    OPTIONAL = 2


class Converter:
    __CONVERSIONS = collections.ChainMap(
        _to_internal_conversions(
            {
                int: marshmallow.fields.Integer,
                float: marshmallow.fields.Float,
                str: marshmallow.fields.String,
                bool: marshmallow.fields.Boolean,
                datetime.datetime: marshmallow.fields.DateTime,
                datetime.time: marshmallow.fields.Time,
                datetime.timedelta: marshmallow.fields.TimeDelta,
                datetime.date: marshmallow.fields.Date,
                decimal.Decimal: marshmallow.fields.Decimal,
                uuid.UUID: marshmallow.fields.UUID,
                typing.Any: marshmallow.fields.Raw,
                typing.Mapping: marshmallow.fields.Mapping,
                typing.MutableMapping: marshmallow.fields.Mapping,
                typing.Dict: marshmallow.fields.Dict,
                typing.List: marshmallow.fields.List,
                typing.Tuple: marshmallow.fields.Tuple,
                (typing.Tuple, list): mm.fields.VarTuple,
                typing.Callable: marshmallow.fields.Function,
                enum.Enum: mm.fields.Enum,
                typing.Union: mm.fields.Union,
                mm.typing.DateTime: marshmallow.fields.DateTime,
                mm.typing.AwareDateTime: marshmallow.fields.AwareDateTime,
                mm.typing.NaiveDateTime: marshmallow.fields.NaiveDateTime,
                mm.typing.Constant: marshmallow.fields.Constant,
                mm.typing.Pluck: marshmallow.fields.Pluck,
                mm.typing.Number: marshmallow.fields.Number,
                mm.typing.Url: marshmallow.fields.Url,
                mm.typing.Email: marshmallow.fields.Email,
            }
        )
    )

    def __init__(self, conversions=None):
        if conversions is not None:
            conversions = _to_internal_conversions(conversions)
        self.conversions = type(self).__CONVERSIONS.new_child(conversions)

    @staticmethod
    def _optional_mutations(type_, metadata):
        metadata.setdefault("default", None)
        metadata.setdefault("missing", None)
        metadata["required"] = False

    @staticmethod
    def _new_type_mutations(type_, metadata):
        metadata.setdefault("description", type_.__name__)

    def _make_type(self, type_, metadata, arguments):
        if type_ not in self.conversions:
            raise ValueError(f"No conversion for type {type_}")
        class_ = self.conversions[type_]
        arguments = (self._convert(a, metadata=metadata) for a in arguments)
        if hasattr(class_, "from_typing"):
            return class_.from_typing(self, arguments, **metadata)
        return class_(*arguments, **metadata)

    def _handle_basic(self, type_, type_info, metadata):
        return self._make_type(type_, metadata, type_info.args if type_info else ())

    def _handle_tuple(self, type_, type_info, metadata):
        tuple_type = typing.Tuple
        args = type_info.args if type_info else ()
        if not args or ... in args:
            tuple_type = (typing.Tuple, list)
            args = (args[0] if args else typing.Any,)
        return self._make_type(tuple_type, metadata, args)

    def _handle_default(self, type_, type_info, metadata):
        warnings.warn(f"Unknown type {type_!r}.")
        return self._make_type(typing.Any, metadata, ())

    def _handle_enum(self, type_, type_info, metadata):
        metadata.setdefault("enum", type_)
        return self._make_type(enum.Enum, metadata, ())

    def _handle_union(self, type_, type_info, metadata):
        args = type_info.args
        nonnone_args = [a for a in args if a is not NoneType]
        if not (type_info.unwrapped is typing.Optional or len(nonnone_args) == 1):
            return self._make_type(typing.Union, metadata, args)
        elif typing.Optional in self.conversions:
            return self._make_type(typing.Optional, metadata, args)
        else:
            new_type = (nonnone_args + [typing.Any])[0]
            self._optional_mutations(type_, metadata)
            return self._convert(new_type, metadata=metadata)

    def _is_new_type(self, type_):
        return getattr(type_, "__supertype__", None) and inspect.isfunction(type_)

    def _handle_new_type(self, type_, type_info, metadata):
        self._new_type_mutations(type_, metadata)
        return self._convert(type_.__supertype__, metadata=metadata)

    def _handle_other(self, type_, type_info, metadata):
        raise ValueError(f"Unknown type {type_}.")

    def _convert(self, type_, *, metadata):
        type_info = typing_inspect_lib.get_type_info(type_)
        if type_info:
            unwrapped = type_info.unwrapped
        else:
            unwrapped = type_
        unwrapped = _LITERAL_CONVERT.get(unwrapped, unwrapped)

        if unwrapped is typing.Tuple:
            return self._handle_tuple(type_, type_info, metadata)

        if type_info and (
            type_info.unwrapped is typing.Optional
            or type_info.unwrapped is typing.Union
        ):
            return self._handle_union(type_, type_info, metadata)

        if unwrapped in self.conversions:
            return self._handle_basic(unwrapped, type_info, metadata)

        if isinstance(type_, enum.EnumMeta):
            return self._handle_enum(type_, type_info, metadata)

        if type_info is None:
            return self._handle_default(type_, type_info, metadata)

        if self._is_new_type(type_):
            return self._handle_new_type(type_, type_info, metadata)

        return self._handle_other(type_, type_info, metadata)

    def convert(self, type_, *, metadata):
        return self._convert(type_, metadata=metadata.copy())
