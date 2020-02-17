"""App dependencies"""
import dash

from nqontrol import settings
from nqontrol.errors import ConfigurationError
from nqontrol.servoDevice import ServoDevice

if settings.DEVICES_LIST:
    devices = [
        ServoDevice(deviceNumber=i, readFromFile=settings.SETTINGS_FILE)
        for i in settings.DEVICES_LIST
    ]
else:
    raise ConfigurationError("No device specified and no save file provided.")

app = dash.Dash(__name__)
