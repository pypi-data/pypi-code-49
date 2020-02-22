import marshmallow
import marshmallow_enum
import marshmallow_union


class Field(marshmallow.fields.Field):
    @classmethod
    def from_typing(cls, _converter, _arguments, **kwargs):
        return cls(**kwargs)


class Integer(marshmallow.fields.Integer, Field):
    pass


class Float(marshmallow.fields.Float, Field):
    pass


class String(marshmallow.fields.String, Field):
    pass


class Boolean(marshmallow.fields.Boolean, Field):
    pass


class DateTime(marshmallow.fields.DateTime, Field):
    pass


class Time(marshmallow.fields.Time, Field):
    pass


class TimeDelta(marshmallow.fields.TimeDelta, Field):
    pass


class Date(marshmallow.fields.Date, Field):
    pass


class Decimal(marshmallow.fields.Decimal, Field):
    pass


class UUID(marshmallow.fields.UUID, Field):
    pass


class Raw(marshmallow.fields.Raw, Field):
    pass


class Mapping(marshmallow.fields.Mapping, Field):
    @classmethod
    def from_typing(cls, _converter, arguments, **kwargs):
        return cls(
            keys=next(arguments, marshmallow.fields.Raw()),
            values=next(arguments, marshmallow.fields.Raw()),
            **kwargs
        )


class Dict(marshmallow.fields.Dict, Field):
    @classmethod
    def from_typing(cls, _converter, arguments, **kwargs):
        return cls(
            keys=next(arguments, marshmallow.fields.Raw()),
            values=next(arguments, marshmallow.fields.Raw()),
            **kwargs
        )


class List(marshmallow.fields.List, Field):
    @classmethod
    def from_typing(cls, _converter, arguments, **kwargs):
        return cls(next(arguments, marshmallow.fields.Raw()), **kwargs)


class Tuple(marshmallow.fields.Tuple, Field):
    @classmethod
    def from_typing(cls, _converter, arguments, **kwargs):
        return cls(tuple(arguments), **kwargs)


class Function(marshmallow.fields.Function, Field):
    pass


class Number(marshmallow.fields.Number, Field):
    @classmethod
    def from_typing(cls, _converter, arguments, **kwargs):
        return cls(*arguments, **kwargs)


class NaiveDateTime(marshmallow.fields.NaiveDateTime, Field):
    @classmethod
    def from_typing(cls, _converter, arguments, **kwargs):
        return cls(*arguments, **kwargs)


class AwareDateTime(marshmallow.fields.AwareDateTime, Field):
    @classmethod
    def from_typing(cls, _converter, arguments, **kwargs):
        return cls(*arguments, **kwargs)


class Url(marshmallow.fields.Url, Field):
    @classmethod
    def from_typing(cls, _converter, arguments, **kwargs):
        return cls(*arguments, **kwargs)


class Email(marshmallow.fields.Email, Field):
    @classmethod
    def from_typing(cls, _converter, arguments, **kwargs):
        return cls(*arguments, **kwargs)


class Method(marshmallow.fields.Method, Field):
    @classmethod
    def from_typing(cls, _converter, arguments, **kwargs):
        return cls(*arguments, **kwargs)


class Constant(marshmallow.fields.Constant, Field):
    @classmethod
    def from_typing(cls, _converter, arguments, **kwargs):
        return cls(*arguments, **kwargs)


class Pluck(marshmallow.fields.Pluck, Field):
    @classmethod
    def from_typing(cls, _converter, arguments, **kwargs):
        return cls(*arguments, **kwargs)


class Enum(marshmallow_enum.EnumField, Field):
    pass


class Union(marshmallow_union.Union, Field):
    @classmethod
    def from_typing(cls, _converter, arguments, **kwargs):
        return cls(tuple(arguments), **kwargs)


_base_conversions = {
    marshmallow.fields.Integer: Integer,
    marshmallow.fields.Float: Float,
    marshmallow.fields.String: String,
    marshmallow.fields.Boolean: Boolean,
    marshmallow.fields.DateTime: DateTime,
    marshmallow.fields.Time: Time,
    marshmallow.fields.TimeDelta: TimeDelta,
    marshmallow.fields.Date: Date,
    marshmallow.fields.Decimal: Decimal,
    marshmallow.fields.UUID: UUID,
    marshmallow.fields.Raw: Raw,
    marshmallow.fields.Mapping: Mapping,
    marshmallow.fields.Dict: Dict,
    marshmallow.fields.List: List,
    marshmallow.fields.Tuple: Tuple,
    marshmallow.fields.Function: Function,
    marshmallow.fields.Number: Number,
    marshmallow.fields.NaiveDateTime: NaiveDateTime,
    marshmallow.fields.AwareDateTime: AwareDateTime,
    marshmallow.fields.Url: Url,
    marshmallow.fields.Email: Email,
    marshmallow.fields.Method: Method,
    marshmallow.fields.Constant: Constant,
    marshmallow.fields.Pluck: Pluck,
    marshmallow_enum.EnumField: Enum,
    marshmallow_union.Union: Union,
}

# TODO: Add
# ClassVar
# ForwardRef
# Type
# TypeVar
# ByteString
# ChainMap
# Counter
# Deque
# DefaultDict
# OrderedDict
# Set
# FrozenSet
# NamedTuple


# Variable-length homogeneous tuple
# Tuple[T, ...]
class VarTuple(marshmallow.fields.List, Field):
    def _serialize(self, value, attr, obj, **kwargs):
        return super()._serialize(list(value), attr, obj, **kwargs)

    def _deserialize(self, value, attr, data, **kwargs):
        return tuple(super()._deserialize(value, attr, data, **kwargs))

    @classmethod
    def from_typing(cls, _converter, arguments, **kwargs):
        return cls(next(arguments, marshmallow.fields.Raw()), **kwargs)
