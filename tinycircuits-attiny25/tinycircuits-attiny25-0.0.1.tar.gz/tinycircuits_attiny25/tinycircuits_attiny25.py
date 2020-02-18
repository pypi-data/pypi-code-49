# TinyCircuits ATtiny25 Python Package designed for use with the TinyCircuits Soil Moisture Wireling
# Written by: Laverena Wienclaw for TinyCircuits
# Initialized: Feb 2020
# Last updated: Feb 2020

import pigpio 
import math

_MIN_CAP_READ = 710 
_MAX_CAP_READ = 975

_ANALOG_READ_MAX     = 1023
_THERMISTOR_NOMINAL  = 10000
_TEMPERATURE_NOMINAL = 25
_B_COEFFICIENT       = 3380  
_SERIES_RESISTOR     = 35000

_ATTINY25_ADDRESS    = 0x30

class ATtiny25:
    def __init__(self):
        self.moisture = 0
        self.temp = 0

    def readMoisture(self):
        pi = pigpio.pi()
        h = pi.i2c_open(1, _ATTINY25_ADDRESS)
        pi.i2c_write_byte(h, 1)
        (b, d) = pi.i2c_read_device(h, 2)
        pi.i2c_close(h)
        pi.stop()
        if b>= 0:
             self.moisture = d[1] | (d[0] << 8)
        self.moisture = self.constrain(self.moisture, _MIN_CAP_READ, _MAX_CAP_READ)
        self.moisture = self.map(self.moisture, _MIN_CAP_READ, _MAX_CAP_READ, 0, 100)

    def readTemp(self):
        pi = pigpio.pi()
        h = pi.i2c_open(1, _ATTINY25_ADDRESS)
        pi.i2c_write_byte(h, 2)
        (b, d) = pi.i2c_read_device(h, 2)
        pi.i2c_close(h)
        pi.stop()
        if b>= 0:
             c = d[1] | (d[0] << 8)

        # Thermistor Calculation
        adcVal = _ANALOG_READ_MAX - c
        resistance = (_SERIES_RESISTOR * _ANALOG_READ_MAX) / adcVal - _SERIES_RESISTOR
        steinhart = resistance / _THERMISTOR_NOMINAL                      # (R/Ro)
        steinhart = math.log(steinhart)                                   # ln(R/Ro)
        steinhart = steinhart / _B_COEFFICIENT                            # 1/B * ln(R/Ro)
        steinhart = steinhart + (1.0 / (_TEMPERATURE_NOMINAL + 273.15))   # + (1/To)
        steinhart = 1.0 / steinhart                                       # Invert
        steinhart = steinhart - 273.15                                    # convert to C
        self.temp = steinhart 

    def constrain(self, val, min_val, max_val):
        return min(max_val, max(min_val, val))

    def map(self, x, in_min, in_max, out_min, out_max):
        return ((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
