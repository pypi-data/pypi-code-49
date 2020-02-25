"""Echo a payload on the threading I/O implementation."""

# Builtins

import logging
import time

# Packages

from phylline.util.logging import hex_bytes

from phyllo.io.cli.args.args import parse_args
from phyllo.io.cli.args.protocol import (
    args_application_stack, args_transport_logical_substack, group_protocol_stack
)
from phyllo.io.polling.serial import connect_serial_retry
from phyllo.io.threading.serial import ThreadedSerialAdapter
from phyllo.io.threading.serial import make_stack as make_threading_stack
from phyllo.protocol.stacks import make_preset_stack
from phyllo.util.logging import config_logging

from tests.io.polling.serial.echo import make_send_data, run_echo
from tests.io.polling.serial.receiver import run_once
from tests.io.threading.serial.receiver import receive_blocking


config_logging()
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def send_data(stack, data, log=True, **expected_data_kwargs):
    """Send data on the stack."""
    if log:
        try:
            logger.info('Sending: {}'.format(hex_bytes(data)))
        except TypeError:
            logger.info('Sending: {}'.format(data))
    with stack.pipeline_lock:
        if expected_data_kwargs:
            stack.send_data(data, **expected_data_kwargs)
        else:
            stack.send(data)


def main(transport_logical_preset, application_preset):
    """Run echo test."""
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

    (data, data_kwargs) = make_send_data(application_preset)
    time.sleep(1.0)
    run_once(
        run_echo, stack, receive_blocking, send_data, data,
        expected_data_kwargs=data_kwargs
    )
    logger.info('Quitting!')


if __name__ == '__main__':
    args = parse_args(
        grouped_args={
            group_protocol_stack: (
                args_transport_logical_substack, args_application_stack
            )
        },
        description='Run payload echo test.'
    )

    main(args.logical, args.application)
