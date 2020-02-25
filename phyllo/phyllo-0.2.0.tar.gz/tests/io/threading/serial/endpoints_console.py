"""Expose an example endpoints text console on the polling I/O implementation."""

# Builtins

import logging
import time

# Packages

import blessed

from phyllo.io.cli.args.args import parse_args
from phyllo.io.cli.args.protocol import (
    args_application_stack, args_transport_logical_substack, group_protocol_stack
)
from phyllo.io.polling.serial import connect_serial_retry
from phyllo.io.threading.serial import ThreadedSerialAdapter
from phyllo.io.threading.serial import make_stack as make_threading_stack
from phyllo.io.tui.console import input_literal
from phyllo.protocol.communication import AutomaticStack, CommunicationLink
from phyllo.protocol.stacks import make_preset_stack
from phyllo.util.logging import config_logging

from tests.io.polling.serial.endpoints_console import (
    LoggingHandler, PingPongHandler, print_example_data, send_data
)
from tests.io.polling.serial.receiver import run_once


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
        print('Received: {}'.format(event))
        yield event


def run_console(stack, handlers, term):
    """Run the echo test."""
    print_example_data()
    while True:
        stack.update_clock()
        time.sleep(0.05)
        data = input_literal(term, 'Send: ')
        if data is not None:
            print('Send: {}'.format(data))
            send_data(data, handlers)


def main(transport_logical_preset, application_preset):
    """Run echo test."""
    connection = connect_serial_retry(baudrate=115200, timeout=None)
    if connection is None:
        logger.fatal('Failed to establish serial connection!')
        return

    handlers = {
        'echo': LoggingHandler(b'echo', name='Echo'),
        'copy': LoggingHandler(b'copy', name='Copy'),
        'reply': LoggingHandler(b'reply', name='Reply'),
        'prefix': LoggingHandler(b'prefix', name='Prefix'),
        'blink': LoggingHandler(b'blink', name='Blink'),
        'ping-pong': PingPongHandler()
    }

    term = blessed.Terminal()
    protocol = AutomaticStack(make_preset_stack(
        transport_logical=transport_logical_preset, application=application_preset
    ), list(handlers.values()), ReceiveLoggerLink())
    stack = ThreadedSerialAdapter(
        connection, make_threading_stack(protocol_stack=protocol)
    )
    logger.info(stack)

    time.sleep(1.0)
    run_once(run_console, stack, handlers, term)
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
