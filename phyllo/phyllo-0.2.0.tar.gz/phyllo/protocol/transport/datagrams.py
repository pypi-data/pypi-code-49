"""Datagram parsing and serialization."""

# Builtins

import struct

# Packages

from phyllo.protocol.communication import DATA_TYPES
from phyllo.protocol.communication import DataUnit, DataUnitLink, StructuredHeader
from phyllo.util.crc import compute_reflected_crc


# Datagram


class DatagramHeader(StructuredHeader):
    """Datagram header.

    In order of increasing offset in the buffer representation:
    Length is the length of the payload.
    Type is the type of the payload.
    """

    FORMAT = '> B B'
    PARSER = struct.Struct(FORMAT)
    SIZE = struct.calcsize(FORMAT)

    def __init__(self, length=0, type=DATA_TYPES[('bytes', 'buffer')]):
        """Initialize field values."""
        super().__init__(type=type)
        self.length = length

    # Implement CommunicationLinkHeader

    @property
    def fields(self):
        """Implement CommunicationLinkHeader.fields."""
        return (self.length, self.type)

    def read(self, buffer):
        """Implement CommunicationLinkHeader.read."""
        (self.length, self.type) = self.unpack(buffer)

    @property
    def length_string(self):
        """Return a string representation of the length field."""
        return 'L{:3}'.format(self.length if self.length is not None else '   ')

    @property
    def field_strings(self):
        """Implement CommunicationLinkHeader.field_strings."""
        return (self.length_string, self.type_string)

    @property
    def members_repr(self):
        """Implement CommunicationLinkHeader.members_repr."""
        return {
            'length': self.length,
            'type': self.type_repr
        }


class Datagram(DataUnit):
    """Datagram containing a header and a payload.

    Datagrams are transmitted unreliably; however, the length field is used to
    check for length corruption in the payload.

    In order of increasing offset in the buffer representation:
    Header contains the header.
    Payload contains the payload.
    """

    TYPE = DATA_TYPES[('transport', 'datagram')]

    HEADER = DatagramHeader

    def __init__(self, header=None, payload=b''):
        """Initialize with optional header and payload.

        Note: saves references, not copies, of header and payload!
        """
        super().__init__(
            header=header, payload=payload,
            size_limit=255 + self.HEADER.SIZE  # set by the header's length field
        )

    # Implement DataUnit

    def update(self):
        """Implement DataUnit.update."""
        self.header.length = len(self.payload)

    # Override DataUnit

    @property
    def consistent(self):
        """Override DataUnit.consistent."""
        return self.header.length == len(self.payload)


class DatagramLink(DataUnitLink):
    """The DatagramLink prepends the data with a small header.

    This is a connectionless link.
    Refer to DatagramHeader for details about the header.

    Interface:
    Above:
        send unencoded bytes of payload or EventData objects with unencoded bytes
            of payload.
            - If a type is given in the context with key 'type' in the EventData
              object, it will be used to set the type field of the datagram header.
            - If a header is given in the context with key 'header' in
              the EventData object, it will be sent as-is with the payload, without
              any validation checking (though a warning will be logged for an
              inconsistent length in a header which is given). This will override
              any type given in the context.
        receive EventData objects with unencoded bytes of payload. The associated
            header will be given in the context with key 'header'. The payload
            type will be given in the context with key 'type'.
    Below:
        to_send EventData objects with header-wrapped bytestrings.
        to_receive header-wrapped bytestrings or EventData objects with
            header-wrapped bytestrings. The type will be given in the context
            with key 'header'.
    """

    DATA_UNIT = Datagram
    RECEIVABLE_TYPES = {
        DATA_UNIT.TYPE,
        DATA_TYPES[('bytes', 'buffer')]
    }

    def __init__(self):
        """Initialize members."""
        super().__init__(logger_name=__name__, logger_indentation=4.5)

    # Override DataUnitLink

    def parse_data_unit(self, event):
        """Override DataUnitLink.parse_data_unit."""
        result = super().parse_data_unit(event)
        if not isinstance(result, self.DATA_UNIT):
            return result

        datagram = result
        if not datagram.consistent:
            self.logger.error(
                'Received payload with inconsistent length:\t{}'
                .format(datagram)
            )
            self.receiver_counter['error_inconsistent'] += 1
            return self.make_link_exception(
                'Received inconsistent length', 'up', event, context={
                    'specified_length': datagram.header.length,
                    'computed_length': len(datagram.payload)
                }
            )

        return datagram


# Validated Datagram


