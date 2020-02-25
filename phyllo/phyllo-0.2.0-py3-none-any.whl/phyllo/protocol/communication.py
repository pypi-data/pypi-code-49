"""Shared utilities for writing communication links.

Communication links implement passing of data between two different endpoints.
"""

# Builtins

import logging
import struct
from collections import Counter, OrderedDict

# Packages

from bidict import bidict

from phylline.links.events import (
    DataEventLink, EventLink, LinkData, LinkEvent, LinkException
)
from phylline.pipelines import AutomaticPipeline, ManualPipeline, Pipeline
from phylline.pipes import AutomaticPipe, ManualPipe, Pipe
from phylline.processors import event_processor, receive
from phylline.util.logging import hex_bytes

from phyllo.util.logging import IndentedLogger


# All message-oriented layers have a 1 byte type field to allow for
# multiplexing/demultiplexing different message payload types:
DATA_TYPES = bidict({  # allowed values: 0x00 - 0x7f
    # Layer
    ('layer', 'control'):      0x00,
    ('layer', 'version'):      0x01,
    ('layer', 'capabilities'): 0x02,
    ('layer', 'error'):        0x03,
    ('layer', 'warn'):         0x04,
    ('layer', 'info'):         0x05,
    ('layer', 'debug'):        0x06,
    ('layer', 'trace'):        0x07,
    ('layer', 'metrics'):      0x08,

    # Bytes
    ('bytes', 'buffer'): 0x10,
    ('bytes', 'stream'): 0x11,
    ('bytes', 'chunk'):  0x12,

    # Transport
    ('transport', 'frame'):              0x20,
    ('transport', 'datagram'):           0x21,
    ('transport', 'validated_datagram'): 0x22,
    ('transport', 'reliable_buffer'):    0x23,
    ('transport', 'ported_buffer'):      0x24,

    # Presentation
    ('presentation', 'document'): 0x40,

    # Application Framework
    ('application', 'pubsub'): 0x60,
    ('application', 'rpc'):    0x61,
    ('application', 'rest'):   0x62,

})

# All documents have a 1 byte format field to allow for
# specification of payload serialization format:
SERIALIZATION_FORMATS = bidict({  # allowed values: 0x00 - 0x7f
    # Layer
    ('layer', 'control'):      0x00,
    ('layer', 'version'):      0x01,
    ('layer', 'capabilities'): 0x02,
    ('layer', 'error'):        0x03,
    ('layer', 'warn'):         0x04,
    ('layer', 'info'):         0x05,
    ('layer', 'debug'):        0x06,
    ('layer', 'trace'):        0x07,
    ('layer', 'metrics'):      0x08,

    # Binary
    # Dynamic
    ('binary', 'dynamic', 'unknown'): 0x10,
    ('binary', 'dynamic', 'msgpack'): 0x11,
    ('binary', 'dynamic', 'cbor'):    0x12,
    ('binary', 'dynamic', 'bson'):    0x13,
    ('binary', 'dynamic', 'avro'):    0x14,
    # Static
    ('binary', 'dynamic', 'protobuf'):    0x30,
    ('binary', 'dynamic', 'thrift'):      0x31,
    ('binary', 'dynamic', 'capnproto'):   0x32,
    ('binary', 'dynamic', 'flatbuffers'): 0x33,

    # Text
    ('text', 'json'): 0x50,
    ('text', 'csv'):  0x51,
})

