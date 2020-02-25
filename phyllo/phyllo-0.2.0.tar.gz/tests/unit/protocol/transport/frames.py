"""Test the protocol.transport.frames module."""

# Builtins

# Packages

from cobs import cobs

from phylline.links.events import LinkException

from phyllo.protocol.transport.frames import FrameLink


def test_normal(frame_link=FrameLink()):
    """Exercise the FrameLink functionality."""
    payload = b'\0\0\0\0\1\2\3\4\0\0\0\0'
    encoded_frame = b'\1\1\1\1\5\1\2\3\4\1\1\1\1'

    # Send
    send_count = frame_link.sender_counter['send']
    to_send_count = frame_link.sender_counter['to_send']
    frame_link.send(payload)
    assert frame_link.sender_counter['send'] == send_count + 1
    assert frame_link.sender_counter['to_send'] == to_send_count + 1
    assert frame_link.has_to_send()
    result = frame_link.to_send()
    assert b'\0' not in encoded_frame
    print(result)
    assert result.data == encoded_frame

    # Receive
    receive_count = frame_link.receiver_counter['receive']
    to_receive_count = frame_link.receiver_counter['to_receive']
    frame_link.to_receive(result)
    assert frame_link.receiver_counter['to_receive'] == to_receive_count + 1
    assert frame_link.receiver_counter['receive'] == receive_count + 1
    assert frame_link.has_receive()
    result = frame_link.receive()
    print(result)
    assert result.data == payload


def test_decode_error():
    """Exercise the FrameLink decoding error handling."""
    bad_frame = b'\5\1\2\3\4\0'
    frame_link = FrameLink()

    # Receive
    print('Expect a DecodeError in logging:')
    frame_link.to_receive(bad_frame)
    assert frame_link.receiver_counter['to_receive'] == 1
    assert frame_link.receiver_counter['receive'] == 0
    assert frame_link.receiver_counter['error'] == 1
    assert frame_link.receiver_counter['error_parse'] == 1
    assert frame_link.has_receive()
    result = frame_link.receive()
    assert isinstance(result, LinkException)
    assert isinstance(result.context['exception'], cobs.DecodeError)
    test_normal(frame_link=frame_link)


def test_encode_error():
    """Exercise the FrameLink decoding error handling."""
    bad_payload = b''.join(b'\1\2\3\4' for i in range(100))
    assert len(bad_payload) > FrameLink.PAYLOAD_SIZE_LIMIT
    frame_link = FrameLink()

    # Send
    print('Expect an excessively long payload error in logging:')
    frame_link.send(bad_payload)
    assert frame_link.sender_counter['send'] == 1
    assert frame_link.sender_counter['to_send'] == 0
    assert frame_link.sender_counter['error_payload_length'] == 1
    assert frame_link.sender_counter['error_invalid_payload'] == 1
    assert not frame_link.has_to_send()
    test_normal(frame_link=frame_link)

    # Send
    print('Expect an invalid data error in logging:')
    send_count = frame_link.sender_counter['send']
    to_send_count = frame_link.sender_counter['to_send']
    frame_link.send(1234)
    assert frame_link.sender_counter['send'] == send_count + 1
    assert frame_link.sender_counter['to_send'] == to_send_count
    assert frame_link.sender_counter['error_invalid_payload'] == 2
    assert not frame_link.has_to_send()
    test_normal(frame_link=frame_link)

    # Send
    print('Expect another invalid data error in logging:')
    send_count = frame_link.sender_counter['send']
    to_send_count = frame_link.sender_counter['to_send']
    frame_link.send([1234, 5678])
    assert frame_link.sender_counter['send'] == send_count + 1
    assert frame_link.sender_counter['to_send'] == to_send_count
    assert frame_link.sender_counter['error_invalid_payload'] == 3
    assert not frame_link.has_to_send()
    test_normal(frame_link=frame_link)
