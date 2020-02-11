import base64
import asyncio
import logging

from abc import ABC

LOG = logging.getLogger(__name__)


INDOOR_SENSOR = 'indoor_sensor'
DOOR_LOCK_SENSOR = 'door_lock_sensor'


class Decoder(ABC):
    ''' Base class for decoders. Abstact. '''
    def __init__(self, data):
        self.raw = data
        self.data = None

    async def decode(self):
        '''
        Decodes the raw data passed to the constructor.
        Override this method with the custom decoder requirements for specific needs.
        '''
        return {k: v for k, v in self.raw}

    async def is_valid(self):
        '''
        Initializes the decoding and returns the decoded data.
        Yo should use this method prior to accessing the data of your decoder and
        verify that it yields a positive result.
        '''

        self.data = await self.decode()

        if self.data:
            return True

        return False

    @property
    def sensor_type(self):
        ''' Optionally set a sensor type for your decoder. '''
        pass


class SensitiviaDecoder(Decoder):
    ''' Decoder for sensitivia sensors. '''
    key_map = {
        'Battery': 'b',
        'AvgTemperature': 't',
        'Humidity': 'h',
        'Lux': 'l',
        'fcnt': 'fcnt',
        'rssi': 'rssi',
        'port': 'port',
    }

    async def decode(self):
        data = {}

        for k, v in self.raw:
            try:
                data[self.key_map[k]] = v
            except KeyError:
                continue

        return data

    async def is_valid(self):
        return await super().is_valid()

    @property
    def sensor_type(self):
        return INDOOR_SENSOR


class DoorLockDecoder(Decoder):
    ''' Decoder for door lock sensors. '''
    async def decode(self):
        data = super().decode()

        open_state = data.get('DI1', None)
        locked_state = data.get('DI2', None)

        return {
            'open': None if open_state is None else open_state == 0,
            'locked': None if locked_state is None else locked_state == 0,
        }

    async def is_valid(self):
        return await super().is_valid()

    @property
    def sensor_type(self):
        return DOOR_LOCK_SENSOR


