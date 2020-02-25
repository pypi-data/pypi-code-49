import math

def centimeters(pin):
    """Return distance in cm from sensor

    Parameters:
      pin (int):     Analog pin to read from (e.g. 1 for A1)

    Returns:         Calculated distance in cm
    """

    from . import arduino
    reading = float(arduino().analogRead(pin+1+14))
    distance = 27.726*((reading*5/1024)**-1.2045)
    return distance

