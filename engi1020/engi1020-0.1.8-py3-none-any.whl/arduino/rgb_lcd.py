from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, returns)


class rgb_lcd(ArduinoObject):

    def __init__(self, connection=None):
        ArduinoObject.__init__(self, connection=connection)
        self.id = self.call('new')

    @arduinoobjectmethod
    def clear(self):
        pass

    @arduinoobjectmethod
    def moveCursor(self, col, row):
        pass

    @arduinoobjectmethod
    def setRGB(self, red, blue, green):
        pass

    @arduinoobjectmethod
    def print(self, value):
        pass

    @arduinoobjectmethod
    def printString(self, value):
        pass
