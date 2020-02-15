from __future__ import annotations

from typing import List, Callable, Optional, Any, Dict
from datetime import timedelta

MetaInfo = Dict[str, Any] # JSON parsed dictionary containing metadata
ValConv = Callable[[Optional[Any]], Optional[Any]] # A function that converts one value to another value
ValConvMaker = Callable[[MetaInfo], ValConv] # A function that accepts col meta data and retuns a ValConv function

def mk_nullable(f : Callable) -> Callable:
	"returns a wrapped function that returns None if the first arg is None, otherwise call the wrapped function"
	def wrapper(arg) -> Optional[Any]:
		return None if arg is None else f(arg)
	return wrapper
