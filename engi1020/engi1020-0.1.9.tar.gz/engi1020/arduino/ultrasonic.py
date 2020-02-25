from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, returns)

class Ultrasonic(ArduinoObject):

    cfg_h_name = 'USE_ultrasonic_distance'

    def __init__(self, connection=None):
        ArduinoObject.__init__(self, connection=connection)
        self.id = self.call('new')

    @arduinoobjectmethod
    def ultraInit(self, port):
        pass
 
    @arduinoobjectmethod
    def get_distance(self):
        pass