# All documents have a 1 byte schema field to allow for
# specification of payload serialization schema:
SCHEMAS = bidict({  # allowed values: 0x00 - 0x7f

    # Generic
    ('generic', 'schemaless'): 0x00,
    # Generic/Primitive
    ('generic', 'primitive', 'none'):    0x01,
    ('generic', 'primitive', 'boolean'): 0x02,
    ('generic', 'primitive', 'uint'):    0x03,
    ('generic', 'primitive', 'uint8'):   0x04,
    ('generic', 'primitive', 'uint16'):  0x05,
    ('generic', 'primitive', 'uint32'):  0x06,
    ('generic', 'primitive', 'uint64'):  0x07,
    ('generic', 'primitive', 'int'):     0x08,
    ('generic', 'primitive', 'int8'):    0x09,
    ('generic', 'primitive', 'int16'):   0x0a,
    ('generic', 'primitive', 'int32'):   0x0b,
    ('generic', 'primitive', 'int64'):   0x0c,
    ('generic', 'primitive', 'float32'): 0x0d,
    ('generic', 'primitive', 'float64'): 0x0e,
    # Generic/Sequence
    ('generic', 'sequence', 'string'):   0x10,
    ('generic', 'sequence', 'string8'):  0x11,
    ('generic', 'sequence', 'string16'): 0x12,
    ('generic', 'sequence', 'string32'): 0x13,
    ('generic', 'sequence', 'string64'): 0x14,
    ('generic', 'sequence', 'binary'):   0x15,
    ('generic', 'sequence', 'binary8'):  0x16,
    ('generic', 'sequence', 'binary16'): 0x17,
    ('generic', 'sequence', 'binary32'): 0x18,
    ('generic', 'sequence', 'binary64'): 0x19,

    # Framework

    # Application
    # Application/Generic
    # Application/Generic/Tuples
    # Application/Generic/Arrays
    # Application/Generic/Maps
    # Application/Debug
    # Application/System
    # Application/Services
    # Application/Computation
    # Application/Devices
    # Application/Miscellaneous
})


class Typed(object):
    """Object with type/format/schema fields."""

    def __init__(
        self, *args, type=DATA_TYPES[('bytes', 'buffer')],
        format=None, schema=None, **kwargs
    ):
        """Initialize members."""
        self.type = type
        self.format = format
        self.schema = schema
        super().__init__(*args, **kwargs)

    # Type

    @property
    def type_string(self):
        """Return a string representation of the type."""
        if self.type in DATA_TYPES.inverse:
            return 'T:{}'.format('/'.join(DATA_TYPES.inverse[self.type]))
        return 'T0x{:02x}'.format(self.type if self.type is not None else '  ')

    @property
    def type_repr(self):
        """Return a representation of the type value."""
        if self.type is None:
            return 'None'
        return '0x{:02x}'.format(self.type)

    # Format

    @property
    def format_string(self):
        """Return a string representation of the format."""
        if self.format in SERIALIZATION_FORMATS.inverse:
            return 'F:{}'.format('/'.join(SERIALIZATION_FORMATS.inverse[self.format]))
        return 'F0x{:02x}'.format(self.format if self.format is not None else '  ')

    @property
    def format_repr(self):
        """Return a representation of the format value."""
        if self.schema is None:
            return 'None'
        return '0x{:02x}'.format(self.format)

    # Schema

    @property
    def schema_string(self):
        """Return a string representation of the schema."""
        if self.schema in SCHEMAS.inverse:
            return 'S:{}'.format('/'.join(SCHEMAS.inverse[self.schema]))
        return 'S0x{:02x}'.format(self.schema if self.schema is not None else '  ')

    @property
    def schema_repr(self):
        """Return a representation of the schema value."""
        if self.schema is None:
            return 'None'
        return '0x{:02x}'.format(self.schema)


class StructuredSection(object):
    """Interface for structured sections of data units in communication links."""

    FORMAT = ''  # override this to specify a header struct format
    PARSER = struct.Struct(FORMAT)  # override this to make a parser with the overridden format
    SIZE = struct.calcsize(FORMAT)  # override this to compute the size with the overridden format

    def unpack(self, buffer):
        """Unpack header fields from a buffer."""
        return self.PARSER.unpack(buffer[:self.SIZE])

    def pack(self, *args):
        """Pack values into a buffer."""
        return self.PARSER.pack(*args)

    @property
    def buffer(self):
        """Return a bytes buffer representation of the header."""
        return self.pack(*self.fields)

    def __eq__(self, other):
        """Check whether two heades have the same field values."""
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.fields == other.fields

    # String representations

    def __str__(self):
        """Return a string representation of the header's field values."""
        return ' | '.join(self.field_strings)

    def __repr__(self):
        """Return a string representation of everything in the header."""
        return '{}({})'.format(self.__class__.__qualname__, ', '.join(
            '{}={}'.format(key, value) for (key, value) in self.members_repr.items()
        ))

    # CommunicationLinkHeader interface

    @property
    def fields(self):
        """Return a tuple of the field members of the header.

        Override this to return the fields which should be packed and unpacked.
        """
        return ()

    def read(self, buffer):
        """Parse header contents from a buffer.

        Override this to set the fields from the buffer.
        """
        pass

    @property
    def field_strings(self):
        """Return a tuple of the string representations of the header's field values."""
        return ()

    @property
    def members_repr(self):
        """Return a dict of the names and string represenations of the header's members."""
        return {}


