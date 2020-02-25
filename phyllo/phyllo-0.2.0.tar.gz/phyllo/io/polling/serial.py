"""Synchronous polling-based support for communication protocol stack on serial io."""

# Builtins

import logging
import time

# Packages

from phylline.pipelines import AutomaticPipeline, ManualPipeline
from phylline.processors import wait

from phyllo.io.interfaces.serial import SerialPipelineAdapter, connect_serial
from phyllo.util.logging import IndentedLogger

import serial


logger = logging.getLogger(__name__)


# Stack adapter


class PollingSerialAdapter(SerialPipelineAdapter):
    """A synchronous polling-based adapter.

    When update() is called, it performs a to_read on the serial connection.
    When any data is received by write(), it performs a write on the serial
    connection and also exposes it on the write buffer.
    """

    def __init__(
        self, connection, pipeline, min_read_length=1,
        logger_name='PollingSerialAdapter', logger_indentation=0, **kwargs
    ):
        """Initialize members."""
        super().__init__(connection, pipeline, **kwargs)
        self.is_manual = isinstance(self.pipeline, ManualPipeline)
        if isinstance(self.pipeline, AutomaticPipeline):
            self.pipeline.after_write = self._write
        self.min_read_length = min_read_length
        self.logger = IndentedLogger(logging.getLogger(logger_name), {
            'class': self.__class__.__qualname__,
            'indentation': logger_indentation
        })

    def _write(self, buffer):
        """Write the buffer to the connection.

        This is used to overwrite the after_write of the bottom of the pipeline
        if it's an automatic pipeline.
        """
        if buffer:
            try:
                # print(buffer)
                self.connection.write(buffer)
            except serial.serialutil.SerialException:
                self.logger.error('Serial device disconnected!')
        yield from wait()

    def start(self):
        """Initialize adapter state."""
        self.update_clock()

    def stop(self):
        """Clean up adapter state."""
        pass

    def update_clock(self):
        """Mimic Pipeline.update_clock.

        If the pipeline is a manual pipeline, it will also sync the pipeline and
        write any data at the bottom to the connection.
        """
        self.pipeline.update_clock(time.time())
        if self.is_manual:
            self.to_write()

    def clock_update_requested(self):
        """Mimic Pipeline.clock_update_requested."""
        current_time = time.time()
        return self.pipeline.clock_update_requested(current_time)

    # StreamLinkBelow-like interface

    def to_read(self, block_until=None):
        """Mimic StreamLinkBelow.to_read.

        Update the read side of the adapter.
        If block_until is a bytestring, read will block until that string is
        reached or until the connection's timeout is reached.
        """
        self.update_clock()
        try:
            if block_until is None and self.connection.in_waiting < self.min_read_length:
                return
        except OSError:
            raise ConnectionResetError('Serial device disconnected!')
        try:
            if block_until is not None:
                read = self.connection.read_until(block_until)
            else:
                read = self.connection.read()
        except serial.serialutil.SerialException:
            raise ConnectionResetError('Serial device disconnected!')
        self.pipeline.to_read(read)

    def to_write(self):
        """Mimic StreamLinkBelow.to_write.

        Update the write side of the adapter. This is used for manual writing
        from the bottom of the pipeline if it's not an automatic pipeline.
        """
        data = self.pipeline.to_write()
        if data:
            try:
                self.connection.write(data)
            except serial.serialutil.SerialException:
                raise ConnectionResetError('Serial device disconnected!')
        return data


# Serial connection


def connect_serial_retry(max_attempts=None, poll_interval=0.2, **kwargs):
    """Attempt persistently to establish a serial connection."""
    attempt = 0
    logger.info(
        'Attempting to connect to a preferred serial port{}...'
        .format(' with up to {} attempts' if max_attempts is not None else '')
    )
    while True:
        connection = connect_serial(**kwargs)
        if connection is not None:
            logger.info('Connected to serial port {}!'.format(connection.name))
            return connection

        logger.debug(
            'Failed to connect to a serial port on attempt {}!'
            .format(attempt, max_attempts)
        )
        if max_attempts is not None:
            if attempt >= max_attempts:
                return
        attempt += 1
        time.sleep(poll_interval)
