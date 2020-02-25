"""Reliably-transmitted reliable buffers with automatic repeat requesting.

Implementation references:
- https://www.ibr.cs.tu-bs.de/courses/ws0910/pcn/Documents/Communication_Networks-
  Fundamentals_Concepts_and_Key_Architectures.pdf
- https://blog.eqrion.net/reliable-networking/
- https://book.systemsapproach.org/direct/reliable.html
- https://courses.engr.illinois.edu/cs438/sp2010/slides/lec04_reliable.pdf
- http://kfall.net/ucbpage/EE122/lec19/lec19.pdf
- http://www.cs.uah.edu/~gcox/570/570lec05-LLCb-f07.pdf
- https://www.cpp.edu/~gsyoung/CS3800/CS380Notes/Part2DataLinkNetworks.pdf
- https://ocw.mit.edu/courses/aeronautics-and-astronautics/16-36-communication-
  systems-engineering-spring-2009/lecture-notes/MIT16_36s09_lec18.pdf
Piggybacking implementation reference:
"""

# Builtins

import logging
import struct
from collections import Counter, deque

# Packages

from phylline.links.clocked import ClockedLink
from phylline.links.events import LinkException
from phylline.util.timing import TimeoutTimer

from phyllo.protocol.communication import DATA_TYPES
from phyllo.protocol.communication import DataUnit, DataUnitLink, StructuredHeader
from phyllo.util.logging import IndentedLogger


# ReliableBuffers

class ReliableBufferFlags(object):
    """ReliableBuffer header flags."""

    class BitfieldFlag(object):
        """Descriptor for access to a flag in a ReliableBufferHeader bitfield."""

        def __init__(self, position):
            """Initialize members which aren't instance-specific."""
            self.position = position
            self.mask = (1 << position)

        def __get__(self, instance, owner):
            """Get the flag from the bitfield."""
            return instance.bitfield & self.mask

        def __set__(self, instance, value):
            """Set the flag in the bitfield."""
            if value:
                instance.bitfield = instance.bitfield | self.mask
            else:
                instance.bitfield = instance.bitfield & ~self.mask

    FLAG_NAMES = [  # Listed in most-significant-bit-first order
        'ext', 'rst', 'sak', 'nak', 'ack', 'nos', 'syn', 'fin'
    ]
    # Listed in least-significant-bit-first order:
    fin = BitfieldFlag(0)
    syn = BitfieldFlag(1)
    nos = BitfieldFlag(2)
    ack = BitfieldFlag(3)
    nak = BitfieldFlag(4)
    sak = BitfieldFlag(5)
    rst = BitfieldFlag(6)
    ext = BitfieldFlag(7)

    def __init__(self, bitfield=0x00, **kwargs):
        """Initialize bitfield.

        Bitfield should be a single byte!
        """
        self.bitfield = bitfield
        for (key, value) in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        """Return a string representation of the reliable buffer's flags."""
        return ' '.join([
            flag_name for flag_name in self.FLAG_NAMES if getattr(self, flag_name)
        ])

    @property
    def bitfield_string(self):
        """Return a bitfield string representation of the reliable buffer's flags."""
        return 'F{}'.format(self.bitfield_repr)

    @property
    def bitfield_repr(self):
        """Return a bitfield string representation of the reliable buffer's flags."""
        return '0b{:08b}'.format(self.bitfield)


