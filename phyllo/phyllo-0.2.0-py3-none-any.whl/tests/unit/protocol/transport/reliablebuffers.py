"""Test the protocol.transport.reliablebuffers module."""

# Builtins

# Packages

from phylline.links.clocked import LinkClockRequest
from phylline.links.events import LinkException
from phylline.util.logging import hex_bytes
from phylline.util.timing import Clock

from phyllo.protocol.communication import DATA_TYPES
from phyllo.protocol.transport.reliablebuffers import GBNSender, ReliableBufferLink
from phyllo.protocol.transport.reliablebuffers import (
    ReliableBuffer, ReliableBufferFlags, ReliableBufferHeader
)


def assert_payload_contents(queue, value_min, value_max):
    """Check whether the payloads of queued reliable_buffers are in the specified range."""
    queue = list(queue)
    assert len(queue) == value_max - value_min + 1
    for reliable_buffer in queue:
        assert reliable_buffer['reliable_buffer'].payload[0] >= value_min
        assert reliable_buffer['reliable_buffer'].payload[0] <= value_max


def test_gbn_sender():
    """Test GBNSender in normal behavior."""
    print('Testing GBN Sender...')
    clock = Clock(time=0)
    sender = GBNSender(clock)

    print('Testing send queue:')
    assert sender.counter['send_flushed'] == 0
    assert len(list(sender.flush_send_queue())) == 0
    assert sender.counter['send_flushed'] == 0
    assert sender.counter['send_queued'] == 0
    for i in range(sender.SENDER_WINDOW_SIZE - 1):
        dummy_reliable_buffer = ReliableBuffer(payload=bytes([i]))
        sender.send(dummy_reliable_buffer)
        assert sender.send_queue_availability
        assert sender.counter['send_queued'] == i + 1
    assert sender.counter['availability_filled'] == 0
    sender.send(ReliableBuffer(payload=bytes([i + 1])))
    assert sender.counter['send_queued'] == sender.SENDER_WINDOW_SIZE
    assert sender.counter['send_availability_filled'] == 1
    assert sender.send_queue_availability == 0
    assert len(sender.send_queue) == sender.SENDER_WINDOW_SIZE
    print(
        'Expect a warning about over-stuffed send queue with reliable_buffer of '
        'payload {}:'.format(hex_bytes([i + 2]))
    )
    assert sender.counter['send_availability_exceeded'] == 0
    sender.send(ReliableBuffer(payload=bytes([i + 2])))
    assert sender.counter['send_queued'] == sender.SENDER_WINDOW_SIZE + 1
    assert sender.counter['send_availability_exceeded'] == 1
    assert sender.send_queue_availability == 0
    assert len(sender.send_queue) == sender.SENDER_WINDOW_SIZE + 1

    print('Testing send queue transmission:')
    assert sender.counter['send_flushed'] == 0
    assert sender.counter['in_flight_queued'] == 0
    assert_payload_contents(
        sender.flush_send_queue(), 0, sender.SENDER_WINDOW_SIZE - 1
    )
    assert sender.counter['send_emptied'] == 0
    assert sender.counter['send_flushed'] == sender.SENDER_WINDOW_SIZE
    assert sender.counter['in_flight_queued'] == sender.SENDER_WINDOW_SIZE
    assert sender.counter['in_flight_availability_filled'] == 1
    assert len(sender.in_flight_queue) == sender.SENDER_WINDOW_SIZE
    assert sender.in_flight_queue_availability == 0
    assert len(sender.send_queue) == 1
    assert sender.send_queue_availability == sender.SENDER_WINDOW_SIZE - 1

    print('Testing in-flight queue timeout:')
    assert not sender.retransmit_from_timeout
    clock.update(time=sender.send_timeout)
    assert sender.retransmit_from_timeout
    assert sender.counter['in_flight_resent'] == 0
    assert len(list(sender.resend_in_flight('timeout'))) == sender.SENDER_WINDOW_SIZE
    assert sender.counter['in_flight_resent'] == sender.SENDER_WINDOW_SIZE
    assert not sender.retransmit_from_timeout
    clock.update(time=2 * sender.send_timeout)
    assert sender.retransmit_from_timeout
    assert len(list(sender.resend_in_flight('timeout'))) == sender.SENDER_WINDOW_SIZE
    assert sender.counter['in_flight_resent'] == 2 * sender.SENDER_WINDOW_SIZE
    assert not sender.retransmit_from_timeout

    print('Testing valid ACK:')
    dummy_ack = ReliableBuffer(
        header=ReliableBufferHeader(ack_num=1, flags=ReliableBufferFlags(ack=True)),
        payload=bytes([128])
    )
    assert not sender.retransmit_from_received(dummy_ack)
    assert sender.counter['in_flight_emptied'] == 0
    sender.to_receive(dummy_ack)
    assert sender.counter['acknowledge'] == 1
    assert sender.last_acknowledged == 1
    assert len(sender.in_flight_queue) == sender.SENDER_WINDOW_SIZE - 1
    assert_payload_contents(sender.in_flight_queue, 1, sender.SENDER_WINDOW_SIZE - 1)
    assert sender.counter['send_emptied'] == 0
    assert_payload_contents(
        sender.flush_send_queue(), sender.SENDER_WINDOW_SIZE, sender.SENDER_WINDOW_SIZE
    )
    assert sender.counter['send_emptied'] == 1
    assert sender.counter['send_flushed'] == sender.SENDER_WINDOW_SIZE + 1
    assert sender.counter['in_flight_queued'] == sender.SENDER_WINDOW_SIZE + 1
    assert sender.counter['send_availability_filled'] == 2
    assert sender.counter['in_flight_emptied'] == 0
    assert len(sender.in_flight_queue) == sender.SENDER_WINDOW_SIZE
    assert sender.in_flight_queue_availability == 0
    assert len(sender.send_queue) == 0
    assert sender.send_queue_availability == sender.SENDER_WINDOW_SIZE

    print('Testing invalid ACK behind:')
    print('Expect an error about unexpected ACK {}:'.format(0))
    dummy_ack = ReliableBuffer(
        header=ReliableBufferHeader(ack_num=0, flags=ReliableBufferFlags(ack=True)),
        payload=bytes([128])
    )
    assert not sender.retransmit_from_received(dummy_ack)
    assert sender.counter['acknowledge_unexpected'] == 0
    sender.to_receive(dummy_ack)
    assert sender.counter['acknowledge_unexpected'] == 1
    assert sender.counter['acknowledge'] == 1
    assert sender.last_acknowledged == 1
    assert len(sender.in_flight_queue) == sender.SENDER_WINDOW_SIZE

    print('Testing invalid ACK ahead:')
    print('Expect an error about unexpected ACK {}:'.format(100))
    dummy_ack = ReliableBuffer(
        header=ReliableBufferHeader(ack_num=100, flags=ReliableBufferFlags(ack=True)),
        payload=bytes([128])
    )
    assert not sender.retransmit_from_received(dummy_ack)
    assert sender.counter['acknowledge_unexpected'] == 1
    sender.to_receive(dummy_ack)
    assert sender.counter['acknowledge_unexpected'] == 2
    assert sender.counter['acknowledge'] == 1
    assert sender.last_acknowledged == 1
    assert len(sender.in_flight_queue) == sender.SENDER_WINDOW_SIZE

    print('Testing NAK:')
    for ack_num in range(sender.SEQUENCE_NUMBER_SPACE):
        assert sender.retransmit_from_received(ReliableBuffer(
            header=ReliableBufferHeader(
                ack_num=ack_num, flags=ReliableBufferFlags(ack=True, nak=True)
            ), payload=bytes([128])
        ))
    assert not sender.retransmit_from_received(ReliableBuffer(
        header=ReliableBufferHeader(ack_num=1, flags=ReliableBufferFlags(nak=True)),
        payload=bytes([128])
    ))

    print('Testing valid multiple ACK:')
    dummy_ack = ReliableBuffer(
        header=ReliableBufferHeader(ack_num=9, flags=ReliableBufferFlags(ack=True)),
        payload=bytes([128])
    )
    assert not sender.retransmit_from_received(dummy_ack)
    assert sender.counter['in_flight_emptied'] == 0
    assert sender.counter['acknowledge'] == 1
    sender.to_receive(dummy_ack)
    assert sender.counter['acknowledge'] == 9
    assert sender.last_acknowledged == 9
    assert len(sender.in_flight_queue) == 0
    assert sender.counter['send_emptied'] == 1
    assert len(sender.send_queue) == 0
    assert sender.in_flight_queue_availability == sender.SENDER_WINDOW_SIZE
    assert len(list(sender.flush_send_queue())) == 0
    assert sender.counter['send_emptied'] == 1
    assert sender.counter['send_flushed'] == sender.SENDER_WINDOW_SIZE + 1
    assert sender.counter['in_flight_queued'] == sender.SENDER_WINDOW_SIZE + 1
    assert sender.counter['send_availability_filled'] == 2
    assert sender.counter['in_flight_emptied'] == 1
    assert len(sender.in_flight_queue) == 0
    assert sender.in_flight_queue_availability == sender.SENDER_WINDOW_SIZE
    assert len(sender.send_queue) == 0
    assert sender.send_queue_availability == sender.SENDER_WINDOW_SIZE

    # TODO: test rollover


