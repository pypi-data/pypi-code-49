"""Echo a payload on the threading I/O implementation as quickly as possible."""

# Builtins

# import cProfile  # for profiling
import logging
# import pstats  # for profiling
import time

# Packages

from phyllo.io.cli.args.args import parse_args
from phyllo.io.cli.args.protocol import (
    args_application_stack, args_transport_logical_substack, group_protocol_stack
)
from phyllo.io.polling.serial import connect_serial_retry
from phyllo.io.threading.serial import ThreadedSerialAdapter
from phyllo.io.threading.serial import make_stack as make_threading_stack
from phyllo.protocol.stacks import make_preset_stack
from phyllo.util.logging import config_logging

from tests.io.polling.serial.echo import make_send_data, send_data
from tests.io.polling.serial.echo_performance import run_echo
from tests.io.threading.serial.receiver import receive_blocking


config_logging()
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def main(
    transport_logical_preset, application_preset,
    report_interval=None, limit=None
):
    """Run loopback test."""
    connection = connect_serial_retry(baudrate=115200, timeout=0)
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
    run_echo(
        stack, receive_blocking, send_data, data, expected_data_kwargs=data_kwargs,
        report_interval=report_interval, limit=limit
    )
    logger.info('Quitting!')


if __name__ == '__main__':
    args = parse_args(
        grouped_args={
            group_protocol_stack: (
                args_transport_logical_substack, args_application_stack
            )
        },
        description='Measure performance on payload echo test.'
    )

    # cProfile.run('main(args.logical, args.application, limit=10000)', 'serial_polling.profile')
    # p = pstats.Stats('serial_threading.profile')
    # p.strip_dirs().sort_stats('cumulative').print_stats(30)

    # main(args.logical, args.application, report_interval=100)  # for UART
    main(args.logical, args.application, report_interval=1000)  # for teensy4 and dueUSB
