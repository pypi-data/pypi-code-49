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

	def peek(self, size=DEFAULT_BUFFER_SIZE):
		if size > DEFAULT_BUFFER_SIZE:
			size = DEFAULT_BUFFER_SIZE

		peeked = super().peek(size)[:size]

		if len(peeked) < size:
			peeked = self.read(size)
			self.seek(-len(peeked), os.SEEK_CUR)

		return peeked
