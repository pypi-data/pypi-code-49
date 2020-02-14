from abc import abstractclassmethod
from abc import abstractmethod


class AbstractCompressedFileUtil:
    @abstractclassmethod
    def load_line_iterator(self, file_name: str) -> iter:
        """
        
        :param file_name: 
        :return: 
        """
        raise NotImplementedError
        pass

    @abstractclassmethod
    def load_lines(self, file_name: str) -> iter:
        """
        
        :param file_name: 
        :return: 
        """
        raise NotImplementedError

    @abstractclassmethod
    def compress_lines_to_archive(self, file_path: str, lines: str) -> None:
        """
        
        :param file_path: 
        :param lines: 
        :return: 
        """
        raise NotImplementedError

    @abstractclassmethod
    def compress_iterator_to_archive(self, file_path: str, line_iterator: iter) -> None:
        """
        
        :param file_path: 
        :param line_iterator: 
        :return: 
        """
        raise NotImplementedError
