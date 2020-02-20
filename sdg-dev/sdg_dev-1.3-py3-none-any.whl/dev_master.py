"""
Created on 3 окт. 2019 г.
@author: chernecov

Модуть содержит класс DevMaster для обмена командами,
через подключаемый интерфейс ввода/вывода,
который должен иметь методы read/write и
вызывать исключение IOError при ошибках чтения/записи.

DevMaster умеет только передавать команды,
т.е. выполняет работу 'Главного' устройства.
"""

import logging
from time import time
from struct import unpack, calcsize
from sdg_utils import dump_bytes
from .dev_err import DevException, DevBadCode
from .protocol import Protocol

""" адрес широковещательной команды """
BROADCAST = b'\x00'


class DevMaster:
    """ Класс реализует работу 'Главного' на шине, умеет передавать команды
    функциями send() и sendto() с ожиданием ответа в течении 'timeout'
    и 'remix' кол-вом ретрансляций команды при отсутствии ответа.
    """

    def __init__(self,
                 io,
                 addr: bytes = None,
                 timeout=.1,
                 remix=3,
                 log=None):
        """ Конструктор класса 'Главного' устройства на шине.

        :param io: интерфейс ввода/вывода, должен иметь методы read(timeout)/write,
            для приема/передачи сообщений. В случае ошибок генерировать IOError.
        :param addr: по умолчанию без адреса, если задать, то при использовании
            метода send() команды будут адресованы устройству с этим адресом.
        :param timeout: таймаут ожидания ответа.
        :param remix: кол-во ретрансляций команды при отсутствии ответа.
        :param log: объект Logger, если не задать будет получен автоматот

        DevMaster генерирует исключение DevException, если:
        подчиненное устройство не ответило (DevNoAckException);
        подчиненное вернуло сообщение "недопустимая команда" (DevBadCmdException);
        при ошибке ввода/вывода, перехватывается IOError (DevIOException).
        """
        self._name = f"{self.__class__.__name__}"
        self._io = io
        self._addr = addr or b''
        self._remix = remix
        self._timeout = timeout
        self.log = log or logging.getLogger(f'{self._name}')
        self.log.info(f"Device '{self._name}' open")
        self._prtcl = None

    def set_io(self, io) -> None:
        """ Задавать интерфейс ввода/вывода можно на ходу. Потребность в горячей
        смене интерфейса, может показаться странной, но она возникла для
        организации автопоиска устройства по доступным интерфейсам (портам).

        :param io: обьект интерфейса вводв/вывода, или None для
            освобождения предыдущего подключенного интерфейса.
        """
        self._io = io

    def set_protocol(self, protocol):
        """Подключить расшифровщик обмена"""
        assert(isinstance(protocol, Protocol))
        self._prtcl = protocol

    def close(self):
        """ Закрыть устройство"""
        self.log.info(f"Device '{self._name}' close")

    def send(self, msg: bytes, ackfrmt='raw', timeout=None, remix=None):
        """ Передать команду подчиненному. При невозможности отправить команду
        через интерфейс ввода/вывода, отсутствии ответа подчиненного или ответа
        "недопустимая команда" генерируется исключение DevException.

        :param msg: код команды + данные при необходимости.
        :param ackfrmt: формат ожидаемого ответа, смотрите в описании модуля 'struct',
                        https://docs.python.org/2/library/struct.html#format-characters
        :param timeout: таймаут ожидания ответа, переопределяет глобальный параметр.
        :param remix: кол-во ретрансляций при отсутствии ответа, переопределяет глобальный.
        :return: ответ подчиненного - кортеж данных в соответствии ackfrmt
            если в кортеже один элемент, то возвращается его значение,
            если ackfrmt='' т.е. ожидалось пустое сообщение, возвращает True,
            если ackfrmt='raw' возвращает (сырые данные) нераспакованный массив bytes.
        """
        return self.sendto(self._addr, msg, ackfrmt, timeout, remix)

    def sendto(self, addr: bytes, msg: bytes, ackfrmt='raw', timeout=None, remix=None):
        """ Передать команду подчиненному с адресом 'addr', если
        addr=BROADCAST, то команда широковещательная. Остальное аналогично send().
        """
        assert (msg and type(msg) is bytes)
        if not self._io:
            raise DevException(f"DevException '{self._name}'._io is None!")

        c = CmdMaster(addr, msg, ackfrmt, self.log,
                      timeout if timeout is not None else self._timeout,
                      remix or self._remix, self._prtcl)
        try:
            rx = None
            while c.is_alive():
                tx = c.check_tx()
                if tx:
                    self._io.write(tx)
                rx = self._io.read(timeout=0.02)
                ack = c.check_rx(rx)
                if type(ack) is DevBadCode:
                    raise DevException(f"DevException '{self._name}' Received", badcode=c.ack)
                if ack is not None:
                    return ack
            raise DevException(f"DevException '{self._name}' No answer for cmd{c.name}! {dump_bytes(rx)}")
        except IOError as e:
            raise DevException(f"DevException '{self._name}'._io err > {e}")