def assert_send_reliable_buffer_ranges(
    to_send, sequence_min, sequence_max, payload_type,
    payload_first=None, payload_second_min=None, payload_second_max=None
):
    """Check whether reliable buffers exactly cover the specified ranges."""
    if payload_second_min is not None and payload_second_max is not None:
        assert len(to_send) == payload_second_max - payload_second_min + 1
    assert to_send[0].data[0] == sequence_min
    assert to_send[-1].data[0] == sequence_max
    for (i, send_buffer) in enumerate(to_send):
        assert send_buffer.data[0] == (sequence_min + i) % GBNSender.SEQUENCE_NUMBER_SPACE
        assert send_buffer.data[3] == payload_type
        if payload_first is not None:
            send_buffer.data[4] == payload_first
        if payload_second_min is not None:
            assert send_buffer.data[5] == (payload_second_min + i) % 256


def assert_receive_reliable_buffer_ranges(
    receive, sequence_min, sequence_max, type,
    payload_first, payload_second_min, payload_second_max
):
    """Check whether reliable buffers exactly cover the specified ranges."""
    assert len(receive) == payload_second_max - payload_second_min + 1
    assert receive[0].context['header'].seq_num == sequence_min
    assert receive[-1].context['header'].seq_num == sequence_max
    for (i, receive_reliable_buffer) in enumerate(receive):
        assert receive_reliable_buffer.context['header'].seq_num == (
            (sequence_min + i) % GBNSender.SEQUENCE_NUMBER_SPACE
        )
        assert receive_reliable_buffer.context['header'].type == type
        receive_reliable_buffer.data[0] == payload_first
        assert receive_reliable_buffer.data[1] == (payload_second_min + i) % 256


