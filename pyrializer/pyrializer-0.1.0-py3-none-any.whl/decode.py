from .util import get_array_type
from .util import get_class_fields


__all__ = [
    'decode'
]


def decode(ftype, context):
    if ftype is None:
        return context
    elif ftype in [str, bool, int, float]:
        return _decode_primitive(ftype, context)
    elif type(ftype) is list:
        return _decode_array(ftype, context)
    elif isinstance(ftype, object):
        return _decode_object(ftype, context)
    raise ValueError(
        f'Unable to decode type {ftype} with context {context}'
    )


def _decode_primitive(ftype, context):
    assert ftype in [str, bool, int, float]

    if context is None:
        return None

    context_type = type(context)
    if ftype is not context_type:
        raise ValueError(
            f'Cannot cast value {context} of type {context_type} as {ftype}'
        )
    return context


def _decode_array(ftype, context):
    if context is None:
        return None

    context_type = type(context)
    if context_type is not list:
        raise ValueError(
            f'Cannot cast value {context} of type {context_type} as list'
        )

    item_type = get_array_type(ftype)
    return [decode(item_type, item_context) for item_context in context]


def _decode_object(ftype, context):
    context_is_none = context is None
    input_context = context if not context_is_none else {}

    obj = ftype()
    fields = get_class_fields(ftype)
    for itemname, itemtype in fields.items():
        itemvalue = decode(itemtype, input_context.get(itemname))
        setattr(obj, itemname, itemvalue)
    setattr(obj, '_pyrializer_is_null', context_is_none)
    return obj
