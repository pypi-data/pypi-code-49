import os

SUPPORTED_EXTENSIONS = ['.txt', '.pdf']


class ExtensionNotSupported(RuntimeError):
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
            raise ExtensionNotSupported(f"{extension} is not supported.")

        return open(filename, mode='r', encoding='utf-8') if extension == '.txt' else open(filename, mode='rb')

    @staticmethod
    def close(file):
        if file:
            file.close()

    @staticmethod
    def content_file(filename: str, file):
        extension = File.get_extension(filename)
        if extension not in SUPPORTED_EXTENSIONS:
            raise ExtensionNotSupported(f"{extension} is not supported.")

        if extension == '.txt':
            return file
