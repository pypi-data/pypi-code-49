from typing import Union, Iterable

Primitive = Union[int, float, str, bytes, bool, None]
ConnEntryValue = Union[Primitive, Iterable[Primitive]]
