"""Test the protocol.stacks module."""

# Builtins

import threading
import time

# Packages

from phyllo.io.threading.primitives import CancellableSemaphore


def test_semaphore():
    """Test CancellableSemaphore."""
    semaphore = CancellableSemaphore()

    def run_consumer():
        while semaphore.acquire():
            print('Consumer acquired a resource!')
            pass
        print('Consumer quitting!')

    consumer_thread = threading.Thread(target=run_consumer)
    consumer_thread.start()
    for i in range(5):
        time.sleep(0.5)
        print('Producer releasing resource {} of 5...'.format(i + 1))
        semaphore.release()
    print('Producer quitting!')
    semaphore.cancel()
    consumer_thread.join()
    print('Consumer joined!')
