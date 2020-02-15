"Data fixing decorator and ancilliary data conversion functions"

from typing import Dict, Callable
from collections import defaultdict
from json import loads
from .util import mk_nullable, MetaInfo, ValConv, ValConvMaker

from .interval import months, seconds

conv_fn: Dict[str, ValConvMaker] = defaultdict(lambda : lambda _ : lambda x: x)

def char_sizer(m: MetaInfo) -> ValConv:
	"returns a function that truncates not-None input string paramenter larger than passed size"
	size: int = m["MaxCharacterCount"]

	def wrapper(s: str) -> str:
		return s[:size]

	return mk_nullable(wrapper) if m["MayBeNull"] else wrapper

conv_fn["CHAR"] = char_sizer
conv_fn.update(months.register_conv_fn())
conv_fn.update(seconds.register_conv_fn())

def fix_data(cls):
	"Class Decorator that applies data conversion functions on cursor data"
	class Wrapper(cls):
		def __init__(self, *args, **kwargs):
			super().__init__(*args, **kwargs)
			self._meta: List[MetaInfo] = None
			self._fmap: List[ValConv] = None # A list of data conversion functions for each column in the result set

		def _readmeta(self):
			self._meta = self._fmap = None
			meta = super().fetchone()
			if meta is not None and len(meta) >= 8:
				self._meta = loads(meta[7])
				if self._meta is not None:
					self._fmap = [conv_fn[m["TypeName"]](m) for m in self._meta]

			super().nextset()

		def executemany(self, *args, **kwargs):
			xs = super().executemany(*args, **kwargs)
			self._readmeta()
			return xs

		def nextset(self):
			self._readmeta()
			return super().nextset()

		def __next__(self):
			row = super().__next__()
			if self._fmap is None or not row:
				return row

			return [f(v) for f, v in zip(self._fmap, row)]

		__iter__ = cls.__iter__
		__enter__ = cls.__enter__
		__exit__ = cls.__exit__

	return Wrapper
