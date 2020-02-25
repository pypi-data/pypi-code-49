"""Messages provide a way to exchange structured data over independent named topics."""

# Builtins

import struct

# Packages

from phylline.util.logging import hex_bytes

from phyllo.protocol.communication import DATA_TYPES
from phyllo.protocol.communication import DataUnit, DataUnitLink, StructuredHeader
from phyllo.protocol.presentation.documents import (
    DocumentLink as PresentationDocumentLink
)


# Message

class MessageHeader(StructuredHeader):
    """Message header.

    In order of increasing offset in the buffer representation:
    Type is the type of the payload.
    TopicLength is the length of the topic.
    """

    FORMAT = '> B B'
    PARSER = struct.Struct(FORMAT)
    SIZE = struct.calcsize(FORMAT)

    def __init__(self, type=DATA_TYPES[('bytes', 'buffer')], topic_length=0):
        """Initialize field values."""
        super().__init__(type=type)
        self.topic_length = topic_length

    # Implement CommunicationLinkHeader

    @property
    def fields(self):
        """Implement CommunicationLinkHeader.fields."""
        return (self.type, self.topic_length)

    def read(self, buffer):
        """Implement CommunicationLinkHeader.read."""
        (self.type, self.topic_length) = self.unpack(buffer)

    @property
    def topic_length_string(self):
        """Return a string representation of the topic_length field."""
        return 'TL{:3}'.format(
            self.topic_length if self.topic_length is not None else '   '
        )

    @property
    def field_strings(self):
        """Implement CommunicationLinkHeader.field_strings."""
        return (self.type_string, self.topic_length_string)

    @property
    def members_repr(self):
        """Implement CommunicationLinkHeader.members_repr."""
        return {
            'type': self.type_repr,
            'topic_length': self.topic_length
        }


class Message(DataUnit):
    """Message containing a pub-sub topic and a payload.

    The topic field specifies the name of the topic/channel used to exchange the
    payload.

    In order of increasing offset in the buffer representation:
    Header contains the header.
    Topic contains the variable-length topic.
    Payload contains the payload.
    """

    TYPE = DATA_TYPES[('application', 'pubsub')]

    HEADER = MessageHeader

    TOPIC_SIZE_LIMIT = 15

    def __init__(self, header=None, topic=b'', payload=b''):
        """Initialize with optional header and payload.

        Note: saves references, not copies, of header and payload!
        """
        self._topic = b''  # initialize topic for payload length checks
        super().__init__(header=header, payload=payload)
        self.topic = topic

    @property
    def topic(self):
        """Return the topic carried by the message."""
        return self._topic

    # Consistency between header and overall datagram

    def update(self):
        """Make header's length field consistent with payload."""
        if self.topic is None:
            self.header.topic_length = 0
            return
        self.header.topic_length = len(self.topic)

    @property
    def consistent(self):
        """Check consistency between header's topic length field and message topic."""
        return self.header.topic_length == len(self.topic)

    @topic.setter
    def topic(self, value):
        if len(value) > self.TOPIC_SIZE_LIMIT:
            raise ValueError(
                'Message topic too long: {} bytes given, {} bytes allowed'
                .format(len(value), self.TOPIC_SIZE_LIMIT)
            )
        self._topic = value

    # Override DataUnit

    def read_body(self, buffer):
        """Override DataUnit.read_body."""
        self.topic = buffer[:self.header.topic_length]
        self.payload = buffer[self.header.topic_length:]

    @property
    def body(self):
        """Override DataUnit.body."""
        return self._topic + self._payload

    @property
    def body_members_str(self):
        """Override DataUnit.body."""
        return [hex_bytes(self.topic, truncate=None), self.full_payload_string]

    @property
    def body_members_repr(self):
        """Override DataUnit.body."""
        return {
            'topic': self.topic,
            'payload': self.payload
        }


# MessageLink

class MessageLink(DataUnitLink):
    """The MessageLink handles wrapping/unwrapping of payloads with a topic.

    Interface:
    Above: sends and receives 2-tuples of a topic and a payload.
    Below: to_send and to_receive messages as a byte buffer with a topic and payload.
    """

    DATA_UNIT = Message
    RECEIVABLE_TYPES = {
        DATA_UNIT.TYPE,
        DATA_TYPES[('bytes', 'buffer')]
    }

    def __init__(self):
        """Initialize members."""
        super().__init__(logger_name=__name__, logger_indentation=3)

    # Override DataUnitLink

    def make_link_received_event(self, message, source_event, context):
        """Override DataUnitLink.make_link_received_event."""
        return self.make_link_data(
            (message.topic, message.payload), 'up', source_event, context=context,
            type=message.header.type
        )

    def make_link_send_data_unit(self, data_event):
        """Override DataUnitLink.make_link_send_data_unit."""
        (topic, payload) = data_event.data
        header = data_event.context.get('header')
        return self.DATA_UNIT(header=header, topic=topic, payload=payload)


class DocumentLink(PresentationDocumentLink):
    """The DocumentLink handles exchange of structured data over named-topic channels.

    By default, the DocumentLink uses MessagePack for data serialization and
    deserialization. The DocumentLink allows exchange of arbitrarily structured
    json-like data (numbers, strings, arrays/tuples, dicts, etc.)

    Interface:
    Above: sends and receives 2-tuples of topics and dicts, arrays, numbers, or strings
    Below: to_send and to_receive 2-tuples of topics and serialized bytestrings
    """

    # Override DataUnitLink

    def make_link_received_data_unit(self, data_event):
        """Override DataUnitLink.make_link_received_data_unit."""
        (topic, document_buffer) = data_event.data
        document = self.DATA_UNIT()
        document.read(document_buffer)
        return (topic, document)

    def make_link_received_event(self, topic_and_document, source_event, context):
        """Override presentation.DocumentLink.make_link_received_event."""
        (topic, document) = topic_and_document
        return self.make_link_data(
            (topic, document.payload), 'up', source_event, context=context,
            type=self.DATA_UNIT.TYPE, format=document.header.format,
            schema=document.header.schema
        )

    def is_control_data_unit(self, topic_and_document):
        """Override presentation.DocumentLink.is_control_data_unit."""
        (topic, document) = topic_and_document
        return super().is_control_data_unit(document)

    def make_link_send_data_unit(self, data_event):
        """Override DataUnitLink.make_link_send_data_unit."""
        (topic, payload) = data_event.data
        header = data_event.context.get('header')
        document = self.DATA_UNIT(header=header, payload=payload)
        return (topic, document)

    def update_send_data_unit_header(self, topic_and_document, data_event):
        """Override presentation.DocumentLink.update_send_data_unit_header."""
        (topic, document) = topic_and_document
        super().update_send_data_unit_header(document, data_event)

    def check_send_data_unit(self, topic_and_document):
        """Override DataUnitLink.check_send_data_unit."""
        (topic, document) = topic_and_document
        super().check_send_data_unit(document)

    def make_send_data_event_data(self, data_unit):
        """Override DataUnitLink.make_send_data_event_data."""
        (topic, document) = data_unit
        return (topic, document.buffer)
