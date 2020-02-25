"""Expose a protocol text console on the polling I/O implementation."""

# Builtins

import logging
import time

# Packages

from phyllo.io.cli.args.args import parse_args
from phyllo.io.cli.args.protocol import (
    args_application_stack, args_transport_logical_substack, group_protocol_stack
)
from phyllo.io.cli.stdin import input_literal
from phyllo.io.polling.serial import PollingSerialAdapter, connect_serial_retry
from phyllo.protocol.communication import AutomaticStack, CommunicationLink
from phyllo.protocol.stacks import make_preset_stack
from phyllo.util.logging import config_logging

from tests.io.polling.serial.echo import make_send_data, send_data
from tests.io.polling.serial.receiver import receive_once_blocking, run_once


config_logging()
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class ReceiveLoggerLink(CommunicationLink):
    """Log all received data."""

    def __init__(self, name=None):
        """Initialize members."""
        super().__init__(
            name=name, receiver_event_passthrough=True, sender_event_passthrough=True
        )

    def receiver_process(self, event):
        """Override CommunicationLink.receiver_process."""
        logger.info('Received: {}'.format(event))
        yield event


def run_console(stack, receiver, sender, application_preset):
    """Run the echo test."""
    logger.info('Example send data: {}'.format(make_send_data(application_preset)[0]))
    while True:
        data = input_literal('Send: ')
        if data is not None:
            sender(stack, data)
        for i in range(2):  # read twice for starting and ending delimiters
            for received in receiver(stack):
                pass


def main(transport_logical_preset, application_preset):
    """Run echo test."""
    connection = connect_serial_retry(baudrate=115200, timeout=0.05)
    if connection is None:
        logger.fatal('Failed to establish serial connection!')
        return

    protocol = AutomaticStack(make_preset_stack(
        transport_logical=transport_logical_preset, application=application_preset
    ), ReceiveLoggerLink())
    stack = PollingSerialAdapter(connection, protocol)
    logger.info(stack)

    time.sleep(1.0)
    run_once(
        run_console, stack, receive_once_blocking, send_data, application_preset
    )
    logger.info('Quitting!')


if __name__ == '__main__':
    args = parse_args(
        grouped_args={
            group_protocol_stack: (
                args_transport_logical_substack, args_application_stack
            )
        },
        description='Run console test.'
    )

    main(args.logical, args.application)
