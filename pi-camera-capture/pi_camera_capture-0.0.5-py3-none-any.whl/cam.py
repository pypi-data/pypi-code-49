import io
from picamera import PiCamera  # pylint: disable=import-error

CAM = PiCamera()
CAM.rotation = 180
CAM.resolution = (300, 300)


def capture():
    stream = io.BytesIO()
    CAM.capture(stream, "jpeg", True)
    stream.seek(0)
    return stream
