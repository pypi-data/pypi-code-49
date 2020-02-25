"""Threading primitives."""

# Builtins

import threading

# Packages


class CancellableSemaphore(object):
    """Semaphore which can be cancelled for early exit."""

    def __init__(self, name=None, initial_value=0):
        """Initialize members."""
        self.name = name
        self.semaphore = threading.Semaphore(value=initial_value)
        self.ready = threading.Condition()
        self.cancelled = False

    def acquire(self):
        """Acquire a resource on the semaphore, or else quit after cancellation."""
        # print('{}: Getting ready...'.format(self.name))
        with self.ready:
            while not self.cancelled:
                # print('{}: Trying to acquire...'.format(self.name))
                if self.semaphore.acquire(blocking=False):
                    # print('{}: Acquired!'.format(self.name))
                    return True
                self.ready.wait()
        # print('{}: Cancelled!'.format(self.name))
        return False  # returns False after cancellation

    def cancel(self):
        """Cancel waiting on the semaphore."""
        with self.ready:
            self.cancelled = True
            self.ready.notify()

    def release(self):
        """Release a resource on the semaphore."""
        with self.ready:
            self.semaphore.release()
            self.ready.notify()
