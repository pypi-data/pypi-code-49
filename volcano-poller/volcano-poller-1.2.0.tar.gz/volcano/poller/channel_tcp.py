#!/usr/bin/python3
import socket
import select

from volcano.general.xml_reader import XmlReader

from . import channel_base


class TcpChannel(channel_base.BaseChannel):
    def __init__(self, node):
        p = XmlReader(node)

        self.ip_addr_ = p.get_str('tcp.ipAddr')
        self.tcp_port_ = p.get_int('tcp.tcpPort')

        self.sock_ = None

    def open(self, timeout_sec: float = 5.0, log=None) -> bool:
        self.safe_close(log)

        if log:
            log.debug('Connecting to {}:{} ...'.format(self.ip_addr_, self.tcp_port_))

        try:
            # self.sock_ = socket.socket()
            # self.sock_.connect ((self.ip_addr_, self.tcp_port_))
            self.sock_ = socket.create_connection((self.ip_addr_, self.tcp_port_), timeout=timeout_sec)
        except Exception as e:
            if log:
                log.warning('Could not connect to {}:{} - {}'.format(self.ip_addr_, self.tcp_port_, e))
            self.safe_close(log)
            return False

        if log:
            log.debug('Connected to {}:{}'.format(self.ip_addr_, self.tcp_port_))

        return True

    def safe_close(self, log=None) -> None:
        if self.sock_ is None:
            return
            
        if log:
            log.debug('Shutdown socket...')

        try:
            self.sock_.shutdown(1)
        except Exception as ex:
            if log:
                log.warning('Error shutdown socket: {}'.format(ex))
            
        if log:
            log.debug('Close socket...')
        try:
            self.sock_.close()
        except Exception as ex:
            if log:
                log.warning('Error closing socket: {}'.format(ex))
                
        self.sock_ = None

    def is_open(self) -> bool:
        return self.sock_ is not None

    def write_all_x(self, data: (bytes, bytearray), log=None) -> None:
        assert isinstance(data, (bytes, bytearray)), data

        if not self.is_open():
            raise ConnectionError('Cant write to closed channel')

        try:
            self.sock_.sendall(data)
        except Exception as ex:
            if log:
                log.warn('Error writing socket: %s', ex)
            self.safe_close(log)
            raise ConnectionError('Could not send data: {}'.format(ex))

    def read_x(self, timeout_sec: float, log=None) -> bytes:

        if not self.is_open():
            raise ConnectionError('Cant read from closed channel')

        fd_read, fd_write, fd_err = select.select([self.sock_], [], [], timeout_sec)    # pylint: disable=unused-variable
        if self.sock_ in fd_read:
            try:
                data = self.sock_.recv(1024)
            except Exception as ex: # Выбрасывает исключения. Я вообще не понимаю, откуда инфа, что при ошибках возвр None
                if log:
                    log.warn('Error reading socket: %s', ex)
                self.safe_close(log)
                raise ConnectionError(ex)
                
            if data:
                return data
            else:
                self.safe_close(log)
                raise ConnectionError('Channel closed while reading')
        else:
            return b''
