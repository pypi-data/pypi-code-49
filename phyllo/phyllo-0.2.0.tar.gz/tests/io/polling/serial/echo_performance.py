"""Echo a payload on the polling I/O implementation as quickly as possible."""

# Builtins

# import cProfile  # for profiling
import json
import logging
# import pstats  # for profiling
import time

# Packages

from phyllo.io.cli.args.args import parse_args
from phyllo.io.cli.args.protocol import (
    args_application_stack, args_transport_logical_substack, group_protocol_stack
)
from phyllo.io.polling.serial import PollingSerialAdapter, connect_serial_retry
from phyllo.protocol.communication import (
    compile_counters, count_receive, count_send, count_to_read, count_to_write
)
from phyllo.protocol.stacks import make_preset_stack
from phyllo.util.logging import config_logging
from phyllo.util.timing import Counter

from tests.io.polling.serial.echo import make_send_data, send_data
from tests.io.polling.serial.receiver import receive_blocking


config_logging()
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def print_counters(stack, time_elapsed):
    """Print counter statistics."""
    logger.info('Elapsed time: {:.4} seconds'.format(time_elapsed))
    counters = compile_counters(stack)
    bottom_counters = stack.bottom.counters
    read_b = count_to_read(bottom_counters)
    if read_b is not None:
        logger.info('{} kB read from serial ({:.4} kBps or {:.4} bps)'.format(
            read_b / 1000, read_b / 1000 / time_elapsed,
            read_b / time_elapsed * 8
        ))
    else:
        logger.info('0 kB read from serial')
    write_b = count_to_write(bottom_counters)
    if write_b is not None:
        logger.info('{} kB written to serial ({:.4} kBps or {:.4} bps)'.format(
            write_b / 1000, write_b / 1000 / time_elapsed,
            write_b / time_elapsed * 8
        ))
    else:
        logger.info('0 kB written to serial')
    top_counters = stack.top.counters
    receive = count_receive(top_counters)
    if read_b is not None and receive is not None:
        logger.info('{} events received at top of pipeline ({:.4} bytes per event)'.format(
            receive, read_b / receive
        ))
    elif receive is not None:
        logger.info('{} events received at top of pipeline'.format(receive))
    else:
        logger.info('0 events received at top of pipeline')
    send = count_send(top_counters)
    if write_b is not None and send is not None:
        logger.info('{} events sent to top of pipeline ({:.4} bytes per event)'.format(
            send, write_b / send
        ))
    elif send is not None:
        logger.info('{} events sent to top of pipeline'.format(send))
    else:
        logger.info('0 events sent to top of pipeline')
    logger.info('Counters:\n{}'.format(
        json.dumps(counters, indent=2, ensure_ascii=False)
    ))


def run_echo(
    stack, receiver, sender, data, report_interval=None, expected_data_kwargs={}, limit=None
):
    """Run the echo performance test."""
    counter = Counter(report_interval=report_interval, event_type='echoes')
    counter.start()
    received = None

    try:
        stack.start()
        sender(stack, data, **expected_data_kwargs)
        for received in receiver(stack):
            if received.data != data:
                logger.error('Unexpected response: {}'.format(received))
            counter.increment()
            counter.report()
            sender(stack, data, log=False, **expected_data_kwargs)
            if counter.count == limit:
                logger.info('Finished exchanging {} echoes!'.format(limit))
                break
    except KeyboardInterrupt:
        print()
        logger.info('Received keyboard interrupt, wrapping up...')
    except ConnectionResetError:
        logger.error('Serial device disconnected!')

    counter.report(force=True)
    if received is None:
        logger.warn('No data echo received!')
    else:
        logger.info('Last data echo received: {}'.format(received))
    print_counters(stack, counter.timer.elapsed)
    logger.info('Cleaning up...')
    stack.stop()


def main(
    transport_logical_preset, application_preset,
    report_interval=None, limit=None
):
    """Run loopback test."""
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
    # p = pstats.Stats('serial_polling.profile')
    # p.strip_dirs().sort_stats('cumulative').print_stats(30)

    # main(args.logical, args.application, report_interval=100)  # for UART
    main(args.logical, args.application, report_interval=1000)  # for teensy4 and dueUSB