class ReliableBufferHeader(StructuredHeader):
    """ReliableBuffer header.

    In order of increasing offset in the buffer representation:
    Sequence number is the sequential transmission number of the reliable buffer.
    Acknowledgement number is the sequential transmission number of a previous
        reliable buffer.
    Flags is a bitfield which specifies things.
    """

    FORMAT = '> B B B B'
    PARSER = struct.Struct(FORMAT)
    SIZE = struct.calcsize(FORMAT)

    def __init__(
        self, seq_num=0, ack_num=0, flags=0x00, type=DATA_TYPES[('bytes', 'buffer')]
    ):
        """Initialize field values."""
        super().__init__(type=type)
        self.seq_num = seq_num
        self.ack_num = ack_num
        if isinstance(flags, ReliableBufferFlags):
            self.flags = flags
        else:
            self.flags = ReliableBufferFlags(flags)

    # Implement CommunicationLinkHeader

    @property
    def fields(self):
        """Implement CommunicationLinkHeader.fields."""
        return (self.seq_num, self.ack_num, self.flags.bitfield, self.type)

    def read(self, buffer):
        """Implement CommunicationLinkHeader.read."""
        (
            self.seq_num, self.ack_num, self.flags.bitfield, self.type
        ) = self.unpack(buffer)

    # String representations

    @property
    def seq_string(self):
        """Return a string representation of the seq field."""
        return 'S{:3}'.format(self.seq_num if self.seq_num is not None else '   ')

    @property
    def ack_string(self):
        """Return a string representation of the ack field."""
        return 'A{:3}'.format(self.ack_num if self.ack_num is not None else '   ')

    @property
    def field_strings(self):
        """Implement CommunicationLinkHeader.field_strings."""
        return (self.seq_string, self.ack_string, str(self.flags), self.type_string)

    @property
    def members_repr(self):
        """Implement CommunicationLinkHeader.members_repr."""
        return {
            'seq_num': self.seq_num,
            'ack_num': self.ack_num,
            'flags': self.flags.bitfield_repr,
            'type': self.type_repr
        }

    # String representations

    @property
    def full_string(self):
        """Return a full string representation of a ReliableBuffer Header."""
        return ' | '.join((
            self.seq_string, self.ack_string, self.flags.bitfield_string, self.type_string
        ))


class ReliableBuffer(DataUnit):
    """ReliableBuffer containing a header and a payload.

    In order of increasing offset in the buffer representation:
    Header contains the header.
    Payload contains the payload.
    """

    TYPE = DATA_TYPES[('transport', 'reliable_buffer')]

    HEADER = ReliableBufferHeader

    def __init__(self, header=None, payload=b''):
        """Initialize with optional header and payload.

        Note: saves references, not copies, of header and payload!
        """
        super().__init__(header=header, payload=payload)

    # String representations

    @property
    def preflight_string(self):
        """Return a send queue representation of the reliable buffer."""
        return '{} | {}'.format(
            self.header.flags.bitfield_string, self.full_payload_string
        )


# Go-Back-N ARQ

