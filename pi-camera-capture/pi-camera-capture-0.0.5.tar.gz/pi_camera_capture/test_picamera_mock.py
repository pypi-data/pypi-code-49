import pi_camera_capture.picamera_mock  # pylint: disable=unused-import
from pi_camera_capture.cam import capture


def test_mock_capture():
    expected_length = 144
    stream = capture()
    assert stream.getbuffer().nbytes == expected_length
