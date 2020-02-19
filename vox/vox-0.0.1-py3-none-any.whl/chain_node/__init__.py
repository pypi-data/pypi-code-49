"""ChainMap that works like nodes and objects."""

import collections
from typing import Any, Dict, MutableMapping, Optional


class ChainMap(MutableMapping[str, Any]):
    """
    A ChainMap that acts like a Node.

    This is useful for scopes that need the nodes to be moved around.
    Whilst possible with collections.ChainMap, it's designed for create
    once, not create and mutate multiple times.
    
    >>> parent = {'a': 1, 'b': 2, 'c': 3}
    >>> cm = ChainMap(parent, b='y', c='z')
    >>> cm['a']
    1
    >>> cm['b']
    'y'
    >>> cm['c']
    'z'
    >>> cm.parent = {'a': 'foo'}
    >>> cm['a']
    'foo'
    """

    __slots__ = ("_parent", "_values", "_chain")

    _values: Dict[str, Any]
    _parent: MutableMapping[str, Any]
    _chain: MutableMapping[str, Any]

    def __init__(
        self, parent: Optional[MutableMapping[str, Any]] = None, **kwargs: Any
    ) -> None:
        self._values = kwargs
        self.parent = parent

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent
        parents = [self._values] + ([] if parent is None else [parent])
        self._chain = collections.ChainMap(*parents)

    def __repr__(self):
        keys = {
            "parent": id(self._parent),
            **self._values,
        }
        values = ", ".join(f"{key}={value!r}" for key, value in keys.items())
        return f"{type(self).__qualname__}({values})"

    def __getitem__(self, key: str) -> Any:
        return self._chain[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self._values[key] = value

    def __delitem__(self, key: str) -> None:
        del self._values[key]

    def __iter__(self):
        return iter(self._chain)

    def __len__(self):
        return len(self._chain)

    def copy(self):
        return type(self)(self._parent, **self._values)

    def update(self, other):
        """
        Update values with another mapping.
        
        If the other mapping is a ChainMap then it will only update by
        the leafs values.

        >>> parent = {'a': 1}
        >>> cm_1 = ChainMap(parent, b=2)
        >>> cm_2 = ChainMap(c=3)
        >>> cm_2.update(cm_1)
        >>> cm_2['c']
        3
        >>> cm_2['b']
        2
        >>> cm_2['a']
        KeyError: ...
        """
        if isinstance(other, ChainMap):
            other = other._values
        if not isinstance(other, collections.abc.Mapping):
            raise TypeError(f"Unknown type {type(other)}")
        self._values.update(other)


class ChainObject(ChainMap):
    """
    A ChainMap that can be accessed via attributes.

    This allows for easier to work with objects, and allows easy typing.

    >>> class Foo(ChainObject):
    ...     a: int
    ...     b: int
    ... 
    >>> parent = {'a': 1}
    >>> f = Foo(parent, b=2)
    >>> f.a
    1
    >>> f.b
    2
    """

    def __getattr__(self, key):
        if key in dir(self):
            return super().__getattribute__(key)
        try:
            return self[key]
        except KeyError:
            raise AttributeError(f"Attribute {key} doesn't exist") from None

    def __setattr__(self, key, value):
        if key in dir(self):
            super().__setattr__(key, value)
        else:
            self[key] = value

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError:
            raise AttributeError(f"Attribute {key} doesn't exist") from None
