"""Test the protocol.application.pubsub module."""

# Builtins

# Packages

from phyllo.protocol.application.endpoints import EndpointHandler, SingleEndpointHandler
from phyllo.protocol.communication import SCHEMAS


class SimpleEndpointHandler(SingleEndpointHandler):
    """Test class for SingleEndpointHandler."""

    # Implement EndpointHandler

    def on_receiver_event(self, endpoint_name, data, source_event):
        """Implement EndpointHandler.on_receiver_event."""
        self.directly_to_send_data((data + 1), previous=source_event)
        self.directly_to_send_data((data + 2), previous=source_event)
        yield data

    def on_sender_event(self, send_data):
        """Implement EndpointHandler.on_sender_event."""
        yield (send_data * 4, {'schema': SCHEMAS[('generic', 'primitive', 'int')]})
        yield (send_data * 8, {})


class TwoEndpointHandler(EndpointHandler):
    """Test class for EndpointHandler."""

    # Implement EndpointHandler

    def on_receiver_event(self, endpoint_name, data, source_event):
        """Implement EndpointHandler.on_receiver_event."""
        if endpoint_name == 'int':
            yield int(data + 1)
        elif endpoint_name == 'float':
            yield float(data + 0.5)

    def on_sender_event(self, send_data):
        """Implement EndpointHandler.on_sender_event."""
        if isinstance(send_data, int):
            yield (
                'int',
                send_data - 1,
                {'schema': SCHEMAS[('generic', 'primitive', 'int')]}
            )
        elif isinstance(send_data, float):
            yield (
                'float',
                send_data - 0.5,
                {'schema': SCHEMAS[('generic', 'primitive', 'float32')]}
            )


def test_normal_passthrough():
    """Exercise the Endpoint functionality."""
    handler = EndpointHandler()

    # Receiver
    handler.to_receive(('foo', 1))
    assert handler.has_receive()
    received = list(handler.receive_all())
    assert len(received) == 1
    assert received[0].data == ('foo', 1)
    assert not handler.has_to_send()

    # Sender
    handler.send(('foo', 8))
    assert handler.has_to_send()
    sent = list(handler.to_send_all())
    assert len(sent) == 1
    assert sent[0].data == ('foo', 8)


def test_normal_single():
    """Exercise the SingleEndpointHandler functionality."""
    handler = SimpleEndpointHandler('foo')

    # Receiver
    handler.to_receive(('foo', 1))
    assert handler.has_receive()
    received = list(handler.receive_all())
    assert len(received) == 1
    assert received[0].data == 1
    assert handler.has_to_send()
    sent = list(handler.to_send_all())
    assert len(sent) == 2
    assert sent[0].data == ('foo', 2)
    assert sent[1].data == ('foo', 3)

    # Sender
    handler.send(8)
    assert handler.has_to_send()
    sent = list(handler.to_send_all())
    assert len(sent) == 2
    assert sent[0].data == ('foo', 32)
    assert sent[1].data == ('foo', 64)


def test_normal_double():
    """Exercise the EndpointHandler functionality."""
    handler = TwoEndpointHandler()

    # Receiver
    handler.to_receive(('int', 1))
    assert handler.has_receive()
    received = list(handler.receive_all())
    assert len(received) == 1
    assert received[0].data == 2
    assert not handler.has_to_send()
    handler.to_receive(('float', 0.5))
    assert handler.has_receive()
    received = list(handler.receive_all())
    assert len(received) == 1
    assert received[0].data == 1.0
    assert not handler.has_to_send()

    # Sender
    handler.send(2)
    assert handler.has_to_send()
    sent = list(handler.to_send_all())
    assert len(sent) == 1
    assert sent[0].data == ('int', 1)
    handler.send(1.0)
    assert handler.has_to_send()
    sent = list(handler.to_send_all())
    assert len(sent) == 1
    assert sent[0].data == ('float', 0.5)