def test_reliable_buffer_link():
    """Test ReliableBufferLink in normal behavior."""
    print('Testing ReliableBuffer Link...')
    reliable_buffer_counter = 0
    reliable_buffer_link = ReliableBufferLink()

    print(
        'Requesting to send {} reliable buffers...'
        .format(2 * GBNSender.SENDER_WINDOW_SIZE)
    )
    for i in range(2 * GBNSender.SENDER_WINDOW_SIZE):
        reliable_buffer_link.send(bytes([0, reliable_buffer_counter]))
        reliable_buffer_counter += 1
    assert (
        reliable_buffer_link.sender_counter['send_reliable_buffer']
        == 2 * GBNSender.SENDER_WINDOW_SIZE
    )
    assert (
        reliable_buffer_link.arq_sender.counter['send_flushed']
        == GBNSender.SENDER_WINDOW_SIZE
    )
    assert (
        reliable_buffer_link.arq_sender.counter['send_queued']
        == 2 * GBNSender.SENDER_WINDOW_SIZE
    )
    assert (
        reliable_buffer_link.arq_sender.counter['send_availability_filled'] == 1
    )
    assert (
        reliable_buffer_link.arq_sender.counter['send_availability_exceeded'] == 0
    )
    assert (
        reliable_buffer_link.sender_counter['to_send_in_flight']
        == GBNSender.SENDER_WINDOW_SIZE
    )
    assert (
        reliable_buffer_link.arq_sender.counter['in_flight_queued']
        == GBNSender.SENDER_WINDOW_SIZE
    )
    assert (
        reliable_buffer_link.arq_sender.counter['in_flight_availability_filled'] == 1
    )
    assert not reliable_buffer_link.arq_sender.send_queue_availability
    assert reliable_buffer_link.has_to_send()
    to_send = list(reliable_buffer_link.to_send_all())
    assert len(to_send) == GBNSender.SENDER_WINDOW_SIZE + 1
    assert isinstance(to_send[1], LinkClockRequest)
    assert to_send[1].requested_time == reliable_buffer_link.arq_sender.send_timeout
    del to_send[1]
    assert_send_reliable_buffer_ranges(
        to_send, 0, GBNSender.SENDER_WINDOW_SIZE - 1, DATA_TYPES[('bytes', 'buffer')],
        0, 0, GBNSender.SENDER_WINDOW_SIZE - 1
    )

    print('Requesting to send another reliable buffer to over-stuff the send queue...')
    print(
        'Expect a warning about over-stuffed send queue with reliable buffer '
        'of payload {}:'.format(hex_bytes([reliable_buffer_counter]))
    )
    reliable_buffer_link.send(bytes([0, reliable_buffer_counter]))
    reliable_buffer_counter += 1
    assert (
        reliable_buffer_link.sender_counter['send_reliable_buffer']
        == reliable_buffer_counter
    )
    assert (
        reliable_buffer_link.arq_sender.counter['send_queued']
        == reliable_buffer_counter
    )
    assert (
        reliable_buffer_link.arq_sender.counter['send_availability_exceeded'] == 1
    )

    print('Letting in-flight reliable buffers time out...')
    assert not reliable_buffer_link.has_to_send()
    reliable_buffer_link.update_clock(reliable_buffer_link.arq_sender.send_timeout)
    assert (
        reliable_buffer_link.clock.time
        == reliable_buffer_link.arq_sender.send_timeout
    )
    assert reliable_buffer_link.sender_counter['timeout_retransmission'] == 1
    assert (
        reliable_buffer_link.sender_counter['to_send_retransmission']
        == GBNSender.SENDER_WINDOW_SIZE
    )
    assert (
        reliable_buffer_link.arq_sender.counter['in_flight_resent']
        == GBNSender.SENDER_WINDOW_SIZE
    )
    assert (
        reliable_buffer_link.sender_counter['to_send_in_flight']
        == GBNSender.SENDER_WINDOW_SIZE
    )
    assert reliable_buffer_link.has_to_send()
    to_send = list(reliable_buffer_link.to_send_all())
    assert len(to_send) == GBNSender.SENDER_WINDOW_SIZE + 1
    assert isinstance(to_send[-1], LinkClockRequest)
    assert (
        to_send[-1].requested_time
        == 2 * reliable_buffer_link.arq_sender.send_timeout
    )
    del to_send[-1]
    assert_send_reliable_buffer_ranges(
        to_send, 0, GBNSender.SENDER_WINDOW_SIZE - 1, DATA_TYPES[('bytes', 'buffer')],
        0, 0, GBNSender.SENDER_WINDOW_SIZE - 1
    )

    print('Receiving a valid ACK...')
    ack = ReliableBuffer(
        header=ReliableBufferHeader(
            seq_num=0, ack_num=1, flags=ReliableBufferFlags(ack=True),
            type=DATA_TYPES[('transport', 'validated_datagram')]
        ), payload=bytes([255, 0])
    )
    assert reliable_buffer_link.arq_sender.counter['acknowledge'] == 0
    reliable_buffer_link.to_receive(ack.buffer)
    # Check receive
    assert reliable_buffer_link.receiver_counter['to_receive_reliable_buffer'] == 1
    assert reliable_buffer_link.receiver_counter['unexpected_reliable_buffer'] == 0
    assert reliable_buffer_link.arq_sender.counter['acknowledge'] == 1
    assert reliable_buffer_link.arq_sender.counter['acknowledge_rollover'] == 0
    assert reliable_buffer_link.arq_sender.counter['acknowledge_unexpected'] == 0
    assert reliable_buffer_link.arq_sender.counter['in_flight_emptied'] == 0
    assert reliable_buffer_link.has_receive()
    receive = list(reliable_buffer_link.receive_all())
    assert len(receive) == 1
    assert_receive_reliable_buffer_ranges(
        receive, 0, 0, DATA_TYPES[('transport', 'validated_datagram')], 255, 0, 0
    )
    # Check to_send
    assert reliable_buffer_link.receiver_counter['requested_retransmission'] == 0
    assert reliable_buffer_link.receiver_counter['to_send_retransmission'] == 0
    assert reliable_buffer_link.receiver_counter['to_send_in_flight'] == 1
    assert (
        reliable_buffer_link.arq_sender.counter['in_flight_queued']
        == GBNSender.SENDER_WINDOW_SIZE + 1
    )
    assert (
        reliable_buffer_link.arq_sender.counter['in_flight_availability_filled'] == 2
    )
    assert reliable_buffer_link.has_to_send()
    to_send = list(reliable_buffer_link.to_send_all())
    assert_send_reliable_buffer_ranges(
        to_send, 8, 8, DATA_TYPES[('bytes', 'buffer')], 0, 8, 8
    )

    print('Letting in-flight reliable buffers time out...')
    assert not reliable_buffer_link.has_to_send()
    reliable_buffer_link.update_clock(
        2 * reliable_buffer_link.arq_sender.send_timeout
    )
    assert (
        reliable_buffer_link.clock.time
        == 2 * reliable_buffer_link.arq_sender.send_timeout
    )
    assert reliable_buffer_link.sender_counter['timeout_retransmission'] == 2
    assert (
        reliable_buffer_link.sender_counter['to_send_retransmission']
        == 2 * GBNSender.SENDER_WINDOW_SIZE
    )
    assert (
        reliable_buffer_link.arq_sender.counter['in_flight_resent']
        == 2 * GBNSender.SENDER_WINDOW_SIZE
    )
    assert (
        reliable_buffer_link.sender_counter['to_send_in_flight']
        == GBNSender.SENDER_WINDOW_SIZE
    )
    assert reliable_buffer_link.has_to_send()
    to_send = list(reliable_buffer_link.to_send_all())
    assert len(to_send) == GBNSender.SENDER_WINDOW_SIZE + 1
    assert isinstance(to_send[-1], LinkClockRequest)
    assert (
        to_send[-1].requested_time
        == 3 * reliable_buffer_link.arq_sender.send_timeout
    )
    del to_send[-1]
    assert_send_reliable_buffer_ranges(
        to_send, 1, GBNSender.SENDER_WINDOW_SIZE, DATA_TYPES[('bytes', 'buffer')],
        0, 1, GBNSender.SENDER_WINDOW_SIZE
    )

    print('Receiving an invalid ACK behind...')
    ack = ReliableBuffer(
        header=ReliableBufferHeader(
            seq_num=1, ack_num=0, flags=ReliableBufferFlags(ack=True)
        ), payload=bytes([255, 1])
    )
    assert reliable_buffer_link.arq_sender.counter['acknowledge'] == 1
    assert reliable_buffer_link.receiver_counter['unexpected_reliable_buffer'] == 0
    print('Expect two errors about unexpected ACK {}:'.format(0))
    reliable_buffer_link.to_receive(ack.buffer)
    # Check receive
    assert reliable_buffer_link.receiver_counter['to_receive_reliable_buffer'] == 2
    assert reliable_buffer_link.receiver_counter['unexpected_reliable_buffer'] == 1
    assert reliable_buffer_link.arq_sender.counter['acknowledge'] == 1
    assert reliable_buffer_link.arq_sender.counter['acknowledge_rollover'] == 0
    assert reliable_buffer_link.arq_sender.counter['acknowledge_unexpected'] == 1
    assert reliable_buffer_link.arq_sender.counter['in_flight_emptied'] == 0
    assert not reliable_buffer_link.has_receive()
    # Check to_send
    assert reliable_buffer_link.receiver_counter['requested_retransmission'] == 0
    assert reliable_buffer_link.receiver_counter['to_send_retransmission'] == 0
    assert reliable_buffer_link.receiver_counter['to_send_in_flight'] == 1

    print('Receiving an invalid ACK ahead...')
    ack = ReliableBuffer(
        header=ReliableBufferHeader(
            seq_num=2, ack_num=255, flags=ReliableBufferFlags(ack=True)
        ), payload=bytes([255, 2])
    )
    print('Expect two errors about unexpected ACK {}:'.format(255))
    assert reliable_buffer_link.arq_sender.counter['acknowledge'] == 1
    reliable_buffer_link.to_receive(ack.buffer)
    # Check receive
    assert reliable_buffer_link.receiver_counter['to_receive_reliable_buffer'] == 3
    assert reliable_buffer_link.receiver_counter['unexpected_reliable_buffer'] == 2
    assert reliable_buffer_link.arq_sender.counter['acknowledge'] == 1
    assert reliable_buffer_link.arq_sender.counter['acknowledge_rollover'] == 0
    assert reliable_buffer_link.arq_sender.counter['acknowledge_unexpected'] == 2
    assert reliable_buffer_link.arq_sender.counter['in_flight_emptied'] == 0
    assert not reliable_buffer_link.has_receive()
    # Check to_send
    assert reliable_buffer_link.receiver_counter['requested_retransmission'] == 0
    assert reliable_buffer_link.receiver_counter['to_send_retransmission'] == 0
    assert reliable_buffer_link.receiver_counter['to_send_in_flight'] == 1
    assert not reliable_buffer_link.has_to_send()

    print('Receiving a NAK...')
    nak = ReliableBuffer(
        header=ReliableBufferHeader(
            seq_num=3, ack_num=1, flags=ReliableBufferFlags(ack=True, nak=True),
            type=DATA_TYPES[('layer', 'control')],
        ), payload=bytes([255, 3])
    )
    assert reliable_buffer_link.receiver_counter['requested_retransmission'] == 0
    assert reliable_buffer_link.arq_sender.counter['acknowledge'] == 1
    assert not reliable_buffer_link.has_to_send()
    reliable_buffer_link.to_receive(nak.buffer)
    # Check receive
    assert reliable_buffer_link.receiver_counter['to_receive_reliable_buffer'] == 4
    assert reliable_buffer_link.arq_sender.counter['acknowledge'] == 1
    assert reliable_buffer_link.receiver_counter['requested_retransmission'] == 1
    assert (
        reliable_buffer_link.receiver_counter['to_send_retransmission']
        == GBNSender.SENDER_WINDOW_SIZE
    )
    assert (
        reliable_buffer_link.arq_sender.counter['in_flight_resent']
        == 3 * GBNSender.SENDER_WINDOW_SIZE
    )
    assert not reliable_buffer_link.has_receive()
    # Check send
    assert (
        reliable_buffer_link.sender_counter['to_send_in_flight']
        == GBNSender.SENDER_WINDOW_SIZE
    )
    assert reliable_buffer_link.has_to_send()
    assert_send_reliable_buffer_ranges(
        list(reliable_buffer_link.to_send_all()), 1, GBNSender.SENDER_WINDOW_SIZE,
        DATA_TYPES[('bytes', 'buffer')], 0, 1, GBNSender.SENDER_WINDOW_SIZE
    )

    print('Receiving a valid multiple ACK...')
    ack = ReliableBuffer(
        header=ReliableBufferHeader(
            seq_num=4, ack_num=9, flags=ReliableBufferFlags(ack=True),
            type=DATA_TYPES[('transport', 'datagram')]
        ), payload=bytes([255, 4])
    )
    assert reliable_buffer_link.receiver_counter['to_receive_reliable_buffer'] == 4
    assert reliable_buffer_link.arq_sender.counter['acknowledge'] == 1
    assert reliable_buffer_link.arq_sender.counter['acknowledge_rollover'] == 0
    assert reliable_buffer_link.arq_sender.counter['in_flight_emptied'] == 0
    reliable_buffer_link.to_receive(ack.buffer)
    # Check receive
    assert reliable_buffer_link.receiver_counter['to_receive_reliable_buffer'] == 5
    assert reliable_buffer_link.arq_sender.counter['acknowledge'] == 9
    assert reliable_buffer_link.arq_sender.counter['acknowledge_rollover'] == 0
    assert reliable_buffer_link.arq_sender.counter['in_flight_emptied'] == 0
    assert reliable_buffer_link.has_receive()
    assert_receive_reliable_buffer_ranges(
        list(reliable_buffer_link.receive_all()), 4, 4,
        DATA_TYPES[('transport', 'datagram')], 255, 4, 4
    )
    # Check send
    assert reliable_buffer_link.receiver_counter['to_send_in_flight'] == 9
    assert reliable_buffer_link.arq_sender.counter['in_flight_queued'] == (
        2 * GBNSender.SENDER_WINDOW_SIZE + 1
    )
    assert (
        reliable_buffer_link.arq_sender.counter['in_flight_availability_filled'] == 3
    )
    assert reliable_buffer_link.has_to_send()
    assert_send_reliable_buffer_ranges(
        list(reliable_buffer_link.to_send_all()),
        GBNSender.SENDER_WINDOW_SIZE + 1, GBNSender.SENDER_WINDOW_SIZE * 2,
        DATA_TYPES[('bytes', 'buffer')], 0,
        GBNSender.SENDER_WINDOW_SIZE + 1, GBNSender.SENDER_WINDOW_SIZE * 2
    )

    # TODO: test rollover

    # TODO: test valid and invalid ACKs around rollover


def test_reliable_buffer_link_receive_exception():
    """Test ReliableBufferLink when it receives an exception."""
    print('Testing ReliableBuffer Link with receiving exception...')
    reliable_buffer_link = ReliableBufferLink()

    assert reliable_buffer_link.receiver_counter['caught_exception'] == 0
    assert reliable_buffer_link.receiver_counter['to_send_nak'] == 0
    reliable_buffer_link.to_receive(LinkException('Dummy exception'))
    assert reliable_buffer_link.receiver_counter['caught_exception'] == 1
    assert reliable_buffer_link.receiver_counter['to_send_nak'] == 1
    # Check receive
    assert not reliable_buffer_link.has_receive()
    # Check to_send
    assert reliable_buffer_link.has_to_send()
    to_send = list(reliable_buffer_link.to_send_all())
    assert len(to_send) == 1
    assert_send_reliable_buffer_ranges(to_send, 0, 0, DATA_TYPES[('layer', 'control')])
    assert to_send[0].data[1] == 0
    flags = ReliableBufferFlags(to_send[0].data[2])
    assert flags.nos
    assert flags.ack
    assert flags.nak
