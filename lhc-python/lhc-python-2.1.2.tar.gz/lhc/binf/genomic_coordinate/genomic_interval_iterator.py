import gzip
import sys

from contextlib import contextmanager
from typing import Iterable, Optional, Type
from .genomic_interval import GenomicInterval


class GenomicIntervalIterator:

    EXTENSIONS = []

    def __next__(self) -> GenomicInterval:
        raise NotImplementedError('This method must be implemented in child class.')


@contextmanager
def open_iterator(filename: Optional[str], input_format: Optional[str], iterators: Iterable[Type[GenomicIntervalIterator]]) -> GenomicIntervalIterator:
    iterator_mapping = {}
    for iterator in iterators:
        for extension in iterator.EXTENSIONS:
            iterator_mapping[extension] = iterator

    if isinstance(filename, str):
        for input_format in iterator_mapping:
            if filename.endswith(input_format):
                break

    if input_format not in iterator_mapping:
        raise ValueError('unrecognised file format: {}'.format(input_format))

    fileobj = sys.stdin if filename is None else \
        gzip.open(filename, 'rt', encoding='utf-8') if filename.endswith('.gz') else \
        open(filename, encoding='utf-8')
    yield iterator_mapping[input_format](fileobj)
    fileobj.close()