class GBNSender(object):
    """Go-back-N ARQ reliable buffer sender."""

    SEQUENCE_NUMBER_SPACE = 256
    RECEIVER_WINDOW_SIZE = 1  # implicit in algorithm implementation
    SENDER_WINDOW_SIZE = 8
    assert SENDER_WINDOW_SIZE <= SEQUENCE_NUMBER_SPACE - RECEIVER_WINDOW_SIZE

    def __init__(self, clock, send_timeout=0.02, in_flight_timeout=1.0):
        """Initialize members.

        send_timeout: (s) when to retransmit an in-flight reliable buffer.
            ReliableBuffer link RTT is around 5 - 7 ms, so 20 ms timeout is safe.
        in_flight_timeout: (s) when to give up on an in-flight reliable buffer.
        """
        self.clock = clock
        self.send_timeout = send_timeout
        self.in_flight_timeout = in_flight_timeout
        self.last_acknowledged = None
        self.last_sent = None
        self.sender_thread = None
        self.send_queue = deque()
        self.in_flight_queue = deque()
        self.logger = IndentedLogger(logging.getLogger(__name__), {
            'class': self.__class__.__qualname__,
            'indentation': 3.5
        })
        self.counter = Counter()

    # Backpressure

    @property
    def send_queue_availability(self):
        """Return the number of reliable buffers which can be added to the send queue."""
        return max(0, self.SENDER_WINDOW_SIZE - len(self.send_queue))

    # ReliableBuffer transmission

    @property
    def in_flight_queue_availability(self):
        """Return the number of reliable buffers which can be added to the send queue."""
        return max(0, self.SENDER_WINDOW_SIZE - len(self.in_flight_queue))

    @property
    def next_seq_num(self):
        """Determine the seq num to assign to the next reliable buffer to move in-flight."""
        if self.last_sent is None:
            return 0
        return (self.last_sent + 1) % self.SEQUENCE_NUMBER_SPACE

    def send(self, reliable_buffer, previous=None):
        """Add a reliable buffer to the send queue."""
        if not self.send_queue_availability:
            self.logger.error(
                'Over-stuffed send queue with reliable buffer: {}'
                .format(reliable_buffer.preflight_string)
            )
            self.counter['send_availability_exceeded'] += 1
        self.logger.debug(
            'Queuing:\t\t\t{}'.format(reliable_buffer.preflight_string)
        )
        # if reliable_buffer.header.length:
        #     self.logger.debug(
        #         'Queuing:\t\t\t{} bytes of data'
        #         .format(reliable_buffer.payload.length)
        #     )
        self.send_queue.append({
            'reliable_buffer': reliable_buffer,
            'send_time': self.clock.time,
            'previous': previous
        })
        if not self.send_queue_availability:
            self.counter['send_availability_filled'] += 1
        self.counter['send_queued'] += 1

    def _make_in_flight(self, reliable_buffer, send_time, previous):
        """Make an in-flight record."""
        resend_timer = self.make_timer()
        resend_timer.start()
        in_flight_timer = self.make_timer(timeout=self.in_flight_timeout)
        in_flight_timer.start()
        return {
            'reliable_buffer': reliable_buffer,
            'send_time': send_time,
            'in_flight_timer': in_flight_timer,  # TODO: warn or give up after timeout
            'resend_timer': resend_timer,
            'resend_attempts': 0,  # TODO: warn or give up after too many attempts
            'previous': previous
        }

    def flush_send_queue(self):
        """Flush reliable_buffer waiting in the send queue.

        This will move reliable_buffer from the send queue to the in-flight queue
        as appropriate, and it will yield every reliable_buffer to send.
        """
        while self.send_queue and self.in_flight_queue_availability:
            to_send = self.send_queue.popleft()
            self.counter['send_flushed'] += 1
            reliable_buffer = to_send['reliable_buffer']
            reliable_buffer.header.seq_num = self.next_seq_num
            # TODO: piggyback acknowledgement number, too
            self.in_flight_queue.append(self._make_in_flight(
                reliable_buffer, to_send['send_time'], to_send['previous']
            ))
            self.counter['in_flight_queued'] += 1
            self.logger.debug(
                'Sending {}:\t\t{}'
                .format(
                    'data' if len(reliable_buffer.payload)
                    else 'control', reliable_buffer
                )
            )
            # self.logger.debug(
            #     'Sending {}:\t\t{}'
            #     .format(
            #         'data' if reliable_buffer.header.length
            #         else 'control', reliable_buffer.header
            #     )
            # )
            self.last_sent = reliable_buffer.header.seq_num
            self._check_window_size()
            yield to_send
            if not self.send_queue:
                self.counter['send_emptied'] += 1
            if not self.in_flight_queue_availability:
                self.counter['in_flight_availability_filled'] += 1

    def reset(self):
        """Clear the send queue and the in-flight queue."""
        if self.send_queue:
            self.logger.warn(
                'Resetting with non-empty send queue: {}'
                .format(self.send_queue)
            )
            self.counter['reset_nonempty_send'] += 1
            self.counter['reset_nonempty_send_lost'] += len(self.send_queue)
        self.send_queue.clear()
        if self.in_flight_queue:
            self.logger.warn(
                'Resetting with non-empty in-flight queue: {}'
                .format(self.in_flight_queue)
            )
            self.counter['reset_nonempty_in_flight'] += 1
            self.counter['reset_nonempty_in_flight_lost'] += len(self.in_flight_queue)
        for in_flight in self.in_flight_queue:
            self.logger.warn(
                'Resetting without waiting for acknowledgement:\t{}'
                .format(in_flight['reliable_buffer'])
            )
            # self.logger.warn(
            #     'Resetting without waiting for acknowledgement:\t{}'
            #     .format(in_flight['reliable_buffer'].header_string)
            # )
        self.in_flight_queue.clear()
        self.counter['reset'] += 1

    # ReliableBuffer reception

    def retransmit_from_received(self, reliable_buffer):
        """Return whether the reliable buffer indicates the need for retransmission."""
        if not reliable_buffer.header.flags.ack:  # TODO: should we ignore ack and only check nak?
            return False
        return reliable_buffer.header.flags.nak

    def to_receive(self, reliable_buffer):
        """Handle received reliable buffer."""
        if not reliable_buffer.header.flags.ack:
            return True

        last_acknowledged = reliable_buffer.header.ack_num  # actually number of next expected
        if self.last_acknowledged is None:
            num_acknowledged = last_acknowledged
        else:
            num_acknowledged = last_acknowledged - self.last_acknowledged
        # print('Acknowleding {} reliable buffers...'.format(num_acknowledged))
        if num_acknowledged + self.SEQUENCE_NUMBER_SPACE < self.SENDER_WINDOW_SIZE:
            # acknowledgement number has rolled over
            self.counter['acknowledge_rollover'] += 1
            num_acknowledged += self.SEQUENCE_NUMBER_SPACE
        if (num_acknowledged > 0) and (num_acknowledged <= self.SENDER_WINDOW_SIZE):
            self.counter['acknowledge'] += num_acknowledged
            self.logger.debug(
                'Received ACK of {} reliable buffer{}'
                .format(num_acknowledged, '' if num_acknowledged == 1 else 's')
            )
            self.last_acknowledged = last_acknowledged
            self._check_window_size()
            for i in range(num_acknowledged):
                self.in_flight_queue.popleft()
                if not self.in_flight_queue and not self.send_queue:
                    self.counter['in_flight_emptied'] += 1
            return True
        elif num_acknowledged == 0 and self.retransmit_from_received(reliable_buffer):
            return True
        else:
            self.counter['acknowledge_unexpected'] += 1
            self.logger.error(
                'Received unexpected ACK {} outside expected range ({}, {}]'
                .format(
                    last_acknowledged, self.last_acknowledged,
                    (self.last_acknowledged + self.SENDER_WINDOW_SIZE)
                    % self.SEQUENCE_NUMBER_SPACE
                )
            )
            return False

    # ReliableBuffer retransmission

    @property
    def next_in_flight(self):
        """Return the first reliable buffer in the in-flight queue."""
        if not self.in_flight_queue:
            return None
        return self.in_flight_queue[0]

    def make_timer(self, timeout=None):
        """Make a timer on the clock."""
        if timeout is None:
            timeout = self.send_timeout
        return TimeoutTimer(timeout=timeout, clock=self.clock)

    @property
    def retransmit_from_timeout(self):
        """Re-send all in-flight reliable buffers if the first one has timed out."""
        next_in_flight = self.next_in_flight
        if not next_in_flight:
            return None
        return next_in_flight['resend_timer'].timed_out

    def resend_in_flight(self, reason):
        """Re-send all in-flight reliable buffers."""
        self.logger.info('Re-sending {} reliable buffer{}'.format(
            len(self.in_flight_queue), '' if len(self.in_flight_queue) == 1 else 's'
        ))
        self.logger.debug('Re-sending:\t\t{}'.format(', '.join([
            str(in_flight['reliable_buffer'].header.seq_num)
            for in_flight in self.in_flight_queue
        ])))
        for in_flight in self.in_flight_queue:
            logging.debug(
                'GBN sender re-sending:\t\t{}'.format(in_flight['reliable_buffer'])
            )
            # logging.debug(
            #     'ARQ sender re-sending:\t\t{}'
            #     .format(timed_reliable_buffer.reliable_buffer.header)
            # )
            in_flight['resend_timer'].reset()
            in_flight['resend_attempts'] += 1
            in_flight['resend_reason'] = reason
            self.counter['in_flight_resent'] += 1
            yield in_flight

    @property
    def window_size(self):
        """Compute window size."""
        if self.last_sent is None:
            return 0
        if self.last_acknowledged is None:
            return self.last_sent + 1
        window_size = (
            self.last_sent
            - (self.last_acknowledged - 1) % self.SEQUENCE_NUMBER_SPACE
        )
        if window_size < 0:
            window_size += self.SEQUENCE_NUMBER_SPACE
        return window_size

    def _check_window_size(self):
        """Check window size invariant."""
        window_size = self.window_size
        try:
            assert window_size <= self.SENDER_WINDOW_SIZE
            self.logger.debug(
                'GBN sender now has {} reliable buffer{} in-flight'
                .format(window_size, '' if window_size == 1 else 's')
            )
        except AssertionError:
            logging.debug(
                '| | | ├-ARQ sender last sent {}, last acknowledged {}'
                .format(self.last_sent, self.last_acknowledged)
            )
            raise RuntimeError(
                'ARQ sender window size {} is larger than limit of {} '
                'reliable buffers!'.format(window_size, self.SENDER_WINDOW_SIZE)
            )

    def make_nak(self):
        """Make a NAK request to request the peer to retransmit."""
        return ReliableBuffer(
            header=ReliableBufferHeader(
                ack_num=self.last_acknowledged if self.last_acknowledged is not None else 0,
                flags=ReliableBufferFlags(nos=True, ack=True, nak=True),
                type=DATA_TYPES[('layer', 'control')]
            ), payload=b''
        )


