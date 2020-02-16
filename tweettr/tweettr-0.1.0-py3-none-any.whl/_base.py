"""base class and casting descriptor for tweettr"""
__author__ = "Andreas Poehlmann"
__email__ = "andreas@poehlmann.io"

import re
from typing import Any, Dict, Literal, Union, get_args, get_origin, get_type_hints
# noinspection PyUnresolvedReferences
from typing import ForwardRef

__all__ = ['TweettrBase', 'enhance_type_hinted_classes_with_descriptors']


class TweettrDescriptor:
    """non-data descriptor to transform twitter 'objects' to python instances

    Allows attribute access through all defined levels of the tweet json
    """
    def __init__(self, name, type_cls, optional=False, as_list=False):
        self._name = name
        self._type_cls = type_cls
        self._optional = optional
        self._as_list = as_list

    def __get__(self, instance, owner):
        try:
            # this accesses the underlying dict of a tweettr instance directly
            values = instance[self._name]
        except KeyError:
            if self._optional:
                return None
            elif self._as_list:
                return []
            else:
                # the requested attribute is missing in the tweet json
                # this probably means you should label this attribute
                # as 'optional' in the relevant class
                raise AttributeError(f'"{owner.__name__}.{self._name}" not found')

        if self._optional and values is None:
            return None
        if self._as_list:
            return [self._type_cls(v) for v in values]

        return self._type_cls(values)


def _typing_to_np_doc(type_, level=0):
    """convert a type decoration used in Tweettr to np doc style type"""
    optional = False
    origin = get_origin(type_)
    t_args = get_args(type_)

    if origin is Union and type(None) in t_args:
        if level == 0:
            optional = True
        output = _typing_to_np_doc(t_args[0], level=level+1)
    elif origin is list:
        output = f'List[{_typing_to_np_doc(t_args[0], level=level+1)!s}]'
    elif origin is dict:
        output = f'Dict[{t_args[0]!s},{t_args[1]!s}]'
    elif origin is Literal:
        output = type(t_args[0]).__name__
    elif isinstance(type_, ForwardRef):
        output = type_.__forward_arg__
    elif type_ is Any:
        output = 'Any'
    else:
        output = type_.__name__

    if level == 0:
        return f'`{output!s}`{", optional" if optional else ""}'
    return output


class TweettrMeta(type):
    """meta class for TweettrBase"""
    def __new__(mcs, name, bases, attrs):
        # set slots if not defined.
        attrs.setdefault('__slots__', ())

        # add annotations in alphabetical order to docstring
        doc_str = attrs.get('__doc__', None)
        if doc_str:
            m = re.search(r"^(?P<indent>\s*)[{]attributes[}]\s*", doc_str, re.MULTILINE)
            if m:
                attribute_items = sorted(attrs.get('__annotations__', {}).items())
                doc_attrs = []
                for attr_name, attr_type in attribute_items:
                    type_str = _typing_to_np_doc(attr_type)
                    doc_attr = f'{attr_name}: {type_str}'
                    doc_attrs.append(doc_attr)
                indent = m.group('indent')
                rendered_attributes = f'\n{indent}'.join(doc_attrs)
                doc_str = doc_str.format(attributes=rendered_attributes)
                attrs['__doc__'] = doc_str

        return super().__new__(mcs, name, bases, attrs)


class TweettrBase(metaclass=TweettrMeta):
    """TweettrBase base class for attribute access to tweet dictionary

    Notes
    -----
      - getitem access provides access to all keys in the dictionary
      - attribute access requires the attribute to be type annotated
    """
    __slots__ = ('_dict', )

    def __init__(self, json_data: Dict[str, Any]):
        self._dict = json_data

    def __getattr__(self, item: str):
        if item in self.__annotations__:
            try:
                return self._dict[item]
            except KeyError:
                return None
        raise AttributeError(f"type object '{self.__class__.__name__}' has no attribute '{item}'")

    def __getitem__(self, item: str):
        return self._dict[item]


def enhance_type_hinted_classes_with_descriptors(cls):
    """enhances the provided cls with non-data descriptors

    attaches a TweettrDescriptor for each type annotated with a subclass of
    TweettrBase. This allows dynamic encapsulation into the specific TweettrBase
    subclass at runtime.

    """
    if not issubclass(cls, TweettrBase):
        raise ValueError(f'class has to be subclass of TweettrBase')
    # Note: the only reason this is required is because of ForwardRefs
    #   otherwise it would be cleaner to do this in the meta class
    type_hints = get_type_hints(cls)
    cls.__annotations__.update(type_hints)  # update with de-referenced hints

    for attr_name, attr_type in cls.__annotations__.items():

        origin = get_origin(attr_type)
        t_args = get_args(attr_type)

        optional = origin is Union and type(None) in t_args
        as_list = origin is list

        if optional or as_list:
            attr_type = t_args[0]

        if isinstance(attr_type, type) and issubclass(attr_type, TweettrBase):
            attr_desc = TweettrDescriptor(attr_name, attr_type,
                                          optional=optional, as_list=as_list)
            setattr(cls, attr_name, attr_desc)
