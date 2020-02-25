"""Synchronous polling-based serial io."""

# Builtins

import logging
from collections import OrderedDict

# Packages

from phylline.links.links import GenericLinkAbove
from phylline.util.interfaces import SetterProperty

import serial.tools.list_ports


logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


# Port selection


def or_filter(filter_predicate_one, filter_predicate_two):
    """Combine two filter predicates with the logical NOT."""
    return lambda properties: (
        filter_predicate_one(properties) or filter_predicate_two(properties)
    )


def and_filter(filter_predicate_one, filter_predicate_two):
    """Combine two filter predicates with the logical AND."""
    return lambda properties: (
        filter_predicate_one(properties) and filter_predicate_two(properties)
    )


def not_filter(filter_predicate):
    """Negate a filter predicate with the logical NOT."""
    return lambda properties: not filter_predicate(properties)


def bind_filter(filter_function, *args, **kwargs):
    """Bind parameters to a port filter predicate function."""
    return lambda properties: filter_function(properties, *args, **kwargs)


def key_value_filter(properties, key, value_substring):
    """Check whether the port has a manufacturer with the specified substring."""
    predicate = value_substring in properties[key]
    return predicate


DEFAULT_PORT_FILTERS = [  # TODO: specify port filters with a json config
    bind_filter(key_value_filter, 'manufacturer', 'Teensyduino'),
    bind_filter(key_value_filter, 'description', 'Arduino Due'),
    bind_filter(key_value_filter, 'description', 'Due'),
    bind_filter(key_value_filter, 'description', 'Arduino'),
    bind_filter(key_value_filter, 'manufacturer', 'Arduino'),
    bind_filter(key_value_filter, 'manufacturer', 'duino')
]


def list_ports():
    """Return an alphabetically-sorted list of ports."""
    return OrderedDict(sorted(
        (port.device, {
            'name': port.name,
            'device': port.device,
            'description': port.description,
            'hwid': port.hwid,
            'vid': port.vid,
            'pid': port.pid,
            'serial_number': port.serial_number,
            'location': port.location,
            'manufacturer': port.manufacturer,
            'interface': port.interface
        })
        for port in serial.tools.list_ports.comports()
    ))


def find_port(filters=DEFAULT_PORT_FILTERS, excluded_ports=[], ports=None):
    """Find a port by the provided filter predicates in order of preference."""
    if ports is None:
        ports = list_ports()
    for filter in filters:
        for (device, properties) in ports.items():
            if filter(properties) and (device not in excluded_ports):
                return (device, properties)


# Connection


def connect_serial(filters=DEFAULT_PORT_FILTERS, excluded_ports=[], **kwargs):
    """Attempt to establish a serial connection."""
    result = find_port(filters=filters, excluded_ports=excluded_ports)
    if result is None:
        return None
    (port, properties) = result
    logger.debug('Attempting to connect to serial port {}: {}'.format(port, properties))
    try:
        connection = serial.Serial(port=port, **kwargs)
        return connection
    except serial.serialutil.SerialException:
        return None


# Adapters


class SerialPipelineAdapter(GenericLinkAbove):
    """A serial connection pipeline adapter."""

    def __init__(self, connection, pipeline, name=None):
        """Initialize members."""
        self.name = name
        self.connection = connection
        self.pipeline = pipeline

    def __repr__(self):
        """Represent the adapter as a string."""
        return '[{}: Serial({}) ~⇌|{}]'.format(
            self.name if self.name is not None else self.__class__.__qualname__,
            self.connection.name,
            self.pipeline
        )

    # DataEventLink-like interface

    def send_data(self, *args, **kwargs):
        """Mimic DataEventLink.send_data."""
        self.pipeline.send_data(*args, **kwargs)

    # Pipeline-like interface

    @property
    def layers(self):
        """Mimic Pipeline.layers."""
        return self.pipeline.layers

    @property
    def pipes(self):
        """Mimic Pipeline.pipes."""
        return self.pipeline.pipes

    @property
    def bottom(self):
        """Mimic Pipeline.bottom."""
        return self.pipeline.bottom

    @property
    def top(self):
        """Mimic Pipeline.top."""
        return self.pipeline.top

    @property
    def next_clock_request(self):
        """Mimic Pipeline.next_clock_request."""
        return self.pipeline.next_clock_request

    @property
    def last_clock_update(self):
        """Mimic Pipeline.last_clock_update."""
        return self.pipeline.last_clock_update

    def update_clock_request(self, request):
        """Mimic Pipeline.update_clock_request."""
        self.pipeline.update_clock_request(request)

    # EventLink/StreamLink-like interface

    @SetterProperty
    def after_receive(self, handler):
        """Mimic EventLink.after_receive."""
        self.pipeline.after_receive = handler

    @SetterProperty
    def after_read(self, handler):
        """Mimic StreamLink.after_read."""
        self.pipeline.after_read = handler

    # Implement GenericLinkAbove

    def receive(self):
        """Implement EventLinkAbove.receive."""
        return self.pipeline.receive()

    def has_receive(self):
        """Implement EventLinkAbove.receive."""
        return self.pipeline.has_receive()

    def send(self, event):
        """Implement EventLinkAbove.send."""
        return self.pipeline.send(event)

    def read(self):
        """Implement StreamLinkAbove.read."""
        return self.pipeline.read()

    def write(self, event):
        """Implement StreamLinkAbove.write."""
        return self.pipeline.write(event)