class StructuredHeader(StructuredSection, Typed):
    """Interface for structured headers of data units."""

    pass


class DataUnit(object):
    """Interface for data units in communication links."""

    TYPE = DATA_TYPES[('bytes', 'buffer')]  # Override this to define a data type

    HEADER = None  # Override this to define a header type
    FOOTER = None  # Override this to define a footer type

    def __init__(self, header=None, payload=b'', footer=None, size_limit=None):
        """Initialize with payload.

        Note: saves references, not copies, of header and payload!
        """
        # Set header
        if header is None and self.HEADER is not None:
            header = self.HEADER()
        if (
            self.HEADER is not None and not isinstance(header, self.HEADER)
            or self.HEADER is None and header is not None
        ):
            raise TypeError(
                'Expected header of type {} but received header of type {}: {}'
                .format(self.HEADER, type(header), header)
            )
        self.header = header

        # Set footer
        if footer is None and self.FOOTER is not None:
            footer = self.FOOTER()
        if (
            self.FOOTER is not None and not isinstance(footer, self.FOOTER)
            or self.FOOTER is None and footer is not None
        ):
            raise TypeError(
                'Expected footer of type {} but received footer of type {}: {}'
                .format(self.FOOTER, type(footer), footer)
            )
        self.footer = footer

        # Set payload
        # This comes last because the length check depends on header and footer.
        self.size_limit = size_limit
        self._payload = None
        self.payload = payload

    @property
    def header_size(self):
        """Return the total overhead size of the header."""
        return self.header.SIZE if self.header is not None else 0

    @property
    def footer_size(self):
        """Return the total overhead size of the footer."""
        return self.footer.SIZE if self.footer is not None else 0

    @property
    def overhead_size(self):
        """Return the total overhead size of the header and footer."""
        return self.header_size + self.footer_size

    @property
    def payload(self):
        """Return the payload carried by the data unit."""
        return self._payload

    @payload.setter
    def payload(self, value):
        if (
            self.payload_size_limit is not None
            and len(value) > self.payload_size_limit
        ):
            raise ValueError(
                'Payload too long: {} bytes given, {} bytes allowed'
                .format(len(value), self.payload_size_limit)
            )
        b'' + value  # ensure that the payload value is compatible with bytes
        self._payload = value

    @property
    def payload_size_limit(self):
        """Return the size limit of the payload."""
        if self.size_limit is None:
            return None

        return self.size_limit - self.overhead_size

    @property
    def body(self):
        """Return a bytes buffer representation of the data unit's body."""
        return self._payload

    @property
    def buffer(self):
        """Return a bytes buffer representation of the data unit."""
        return (
            (self.header.buffer if self.header is not None else b'')
            + self.body
            + (self.footer.buffer if self.footer is not None else b'')
        )

    def read_body(self, buffer):
        """Parse the body from a buffer."""
        self.payload = buffer

    def read(self, buffer):
        """Parse data unit contents from a buffer."""
        if self.header is not None:
            self.header.read(buffer[:self.header_size])
        self.read_body(buffer[self.header_size:len(buffer) - self.footer_size])
        if self.footer is not None:
            self.footer.read(buffer[len(buffer) - self.footer_size:len(buffer)])

    # String representations

    @property
    def full_payload_string(self):
        """Return a full string representation of the payload."""
        return hex_bytes(self.payload, truncate=None)

    @property
    def body_members_str(self):
        """Return a list of the full representations of the data unit's body members."""
        return [self.full_payload_string]

    def __str__(self):
        """Return a full representation of the data unit."""
        elements = self.body_members_str
        if self.header is not None:
            elements.insert(0, str(self.header))
        if self.footer is not None:
            elements.append(str(self.footer))
        return ' | '.join(elements)

    def __repr__(self):
        """Return a string representation of everything in the header."""
        return '{}({})'.format(self.__class__.__qualname__, ', '.join(
            '{}={}'.format(key, value) for (key, value) in self.members_repr.items()
        ))

    # DataUnit interface

    @property
    def consistent(self):
        """Check whether the data unit is internally consistent."""
        return True

    def update(self):
        """Update the data unit for internal consistency."""
        pass

    @property
    def body_members_repr(self):
        """Return a dict of the names and string representations of the data unit's body."""
        return {
            'payload': self.payload
        }

    @property
    def members_repr(self):
        """Return a dict of the names and string representations of the data unit's members."""
        return {
            'header': self.header,
            **self.body_members_repr,
            'footer': self.footer,
            'size_limit': self.size_limit
        }


