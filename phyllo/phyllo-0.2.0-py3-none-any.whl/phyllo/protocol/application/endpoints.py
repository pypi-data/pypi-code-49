"""Endpoints provide a way to react to application events."""

# Builtins

# Packages

from phylline.links.events import LinkEvent, LinkException

from phyllo.protocol.communication import DATA_TYPES
from phyllo.protocol.presentation.documents import (
    DocumentLink as PresentationDocumentLink
)


class EndpointHandler(PresentationDocumentLink):
    """A communication link to handle documents depending on their named endpoints."""

    TYPE = DATA_TYPES['presentation', 'document']

    def match_receiver(self, endpoint_name):
        """Determine whether to handle a received data unit on the specified endpoint.

        Override this to filter endpoint names.
        """
        return True

    def match_sender(self, send_data):
        """Determine whether to handle a send data unit on the specified endpoint.

        Override this to filter endpoint names.
        """
        return True

    def on_receiver_event(self, endpoint_name, data, source_event):
        """Handle receiver data matched on the specified endpoint name.

        Yield any events to expose to the layer above, or else yield from []
        if there are no events to expose to the layer above.
        """
        yield (endpoint_name, data)

    def on_sender_event(self, send_data):
        """Handle sender data matched on the specified endpoint name.

        Yield any events to send to the layer below, or else yield from []
        if there are no events to send to the layer below.
        """
        (endpoint_name, data) = send_data
        yield (endpoint_name, data)

    def deduce_sender_result(self, handler_result):
        """Deduce the endpoint name and any args for the sender handler results."""
        endpoint_name = handler_result[0]
        data = handler_result[1]
        if len(handler_result) > 2:
            make_data_kwargs = handler_result[2]
        else:
            make_data_kwargs = {}
        return (endpoint_name, data, make_data_kwargs)

    def directly_to_send_data(
        self, data, previous=None, format=None, schema=None, context=None
    ):
        """Directly send communication data."""
        data = self.make_link_data(
            data, 'down', previous, type=self.TYPE, context=context,
            format=format if format is not None else self.default_format,
            schema=schema if schema is not None else self.default_schema,
        )
        self.directly_to_send(data)

    # Override DataUnitLink

    def check_send_data_unit(self, data_unit):
        """Check the buffer of the data unit to be sent."""
        pass

    def receiver_process(self, event):
        """Override DataUnitLink.receiver_process."""
        if isinstance(event, LinkException):
            yield event
            return

        result = self.parse_data_unit(event)
        if isinstance(result, LinkException):
            yield result
        if not self.is_exposable_data_unit(result):
            self.on_internal_data(result, event)
            return

        (endpoint_name, data) = result
        if not self.match_receiver(endpoint_name):
            return

        self.logger.debug('Handling received on {}: {}'.format(endpoint_name, data))
        for handler_result in self.on_receiver_event(endpoint_name, data, event):
            if isinstance(handler_result, LinkEvent):
                yield handler_result
                continue

            self.logger.debug('Receiving: {}'.format(handler_result))
            yield self.make_link_received_event(handler_result, event, {})

    def sender_process(self, event):
        """Override DataUnitLink.sender_process."""
        data_unit = self.make_data_unit(event)
        if data_unit is None:
            return

        send_data = data_unit
        if not self.match_sender(send_data):
            return

        self.logger.debug('Handling send: {}'.format(send_data))
        for handler_result in self.on_sender_event(send_data):
            if isinstance(handler_result, LinkEvent):
                yield handler_result
                continue

            (
                endpoint_name, data, make_data_kwargs
            ) = self.deduce_sender_result(handler_result)
            self.logger.debug('Sending on {}: {}{}'.format(
                endpoint_name, data,
                ' with options: {}'.format(make_data_kwargs)
                if make_data_kwargs else ''
            ))
            data_event = self.make_link_data(
                self.make_send_data_event_data((endpoint_name, data)),
                'down', event, type=self.TYPE, **make_data_kwargs
            )
            yield data_event

    # Override PresentationDocumentLink

    def make_link_received_data_unit(self, data_event):
        """Override DataUnitLink.make_link_received_data_unit."""
        (topic, data) = data_event.data
        return (topic, data)

    def make_link_received_event(
        self, handler_result, source_event, context, format=None, schema=None
    ):
        """Override DataUnitLink.make_link_received_event."""
        return self.make_link_data(
            handler_result, 'up', source_event, context=context, type=self.TYPE,
            format=format if format is not None else self.default_format,
            schema=schema if schema is not None else self.default_schema
        )

    def is_control_data_unit(self, data):
        """Override DataUnitLink.is_control_data_unit."""
        return False

    def make_link_send_data_event(self, event, format=None, schema=None):
        """Override DataUnitLink.make_link_send_data_event."""
        return self.get_link_data(
            event, 'down',
            format=format if format is not None else self.default_format,
            schema=schema if schema is not None else self.default_schema,
            type=self.TYPE
        )

    def make_link_send_data_unit(self, data_event):
        """Override DataUnitLink.make_link_send_data_unit."""
        return data_event.data

    def update_send_data_unit_header(self, data, data_event):
        """Override DataUnitLink.update_send_data_unit_header."""
        pass

    def make_send_data_event_data(self, data_unit):
        """Override DataUnitLink.make_send_data_event_data."""
        (topic, data) = data_unit
        return (topic, data)


class SingleEndpointHandler(EndpointHandler):
    """A communication link to handle documents matching a single named endpoint."""

    def __init__(self, endpoint_name, *args, **kwargs):
        """Initialize members."""
        self.endpoint_name = endpoint_name
        if 'name' not in kwargs:
            kwargs = {
                'name': endpoint_name,
                **kwargs
            }
        super().__init__(*args, **kwargs)

    def directly_to_send_data(
        self, data, previous=None, format=None, schema=None, context=None
    ):
        """Directly send communication data."""
        self.directly_to_send(self.make_link_data(
            (self.endpoint_name, data), 'down', previous,
            type=self.TYPE, context=context,
            format=format if format is not None else self.default_format,
            schema=schema if schema is not None else self.default_schema,
        ))

    # Implement EndpointHandler

    def match_receiver(self, endpoint_name):
        """Implement EndpointHandler.match_receiver."""
        return endpoint_name == self.endpoint_name

    def match_sender(self, send_data):
        """Implement EndpointHandler.match_sender."""
        return True

    # Override EndpointHandler

    def deduce_sender_result(self, handler_result):
        """Override EndpointHandler.deduce_sender_result."""
        (send_data, make_data_kwargs) = handler_result
        return (self.endpoint_name, send_data, make_data_kwargs)