class ElsysDecoder(Decoder):
    ''' Decoder used to decode all sensor types from Elsys '''
    TYPE_TEMP = 0x01  # Temp 2 bytes -3276. -->
    TYPE_RH = 0x02  # Humidity 1 byte  0-100%
    TYPE_ACC = 0x03  # Acceleration 3 bytes X,Y,Z -128 --> 127 +/-63=1G
    TYPE_LIGHT = 0x04  # Light 2 bytes 0-->65535 Lux
    TYPE_MOTION = 0x05  # No of motion 1 byte  0-255
    TYPE_CO2 = 0x06  # Co2 2 bytes 0-65535 ppm
    TYPE_VDD = 0x07  # VDD 2byte 0-65535mV
    TYPE_ANALOG1 = 0x08  # VDD 2byte 0-65535mV
    TYPE_GPS = 0x09  # 3bytes lat 3bytes long binary
    TYPE_PULSE1 = 0x0A  # 2bytes relative pulse count
    TYPE_PULSE1_ABS = 0x0B  # 4bytes no 0->0xFFFFFFFF
    TYPE_EXT_TEMP1 = 0x0C  # 2bytes -3276.5C-->3276.5C
    TYPE_EXT_DIGITAL = 0x0D  # 1bytes value 1 or 0
    TYPE_EXT_DISTANCE = 0x0E  # 2bytes distance in mm
    TYPE_ACC_MOTION = 0x0F  # 1byte number of vibration/motion
    TYPE_IR_TEMP = 0x10  # 2bytes internal temp 2bytes external temp -3276.5C-->3276.5C
    TYPE_OCCUPANCY = 0x11  # 1byte data
    TYPE_WATERLEAK = 0x12  # 1byte data 0-255
    TYPE_GRIDEYE = 0x13  # 65byte temperature data 1byte ref+64byte external temp
    TYPE_PRESSURE = 0x14  # 4byte pressure data (hPa)
    TYPE_SOUND = 0x15  # 2byte sound data (peak/avg)
    TYPE_PULSE2 = 0x16  # 2bytes 0-->0xFFFF
    TYPE_PULSE2_ABS = 0x17  # 4bytes no 0->0xFFFFFFFF
    TYPE_ANALOG2 = 0x18  # 2bytes voltage in mV
    TYPE_EXT_TEMP2 = 0x19

    async def is_valid(self):
        try:
            self.data = await self.decode()

            if self.data:
                return True

        except IndexError:
            return False # TODO: reraise a better error message and handle in caller.

        return False

    @property
    def sensor_type(self):
        return INDOOR_SENSOR

    async def _decode_hex(self, data):
        obj = {}
        i = 0
        while i < len(data):
            if data[i] == self.TYPE_TEMP:
                num = int(data[i+1] << 8 | data[i+2])
                if num > 0x7FFF:
                    num -= 0x10000
                obj['t'] = num/10
                i += 2
            elif data[i] == self.TYPE_RH:
                obj['h'] = data[i+1]
                i += 1
            elif data[i] == self.TYPE_ACC:
                i += 2
            elif data[i] == self.TYPE_LIGHT:
                obj['l'] = int(data[i+1] << 8 | data[i+2])
                i += 2
            elif data[i] == self.TYPE_MOTION:
                obj['m'] = data[i+1]
                i += 1
            elif data[i] == self.TYPE_CO2:
                obj['c'] = int(data[i+1] << 8 | data[i+2])
                i += 2
            elif data[i] == self.TYPE_VDD:
                obj['b'] = int(data[i+1] << 8 | data[i+2])
                i += 2
            elif data[i] == self.TYPE_ANALOG1:
                obj['a1'] = int(data[i+1] << 8 | data[i+2])
                i += 2
            elif data[i] == self.TYPE_GPS:
                i += 6
            elif data[i] == self.TYPE_PULSE1:
                obj['p1'] = int(data[i+1] << 8 | data[i+2])
                i += 2
            elif data[i] == self.TYPE_PULSE1_ABS:
                i += 4
            elif data[i] == self.TYPE_EXT_TEMP1:
                i += 2
            elif data[i] == self.TYPE_EXT_DIGITAL:
                obj['edig'] = data[i+1]
                i += 1
            elif data[i] == self.TYPE_EXT_DISTANCE:
                obj['edis'] = int(data[i+1] << 8 | data[i+2])
                i += 2
            elif data[i] == self.TYPE_ACC_MOTION:
                obj['am'] = data[i+1]
                i += 1
            elif data[i] == self.TYPE_IR_TEMP:
                internal_temp = int(data[i+1] << 8 | data[i+2])
                if internal_temp > 0x7FFF:
                    internal_temp -= 0x10000

                external_temp = int(data[i+3] << 8 | data[i+4])
                if external_temp > 0x7FFF:
                    external_temp -= 0x10000

                obj['irit'] = internal_temp/10
                obj['iret'] = external_temp/10

                i += 4
            elif data[i] == self.TYPE_OCCUPANCY:
                obj['o'] = data[i+1]
                i += 1
            elif data[i] == self.TYPE_WATERLEAK:
                obj['w'] = data[i+1]
                i += 1
            elif data[i] == self.TYPE_GRIDEYE:
                i += 65
            elif data[i] == self.TYPE_PRESSURE:
                i += 4
            elif data[i] == self.TYPE_SOUND:
                i += 2
            elif data[i] == self.TYPE_PULSE2:
                obj['p2'] = int(data[i+1] << 8 | data[i+2])
                i += 2
            elif data[i] == self.TYPE_PULSE2_ABS:
                i += 4
            elif data[i] == self.TYPE_ANALOG2:
                obj['a2'] = int(data[i+1] << 8 | data[i+2])
                i += 2
            elif data[i] == self.TYPE_EXT_TEMP2:
                i += 2
            else:
                LOG.error('Couldnt decode hex, at pos %s value %s', i, data[i])
                i = len(data)
            i = i+1

        return obj


class AdvantechElsysDecoder(ElsysDecoder):
    ''' Decodes elsys data comming from Advantech Wise-PaaS. '''
    async def decode(self):
        data = {}

        for k, v in self.raw:
            if k == 'hex':
                data.update(await self._decode_hex(
                    data=bytes.fromhex(v)
                ))
            else:
                data[k] = v

        LOG.debug('Decoded %s from %s', data, self.raw)
        return data


class ChirpElsysDecoder(ElsysDecoder):
    ''' Decodes elsys data comming from a Chirpstack server. '''
    async def decode(self):
        data = await self._decode_hex(
            data=base64.b64decode(self.raw)
        )

        LOG.debug('Decoded %s from %s', data, self.raw)
        return data
