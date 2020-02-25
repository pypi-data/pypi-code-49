"""Test the protocol.transport.datagrams module."""

# Builtins

import struct

# Packages

from phylline.links.events import LinkException
from phylline.pipelines import AutomaticPipeline

from phyllo.protocol.communication import DATA_TYPES
from phyllo.protocol.transport.datagrams import (
    Datagram, DatagramHeader, DatagramLink
)
from phyllo.protocol.transport.datagrams import (
    ValidatedDatagramHeader, ValidatedDatagramLink
)


# Datagram


def test_normal(datagram_link=DatagramLink()):
    """Exercise the DatagramLink functionality."""
    print('Testing {}...'.format(datagram_link.__class__.__qualname__))
    payload = b'\1\2\3\4\0'
    datagram_buffer = b'\5\x10\1\2\3\4\0'

    # Send
    send_count = datagram_link.sender_counter['send']
    to_send_count = datagram_link.sender_counter['to_send']
    datagram_link.send(payload)
    assert datagram_link.sender_counter['send'] == send_count + 1
    assert datagram_link.sender_counter['to_send'] == to_send_count + 1
    assert datagram_link.has_to_send()
    result = datagram_link.to_send()
    assert result.data == datagram_buffer

    # Receive
    receive_count = datagram_link.receiver_counter['receive']
    to_receive_count = datagram_link.receiver_counter['to_receive']
    datagram_link.to_receive(result)
    assert datagram_link.receiver_counter['to_receive'] == to_receive_count + 1
    assert datagram_link.receiver_counter['receive'] == receive_count + 1
    assert datagram_link.has_receive()
    result = datagram_link.receive()
    print(result)
    assert result.data == payload


def test_invalid_data():
    """Exercise the DatagramLink error handling."""
    print('Testing Datagram Link with invalid payloads...')
    bad_payload = b''.join(b'\1\2\3\4' for i in range(100))
    assert len(bad_payload) > Datagram().payload_size_limit
    datagram_link = DatagramLink()

    # Send
    print('Expect an excessively long payload error in logging:')
    datagram_link.send(bad_payload)
    assert datagram_link.sender_counter['send'] == 1
    assert datagram_link.sender_counter['to_send'] == 0
    assert datagram_link.sender_counter['error_invalid_payload'] == 1
    assert not datagram_link.has_to_send()
    test_normal(datagram_link=datagram_link)

    # Receive
    print('Expect a parse error in logging:')
    receive_count = datagram_link.receiver_counter['receive']
    to_receive_count = datagram_link.receiver_counter['to_receive']
    datagram_link.to_receive(b'\1')
    assert datagram_link.receiver_counter['to_receive'] == to_receive_count + 1
    assert datagram_link.receiver_counter['receive'] == receive_count
    assert datagram_link.receiver_counter['error'] == 1
    assert datagram_link.receiver_counter['error_parse'] == 1
    assert datagram_link.has_receive()
    result = datagram_link.receive()
    assert isinstance(result, LinkException)
    assert isinstance(result.context['exception'], struct.error)
    test_normal(datagram_link=datagram_link)


def test_invalid_length():
    """Exercise the DatagramLink error handling."""
    print('Testing Datagram Link with invalid lengths...')
    datagram_link = DatagramLink()
    payload = b'\1\2\3\4\0'
    header = DatagramHeader(length=4, type=DATA_TYPES[('bytes', 'buffer')])
    datagram_buffer = b'\4\x10\1\2\3\4\0'

    # Send
    print('Expect an inconsistent length warning in logging:')
    datagram_link.send_data(payload, context={'header': header})
    assert datagram_link.sender_counter['send'] == 1
    assert datagram_link.sender_counter['to_send'] == 1
    assert datagram_link.sender_counter['warning_inconsistent'] == 1
    assert datagram_link.has_to_send()
    result = datagram_link.to_send()
    assert result.data == datagram_buffer
    test_normal(datagram_link=datagram_link)

    # Receive
    print('Expect an inconsistent length error in logging:')
    receive_count = datagram_link.receiver_counter['receive']
    to_receive_count = datagram_link.receiver_counter['to_receive']
    datagram_link.to_receive(result)
    assert datagram_link.receiver_counter['to_receive'] == to_receive_count + 1
    assert datagram_link.receiver_counter['receive'] == receive_count
    assert datagram_link.receiver_counter['error'] == 1
    assert datagram_link.receiver_counter['error_inconsistent'] == 1
    assert datagram_link.has_receive()
    result = datagram_link.receive()
    assert isinstance(result, LinkException)
    assert result.context['specified_length'] == 4
    assert result.context['computed_length'] == 5
    test_normal(datagram_link=datagram_link)


# ValidatedDatagram


