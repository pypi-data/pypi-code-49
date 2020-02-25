from .util import get_array_type
from .util import get_class_fields

__all__ = [
    'encode'
]


def encode(ftype, context):
    if context is None:
        return None
    elif ftype is None:
        return context
    elif ftype in [str, bool, int, float]:
        return _encode_primitive(ftype, context)
    elif type(ftype) is list:
        return _encode_array(ftype, context)
    elif isinstance(context, object):
        return _encode_object(ftype, context)
    raise ValueError(f'Cannot encode type {ftype} with context {context}')


def _encode_primitive(ftype, context):
    context_type = type(context)
    if context_type is not ftype:
        raise ValueError(f'Cannot encode type {ftype} with context {context}')
    return context


def _encode_array(ftype, context):
    item_type = get_array_type(ftype)
    return [encode(item_type, item) for item in context]


def _encode_object(ftype, context):
    object_is_null = getattr(context, '_pyrializer_is_null', False)
    if object_is_null:
        return None

    dictionary = {}
    fields = get_class_fields(ftype)
    for itemname, itemtype in fields.items():
        itemcontext = getattr(context, itemname)
        dictionary[itemname] = encode(itemtype, itemcontext)
    return dictionary
