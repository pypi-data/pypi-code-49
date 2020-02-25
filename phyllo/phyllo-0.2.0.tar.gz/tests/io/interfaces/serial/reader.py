"""Print all data read on the serial port."""

# Builtins

import logging

# Packages

from phyllo.io.polling.serial import connect_serial_retry
from phyllo.util.logging import config_logging

from serial.serialutil import SerialException


config_logging()
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def main():
    """Run read test."""
    connection = connect_serial_retry(baudrate=115200, timeout=None)
    read = b''
    while True:
        try:
            read += connection.read_until(b'\0')
            if len(read) > 1:
                logger.info(read)
                read = b''
        except SerialException:
            logging.error('Serial device disconnected!')
            return
        except (KeyboardInterrupt, EOFError):
            print()
            logger.info('Quitting!')
            return


if __name__ == '__main__':
    main()
