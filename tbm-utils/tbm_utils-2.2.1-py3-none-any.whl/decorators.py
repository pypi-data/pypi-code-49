__all__ = [
	'cast_to_list',
	'datareader',
]

import functools

import wrapt

from .io import DataReader


def cast_to_list(position):
	"""Cast the positional argument at given position into a list if not already a list."""

	@wrapt.decorator
	def wrapper(wrapped, instance, args, kwargs):
		if not isinstance(args[position], list):
			args = list(args)
			args[position] = [args[position]]
			args = tuple(args)

		return wrapped(*args, **kwargs)

	return wrapper


def datareader(wrapped=None, *, position=0):
	"""Cast the positional argument at given position to :class:`DataReader`."""

	if wrapped is None:  # pragma: nocover
		return functools.partial(datareader, position=position)

	@wrapt.decorator
	def wrapper(wrapped, instance, args, kwargs):
		if not isinstance(args[position], DataReader):
			args = list(args)
			data = DataReader(args[position])
			args = (data, *args[1:])

		return wrapped(*args, **kwargs)

	return wrapper(wrapped)