class CommunicationLinkData(Typed, LinkData):
    """Event indicating a unit of data which was passed up or down a CommunicationLink layer."""

    def __init__(
        self, data, type=DATA_TYPES[('bytes', 'buffer')], format=None, schema=None,
        direction='up', context=None, instance=None, previous=None
    ):
        """Initialize members."""
        super().__init__(
            data, type=type, format=format, schema=schema, direction=direction,
            context=context, instance=instance, previous=previous
        )

    # Override LinkData

    def __str__(self):
        """Override LinkData.__str__."""
        return '{} passed {} in ({}){} of type {}{}{}: {}{}'.format(
            self.__class__.__qualname__,
            self.direction, self.link,
            ' with context({})'.format(self.context) if self.context else '',
            self.type_string,
            ' and format {}'.format(self.format_string) if self.format is not None else '',
            ' and schema {}'.format(self.schema_string) if self.schema is not None else '',
            hex_bytes(self.data) if isinstance(self.data, (bytes, bytearray)) else self.data,
            ', due to ({})'.format(self.previous) if self.previous is not None else ''
        )

    def __repr__(self):
        """Override LinkData.__repr__."""
        return (
            '{}({}, type={}, format={}, schema={}, '
            'direction={}, context={}, instance={}, previous={})'
            .format(
                self.__class__.__qualname__, self.data,
                self.type_repr, self.format_repr, self.schema_repr,
                self.direction, self.context, self.link, self.previous
            )
        )


class TypedLink(DataEventLink):
    """Typed event link."""

    # Override DataEventLink

    def send_data(
        self, data, type=DATA_TYPES[('bytes', 'buffer')], format=None, schema=None,
        context=None
    ):
        """Override DataEventLink.send_data."""
        self._sender.send(CommunicationLinkData(
            data, type=type, format=format, schema=schema,
            direction='down', context=context
        ))

    def get_link_data(
        self, event, direction, type=DATA_TYPES[('bytes', 'buffer')],
        format=None, schema=None, context=None
    ):
        """Override DataEventLink.get_link_data.

        The type in the returned CommunicationLinkData object describes the type of
        the object itself, not of the payload.
        """
        if isinstance(event, CommunicationLinkData):
            return CommunicationLinkData(
                event.data, type=event.type, format=event.format, schema=event.schema,
                direction=direction,
                context=event.context.copy() if context is None else context,
                instance=self, previous=event
            )
        elif isinstance(event, LinkData):
            return CommunicationLinkData(
                event.data, type=type, format=format, schema=schema, direction=direction,
                context=event.context.copy() if context is None else context,
                instance=self, previous=event
            )
        elif not isinstance(event, LinkEvent):
            return CommunicationLinkData(
                event, type=type, format=format, schema=schema, direction=direction,
                context=context, instance=self
            )

    def make_link_data(
        self, data, direction, previous, type=DATA_TYPES[('bytes', 'buffer')],
        format=None, schema=None, context=None
    ):
        """Return a LinkData event from the provided data."""
        return CommunicationLinkData(
            data, type=type, format=format, schema=schema, direction=direction,
            context=context, instance=self, previous=previous
        )