class GBNReceiver(object):
    """Go-back-N ARQ reliable buffer receiver."""

    SEQUENCE_NUMBER_SPACE = 256
    RECEIVER_WINDOW_SIZE = 1  # implicit in algorithm implementation
    PIGGYBACK_TIMEOUT = 0.004  # s

    def __init__(self):
        """Initialize members."""
        self.counter = Counter()

    def received_expected(self, reliable_buffer):
        """Handle received reliable buffer."""
        return True


class ReliableBufferLink(ClockedLink, DataUnitLink):
    """The ReliableBufferLink implements reliable in-order data transmission.

    The reliable buffer layer handles data transport reliability with connection
    hand-shaking and reliable buffer resending. This is a connection-based link.
    Refer to ReliableBufferHeader for details about the header prepended to the data.

    Interface:
    Above:
        send unencoded bytes of payload or EventData objects with unencoded bytes
            of payload. If a header is given in the context with key 'header' in
            the EventData object, it will be completed (i.e. ARQ information
            filled in) and sent with the payload.
        receive EventData objects with unencoded bytes of payload. The associated
            header will be given in the context with  key 'header'.
    Below:
        to_send EventData objects with header-wrapped bytestrings.
        to_receive header-wrapped bytestrings or EventData objects with
            header-wrapped bytestrings.
    """

    DATA_UNIT = ReliableBuffer
    RECEIVABLE_TYPES = {
        DATA_UNIT.TYPE,
        DATA_TYPES[('bytes', 'buffer')]
    }

    def __init__(self, clock_start=0.0):
        """Initialize members."""
        super().__init__(
            clock_start=clock_start, logger_name=__name__, logger_indentation=3
        )

        self.arq_sender = GBNSender(self.clock)
        self.arq_receiver = GBNReceiver()

    # Override CommunicationLink
    @property
    def counters(self):
        """Override CommunicationLink.counters."""
        return {
            'arq_receiver': self.arq_receiver.counter,
            'arq_sender': self.arq_sender.counter,
            **super().counters
        }

    def _make_clock_request(self):
        next_in_flight = self.arq_sender.next_in_flight
        if next_in_flight is None:
            return None
        return self.make_clock_request(
            next_in_flight['resend_timer'].timeout_time, context=next_in_flight
        )

    def _make_context_from_resend(self, in_flight):
        """Make context from to_send record.

        send_time is the clock time that the reliable buffer was added to the send queue.
        resend_time is the clock time that the latest re-transmission attempt occurred.
        in_flight_start_time is the clock time that the reliable buffer was moved from
            the send queue to the in-flight queue and the first transmission attempted.
        resend_attempts is the total number of re-transmission attempts made, incuding
            the current attempt.
        in_flight_duration is the total duration that the reliable buffer has been on the
            in-flight queue.
        reason is the reason for the retransmission.
        """
        return {
            'send_time': in_flight['send_time'],
            'resend_time': self.clock.time,
            'in_flight_start_time': in_flight['in_flight_timer'].start_time,
            'resend_attempts': in_flight['resend_attempts'],
            'in_flight_duration': in_flight['in_flight_timer'].elapsed,
            'resend_reason': in_flight.get('resend_reason'),
        }

    def _make_context_from_to_send(self, to_send):
        """Make context from to_send record.

        send_time is the clock time that the reliable buffer was added to the send queue.
        in_flight_start_time is the clock time that the reliable buffer was moved from
            the send queue to the in-flight queue and the first transmission attempted.
        """
        return {
            'send_time': to_send['send_time'],
            'in_flight_start_time': self.clock.time
        }

    # Override DataUnitLink

    def parse_data_unit(self, event):
        """Override DataUnitLink.parse_data_unit."""
        result = super().parse_data_unit(event)
        if not isinstance(result, self.DATA_UNIT):
            return result

        reliable_buffer = result
        # TODO: If the reliable buffer is not consistent, log and return None
        self._log_received(reliable_buffer)
        return reliable_buffer

    def receiver_process(self, event):
        """Override DataUnitLink.receiver_process."""
        self.update_clock_time(event)
        if isinstance(event, LinkException):
            self.receiver_counter['caught_exception'] += 1
            data_event = self.make_link_data(
                self.arq_sender.make_nak().buffer, 'down', event
            )
            self.receiver_counter['to_send_nak'] += 1
            self.directly_to_send(data_event)
            return

        reliable_buffer = self.parse_data_unit(event)
        if reliable_buffer is None:
            return

        self.receiver_counter['to_receive_reliable_buffer'] += 1
        if self.arq_sender.retransmit_from_received(reliable_buffer):
            self.receiver_counter['requested_retransmission'] += 1
            self.logger.info(
                'Received retransmission request:\t\t{}'
                .format(reliable_buffer.header)
            )
            for in_flight in self.arq_sender.resend_in_flight('NAK'):
                data_event = self.make_link_data(
                    in_flight['reliable_buffer'].buffer, 'down', event,
                    type=self.DATA_UNIT.TYPE,
                    context=self._make_context_from_resend(in_flight)
                )
                self.receiver_counter['to_send_retransmission'] += 1
                self.directly_to_send(data_event)
        if not self.arq_sender.to_receive(reliable_buffer):
            self.receiver_counter['unexpected_reliable_buffer'] += 1
            self.logger.error(
                'Received reliable buffer with unexpected ACK {}'
                .format(reliable_buffer)
            )
            return

        if not self.arq_receiver.received_expected(reliable_buffer):
            self.receiver_counter['unexpected_reliable_buffer'] += 1
            data_event = self.make_link_data(
                self.arq_sender.make_nak().buffer, 'down', event,
                context={'reliable_buffer': reliable_buffer}
            )
            self.receiver_counter['to_send_nak'] += 1
            self.directly_to_send(data_event)
            return

        if reliable_buffer.header.type >= DATA_TYPES[('bytes', 'buffer')]:
            yield self.make_link_received_event(
                reliable_buffer, event, {'header': reliable_buffer.header}
            )
        for to_send in self.arq_sender.flush_send_queue():
            data_event = self.make_link_data(
                to_send['reliable_buffer'].buffer, 'down', event,
                context=self._make_context_from_to_send(to_send)
            )
            self.receiver_counter['to_send_in_flight'] += 1
            self.directly_to_send(data_event)

    def make_data_unit(self, event):
        """Override DataUnitLink.make_data_unit."""
        result = super().make_data_unit(event)
        if result is None:
            return

        reliable_buffer = result
        self.logger.debug(
            'Sending:\t\t\t{}'.format(reliable_buffer.preflight_string)
        )
        return reliable_buffer

    def sender_process(self, event):
        """Override DataUnitLink.sender_process."""
        self.update_clock_time(event)
        reliable_buffer = self.make_data_unit(event)
        if reliable_buffer is not None:
            self.sender_counter['send_reliable_buffer'] += 1
            self.arq_sender.send(reliable_buffer, event)
        if self.arq_sender.retransmit_from_timeout:
            self.logger.info(
                'In-flight reliable_buffer timed out:\t\t{}'
                .format(self.arq_sender.next_in_flight['reliable_buffer'].header)
            )
            self.sender_counter['timeout_retransmission'] += 1
            for in_flight in self.arq_sender.resend_in_flight('timeout'):
                data_event = self.make_link_data(
                    in_flight['reliable_buffer'].buffer, 'down', event,
                    type=self.DATA_UNIT.TYPE,
                    context=self._make_context_from_resend(in_flight)
                )
                self.sender_counter['to_send_retransmission'] += 1
                yield data_event

        for to_send in self.arq_sender.flush_send_queue():
            data_event = self.make_link_data(
                to_send['reliable_buffer'].buffer, 'down', event,
                type=self.DATA_UNIT.TYPE,
                context=self._make_context_from_to_send(to_send)
            )
            self.sender_counter['to_send_in_flight'] += 1
            yield data_event

        clock_request = self._make_clock_request()
        if clock_request is not None:
            yield clock_request

    # Logging

    def _log_received(self, reliable_buffer):
        """Emit logging message of received reliable buffer."""
        if reliable_buffer.header.flags.nak and reliable_buffer.header.flags.ack:
            self.logger.debug(
                'Received NAK {}:\t\t{}'
                .format(reliable_buffer.header.ack_num, reliable_buffer)
            )
        elif reliable_buffer.header.flags.ack:
            self.logger.debug(
                'Received ACK {}:\t\t{}'
                .format(reliable_buffer.header.ack_num, reliable_buffer)
            )
        else:
            self.logger.debug(
                'Received data:\t\t{}'.format(reliable_buffer)
            )
        # if reliable_buffer.header.length == 0:
        #     self.logger.debug(
        #         'ReliableBuffer Link received control:\t{}'
        #         .format(reliable_buffer.header.control_fields_string)
        #     )
        # else:
        #     self.logger.debug(
        #         'reliable_buffer.header)
        #     )