class CmdMaster:
    """ Это вспомогательный ксасс для работы SdgMaster
    представляющий каждую команду как отдельный объект"""

    def __init__(self, addr, msg, ackfrmt, log, timeout, remix, prtcl):
        self.log = log
        self.addr = addr or b''
        self.msg = msg
        self.ackfrmt = ackfrmt
        self.TIMEOUT = timeout
        self.REMIX = remix
        self.live = 2 + remix
        self.time = 0
        self.ack = None
        str_addr = f"{addr[0]:02x}:" if addr else ''
        self.name = f"[{str_addr}{msg[0]:02x}]"
        self.prtcl = prtcl

    def is_alive(self):
        """ Жива ли команда? """
        return self.live

    def check_tx(self):
        """ Передает команду когда пришло время очередной попытки """
        if self.live and time() > self.time:
            self.time = time() + self.TIMEOUT
            self.live -= 1
            if self.live:
                ts = '' if self.live > self.REMIX else f"?{self.REMIX - self.live + 1}"
                tx = self.addr + self.msg
                note = self.prtcl.note(tx) if self.prtcl else ""
                self.log.debug(f">cmd{self.name}{ts} {note}".rstrip() + ' ' + dump_bytes(tx))
                # если команда широковещательная ретрансляций нет
                if self.addr == BROADCAST:
                    self.live = 1
                return tx

    def check_rx(self, rx):
        """ Проверяет является ли принятое сообщение ответом на команду"""
        ts = dump_bytes(rx)
        note = self.prtcl.note(rx) if self.prtcl else ""
        # для обработки BROADCAST, функция должна вызываться и при отсутствии rx
        if self.addr == BROADCAST and not self.live:
            # на широковещательные сообщения ответ True перед смертью
            self.log.debug(f"<ack{self.name} is broadcast")
            self.ack = True
        # адрес совпал
        elif not self.addr or (rx and rx[0] == self.addr[0]):
            if self.addr:
                rx = rx[1:]
            # код совпал
            if rx and rx[0] == self.msg[0] | 0x80:
                # любой размер (сырые данные)
                if self.ackfrmt == 'raw':
                    self.ack = rx[1:]
                # размер совпадает
                elif calcsize(self.ackfrmt) == len(rx) - 1:
                    if self.ackfrmt == '':
                        self.ack = True
                    else:
                        ack = unpack(self.ackfrmt, rx[1:])
                        self.ack = ack[0] if len(ack) == 1 else ack
                # неправильный размер сообщения
                else:
                    waitsize = 1 + calcsize(self.ackfrmt) + len(self.addr)
                    self.log.warning(f"<ack{self.name}!size wait({waitsize})!={ts}")
                if self.ack is not None:
                    self.log.debug(f"<ack{self.name} {note}".rstrip() + ' ' + ts)
            # недопустимая команда
            elif rx and rx[0] == 0xF0 and rx[1] == self.msg[0]:
                badcode = DevBadCode(-rx[2] if len(rx) == 3 else 0)
                self.log.debug(f"<ack{self.name}!{badcode} {ts}")
                self.ack = badcode
        return self.ack
