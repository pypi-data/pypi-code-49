__all__ = [
	'DataReader',
]

import os
from io import (
	DEFAULT_BUFFER_SIZE,
	BufferedReader,
	BytesIO,
	FileIO,
)


class DataReader(BufferedReader):
	"""A buffered reader wrapper.

	It includes support for filepaths, file-like objects, and bytes-like objects.

	Parameters:
		data (DataReader, BufferedReader, os.PathLike, str, bytes, bytearray, memoryview):
			The object to provide the :class:`BufferedReader` interface for.
		buffer_size(int): The size of the internal buffer. (Default: io.DEFAULT_BUFFER_SIZE)
	"""
	def __init__(
		self,
		data,
		buffer_size=DEFAULT_BUFFER_SIZE,
	):
		if isinstance(data, (BufferedReader, DataReader)):
			if isinstance(data.raw, FileIO):
				data = FileIO(data.name, 'rb')
			else:
				data = BytesIO(data.read())
		elif isinstance(data, (os.PathLike, str)):
			data = FileIO(data, 'rb')
		elif isinstance(data, (bytearray, bytes, memoryview)):
			data = BytesIO(data)

		super().__init__(data, buffer_size=buffer_size)

		self.accumulator = 0
		self.bit_count = 0

	def peek(self, size=DEFAULT_BUFFER_SIZE):
		if size > DEFAULT_BUFFER_SIZE:
			size = DEFAULT_BUFFER_SIZE

		peeked = super().peek(size)[:size]

		if len(peeked) < size:
			peeked = self.read(size)
			self.seek(-len(peeked), os.SEEK_CUR)

		return peeked

	def read(self, size=-1):
		self.accumulator = 0
		self.bit_count = 0

		return super().read(size)

	# From https://rosettacode.org/wiki/Bitwise_IO#Python
	def _readbit(self):
		if not self.bit_count:
			a = self.read(1)

			if a:  # pragma: nobranch
				self.accumulator = ord(a)

			self.bit_count = 8

		rv = (self.accumulator & (1 << self.bit_count - 1)) >> self.bit_count - 1

		self.bit_count -= 1

		return rv

	def readbits(self, n):
		v = 0
		while n > 0:
			v = (v << 1) | self._readbit()
			n -= 1

		return v
