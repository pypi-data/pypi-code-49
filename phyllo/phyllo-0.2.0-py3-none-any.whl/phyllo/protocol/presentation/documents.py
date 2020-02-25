"""Documents provide a way to exchange structured data."""

# Builtins

import struct

# Packages

import msgpack

from phyllo.protocol.communication import DATA_TYPES, SCHEMAS, SERIALIZATION_FORMATS
from phyllo.protocol.communication import DataUnit, DataUnitLink, StructuredHeader


# Document

class DocumentHeader(StructuredHeader):
    """Document header.

    In order of increasing offset in the buffer representation:
    Schema is the payload schema code.
    """

    FORMAT = '> B B'
    PARSER = struct.Struct(FORMAT)
    SIZE = struct.calcsize(FORMAT)

    def __init__(
        self, format=SERIALIZATION_FORMATS[('binary', 'dynamic', 'unknown')],
        schema=SCHEMAS[('generic', 'schemaless')]
    ):
        """Initialize field values."""
        super().__init__(
            type=DATA_TYPES[('presentation', 'document')], format=format, schema=schema
        )

    # Implement CommunicationLinkHeader

    @property
    def fields(self):
        """Implement CommunicationLinkHeader.fields."""
        return (self.format, self.schema)

    def read(self, buffer):
        """Implement CommunicationLinkHeader.read."""
        (self.format, self.schema) = self.unpack(buffer)

    @property
    def field_strings(self):
        """Implement CommunicationLinkHeader.field_strings."""
        return (self.format_string, self.schema_string)

    @property
    def members_repr(self):
        """Implement CommunicationLinkHeader.members_repr."""
        return {
            'format': self.format_repr,
            'schema': self.schema_repr
        }


class Document(DataUnit):
    """Document containing a header and a payload (which is serialized as a body).

    The schema field specifies the content schema of the body.

    Note: if the payload member is modified without using the setter (e.g. if
    the payload is modified in-place), the update() method needs to be called
    to update the body.

    In order of increasing offset in the buffer representation:
    Header contains the header.
    Body contains the body.
    """

    TYPE = DATA_TYPES[('presentation', 'document')]

    HEADER = DocumentHeader

    def __init__(self, header=None, payload=None):
        """Initialize with optional header and payload.

        Note: saves references, not copies, of header and payload!
        """
        super().__init__(header=header, payload=payload)

    # Override DataUnit

    @property
    def payload(self):
        """Override DataUnit.payload."""
        return super().payload

    @payload.setter
    def payload(self, value):
        """Override DataUnit.payload.setter."""
        self._payload = value

    @property
    def body(self):
        """Override DataUnit.body."""
        serialized = self.serialize(self.payload, self.header.format, self.header.schema)
        return serialized

    def read_body(self, buffer):
        """Override DataUnit.read_body."""
        self.payload = None
        self.payload = self.deserialize(buffer, self.header.format, self.header.schema)

    @property
    def full_payload_string(self):
        """Override DataUnit.full_payload_string."""
        return repr(self.body)

    # Document interface

    def deserialize(self, body, format, schema):
        """Deserialize the body with the given schema code.

        Override this to implement functionality.
        """
        if format == SERIALIZATION_FORMATS[('binary', 'dynamic', 'msgpack')]:
            return msgpack.unpackb(body, use_list=False, raw=False, strict_map_key=False)
        else:
            raise NotImplementedError(
                'Unimplemented deserializer for format {}!'
                .format(self.header.format_string)
            )

    def serialize(self, payload, format, schema):
        """Serialize the payload with the given schema code.

        Override this to implement functionality.
        """
        if format == SERIALIZATION_FORMATS[('binary', 'dynamic', 'msgpack')]:
            return msgpack.packb(payload, use_bin_type=True)
        else:
            raise NotImplementedError(
                'Unimplemented serializer for format {}!'
                .format(self.header.format_string)
            )


# DocumentLink


class DocumentLink(DataUnitLink):
    """The DocumentLink handles serialization/deserialization of structured data.

    By default, the DocumentLink uses MessagePack for data serialization and
    deserialization. The DocumentLink allows exchange of arbitrarily structured
    json-like data (numbers, strings, arrays/tuples, dicts, etc.)

    Interface:
    Above: sends and receives dicts, arrays, numbers, or strings
    Below: to_send and to_receive serialized bytestrings
    """

    DATA_UNIT = Document
    RECEIVABLE_TYPES = {
        DATA_UNIT.TYPE,
        DATA_TYPES[('bytes', 'buffer')]
    }

    def __init__(
        self, default_format=SERIALIZATION_FORMATS[('binary', 'dynamic', 'msgpack')],
        default_schema=SCHEMAS[('generic', 'schemaless')], **kwargs
    ):
        """Initialize members."""
        super().__init__(logger_name=__name__, logger_indentation=3, **kwargs)
        self.default_format = default_format
        self.default_schema = default_schema

    # Override CommunicationLink

    def send_data(
        self, data, type=DATA_UNIT.TYPE, format=None, schema=None, context=None
    ):
        """Override CommunicationLink.send_data."""
        if format is None:
            format = self.default_format
        if schema is None:
            schema = self.default_schema
        super().send_data(
            data, type=type, format=format, schema=schema, context=context
        )

    # Override DataUnitLink

    def make_link_received_event(self, document, source_event, context):
        """Override DataUnitLink.make_link_received_event."""
        return self.make_link_data(
            document.payload, 'up', source_event, context=context,
            type=self.DATA_UNIT.TYPE, format=document.header.format,
            schema=document.header.schema
        )

    def is_control_data_unit(self, document):
        """Override DataUnitLink.is_control_data_unit."""
        return document.header.schema < SCHEMAS[('generic', 'schemaless')]

    def make_link_send_data_event(self, event):
        """Override DataUnitLink.make_link_send_data_event."""
        link_data = self.get_link_data(
            event, 'down', format=self.default_format, schema=self.default_schema,
            type=self.DATA_UNIT.TYPE
        )
        if link_data is None:
            return
        if link_data.format is None:
            link_data.format = self.default_format
        if link_data.schema is None:
            link_data.schema = self.default_schema
        return link_data

    def update_send_data_unit_header(self, document, data_event):
        """Override DataUnitLink.update_send_data_unit_header."""
        document.header.format = data_event.format
        document.header.schema = data_event.schema
        document.update()
