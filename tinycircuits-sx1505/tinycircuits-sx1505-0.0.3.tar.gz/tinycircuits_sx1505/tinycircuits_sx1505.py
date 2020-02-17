# SX1505 Library
# Written for use with TinyCircuits Joystick (SKRHABE010) and Rotary (SH-7010TA) Wirelings
# Written by: Laverena Wienclaw for TinyCircuits

import pigpio

_SX1505_I2CADDR	     = 0x20
_SX1505_REG_DATA     = 0x00
_SX1505_REGDIR       = 0x01	# 0 -> output, 1 -> input
_SX1505_REG_PULLUP   = 0x02 	# 0 -> pull-up disabled, 1 -> pull-up enabled
_SX1505_REG_PULLDOWN = 0x03

_SX1505_REG_INTMASK       = 0x05
_SX1505_REG_SENSE_HI      = 0x06
_SX1505_REG_SENSE_LO      = 0x07
_SX1505_REG_INT_SRC       = 0x08
_SX1505_REG_EVENT_STATUS  = 0x09
_SX1505_REG_PLD_MODE      = 0x10
_SX1505_REG_PLD_T0        = 0x11
_SX1505_REG_PLD_T1        = 0x12
_SX1505_REG_PLD_T2        = 0x13
_SX1505_REG_PLD_T3        = 0x14
_SX1505_REG_PLD_T4        = 0x15

# Definitions of joystick directions
# NOTE: "UP" is the direction closest to the Wireling connector
_JOYSTICK_UP      = 0x02 	# 185 raw
_JOYSTICK_DOWN    = 0x80 	# 59  raw
_JOYSTICK_LEFT    = 0x01 	# 186 raw
_JOYSTICK_RIGHT	  = 0x08 	# 179 raw
_JOYSTICK_PRESS	  = 0x10 	# 171 raw

class SX1505: 
    def __init__(self):
        pi = pigpio.pi()
        h = pi.i2c_open(1, _SX1505_I2CADDR)
        pi.i2c_write_byte_data(h, _SX1505_REGDIR, 0xFF)
        pi.i2c_write_byte_data(h, _SX1505_REG_PLD_MODE, 0x00)
        pi.i2c_write_byte_data(h, _SX1505_REG_DATA, 0x00)
        pi.i2c_write_byte_data(h, _SX1505_REG_PULLUP, 0x9B)
        pi.i2c_close(h)

        # Joystick directions
        self.up = False
        self.down = False
        self.left = False
        self.right = False

    def write(self, regAddr, regData):
        pi = pigpio.pi()
        h = pi.i2c_open(1, _SX1505_I2CADDR)
        pi.i2c_write_byte(h, regAddr)
        pi.i2c_write_byte(h, regData)
        pi.i2c_close(h)

    def read(self, regAddr):
        pi = pigpio.pi()
        h = pi.i2c_open(1, _SX1505_I2CADDR)
        pi.i2c_write_byte(h, regAddr)
        value = pi.i2c_read_byte_data(h, regAddr)
        pi.i2c_close(h)
        return value

    def getRegData(self):
        pi = pigpio.pi()
        h = pi.i2c_open(1, _SX1505_I2CADDR)
        value = pi.i2c_read_byte_data(h, _SX1505_REG_DATA)
        pi.i2c_close(h) # Closes I2C device associated with handle
        pi.stop() # Release pigpio resources
        return value

    def getJoystickPos(self):
        rawPos = self.getRegData()
        position = ~rawPos

        if (position & _JOYSTICK_UP):
           self.up = True
        elif (position & _JOYSTICK_DOWN):
           self.down = True
        elif (position & _JOYSTICK_LEFT):
           self.left = True
        elif (position & _JOYSTICK_RIGHT):
           self.right = True
        else:
           self.up = False
           self.down = False
           self.left = False
           self.right = False

    def getRotaryPos(self):
        rawPos = self.getRegData()
        rawPosition = ~rawPos
        position = 0x00

        position |= (rawPosition & 0x08)
        position |= ((rawPosition & 0x02) << 1)
        position |= ((rawPosition & 0x010) >> 3)
        position |= (rawPosition & 0x01)

        return position