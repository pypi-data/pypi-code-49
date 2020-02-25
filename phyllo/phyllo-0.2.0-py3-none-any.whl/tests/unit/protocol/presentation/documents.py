"""Test the protocol.presentation.documents module."""

# Builtins

# Packages

import msgpack

from phylline.links.events import LinkException

from phyllo.protocol.communication import DATA_TYPES, SCHEMAS, SERIALIZATION_FORMATS
from phyllo.protocol.presentation.documents import DocumentLink


def test_normal(document_link=DocumentLink()):
    """Exercise the DocumentLink functionality."""
    document = ((0, 1), True, {'foo': 'bar'}, None)
    serialized_document = bytes([
        # Header
        SERIALIZATION_FORMATS[('binary', 'dynamic', 'msgpack')],
        SCHEMAS[('generic', 'schemaless')],
        # Body
        0x94,  # list start
        0x92, 0x00, 0x01,  # (0, 1)
        0xc3,  # True
        0x81, 0xa3, 0x66, 0x6f, 0x6f, 0xa3, 0x62, 0x61, 0x72,  # {'foo': 'bar'}
        0xc0  # None
    ])

    # Send
    send_count = document_link.sender_counter['send']
    to_send_count = document_link.sender_counter['to_send']
    document_link.send(document)
    assert document_link.sender_counter['send'] == send_count + 1
    assert document_link.sender_counter['to_send'] == to_send_count + 1
    assert document_link.has_to_send()
    result = document_link.to_send()
    assert result.data == serialized_document

    # Receive
    receive_count = document_link.receiver_counter['receive']
    to_receive_count = document_link.receiver_counter['to_receive']
    document_link.to_receive(result)
    assert document_link.receiver_counter['to_receive'] == to_receive_count + 1
    assert document_link.receiver_counter['receive'] == receive_count + 1
    assert document_link.has_receive()
    result = document_link.receive()
    assert result.data == document
    assert result.type == DATA_TYPES[('presentation', 'document')]
    assert result.format == SERIALIZATION_FORMATS[('binary', 'dynamic', 'msgpack')]
    assert result.schema == SCHEMAS[('generic', 'schemaless')]

    # Send
    send_count = document_link.sender_counter['send']
    to_send_count = document_link.sender_counter['to_send']
    document_link.send_data(42, schema=SCHEMAS[('generic', 'primitive', 'uint8')])
    assert document_link.sender_counter['send'] == send_count + 1
    assert document_link.sender_counter['to_send'] == to_send_count + 1
    assert document_link.has_to_send()
    result = document_link.to_send()
    assert result.data == bytes([
        SERIALIZATION_FORMATS[('binary', 'dynamic', 'msgpack')],
        SCHEMAS[('generic', 'primitive', 'uint8')],
        42
    ])

    # Receive
    receive_count = document_link.receiver_counter['receive']
    to_receive_count = document_link.receiver_counter['to_receive']
    document_link.to_receive(result)
    assert document_link.receiver_counter['to_receive'] == to_receive_count + 1
    assert document_link.receiver_counter['receive'] == receive_count + 1
    assert document_link.has_receive()
    result = document_link.receive()
    assert result.data == 42
    assert result.type == DATA_TYPES[('presentation', 'document')]
    assert result.format == SERIALIZATION_FORMATS[('binary', 'dynamic', 'msgpack')]
    assert result.schema == SCHEMAS[('generic', 'primitive', 'uint8')]


def test_deserialize_error():
    """Exercise the DocumentLink decoding error handling."""
    bad_document = b'\x11\x31\x60\1\2\3\4\0'
    document_link = DocumentLink()

    # Receive
    print('Expect a NotImplemented error in logging:')
    document_link.to_receive(b'\x00' + bad_document[1:])
    assert document_link.receiver_counter['to_receive'] == 1
    assert document_link.receiver_counter['receive'] == 0
    assert document_link.receiver_counter['error'] == 1
    assert document_link.receiver_counter['error_parse'] == 1
    assert document_link.has_receive()
    result = document_link.receive()
    assert isinstance(result, LinkException)
    assert isinstance(result.context['exception'], NotImplementedError)
    test_normal(document_link=document_link)

    # Receive
    print('Expect a ExtraData error in logging:')
    to_receive = document_link.receiver_counter['to_receive']
    receive = document_link.receiver_counter['receive']
    error = document_link.receiver_counter['error']
    error_parse = document_link.receiver_counter['error_parse']
    document_link.to_receive(bad_document)
    assert document_link.receiver_counter['to_receive'] == to_receive + 1
    assert document_link.receiver_counter['receive'] == receive
    assert document_link.receiver_counter['error'] == error + 1
    assert document_link.receiver_counter['error_parse'] == error_parse + 1
    assert document_link.has_receive()
    result = document_link.receive()
    assert isinstance(result, LinkException)
    assert isinstance(result.context['exception'], msgpack.exceptions.ExtraData)
    test_normal(document_link=document_link)


def test_serialize_error():
    """Exercise the DocumentLink decoding error handling."""
    bad_document = object()
    document_link = DocumentLink()

    # Send
    print('Expect an invalid data error in logging:')
    document_link.send(bad_document)
    assert document_link.sender_counter['send'] == 1
    assert document_link.sender_counter['to_send'] == 0
    assert document_link.sender_counter['error_invalid_payload'] == 1
    assert not document_link.has_to_send()
    test_normal(document_link=document_link)

    # Send
    print('Expect an invalid data error in logging:')
    send_count = document_link.sender_counter['send']
    to_send_count = document_link.sender_counter['to_send']
    document_link.send(object())
    assert document_link.sender_counter['send'] == send_count + 1
    assert document_link.sender_counter['to_send'] == to_send_count
    assert document_link.sender_counter['error_invalid_payload'] == 2
    assert not document_link.has_to_send()
    test_normal(document_link=document_link)
