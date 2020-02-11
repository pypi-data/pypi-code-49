import logging
import asyncio
import signal
from typing import Coroutine

from pipeline import STOP


LOG = logging.getLogger(__name__)


async def task_wrapper(task: Coroutine):
    ''' Wraps a coroutine as a task and passes the global stop signal to it '''
    try:
        await task(stop_signal=STOP)
    except asyncio.CancelledError:
        LOG.debug('Cancelled: %s', task.__name__)
    except asyncio.TimeoutError:
        LOG.debug('Timed out: %s. Restarting.', task.__name__)


def main(task):
    '''
    Main entry point for a task.
    Adds signal handlers and starts the task.
    '''
    loop = asyncio.get_event_loop()

    # connect signal handler for stopping program
    stop_signals = [signal.SIGINT, signal.SIGHUP]
    for value in stop_signals:
        loop.add_signal_handler(value, STOP.set)

    LOG.debug('Starting loop.')
    loop.run_until_complete(asyncio.gather(
        task_wrapper(task),
    ))

    LOG.debug('Main finished.')
