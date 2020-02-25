"""Expose an example endpoints text console on the polling I/O implementation."""

# Builtins

import logging
import time

# Packages

from phylline.links.clocked import ClockedLink, LinkClockRequest
from phylline.util.timing import TimeoutTimer

from phyllo.io.cli.args.args import parse_args
from phyllo.io.cli.args.protocol import (
    args_application_stack, args_transport_logical_substack, group_protocol_stack
)
from phyllo.io.cli.stdin import input_literal
from phyllo.io.polling.serial import PollingSerialAdapter, connect_serial_retry
from phyllo.protocol.application.endpoints import EndpointHandler, SingleEndpointHandler
from phyllo.protocol.communication import AutomaticStack, CommunicationLinkData
from phyllo.protocol.communication import DATA_TYPES
from phyllo.protocol.stacks import make_preset_stack
from phyllo.util.logging import config_logging

from tests.io.polling.serial.console import ReceiveLoggerLink
from tests.io.polling.serial.receiver import receive_once_blocking, run_once


config_logging()
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class PingPongHandler(EndpointHandler, ClockedLink):
    """Handler for playing ping-pong in the background."""

    def __init__(self, ping_name=b'ping', pong_name=b'pong'):
        """Initialize members."""
        self.ping_name = ping_name
        self.pong_name = pong_name
        self.ping_counter = 0
        self.active = False
        super().__init__()
        self.pong_timer = TimeoutTimer(clock=self.clock)

    def make_ping(self):
        """Make a ping."""
        self.ping_counter += 1
        logger.info('Ping-pong sending ping {}'.format(self.ping_counter))
        return (self.ping_name, self.ping_counter)

    # Implement DataUnitLink

    def on_internal_data(self, parse_result, event):
        """Implement DataUnitLink.on_internal_data."""
        self.update_clock_time(event)
        if self.pong_timer.timed_out:
            self.pong_timer.reset_and_stop()
            self.directly_to_send_data(self.make_ping())

    # Implement EndpointHandler

    def match_receiver(self, endpoint_name):
        """Implement EndpointHandler.match_receiver."""
        return endpoint_name == self.pong_name

    def on_receiver_event(self, endpoint_name, data, source_event):
        """Implement EndpointHandler.on_receiver_event."""
        if endpoint_name == self.pong_name:
            logger.info('Ping-pong received pong {}'.format(data))
            self.pong_timer.start()
            clock_request = self.make_clock_request(self.pong_timer.timeout_time)
            if clock_request is not None:
                yield clock_request

    def on_sender_event(self, send_data):
        """Implement EndpointHandler.on_sender_event."""
        if send_data:
            logger.info('Starting ping-pong with interval of {} sec!'.format(send_data))
            self.pong_timer.timeout = send_data
            yield self.make_ping()
        else:
            logger.info('Stopping ping-pong.')
            self.pong_timer.reset_and_stop()


class LoggingHandler(SingleEndpointHandler):
    """Handler for logging send and receive data."""

    # Implement EndpointHandler

    def on_receiver_event(self, endpoint_name, data, source_event):
        """Implement EndpointHandler.on_receiver_event."""
        logger.info('{} response on {}: {}'.format(self.name, endpoint_name, data))
        yield from []

    def on_sender_event(self, send_data):
        """Implement EndpointHandler.on_receiver_event."""
        logger.info('{} requesting on {}: {}'.format(self.name, self.endpoint_name, send_data))
        yield (send_data, {})


def print_example_data():
    """Print examples of send data for handlers."""
    print('Example send data for echo handler: (\'echo\', (1, True, ("hello", None)))')
    print('Example send data for copy: (\'copy\', (1, True, ("hello", None)))')
    print('Example send data for reply: (\'reply\', True)')
    print('Example send data for reply: \'reply\'')
    print('Example send data for prefix: (\'prefix\', (\'world!\', \'hello, \'))')
    print('Example send data for blink: (\'blink\', True)')
    print('Example send data for blink: (\'blink\', False)')
    print('Example send data for ping-pong: (\'ping-pong\', 1.0)')
    print('Example send data for ping-pong: (\'ping-pong\', False)')


def send_data(data, handlers):
    """Send the data to its corresponding handler."""
    try:
        try:
            (handler_name, handler_args) = data
        except (ValueError, TypeError):
            handler_name = data
            handler_args = ()
        handler = handlers[handler_name]
        handler.send(CommunicationLinkData(
            handler_args, type=DATA_TYPES[('presentation', 'document')],
            direction='down', instance='console input', previous=data
        ))
    except (KeyError, IndexError, TypeError, ValueError):
        logger.exception('Ignored invalid input: {}'.format(data))


def run_console(stack, receiver, handlers):
    """Run the echo test."""
    print_example_data()
    while True:
        stack.update_clock()
        data = input_literal('Send: ')
        if data is not None:
            send_data(data, handlers)
        for i in range(2):  # read twice for starting and ending delimiters
            for received in receiver(stack):
                if isinstance(received, LinkClockRequest):
                    stack.update_clock_request(received)
                else:
                    print('Received: {}'.format(received))


def main(transport_logical_preset, application_preset):
    """Run echo test."""
    connection = connect_serial_retry(baudrate=115200, timeout=0.05)
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

    protocol = AutomaticStack(make_preset_stack(
        transport_logical=transport_logical_preset, application=application_preset
    ), list(handlers.values()), ReceiveLoggerLink())
    stack = PollingSerialAdapter(connection, protocol)
    logger.info(stack)

    time.sleep(1.0)
    run_once(run_console, stack, receive_once_blocking, handlers)
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
