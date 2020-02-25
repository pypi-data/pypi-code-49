"""Print all data received on the serial port."""

# Builtins

import logging

# Packages

from phylline.links.events import LinkException

from phyllo.io.cli.args.args import parse_args
from phyllo.io.cli.args.protocol import (
    args_application_stack, args_transport_logical_substack, group_protocol_stack
)
from phyllo.io.polling.serial import PollingSerialAdapter, connect_serial_retry
from phyllo.protocol.stacks import make_preset_stack
from phyllo.util.logging import config_logging

from tests.io.interfaces.serial.receiver import run_once as run_once_generic


config_logging()
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def receive_once_blocking(stack):
    """Receive outstanding data on the stack."""
    stack.update_clock()
    stack.to_read(block_until=b'\0')
    while stack.has_receive():
        stack.update_clock()
        data = stack.receive()
        if isinstance(data, LinkException):
            logger.error('Unexpected error: {}'.format(data))
        else:
            yield data


def receive_blocking(stack):
    """Repeatedly receive data on the stack."""
    while True:
        yield from receive_once_blocking(stack)


def run_read(stack, receiver):
    """Print everything received by the stack."""
    for received in receiver(stack):
        logger.info(received)


def run_once(runner, stack, *args, **kwargs):
    """Run a runner function once, setting up and tearing down the stack as needed."""
    stack.start()
    run_once_generic(runner, stack, *args, **kwargs)
    logger.info('Cleaning up...')
    stack.stop()


def main(transport_logical_preset, application_preset):
    """List the ports."""
    connection = connect_serial_retry(baudrate=115200, timeout=1.0)
    if connection is None:
        logger.fatal('Failed to establish serial connection!')
        return

    protocol = make_preset_stack(
        transport_logical=transport_logical_preset, application=application_preset
    )
    stack = PollingSerialAdapter(connection, protocol)
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
