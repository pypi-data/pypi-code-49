#!/usr/bin/python3
import serial

from volcano.general.xml_reader import XmlReader, LoadException

from . import channel_base

g_parity_map = {
    'N': serial.PARITY_NONE,
    'E': serial.PARITY_EVEN,
    'O': serial.PARITY_ODD,
}
g_bytesize_map = {
    '8': serial.EIGHTBITS,
}
g_stopbits_map = {
    '1': serial.STOPBITS_ONE,
}


# throws ValueError
# s = '9600 8n1'
def parse_serial_options(s: str) -> dict:
    assert isinstance(s, str), s

    words = s.split(' ')
    if len(words) != 2:
        raise ValueError('Should be 2 words')

    if len(words[1]) != 3:
        raise ValueError('Second item should be in form 8n1')

    baudrate = int(words[0])    # ! ValueError
    if baudrate not in [9600, 19200, 38400]:
        raise ValueError('Invalid baudrate value: {}'.format(baudrate))

    bytesize = words[1][0]
    if bytesize not in g_bytesize_map:
        raise ValueError('Invalid data bits value: {}'.format(bytesize))

    parity = words[1][1].upper()
    if parity not in g_parity_map:
        raise ValueError('Invalid parity: {}'.format(parity))

    stopbits = words[1][2]
    if stopbits not in g_stopbits_map:
        raise ValueError('Invalid stop bits value: {}'.format(stopbits))

    return {
        'baudrate': baudrate,
        'bytesize': g_bytesize_map[bytesize],
        'parity': g_parity_map[parity],
        'stopbits': g_stopbits_map[stopbits]
    }


class SerialChannel(channel_base.BaseChannel):
    def __init__(self, node):
        p = XmlReader(node)

        self.device_name_ = p.get_str('serial.device')

        params_s = p.get_str('serial.params')
        try:
            self.params_ = parse_serial_options(params_s)
        except ValueError as ex:
            raise LoadException('Parameters are invalid: {}'.format(ex), node)

        self.port_ = serial.Serial()

        self.port_.port = self.device_name_
        self.port_.baudrate = self.params_['baudrate']
        self.port_.parity = self.params_['parity']
        self.port_.bytesize = self.params_['bytesize']
        self.port_.stopbits = self.params_['stopbits']

    def open(self, timeout_sec: float = 5.0, log=None) -> bool:
        self.safe_close(log)

        try:
            self.port_.open()
        except Exception as ex:
            self.safe_close(log)
            log.error('Could not open port %s:%s - %s', self.device_name_, self.params_, ex)
            return False

        return True

    def safe_close(self, log=None) -> None:
        if self.is_open():
            self.port_.close()

    def is_open(self) -> bool:
        # https://stackoverflow.com/questions/41987168/serial-object-has-no-attribute-is-open
        # PySerial had isOpen() function until v3.0
        if float(serial.VERSION) < 3.0:
            return self.port_.isOpen()
        else:
            return self.port_.is_open

    def write_all_x(self, data: (bytes, bytearray), log=None) -> None:
        assert isinstance(data, (bytes, bytearray)), data

        if not self.is_open():
            raise ConnectionError('Cant write to closed channel')

        try:
            self.port_.write(data)
        except Exception as ex:
            self.safe_close(log)
            raise ConnectionError('Could not send data: {}'.format(ex))

    def read_x(self, timeout_sec: float, log=None) -> bytes:
        if not self.is_open():
            raise ConnectionError('Cant read from closed channel')

        self.port_.timeout = timeout_sec
        d = self.port_.read(1)
        return d