def test_validated_normal(datagram_link=ValidatedDatagramLink()):
    """Exercise the ValidatedDatagramLink functionality."""
    print('Testing Validated Datagram Link...')
    payload = b'\1\2\3\4\0'
    crc = b'\xd2\xaa\x86\xd0'

    # Send
    send_count = datagram_link.sender_counter['send']
    to_send_count = datagram_link.sender_counter['to_send']
    datagram_link.send(payload)
    assert datagram_link.sender_counter['send'] == send_count + 1
    assert datagram_link.sender_counter['to_send'] == to_send_count + 1
    assert datagram_link.has_to_send()
    result = datagram_link.to_send()
    assert result.data[:4] == crc

    # Receive
    receive_count = datagram_link.receiver_counter['receive']
    to_receive_count = datagram_link.receiver_counter['to_receive']
    datagram_link.to_receive(result)
    assert datagram_link.receiver_counter['to_receive'] == to_receive_count + 1
    assert datagram_link.receiver_counter['receive'] == receive_count + 1
    assert datagram_link.has_receive()
    result = datagram_link.receive()
    assert result.data == payload


def test_validated_invalid_data():
    """Exercise the ValidatedDatagramLink error handling."""
    print('Testing Validated Datagram Link with invalid data...')
    datagram_link = ValidatedDatagramLink()
    payload = [1234, 5678]
    header = ValidatedDatagramHeader(crc=0)

    # Send
    print('Expect an inconsistent payload error in logging:')
    datagram_link.send_data(payload, context={'header': header})
    assert datagram_link.sender_counter['send'] == 1
    assert datagram_link.sender_counter['to_send'] == 0
    assert datagram_link.sender_counter['error_invalid_payload'] == 1
    assert not datagram_link.has_to_send()
    test_validated_normal(datagram_link=datagram_link)

    # Receive
    print('Expect an inconsistent payload error in logging:')
    receive_count = datagram_link.receiver_counter['receive']
    to_receive_count = datagram_link.receiver_counter['to_receive']
    datagram_link.to_receive(payload)
    assert datagram_link.receiver_counter['to_receive'] == to_receive_count + 1
    assert datagram_link.receiver_counter['receive'] == receive_count
    assert datagram_link.receiver_counter['error'] == 1
    assert datagram_link.receiver_counter['error_parse'] == 1
    assert datagram_link.has_receive()
    result = datagram_link.receive()
    assert isinstance(result, LinkException)
    assert isinstance(result.context['exception'], TypeError)
    test_validated_normal(datagram_link=datagram_link)


def test_validated_invalid_crc():
    """Exercise the ValidatedDatagramLink error handling."""
    print('Testing Validated Datagram Link with invalid CRCs...')
    datagram_link = ValidatedDatagramLink()
    payload = b'\1\2\3\4\0'
    header = ValidatedDatagramHeader(crc=0, type=DATA_TYPES[('bytes', 'buffer')])

    # Send
    print('Expect an inconsistent crc warning in logging:')
    datagram_link.send_data(payload, context={'header': header})
    assert datagram_link.sender_counter['send'] == 1
    assert datagram_link.sender_counter['to_send'] == 1
    assert datagram_link.sender_counter['warning_inconsistent'] == 1
    assert datagram_link.has_to_send()
    result = datagram_link.to_send()
    test_validated_normal(datagram_link=datagram_link)

    # Receive
    print('Expect an inconsistent crc error in logging:')
    receive_count = datagram_link.receiver_counter['receive']
    to_receive_count = datagram_link.receiver_counter['to_receive']
    datagram_link.to_receive(result)
    assert datagram_link.receiver_counter['to_receive'] == to_receive_count + 1
    assert datagram_link.receiver_counter['receive'] == receive_count
    assert datagram_link.receiver_counter['error'] == 1
    assert datagram_link.receiver_counter['error_inconsistent'] == 1
    assert datagram_link.has_receive()
    result = datagram_link.receive()
    assert isinstance(result, LinkException)
    assert result.context['specified_crc'] == 0
    assert result.context['computed_crc'] == 0xd2aa86d0
    test_validated_normal(datagram_link=datagram_link)


# Stack


def test_stack():
    """Exercise the DatagramLink + ValidatedDatagramLink stack integration."""
    print('Testing Validated Datagram Link stacked on Datagram Link...')
    payload = b'\1\2\3\4\0'
    header = ValidatedDatagramHeader(crc=0xd2aa86d0)
    datagram_buffer = b'\x0a\x22\xd2\xaa\x86\xd0\x10\1\2\3\4\0'
    pipeline = AutomaticPipeline(DatagramLink(), ValidatedDatagramLink())

    # Send
    pipeline.top.send(payload)
    assert pipeline.bottom.has_to_send()
    result = pipeline.bottom.to_send()
    assert result.data == datagram_buffer

    # Receive
    pipeline.bottom.to_receive(datagram_buffer)
    assert pipeline.top.has_receive()
    result = pipeline.top.receive()
    assert result.data == payload
    assert result.context['header'] == header
