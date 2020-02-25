import math

def celsius(pin):
    """Return temperature in celsius from sensor

    Parameters:
      pin (int):     Analog pin to read from (e.g. 1 for A1)

    Returns:         Calculated temperature in Celsius
    """

    from . import arduino
    reading = float(arduino().analogRead(pin+14))
    R = 1023.0/reading-1.0
    R = 100000*R
    temperature = 1.0/(math.log10(R/100000)/4275+1/298.15)-273.15;
    return temperature

