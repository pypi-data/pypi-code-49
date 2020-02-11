import os
import functools
from typing import List

import PyPDF2


SUPPORTED_EXTENSIONS = ['.txt', '.pdf']


class ExceptionNotSupported(RuntimeError):
    ...


class File:

    @staticmethod
    def get_extension(filename: str) -> str:
        extension = -1
        return os.path.splitext(filename)[extension]

    @staticmethod
    def open(filename: str):
        """
        Define the mode to open the file based in its extension.
        :param filename:
        :return: 'r' or 'rb'
        """
        extension = File.get_extension(filename)
        if extension not in SUPPORTED_EXTENSIONS:
            raise ExceptionNotSupported(f"{extension} is not supported.")

        return open(filename, mode='r', encoding='utf-8') if extension == '.txt' else open(filename, mode='rb')

    @staticmethod
    def close(file):
        if file:
            file.close()

    @staticmethod
    def content_file(filename: str, file):
        extension = File.get_extension(filename)
        if extension not in SUPPORTED_EXTENSIONS:
            raise ExceptionNotSupported(f"{extension} is not supported.")

        if extension == '.txt':
            return file

        pdf_file_reader = PyPDF2.PdfFileReader(file)
        return PDF(pdf_file_reader).all()


class PDF:
    """TODO : reader pagination of .txt and .pdf files"""
    def __init__(self, file_reader):
        self._reader = file_reader
        self._page = 0

    def all(self):
        text = []
        for i in range(self._reader.numPages):
            text += self._reader.getPage(i).extractText().split("\n")
        return text


