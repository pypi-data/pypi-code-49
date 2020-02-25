"""Concurrent thread-based support for communication protocol stack on serial io."""

# Builtins

import threading
import time  # for testing

# Packages

from phylline.pipelines import AutomaticPipeline
from phylline.processors import wait

from phyllo.io.polling.serial import SerialPipelineAdapter
from phyllo.io.threading.links import StackThreadSynchronizer, ThreadSynchronizer
from phyllo.protocol.communication import AutomaticStack
from phyllo.protocol.stacks import make_stack as make_protocol_stack

import serial


# Stack adapter


def make_stack(protocol_stack=None, stack=AutomaticStack, name='Threaded'):
    """Make a transport stack."""
    if protocol_stack is None:
        protocol_stack = make_protocol_stack()
    return stack(
        protocol_stack, StackThreadSynchronizer(direction='receive'), name=name
    )


class ThreadedSerialAdapter(SerialPipelineAdapter):
    """A concurrent threaded adapter.

    Serial data is read in a separate thread, while serial data is written in
    the same thread (to transmit backpressure).
    """

    def __init__(self, connection, pipeline, read_delim=b'\0', read_size=255):
        """Initialize members."""
        self.connection = connection
        connection.timeout = None  # serial should do blocking reads
        connection.write_timeout = None  # serial should do blocking writes
        self.read_delim = read_delim
        self.read_size = read_size
        self.pipeline = pipeline
        self.pipeline_lock = threading.Lock()
        if isinstance(self.pipeline, AutomaticPipeline):
            self.pipeline.bottom.after_write = self._write
        else:
            raise NotImplementedError(
                'ThreadedSerialAdapter only supports AutomaticPipeline!'
            )

        # Synchronization
        adapters = [
            link for link in pipeline.layers if isinstance(link, ThreadSynchronizer)
        ]
        try:
            self.receive_adapter = next(
                adapter for adapter in adapters if adapter.direction == 'receive'
            )
        except StopIteration:
            raise ValueError(
                'ThreadedSerialAdapter requires a pipeline containing a ThreadingEvent '
                'adapter with direction "receive" in it!'
            )
        self.has_receive = self.receive_adapter.semaphore_receive

        # Top
        non_adapters = [
            link for link in pipeline.layers if not isinstance(link, ThreadSynchronizer)
        ]
        self._top = non_adapters[-1]

        # Threads
        self.receiver_running = False
        self._receiver = None
        self.receiver_disconnected = False

    def update_clock(self):
        """Update the pipeline's clock."""
        with self.pipeline_lock:
            # print(
            #     'Updating stack clock! Next clock request: {}'
            #     .format(self.pipeline.next_clock_request)
            # )
            self.pipeline.update_clock(time.time())

    def _write(self, buffer):
        """Write the buffer to the connection.

        This is used to overwrite the after_write of the bottom of the pipeline
        if it's an automatic pipeline.
        """
        try:
            if buffer:
                # print(buffer)
                self.connection.write(buffer)
        except serial.serialutil.SerialException:
            self.receiver_running = False
            self.has_receive.cancel()
            self.logger.error('Serial device disconnected!')
        yield from wait()

    def run_receiver(self):
        """Thread function for receiving data."""
        self.update_clock()
        try:
            # print('Running receiver...')
            while self.receiver_running:
                self.to_read()
        except KeyboardInterrupt:
            self.has_receive.cancel()
            self.receiver_running = False
        except ConnectionResetError:
            self.has_receive.cancel()
            self.receiver_running = False
            self.receiver_disconnected = True

    def start(self):
        """Start the threads."""
        self.receiver_running = True
        self._receiver = threading.Thread(
            target=self.run_receiver,
            name='{} receiver'.format(self.__class__.__qualname__)
        )
        self._receiver.start()

    def stop(self):
        """Stop the threads."""
        self.receiver_running = False
        self.connection.cancel_read()
        self.connection.cancel_write()
        self.has_receive.cancel()
        self._receiver.join()

    def __str__(self):
        """Represent the adapter as a string."""
        return '{}: Serial({}) ~⇌|{}'.format(
            self.__class__.__qualname__,
            self.connection.name,
            self.pipeline
        )

    # Override SerialPipelineAdapter

    @property
    def top(self):
        """Override SerialPipelineAdapter.top."""
        try:
            return self._top.top
        except AttributeError:
            self._top

    # StreamLinkBelow-like interface

    def to_read(self):
        """Update the read side of the adapter."""
        try:
            self.update_clock()
            if self.pipeline.next_clock_request is None:
                self.connection.timeout = None
            else:
                self.connection.timeout = max(
                    0, self.pipeline.next_clock_request.requested_time - time.time()
                )
                # print('Set read timeout to {} s!'.format(self.connection.timeout))
            if self.read_delim is None:
                read = self.connection.read()
            else:
                read = self.connection.read_until(self.read_delim, self.read_size)
        except serial.serialutil.SerialException:
            self.receiver_running = False
            self.has_receive.cancel()
            raise ConnectionResetError('Serial device disconnected!')
        if self.receiver_running:  # check since cancelled read can give partial data
            self.update_clock()
            # print('Read: {}'.format(read))
            with self.pipeline_lock:
                self.pipeline.bottom.to_read(read)