class CommunicationLink(TypedLink, EventLink):
    """Utility class for writing communicatation protocol links."""

    def __init__(self, logger_name=__name__, logger_indentation=0, **kwargs):
        """Initialize members."""
        super().__init__(**kwargs)
        self.logger = IndentedLogger(logging.getLogger(logger_name), {
            'class': self.__class__.__qualname__,
            'indentation': logger_indentation
        })
        self.receiver_counter = Counter()
        self.sender_counter = Counter()

    @property
    def counters(self):
        """Return associated counters."""
        return {
            'receiver': self.receiver_counter,
            'sender': self.sender_counter
        }

    def check_receive_type(self, data_event, receivable_types):
        """Check whether an event contains a receivable type."""
        type = data_event.type
        if type not in receivable_types:
            self.logger.error(
                'Cannot receive data of type {}: {}'
                .format(data_event.type_string, data_event)
            )
            self.receiver_counter['unreceivable_type'] += 1
            return self.make_link_exception(
                'Received unreceivable type', 'up', data_event.previous, context={
                    'type': type,
                    'receivable_types': receivable_types
                }
            )

    def check_receive_schema(self, data_event, receivable_schemas):
        """Check whether an event contains a document of a receivable schema."""
        result = self.check_receive_type(
            data_event, {DATA_TYPES[('presentation', 'document')]}
        )
        if result is not None:
            return result

        schema = data_event.schema
        if schema not in receivable_schemas:
            self.logger.error(
                'Cannot receive document of schema {}: {}'
                .format(data_event.schema_string, data_event)
            )
            self.receiver_counter['unreceivable_schema'] += 1
            return self.make_link_exception(
                'Received unreceivable schema', 'up', data_event.previous, context={
                    'type': data_event.type,
                    'schema': schema,
                    'receivable_schemas': receivable_schemas
                }
            )

    # CommunicationLink interface

    def receiver_process(self, event):
        """Do any receiver processing of the event and generate any events to pass up.

        Override this method to implement functionality.
        Yield events from this method to pass them up.
        """
        yield event

    def sender_process(self, event):
        """Do any sender processing of the event and generate any events to pass up.

        Override this method to implement functionality.
        Yield events from this method to pass them down.
        """
        yield event

    # Override EventLink

    @event_processor
    def receiver_processor(self):
        """Event receiver processor."""
        while True:
            try:
                event = yield from receive()
                try:
                    self.receiver_counter['to_receive'] += 1
                    for event in self.receiver_process(event):
                        if isinstance(event, LinkException):
                            self.receiver_counter['error'] += 1
                        else:
                            self.receiver_counter['receive'] += 1
                        yield from self.after_receive(event)
                except Exception as e:
                    self.logger.exception(
                        'Uncaught receiver exception due to: {}'.format(event)
                    )
                    self.receiver_counter['error_uncaught'] += 1
            except Exception as e:
                self.logger.exception('Uncaught receiver exception!')
                self.receiver_counter['error_uncaught'] += 1

    @event_processor
    def sender_processor(self):
        """Event sender processor."""
        while True:
            try:
                event = yield from receive()
                try:
                    self.sender_counter['send'] += 1
                    for event in self.sender_process(event):
                        if isinstance(event, LinkException):
                            self.sender_counter['error'] += 1
                        else:
                            self.sender_counter['to_send'] += 1
                        yield from self.after_send(event)
                except Exception as e:
                    self.logger.exception(
                        'Uncaught sender exception due to: {}'.format(event)
                    )
                    self.receiver_counter['error_uncaught'] += 1
            except Exception as e:
                self.logger.exception('Uncaught sender exception!')
                self.sender_counter['error_uncaught'] += 1


