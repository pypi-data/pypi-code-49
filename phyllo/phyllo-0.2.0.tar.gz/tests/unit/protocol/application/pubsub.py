"""Test the protocol.application.pubsub module."""

# Builtins

import struct

# Packages

import msgpack

from phylline.links.events import LinkException
from phylline.pipelines import AutomaticPipeline

from phyllo.protocol.application.pubsub import DocumentLink, MessageLink
from phyllo.protocol.communication import DATA_TYPES, SCHEMAS, SERIALIZATION_FORMATS


def test_normal(message_link=MessageLink()):
    """Exercise the MessageLink functionality."""
    topic = 'test'.encode('utf-8')
    payload = b'\1\2\3\4\0'
    message_buffer = b'\x10\4test\1\2\3\4\0'

    # Send
    send_count = message_link.sender_counter['send']
    to_send_count = message_link.sender_counter['to_send']
    message_link.send((topic, payload))
    assert message_link.sender_counter['send'] == send_count + 1
    assert message_link.sender_counter['to_send'] == to_send_count + 1
    assert message_link.has_to_send()
    result = message_link.to_send()
    assert result.data == message_buffer

    # Receive
    receive_count = message_link.receiver_counter['receive']
    to_receive_count = message_link.receiver_counter['to_receive']
    message_link.to_receive(result)
    assert message_link.receiver_counter['to_receive'] == to_receive_count + 1
    assert message_link.receiver_counter['receive'] == receive_count + 1
    assert message_link.has_receive()
    result = message_link.receive()
    assert result.data == (topic, payload)


def test_invalid_payload():
    """Exercise the MessageLink error handling."""
    topic = 'test'.encode('utf-8')
    message_link = MessageLink()

    # Send
    print('Expect an invalid data error in logging:')
    send_count = message_link.sender_counter['send']
    to_send_count = message_link.sender_counter['to_send']
    invalid_payload_count = message_link.sender_counter['error_invalid_payload']
    message_link.send(object())
    assert message_link.sender_counter['send'] == send_count + 1
    assert message_link.sender_counter['to_send'] == to_send_count
    assert message_link.sender_counter['error_invalid_payload'] == invalid_payload_count + 1
    assert not message_link.has_to_send()
    test_normal(message_link=message_link)

    # Send
    print('Expect another invalid data error in logging:')
    send_count = message_link.sender_counter['send']
    to_send_count = message_link.sender_counter['to_send']
    invalid_payload_count = message_link.sender_counter['error_invalid_payload']
    message_link.send((topic, object()))
    assert message_link.sender_counter['send'] == send_count + 1
    assert message_link.sender_counter['to_send'] == to_send_count
    assert message_link.sender_counter['error_invalid_payload'] == invalid_payload_count + 1
    assert not message_link.has_to_send()
    test_normal(message_link=message_link)

    # Send
    print('Expect another invalid data error in logging:')
    send_count = message_link.sender_counter['send']
    to_send_count = message_link.sender_counter['to_send']
    invalid_payload_count = message_link.sender_counter['error_invalid_payload']
    message_link.send(topic)
    assert message_link.sender_counter['send'] == send_count + 1
    assert message_link.sender_counter['to_send'] == to_send_count
    assert message_link.sender_counter['error_invalid_payload'] == invalid_payload_count + 1
    assert not message_link.has_to_send()
    test_normal(message_link=message_link)

    # Send
    print('Expect another invalid data error in logging:')
    send_count = message_link.sender_counter['send']
    to_send_count = message_link.sender_counter['to_send']
    invalid_payload_count = message_link.sender_counter['error_invalid_payload']
    message_link.send((topic, 'foo', 'bar'))
    assert message_link.sender_counter['send'] == send_count + 1
    assert message_link.sender_counter['to_send'] == to_send_count
    assert message_link.sender_counter['error_invalid_payload'] == invalid_payload_count + 1
    assert not message_link.has_to_send()
    test_normal(message_link=message_link)

    # Send
    print('Expect a topic length error in logging:')
    send_count = message_link.sender_counter['send']
    to_send_count = message_link.sender_counter['to_send']
    invalid_payload_count = message_link.sender_counter['error_invalid_payload']
    message_link.send((b'abcdefghijkmnlop', b'foo'))
    assert message_link.sender_counter['send'] == send_count + 1
    assert message_link.sender_counter['to_send'] == to_send_count
    assert message_link.sender_counter['error_invalid_payload'] == invalid_payload_count + 1
    assert not message_link.has_to_send()
    test_normal(message_link=message_link)

    # Receive
    print('Expect another invalid data error in logging:')
    receive_count = message_link.receiver_counter['receive']
    to_receive_count = message_link.receiver_counter['to_receive']
    message_link.to_receive(b'\1')
    assert message_link.receiver_counter['to_receive'] == to_receive_count + 1
    assert message_link.receiver_counter['receive'] == receive_count
    assert message_link.receiver_counter['error'] == 1
    assert message_link.receiver_counter['error_parse'] == 1
    assert message_link.has_receive()
    result = message_link.receive()
    assert isinstance(result, LinkException)
    assert isinstance(result.context['exception'], struct.error)
    test_normal(message_link=message_link)


