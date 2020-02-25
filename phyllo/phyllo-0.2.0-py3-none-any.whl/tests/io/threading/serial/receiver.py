"""Print all data received on the serial port."""

# Builtins

import logging

# Packages

from phylline.links.events import LinkException

from phyllo.io.cli.args.args import parse_args
from phyllo.io.cli.args.protocol import (
    args_application_stack, args_transport_logical_substack, group_protocol_stack
)
from phyllo.io.polling.serial import connect_serial_retry
from phyllo.io.threading.serial import ThreadedSerialAdapter
from phyllo.io.threading.serial import make_stack as make_threading_stack
from phyllo.protocol.stacks import make_preset_stack
from phyllo.util.logging import config_logging

from tests.io.polling.serial.receiver import run_once, run_read


config_logging()
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def receive_blocking(stack):
    """Repeatedly receive data on the stack."""
    while stack.has_receive.acquire():
        data = stack.receive()
        if isinstance(data, LinkException):
            logger.error('Unexpected error: {}'.format(data))
        else:
            yield data
    if stack.receiver_disconnected:
        raise ConnectionResetError


def main(transport_logical_preset, application_preset):
    """List the ports."""
    connection = connect_serial_retry(baudrate=115200, timeout=1.0)
    if connection is None:
        logger.fatal('Failed to establish serial connection!')
        return

    protocol = make_preset_stack(
        transport_logical=transport_logical_preset, application=application_preset
    )
    stack = ThreadedSerialAdapter(
        connection, make_threading_stack(protocol_stack=protocol)
    )
    logger.info(stack)

    run_once(run_read, stack, receive_blocking)
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
