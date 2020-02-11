"""Arduino API wrapper.

This code assumes that there is only one Arduino device connected.
"""

import nanpy


# Assuming there's only one Arduino connected to this computer, here it is.
a = None

def arduino():
    """Return Arduino API, instantiating if needed."""

    global a

    if a is None:
        import sys

        if sys.platform == 'win32':
            print('Check Windows Device Manager to see which COM the Arduino Uno has been assigned') 
            port = input('Please specify COM port (eg. COM10): ')
            a = nanpy.ArduinoApi(connection=nanpy.SerialManager(device=port))
        else:
            a = nanpy.ArduinoApi(connection=nanpy.SerialManager())

    return a


def analog_read(pin):
    """Read a value from an analog port.

    Parameters:
      pin (int):     Analog pin to read from (e.g., 2 for A2).

    Returns:         Quantized analog value (0–1023).
    """
    return arduino().analogRead(pin+14)

def analog_write(pin, duty):
    """Write a value to an analog port.

    Parameters:
      pin (int):     Analog pin to write to (e.g., 2 for A2).
      duty (int):    Duty cycle to set (0–255).
    """
    return arduino().analogWrite(pin+14, duty)

def digital_read(pin):
    """Read a value from a digital port.

    Parameters:
      pin (int):     Digital pin to read from (e.g., 4 for D4).

    Returns:         True or False.
    """
    return arduino().digitalRead(pin)

def digital_write(pin, value):
    """Write a value to a digital port.

    Parameters:
      pin (int):     Digital pin to write to (e.g., 4 for D4).
      value (bool):  Value to write (True or False).
    """
    return arduino().digitalWrite(pin, value)


from . import lcd
lcd_clear = lcd.clear
lcd_move_cursor = lcd.move_cursor
lcd_print = lcd.print
lcd_hsv = lcd.hsv
lcd_rgb = lcd.rgb

from . import temperature
temp_celsius = temperature.celsius

from . import motor
servo_move = motor.move
servo_read = motor.read

from . import buzzer
buzzer_note = buzzer.note
buzzer_stop = buzzer.stop
