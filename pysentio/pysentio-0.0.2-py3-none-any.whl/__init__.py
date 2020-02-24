from serial import Serial, SerialException
from const import NAME, VERSION, DEFAULT_BAUD, DEFAULT_SERIALPORT
import logging

_LOGGER = logging.getLogger(NAME)

class SentioPro:
    def __init__(self, port, baud, timeout=SERIAL_READ_TIMEOUT):
        self._port = port
        self._baud = baud
        self._timeout = timeout
        self._serial = Serial(self._port, self._baud, timeout=self._timeout)

    def open(self):
        self._serial.port = self._port
        self._serial.baudrate = self._baud
        self._serial.timeout = self._timeout
        self._serial.open()
        self._serial.flushInput()
        self._serial.flushOutput()

    def close(self):
        self._serial.close()

    def _write_cmd(self, cmd):
        """Write a cmd."""
        self._serial.write(cmd)

    def _write_read(self, msg):
        """Write to the port and read the return."""

        ret = ""

        try:
            if not self._serial.is_open:
                self._serial.open()
                print('Opened')
            mesg = msg.encode("utf-8")
            print('Cmd->{}'.format(msg))
            qq = self._serial.write(mesg)
            print('Bytes written {}'.format(qq))
            ret = self._serial.read_until(';\r\n'.encode('utf-8'), 400).decode("utf-8")
            print('Response->{}'.format(ret))
        except SerialException:
            _LOGGER.error("Problem communicating with %s", self._port)
#        self._serial.close()
        return ret