def test_document_normal(document_link=DocumentLink()):
    """Exercise the DocumentLink functionality."""
    topic = 'test'.encode('utf-8')
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
    document_link.send((topic, document))
    assert document_link.sender_counter['send'] == send_count + 1
    assert document_link.sender_counter['to_send'] == to_send_count + 1
    assert document_link.has_to_send()
    result = document_link.to_send()
    assert result.data == (topic, serialized_document)

    # Receive
    receive_count = document_link.receiver_counter['receive']
    to_receive_count = document_link.receiver_counter['to_receive']
    document_link.to_receive(result)
    assert document_link.receiver_counter['to_receive'] == to_receive_count + 1
    assert document_link.receiver_counter['receive'] == receive_count + 1
    assert document_link.has_receive()
    result = document_link.receive()
    assert result.data == (topic, document)
    assert result.type == DATA_TYPES[('presentation', 'document')]
    assert result.format == SERIALIZATION_FORMATS[('binary', 'dynamic', 'msgpack')]
    assert result.schema == SCHEMAS[('generic', 'schemaless')]

    # Send
    send_count = document_link.sender_counter['send']
    to_send_count = document_link.sender_counter['to_send']
    document_link.send_data((topic, 42), schema=SCHEMAS[('generic', 'primitive', 'uint8')])
    assert document_link.sender_counter['send'] == send_count + 1
    assert document_link.sender_counter['to_send'] == to_send_count + 1
    assert document_link.has_to_send()
    result = document_link.to_send()
    assert result.data == (topic, bytes([
        SERIALIZATION_FORMATS[('binary', 'dynamic', 'msgpack')],
        SCHEMAS[('generic', 'primitive', 'uint8')],
        42
    ]))

    # Receive
    receive_count = document_link.receiver_counter['receive']
    to_receive_count = document_link.receiver_counter['to_receive']
    document_link.to_receive(result)
    assert document_link.receiver_counter['to_receive'] == to_receive_count + 1
    assert document_link.receiver_counter['receive'] == receive_count + 1
    assert document_link.has_receive()
    result = document_link.receive()
    assert result.data == (topic, 42)
    assert result.type == DATA_TYPES[('presentation', 'document')]
    assert result.format == SERIALIZATION_FORMATS[('binary', 'dynamic', 'msgpack')]
    assert result.schema == SCHEMAS[('generic', 'primitive', 'uint8')]


def test_document_invalid_payload(document_link=DocumentLink()):
    """Exercise the DocumentLink error handling."""
    topic = 'test'.encode('utf-8')
    bad_payload = b'\x11\x31\x60\1\2\3\4\0'

    # Receive
    print('Expect an invalid data error in logging:')
    to_receive = document_link.receiver_counter['to_receive']
    receive = document_link.receiver_counter['receive']
    error_parse = document_link.receiver_counter['error_parse']
    document_link.to_receive(b'foo')
    assert document_link.receiver_counter['to_receive'] == to_receive + 1
    assert document_link.receiver_counter['receive'] == receive
    assert document_link.receiver_counter['error'] == 1
    assert document_link.receiver_counter['error_parse'] == error_parse + 1
    assert document_link.has_receive()
    result = document_link.receive()
    assert isinstance(result, LinkException)
    assert isinstance(result.context['exception'], ValueError)
    test_document_normal(document_link=document_link)

    # Receive
    print('Expect a ExtraData error in logging:')
    to_receive = document_link.receiver_counter['to_receive']
    receive = document_link.receiver_counter['receive']
    error = document_link.receiver_counter['error']
    error_parse = document_link.receiver_counter['error_parse']
    document_link.to_receive((topic, bad_payload))
    assert document_link.receiver_counter['to_receive'] == to_receive + 1
    assert document_link.receiver_counter['receive'] == receive
    assert document_link.receiver_counter['error'] == error + 1
    assert document_link.receiver_counter['error_parse'] == error_parse + 1
    assert document_link.has_receive()
    result = document_link.receive()
    assert isinstance(result, LinkException)
    assert isinstance(result.context['exception'], msgpack.exceptions.ExtraData)
    test_document_normal(document_link=document_link)

    # Send
    print('Expect an invalid data error in logging:')
    send = document_link.sender_counter['send']
    to_send = document_link.sender_counter['to_send']
    document_link.send(b'foo')
    assert document_link.sender_counter['send'] == send + 1
    assert document_link.sender_counter['to_send'] == to_send
    assert document_link.sender_counter['error_invalid_payload'] == 1
    assert not document_link.has_to_send()
    test_document_normal(document_link=document_link)


def test_stack():
    """Exercise the MessageLink + DocumentLink stack integration."""
    print('Testing Pub-Sub Document Link stacked on Pub-Sub Message Link...')
    topic = 'test'.encode('utf-8')
    document = ((0, 1), True, {'foo': 'bar'}, None)
    message_buffer = bytes([
        # Message Header
        0x40,  # presentation/document
        0x04,  # topic length
        # Message Topic
        0x74, 0x65, 0x73, 0x74,
        # Document Header
        0x11,  # binary/dynamic/msgpack
        0x00,  # generic/schemaless
        # Body
        0x94,  # list start
        0x92, 0x00, 0x01,  # (0, 1)
        0xc3,  # True
        0x81, 0xa3, 0x66, 0x6f, 0x6f, 0xa3, 0x62, 0x61, 0x72,  # {'foo': 'bar'}
        0xc0  # None
    ])
    pipeline = AutomaticPipeline(MessageLink(), DocumentLink())

    # Send
    pipeline.top.send((topic, document))
    assert pipeline.bottom.has_to_send()
    result = pipeline.bottom.to_send()
    assert result.data == message_buffer

    # Receive
    pipeline.bottom.to_receive(message_buffer)
    assert pipeline.top.has_receive()
    result = pipeline.top.receive()
    assert result.data == (topic, document)
    assert result.type == DATA_TYPES[('presentation', 'document')]
    assert result.format == SERIALIZATION_FORMATS[('binary', 'dynamic', 'msgpack')]
    assert result.schema == SCHEMAS[('generic', 'schemaless')]
