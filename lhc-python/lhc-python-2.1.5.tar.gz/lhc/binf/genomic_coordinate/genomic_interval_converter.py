from typing import Iterable, Optional, Type
from .genomic_interval import GenomicInterval


class GenomicIntervalConverter:

    EXTENSIONS = []

    def __iter__(self) -> Iterable[GenomicInterval]:
        raise NotImplementedError('This method must be implemented in child class.')

    def parse(self, line: str) -> GenomicInterval:
        raise NotImplementedError('This method must be implemented in child class.')

    def format(self, interval: GenomicInterval) -> str:
        raise NotImplementedError('This method must be implemented in child class.')


def get_converter(filename: Optional[str], file_format: Optional[str], converters: Iterable[Type[GenomicIntervalConverter]]) -> Type[GenomicIntervalConverter]:
    converter_mapping = {}
    for converter in converters:
        for extension in converter.EXTENSIONS:
            converter_mapping[extension] = converter

    if isinstance(filename, str):
        for file_format in converter_mapping:
            if filename.endswith(file_format):
                break

    if file_format not in converter_mapping:
        raise ValueError('unrecognised file format: {}'.format(file_format))

    return converter_mapping[file_format]
