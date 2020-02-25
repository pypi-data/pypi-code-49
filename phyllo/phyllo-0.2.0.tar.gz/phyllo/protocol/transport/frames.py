"""Framing of data ensures that the data can be passed as delimited buffer chunks.

In other words, it encodes the data so that anything which looks like a buffer
chunk delimiters is encoded to no longer look like a buffer chunk delimiter.
"""

# Builtins

import logging
from bisect import bisect_right
from collections import Counter

# Packages

from cobs import cobs

from phylline.links.links import ChunkedStreamLink
from phylline.processors import event_processor, receive
from phylline.processors import read_until, stream_processor
from phylline.util.logging import hex_bytes

from phyllo.protocol.communication import DATA_TYPES, DataUnitLink, TypedLink
from phyllo.util.logging import IndentedLogger


class ChunkedStreamLink(TypedLink, ChunkedStreamLink):
    """ChunkedStreamLink instrumented with counters."""

    TYPE = DATA_TYPES[('bytes', 'chunk')]

    SENDABLE_TYPES = {
        # DATA_TYPES[('bytes', 'buffer')],
        DATA_TYPES[('bytes', 'chunk')],
        DATA_TYPES[('transport', 'frame')],
    }

    def __init__(self, *args, **kwargs):
        """Initialize members."""
        super().__init__(*args, **kwargs)
        self.logger = IndentedLogger(logging.getLogger(__name__), {
            'class': self.__class__.__qualname__,
            'indentation': 6
        })

        self.reader_counter = Counter()
        self.sender_counter = Counter()

        self.receiver_hist = Counter()
        self.sender_hist = Counter()

        self.hist_bin_boundaries = [
            8, 16, 24, 32,
            48, 64, 80,
            100, 150, 200, 250
        ]
        self.receiver_hist_coarse = Counter({
            self._coarse_length(length): 0
            for length in [0] + self.hist_bin_boundaries
        })
        self.sender_hist_coarse = Counter({
            self._coarse_length(length): 0
            for length in [0] + self.hist_bin_boundaries
        })

    @property
    def counters(self):
        """Return associated counters."""
        return {
            'reader': self.reader_counter,
            'sender': self.sender_counter,
            'receiver_hist': self.receiver_hist,
            'sender_hist': self.sender_hist,
            'receiver_hist_coarse': self.receiver_hist_coarse,
            'sender_hist_coarse': self.sender_hist_coarse,
        }

    def _coarse_length(self, length):
        bin_right = bisect_right(self.hist_bin_boundaries, length)
        if bin_right == 0:
            return '[0, {})'.format(self.hist_bin_boundaries[0])
        elif bin_right == len(self.hist_bin_boundaries):
            return '[{}, ∞)'.format(self.hist_bin_boundaries[-1])
        else:
            return '[{}, {})'.format(
                self.hist_bin_boundaries[bin_right - 1],
                self.hist_bin_boundaries[bin_right]
            )

    def _update_read_length_stats(self, buffer):
        length = len(buffer)
        self.reader_counter['to_read'] += length
        self.receiver_hist[length] += 1
        self.receiver_hist_coarse[self._coarse_length(length)] += 1

    def _update_send_length_stats(self, stream_contents):
        self.sender_counter['to_write'] += len(stream_contents)
        length = len(stream_contents) - 2
        self.sender_hist[length] += 1
        self.sender_hist_coarse[self._coarse_length(length)] += 1

    # Override ChunkedStreamLink

    @stream_processor
    def reader_processor(self, chunk_separator):
        """Override ChunkedStreamLink.reader_processor."""
        while True:
            buffer = yield from read_until(chunk_separator)
            self.reader_counter['to_read'] += 1
            if len(buffer) == 0:
                continue
            self.logger.debug('Reading: {}'.format(hex_bytes(buffer)))
            self._update_read_length_stats(buffer)
            data_event = self.make_link_data(buffer, 'up', None, type=self.TYPE)
            self.reader_counter['receive'] += 1
            self._event_link.to_receive(data_event)

    @event_processor
    def sender_processor(self, chunk_separator, begin_chunk_separator):
        """Override ChunkedStreamLink.sender_processor."""
        while True:
            event = yield from receive()
            data_event = self.get_link_data(event, 'down')
            if data_event.type not in self.SENDABLE_TYPES:
                self.logger.error(
                    '{} cannot send data of type {}!'
                    .format(self.__class__.__qualname__, data_event.type_string)
                )
                continue
            payload = data_event.data
            if len(payload) == 0:
                continue
            self.sender_counter['send'] += 1
            stream_contents = payload + chunk_separator
            if begin_chunk_separator:
                stream_contents = chunk_separator + stream_contents
            self.logger.debug('Writing: {}'.format(hex_bytes(stream_contents)))
            self._update_send_length_stats(stream_contents)
            self._stream_link.write(stream_contents)


class Frame(bytes):
    """The Frame is a COBS-encoded byte buffer."""

    TYPE = DATA_TYPES[('transport', 'frame')]


class FrameLink(DataUnitLink):
    """The FrameLink uses COBS (consistent overhead byte-stuffing) for framing.

    The COBS encoding scheme allows 0x00 to be used as a frame delimiter
    to indicate the end of the frame; all other bytes are frame payload.
    This allows a FrameLink to sit on top of a ChunkedStreamLink.

    Interface:
    Above: sends and receives unencoded bytestrings
    Below: to_send and to_receive COBS-encoded bytestrings
    """

    DATA_UNIT = Frame
    TYPE = DATA_UNIT.TYPE
    PAYLOAD_SIZE_LIMIT = 254  # excluding frame delimiter
    RECEIVABLE_TYPES = {
        TYPE,
        DATA_TYPES[('bytes', 'chunk')],
        DATA_TYPES[('bytes', 'buffer')]
    }
    SENDABLE_TYPES = {
        DATA_TYPES[('bytes', 'buffer')],
        DATA_TYPES[('transport', 'datagram')]
    }

    def __init__(self):
        """Initialize members."""
        super().__init__(logger_name=__name__, logger_indentation=5)

    # Override DataUnitLink

    def make_link_received_data_unit(self, data_event):
        """Make a received data unit from a received data event."""
        encoded_frame = data_event.data
        frame_payload = cobs.decode(encoded_frame)
        return frame_payload

    def is_control_data_unit(self, frame):
        """Override DataUnitLink.is_control_data_unit."""
        return False

    def make_link_received_event(self, frame_payload, source_event, context):
        """Override DataUnitLink.make_link_received_event."""
        return self.make_link_data(
            frame_payload, 'up', source_event, context=context,
            type=DATA_TYPES[('bytes', 'buffer')]
        )

    def make_link_send_data_unit(self, data_event):
        """Override DataUnitLink.make_link_send_data_unit."""
        frame_payload = data_event.data
        if len(frame_payload) > self.PAYLOAD_SIZE_LIMIT:
            self.sender_counter['error_payload_length'] += 1
            raise ValueError(
                'Cannot send an excessively long payload: {} bytes given, '
                '{} bytes allowed'
                .format(len(frame_payload), self.PAYLOAD_SIZE_LIMIT)
            )
        return cobs.encode(frame_payload)

    def update_send_data_unit_header(self, data_unit, data_event):
        """Override DataUnitLink.update_send_data_unit_header."""
        pass

    def check_send_data_unit(self, data_unit):
        """Override DataUnitLink.check_send_data_unit."""
        pass

    def make_send_data_event_data(self, frame):
        """Override DataUnitLink.make_send_data_event_data."""
        return frame
