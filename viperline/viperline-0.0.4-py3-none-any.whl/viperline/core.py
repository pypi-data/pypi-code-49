import csv
from typing import Iterator
from enum import Enum


class ProcessingMode(Enum):
    MULTI_PROCESSING = "multiprocessing"
    MULTI_THREADING = "multithreading"
    DEFAULT = "default"


def load(file_name: str, processing_mode: ProcessingMode) -> Iterator[str]:
    if processing_mode == ProcessingMode.DEFAULT:
        try:
            with open(file_name) as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
        except Exception as err:
            print(
                'Error opening file {}'.format(file_name),
                '{}'.format(err)
            )
    # if processing_mode == ProcessingMode.MULTI_THREADING:
        # use threading to read pieces of file concurrently
    # if processing_mode == ProcessingMode.MULTI_PROCESSING:
        # use multiprocessing read pieces of file in parallel
        # join pieces of file
        # return file iterator


# def transform():
    # if threading option
    # use threading to transform data concurrently
    # transform row using function
    # if multiprocessing option
    # use multiprocessing read pieces of data in parallel
    # transform row using function
    # join data pieces
    # return data iterator
