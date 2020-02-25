"""Echo a payload on the polling I/O implementation."""

# Builtins

import logging
import time

# Packages

from phylline.util.logging import hex_bytes

from phyllo.io.cli.args.args import parse_args
from phyllo.io.cli.args.protocol import (
    args_application_stack, args_transport_logical_substack, group_protocol_stack
)
from phyllo.io.polling.serial import PollingSerialAdapter, connect_serial_retry
from phyllo.protocol.communication import DATA_TYPES, SERIALIZATION_FORMATS
from phyllo.protocol.stacks import make_preset_stack
from phyllo.util.logging import config_logging

from tests.io.polling.serial.receiver import receive_blocking, run_once


config_logging()
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def send_data(stack, data, log=True, **expected_data_kwargs):
    """Send data on the stack."""
    if log:
        try:
            logger.info('Sending: {}'.format(hex_bytes(data)))
        except (TypeError, ValueError):
            logger.info('Sending: {}'.format(data))
    if expected_data_kwargs:
        stack.send_data(data, **expected_data_kwargs)
    else:
        stack.send(data)


def run_echo(stack, receiver, sender, data, expected_data_kwargs, interval=1.0):
    """Run the echo test."""
    sender(stack, data, **expected_data_kwargs)
    for received in receiver(stack):
        logger.info('Received: {}'.format(received))
        time.sleep(interval)
        sender(stack, data, **expected_data_kwargs)


def make_send_data(application_preset):
    """Generate the data to send to the protocol."""
    if application_preset == 'none':
        # data = bytes([i for i in range(32)])
        # data = bytes([i for i in range(54)])  # for teensy 4.0
        data = bytes([i for i in range(54)])  # for teensy lc & micro
        data_kwargs = {}
    else:
        if application_preset == 'pubsub':
            # (data, schema) = (tuple(i for i in range(185 - 18)), 0x60)  # for due and teensy 4.0
            (data, schema) = (tuple(i for i in range(50 - 24)), 0x60)  # for teensy lc & micro
            # (data, schema) = (tuple(i for i in range(50 - 18)), 0x60)  # for uno

            data = (b'echo', data)
            # data = (b'copy', data)
            # data = (b'reply', data)
            # data = (b'ping', data)
            # (data, schema) = ((b'blink', True), 0x02)
            # (data, schema) = ((b'blink', False), 0x02)
            # (data, schema) = ((b'prefix', ('world!', 'Hello, ')), 0x00)
        elif application_preset == 'minimal':
            # (data, schema) = (tuple(i for i in range(185 - 18)), 0x60)  # for due and teensy 4.0
            (data, schema) = (tuple(i for i in range(50 - 24)), 0x60)  # for teensy lc & micro
            # (data, schema) = (tuple(i for i in range(50 - 18)), 0x60)  # for uno

            (data, schema) = (('hello', True, None, 0.125, b'\x00\x01\x02\x03\x04') + data, 0x00)
            # (data, schema) = (('hello', 123, 456, 789), 0x00)
        else:
            raise NotImplementedError('Unsupported protocol configuration!')

        data_kwargs = {
            'schema': schema,
            'format': SERIALIZATION_FORMATS[('binary', 'dynamic', 'msgpack')],
            'type': DATA_TYPES[('presentation', 'document')]
        }

    return (data, data_kwargs)


def main(transport_logical_preset, application_preset):
    """Run echo test."""
    connection = connect_serial_retry(baudrate=115200, timeout=1.0)
    if connection is None:
        logger.fatal('Failed to establish serial connection!')
        return

    protocol = make_preset_stack(
        transport_logical=transport_logical_preset, application=application_preset
    )
    stack = PollingSerialAdapter(connection, protocol)
    logger.info(stack)

    (data, data_kwargs) = make_send_data(application_preset)
    time.sleep(1.0)
    run_once(
        run_echo, stack, receive_blocking, send_data,
        data, expected_data_kwargs=data_kwargs
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
