import gzip
import sys

from contextlib import contextmanager
from typing import Iterable, Optional, Type
from .genomic_interval import GenomicInterval


class GenomicIntervalFormatter:

    EXTENSIONS = []

    def format(self, interval: GenomicInterval) -> str:
        raise NotImplementedError('This method must be implemented in child class.')


def get_formatter(filename: Optional[str], output_format: Optional[str], formatters: Iterable[Type[GenomicIntervalFormatter]]) -> GenomicIntervalFormatter:
    formatter_mapping = {}
    for writer in formatters:
        for extension in writer.EXTENSIONS:
            formatter_mapping[extension] = writer

    if isinstance(filename, str):
        for output_format in formatter_mapping:
            if filename.endswith(output_format):
                break

    if output_format not in formatter_mapping:
        raise ValueError('unrecognised file format: {}'.format(output_format))

    return formatter_mapping[output_format]()
