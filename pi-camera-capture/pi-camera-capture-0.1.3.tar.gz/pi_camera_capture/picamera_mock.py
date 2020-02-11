import sys
from unittest.mock import MagicMock
from PIL import Image


class PiCameraMock:  # pylint: disable=too-few-public-methods
    def capture(self, stream, _, __):  # pylint: disable=no-self-use
        img = Image.new("RGBA", (50, 50), (256, 0, 0))
        img.save(stream, "png")


def import_picamera_mock():
    picamera = MagicMock()
    picamera.PiCamera = PiCameraMock
    sys.modules["picamera"] = picamera


import_picamera_mock()