class ValidatedDatagramHeader(StructuredHeader):
    """Validated datagram header.

    In order of increasing offset in the buffer representation:
    CRC is the CRC32sub8 of the payload.
    Type is the type of the payload.
    """

    FORMAT = '> L B'
    PARSER = struct.Struct(FORMAT)
    SIZE = struct.calcsize(FORMAT)
    PROTECTED_OFFSET = 4  # position at which CRC-protected data begins

    def __init__(self, crc=0, type=DATA_TYPES[('bytes', 'buffer')]):
        """Initialize field values."""
        super().__init__(type=type)
        self.crc = crc

    # Implement CommunicationLinkHeader

    @property
    def fields(self):
        """Implement CommunicationLinkHeader.fields."""
        return (self.crc, self.type)

    def read(self, buffer):
        """Implement CommunicationLinkHeader.read."""
        (self.crc, self.type) = self.unpack(buffer)

    @property
    def field_strings(self):
        """Implement CommunicationLinkHeader.field_strings."""
        crc_string = 'C0x{:08x}'.format(
            self.crc if self.crc is not None else '        '
        )
        return (crc_string, self.type_string)

    @property
    def members_repr(self):
        """Implement CommunicationLinkHeader.members_repr."""
        return {
            'crc': '0x{:08x}'.format(self.crc),
            'type': self.type_repr
        }


class ValidatedDatagram(DataUnit):
    """Validated Datagram containing a header and a payload.

    The CRC header field is used to check for data corruption in the rest of the
    header and the payload.

    In order of increasing offset in the buffer representation:
    Header contains the header.
    Payload contains the payload.
    """

    TYPE = DATA_TYPES[('transport', 'validated_datagram')]

    HEADER = ValidatedDatagramHeader

    def __init__(self, header=None, payload=b''):
        """Initialize with optional header and payload.

        Note: saves references, not copies, of header and payload!
        """
        self._cached_crc = None
        super().__init__(header=header, payload=payload)

    @property
    def crc(self):
        """Return the crc of the protected section of the datagram."""
        if self._cached_crc is None:
            if self.payload is not None:
                self._cached_crc = self._computed_crc
            else:
                self._cached_crc = 0
        return self._cached_crc

    # Implement DataUnit

    def update(self):
        """Implement DataUnit.update."""
        self.header.crc = self.crc

    # Override DataUnit

    @property
    def payload(self):
        """Override DataUnit.payload."""
        return super().payload

    @payload.setter
    def payload(self, value):
        """Override DataUnit.payload.setter."""
        super(ValidatedDatagram, self.__class__).payload.fset(self, value)
        self._cached_crc = None

    @property
    def consistent(self):
        """Override DataUnit.consistent."""
        if self._cached_crc is None:
            if self.payload is not None:
                self._cached_crc = self._computed_crc
            else:
                self._cached_crc = 0
        return self.header.crc == self._cached_crc

    # Implementation details

    @property
    def _computed_crc(self):
        """Return a computed CRC of the protected part of the datagram."""
        try:
            return compute_reflected_crc(self._protected_buffer)
        except struct.error:
            return None

    @property
    def _protected_buffer(self):
        """Return a bytes buffer representation of the protected part of the datagram."""
        return self.buffer[ValidatedDatagramHeader.PROTECTED_OFFSET:]


class ValidatedDatagramLink(DataUnitLink):
    """The ValidatedDatagramLink computes the CRC field in the datagram header.

    This is a connectionless link. It must sit on top of a DatagramLink.

    Refer to DatagramHeader for details about the header.

    Interface:
    Above:
        send unencoded bytes of payload or EventData objects with unencoded bytes
            of payload.
            - If a type is given in the context with key 'type' in the EventData
              object, it will be used to set the type field of the datagram header.
            - If a header is given in the context with key 'header' in
              the EventData object, it will be sent as-is with the payload, without
              any validation checking (though a warning will be logged for an
              inconsistent crc in a header which is given). This will override
              any type given in the context.
        receive EventData objects with unencoded bytes of payload. The associated
            header will be given in the context with key 'header'. The payload
            type will be given in the context with key 'type'.
    Below:
        to_send and to_receive EventData objects with unencoded bytes of payload,
            along with the associated header given in the context with key 'header'
            and the type given in the context with key 'type'.
    """

    DATA_UNIT = ValidatedDatagram
    RECEIVABLE_TYPES = {
        DATA_UNIT.TYPE,
        DATA_TYPES[('bytes', 'buffer')]
    }

    def __init__(self):
        """Initialize members."""
        super().__init__(logger_name=__name__, logger_indentation=4)

    # Override DataUnitLink

    def parse_data_unit(self, event):
        """Override DataUnitLink.parse_data_unit."""
        result = super().parse_data_unit(event)
        if not isinstance(result, self.DATA_UNIT):
            return result

        datagram = result
        if not datagram.consistent:
            self.logger.error(
                'Received validated datagram with inconsistent CRC:\t{}'
                .format(datagram)
            )
            self.receiver_counter['error_inconsistent'] += 1
            return self.make_link_exception(
                'Received inconsistent crc', 'up', event, context={
                    'specified_crc': datagram.header.crc,
                    'computed_crc': datagram.crc,
                }
            )

        return datagram