class DataUnitLink(CommunicationLink):
    """Utility class for writing DataUnit-based communication protocol links.

    Default implementations merely transform received data and sending data.
    """

    DATA_UNIT = DataUnit  # Override this to specify a data unit class
    RECEIVABLE_TYPES = {  # Override this to specify receivable types
        DATA_UNIT.TYPE,
        DATA_TYPES[('bytes', 'buffer')]
    }

    # Receiving data units

    def make_link_received_data_unit(self, data_event):
        """Make a received data unit from a received data event."""
        buffer = data_event.data
        data_unit = self.DATA_UNIT()
        data_unit.read(buffer)
        return data_unit

    def parse_data_unit(self, event):
        """Attempt to parse a data unit from a to_receive event."""
        data_event = self.get_link_data(event, 'up')
        if data_event is None:  # the event is not data, e.g. a clock update event
            return None

        result = self.check_receive_type(data_event, self.RECEIVABLE_TYPES)
        if result is not None:  # i.e. result is an exception
            return result

        try:
            data_unit = self.make_link_received_data_unit(data_event)
        except Exception as e:
            self.logger.exception(
                'Cannot parse invalid data unit: {}'.format(data_event)
            )
            self.receiver_counter['error_parse'] += 1
            return self.make_link_exception(
                'Received unparseable', 'up', event, context={'exception': e}
            )

        return data_unit

    def is_exposable_data_unit(self, parse_result):
        """Check whether the parse result is a data unit to expose."""
        return not (
            parse_result is None
            or isinstance(parse_result, LinkException)
            or self.is_control_data_unit(parse_result)
        )

    def on_internal_data(self, parse_result, event):
        """Handle a parse result or event which is not exposable."""
        pass

    def is_control_data_unit(self, data_unit):
        """Check whether the data_unit is actually a control message."""
        return data_unit.header.type < DATA_TYPES[('bytes', 'buffer')]

    def make_link_received_event(self, data_unit, source_event, context):
        """Make a receive event from a data unit processed by receiver_process."""
        return self.make_link_data(
            data_unit.payload, 'up', source_event, context=context,
            type=data_unit.header.type
        )

    def control_data_unit_process(self, data_unit):
        """Handle any control data units.

        Override this to implement logic for handling control data units.
        """
        pass

    # Sending data units

    def make_link_send_data_event(self, event):
        """Make a send data event from a data unit or event to send."""
        return self.get_link_data(event, 'down')

    def make_link_send_data_unit(self, data_event):
        """Make a send data unit from a send data event."""
        payload = data_event.data
        header = data_event.context.get('header')
        return self.DATA_UNIT(header=header, payload=payload)

    def update_send_data_unit_header(self, data_unit, data_event):
        """Update the header of the data unit to be sent."""
        data_unit.header.type = data_event.type
        data_unit.update()

    def check_send_data_unit(self, data_unit):
        """Check the buffer of the data unit to be sent."""
        if not data_unit.consistent:
            self.logger.warning(
                'Sending data unit with internal inconsistency: {}'
                .format(data_unit)
            )
            self.sender_counter['warning_inconsistent'] += 1
        data_unit.buffer

    def make_data_unit(self, event):
        """Attempt to make a data unit from a send event."""
        data_event = self.make_link_send_data_event(event)
        if data_event is None:
            return

        header = data_event.context.get('header')
        try:
            data_unit = self.make_link_send_data_unit(data_event)
            if header is None:
                self.update_send_data_unit_header(data_unit, data_event)
            self.check_send_data_unit(data_unit)
        except Exception:
            self.logger.exception(
                'Cannot send data unit from invalid send data: {}'.format(data_event)
            )
            self.sender_counter['error_invalid_payload'] += 1
            return

        return data_unit

    def make_send_data_event_data(self, data_unit):
        """Return the representation of data to pass down in as a send link data."""
        return data_unit.buffer

    # Implement CommunicationLink

    def receiver_process(self, event):
        """Implement CommunicationLink.receiver_process."""
        if isinstance(event, LinkException):
            yield event
            return

        result = self.parse_data_unit(event)
        if isinstance(result, LinkException):
            yield result
            return
        if not self.is_exposable_data_unit(result):
            self.on_internal_data(result, event)
            return

        try:
            self.logger.debug('Receiving: {}'.format(hex_bytes(result)))
        except (TypeError, ValueError):
            self.logger.debug('Receiving: {}'.format(result))
        context = {}
        if isinstance(result, DataUnit):
            data_unit = result
            if data_unit.header is not None:
                context['header'] = data_unit.header
            if data_unit.footer is not None:
                context['footer'] = data_unit.footer
        yield self.make_link_received_event(result, event, context)

    def sender_process(self, event):
        """Implement CommunicationLink.sender_process."""
        data_unit = self.make_data_unit(event)
        if data_unit is None:
            return

        try:
            self.logger.debug('Sending: {}'.format(hex_bytes(data_unit)))
        except (TypeError, ValueError):
            self.logger.debug('Sending: {}'.format(data_unit))
        data_event = self.make_link_data(
            self.make_send_data_event_data(data_unit),
            'down', event, type=self.DATA_UNIT.TYPE
        )
        yield data_event


