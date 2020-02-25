"""Print all data received on the serial port."""

# Builtins

import logging
import time

# Packages

from phylline.links.events import LinkException

from phyllo.io.cli.args.args import parse_args
from phyllo.io.cli.args.protocol import (
    args_application_stack, args_transport_logical_substack, group_protocol_stack
)
from phyllo.io.polling.serial import connect_serial_retry
from phyllo.protocol.stacks import make_preset_stack
from phyllo.util.logging import config_logging


config_logging()
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def receive_once_blocking(connection, protocol):
    """Receive any outstanding data on the stack."""
    protocol.to_read(connection.read_until(b'\0'))
    while protocol.has_receive():
        protocol.update_clock(time.time())
        data = protocol.receive()
        if isinstance(data, LinkException):
            logger.error('Unexpected error: {}'.format(data))
        else:
            yield data


def receive_blocking(connection, protocol):
    """Repeatedly receive data on the stack."""
    while True:
        yield from receive_once_blocking(connection, protocol)


def run_read(connection, protocol, receiver):
    """Print everything received by the stack."""
    protocol.update_clock(time.time())
    for received in receiver(connection, protocol):
        logger.info(received)


def run_once(runner, *args, **kwargs):
    """Run a runner function once and exit upon device disconnection or Ctrl+C."""
    try:
        runner(*args, **kwargs)
    except KeyboardInterrupt:
        print()
        logger.info('Received keyboard interrupt, wrapping up...')
    except ConnectionResetError:
        logging.error('Serial device disconnected!')


def main(transport_logical_preset, application_preset):
    """Run receive test.."""
    connection = connect_serial_retry(baudrate=115200, timeout=1.0)
    if connection is None:
        logger.fatal('Failed to establish serial connection!')
        return

    protocol = make_preset_stack(
        transport_logical=transport_logical_preset, application=application_preset
    )
    logger.info(protocol)

    run_once(run_read, connection, protocol, receive_blocking)
    logger.info('Quitting!')


if __name__ == '__main__':
    args = parse_args(
        grouped_args={
            group_protocol_stack: (
                args_transport_logical_substack, args_application_stack
            )
        },
        description='Print all data received on the serial port.'
    )
    main(args.logical, args.application)
