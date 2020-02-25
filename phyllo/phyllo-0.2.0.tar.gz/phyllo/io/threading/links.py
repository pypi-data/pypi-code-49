"""Thread-aware communication protocol links."""

# Builtins

# Packages
from phylline.links.events import EventLink
from phylline.processors import event_processor, receive

from phyllo.io.threading.primitives import CancellableSemaphore
from phyllo.protocol.communication import TypedLink


class ThreadSynchronizer(EventLink):
    """An EventLink which releases semaphores on send and receive.

    It passes events through unmodified in both directions.
    """

    def __init__(self, direction):
        """Initialize members."""
        self.semaphore_receive = CancellableSemaphore('receive')
        self.semaphore_to_send = CancellableSemaphore('to_send')
        self.direction = direction
        super().__init__(
            name=direction, sender_processor=self.sender_processor
        )

    @event_processor
    def receiver_processor(self):
        """Override EventLink.receiver_processor."""
        while True:
            event = yield from receive()
            # print('Threading Event Adapter received: {}'.format(event))
            yield from self.after_receive(event)
            self.semaphore_receive.release()

    @event_processor
    def sender_processor(self):
        """Override EventLink.sender_processor."""
        while True:
            event = yield from receive()
            # print('Threading Event Adapter sending: {}'.format(event))
            yield from self.after_send(event)
            self.semaphore_to_send.release()


class StackThreadSynchronizer(ThreadSynchronizer, TypedLink):
    """A ThreadSynchronizer with a DataUnitLink-like interface.."""

    pass