# Counters


def compile_counters(stack):
    """Return an ordered dict of all counters in all layers of a stack."""
    return OrderedDict([
        (
            link.name if link.name is not None else str(link),
            link.counters
        )
        for link in stack.layers if hasattr(link, 'counters')
    ])


def count_to_read(link_counters):
    """Find the to_read count in the counters returned by a CommunicationLink."""
    for processor in link_counters.values():
        if 'to_read' in processor:
            return processor['to_read']


def count_to_write(link_counters):
    """Find the to_write count in the counters returned by a CommunicationLink."""
    for processor in link_counters.values():
        if 'to_write' in processor:
            return processor['to_write']


def count_receive(link_counters):
    """Find the receive count in the counters returned by a CommunicationLink."""
    for processor in link_counters.values():
        if 'receive' in processor:
            return processor['receive']


def count_send(link_counters):
    """Find the send count in the counters returned by a CommunicationLink."""
    for processor in link_counters.values():
        if 'send' in processor:
            return processor['send']


# Stacks


class StackPipe(Pipe):
    """A pipe with a DataUnitLink-like interface."""

    # DataEventLink-like interface

    def send_data(self, *args, **kwargs):
        """Mimic DataEvent.send_data."""
        for top in self.top:
            try:
                top.send_data(*args, **kwargs)
            except AttributeError:
                pass


class ManualStackPipe(StackPipe, ManualPipe):
    """A communication protocol pipe which passes data automatically."""

    pass


class AutomaticStackPipe(StackPipe, AutomaticPipe):
    """A communication protocol pipe which passes data automatically."""

    pass


class Stack(Pipeline):
    """A pipeline with a DataUnitLink-like interface.

    Bottom and top will return links whenever possible.
    """

    # Override Pipeline

    @property
    def bottom(self):
        """Override Pipeline.bottom."""
        bottom_layer = super().bottom
        try:
            return bottom_layer.bottom
        except AttributeError:
            return bottom_layer

    @property
    def top(self):
        """Override Pipeline.top."""
        top_layer = super().top
        try:
            return top_layer.top
        except AttributeError:
            return top_layer

    # DataEventLink-like interface

    def send_data(self, *args, **kwargs):
        """Mimic DataEventLink.send_data."""
        self.pipes[-1].send_data(*args, **kwargs)

    # CommunicationLink-like interface

    @property
    def counters(self):
        """Return associated counters."""
        return compile_counters(self)


class AutomaticStack(Stack, AutomaticPipeline):
    """A communication protocol stack which passes data automatically."""

    def __init__(self, *layers, pipe_factory=AutomaticStackPipe, **kwargs):
        """Initialize the pipeline."""
        super().__init__(*layers, pipe_factory=pipe_factory, **kwargs)


class ManualStack(Stack, ManualPipeline):
    """A communication protocol stack which passes data automatically."""

    def __init__(self, *layers, pipe_factory=ManualStackPipe, **kwargs):
        """Initialize the pipeline."""
        super().__init__(*layers, pipe_factory=pipe_factory, **kwargs)


PRESET_STACK_TYPES = {
    'automatic': AutomaticStack,
    'manual': ManualStack
}
