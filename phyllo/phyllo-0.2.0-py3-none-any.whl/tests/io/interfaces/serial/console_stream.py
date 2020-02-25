"""Send and receive bytes on the serial port."""

# Builtins

import logging

# Packages

from phyllo.io.polling.serial import connect_serial_retry


logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def main():
    """List the ports."""
    connection = connect_serial_retry(baudrate=115200, timeout=1.0)
    read = b''
    while True:
        try:
            write = input('Write: ')
            if not write:
                raise EOFError
            write = write.encode('ascii') + b'\0'
            connection.write(write)
            read += connection.read_until(b'\0')
            if len(read) > 1:
                print(read)
                read = b''
        except (KeyboardInterrupt, EOFError):
            print()
            print('Quitting!')
            return


if __name__ == '__main__':
    main()
