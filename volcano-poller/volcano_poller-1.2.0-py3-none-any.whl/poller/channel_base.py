#!/usr/bin/python3

'''
    Специфика каналов связана с их использованием в драйвере. Мне не нужна гора различных
    непредсказуемых Exception, потому что логика модуля подразумевает нормальную работу с ошибками В/В.
    В связи с этим все возможные ошибки должны быть сведены к одному исключению
        -   ConnectionError - при невозможности дальнейшего использования канала. При этом канал должен сам
                                закрываться. После повторного открытия канал снова можно использовать.
'''


class BaseChannel:
    # Doesnt' raise. Returns True if channel is connected
    def open(self, timeout_sec: float = 5.0, log=None) -> bool:
        raise NotImplementedError()

    # raise ConnectionError
    def reset_rcv_buf_x(self, log=None) -> None:
        self.read_x(0.0, log)

    # Doesnt' raise
    def safe_close(self, log=None) -> None:
        raise NotImplementedError()

    # Doesnt' raise
    def is_open(self) -> bool:
        raise NotImplementedError()

    # raise ConnectionError
    def write_all_x(self, data: (bytes, bytearray), log=None) -> None:
        raise NotImplementedError()

    # raise ConnectionError
    # if no data, returns empty bytes object
    def read_x(self, timeout_sec: float, log=None) -> bytes:
        raise NotImplementedError()
