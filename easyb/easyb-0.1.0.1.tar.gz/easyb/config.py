#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#
#    Copyright (C) 2017, Kai Raphahn <kai.raphahn@laburec.de>
#

from typing import List, Union

from easyb.definitions import Error, Status, Unit

__all__ = [
    "Config"
]

_error = [
    {
        "code": 16352,
        "text": "Value over measurement range"
    },
    {
        "code": 16353,
        "text": "Value under measurement range"
    },
    {
        "code": 16362,
        "text": "Calculation impossible"
    },
    {
        "code": 16363,
        "text": "System error"
    },
    {
        "code": 16364,
        "text": "Battery empty"
    },
    {
        "code": 16365,
        "text": "No sensor"
    },
    {
        "code": 16366,
        "text": "Recording error: EEPROM error"
    },
    {
        "code": 16367,
        "text": "EEPROM checksum invalid"
    },
    {
        "code": 16368,
        "text": "Recording error: error 6, system restart"
    },
    {
        "code": 16369,
        "text": "Recording error: data pointer"
    },
    {
        "code": 16370,
        "text": "Recording error: marker data invalid"
    },
    {
        "code": 16370,
        "text": "Data invalid"
    },
    {
        "code": 0,
        "text": "Unknown error"
    }
]

_status = [
    {
        "bit": 0x0001,
        "text": "Max. alarm"
    },
    {
        "bit": 0x0002,
        "text": "Min. alarm"
    },
    {
        "bit": 0x0004,
        "text": "Value over presentable area"
    },
    {
        "bit": 0x0008,
        "text": "Value under presentable area"
    },
    {
        "bit": 0x0010,
        "text": "reserved"
    },
    {
        "bit": 0x0020,
        "text": "reserved"
    },
    {
        "bit": 0x0040,
        "text": "reserved"
    },
    {
        "bit": 0x0080,
        "text": "reserved"
    },
    {
        "bit": 0x0100,
        "text": "Value over measurement range"
    },
    {
        "bit": 0x0200,
        "text": "Value under measurement range"
    },
    {
        "bit": 0x0400,
        "text": "Sensor error"
    },
    {
        "bit": 0x0800,
        "text": "reserved"
    },
    {
        "bit": 0x1000,
        "text": "System error"
    },
    {
        "bit": 0x2000,
        "text": "Calculation impossible"
    },
    {
        "bit": 0x4000,
        "text": "reserved"
    },
    {
        "bit": 0x8000,
        "text": "Battery low"
    }
]

_units = [
    {
        "code": 1,
        "value": "°C"
    },
    {
        "code": 2,
        "value": "°F"
    },
    {
        "code": 3,
        "value": "°K"
    },
    {
        "code": 10,
        "value": "% r.F."
    },
    {
        "code": 18,
        "value": "inHg(0°C)"
    },
    {
        "code": 19,
        "value": "inHg(60°F)"
    },
    {
        "code": 20,
        "value": "bar"
    },
    {
        "code": 21,
        "value": "mbar"
    },
    {
        "code": 22,
        "value": "Pascal"
    },
    {
        "code": 23,
        "value": "hPascal"
    },
    {
        "code": 24,
        "value": "kPascal"
    },
    {
        "code": 25,
        "value": "MPascal"
    },
    {
        "code": 26,
        "value": "kg/cm²"
    },
    {
        "code": 27,
        "value": "mmHg"
    },
    {
        "code": 28,
        "value": "PSI"
    },
    {
        "code": 29,
        "value": "mm H20"
    },
    {
        "code": 30,
        "value": "S/cm"
    },
    {
        "code": 31,
        "value": "mS/cm"
    },
    {
        "code": 32,
        "value": "μS/cm"
    },
    {
        "code": 40,
        "value": "pH"
    },
    {
        "code": 42,
        "value": "rH"
    },
    {
        "code": 45,
        "value": "mg/l O2"
    },
    {
        "code": 46,
        "value": "% Sat O2"
    },
    {
        "code": 47,
        "value": "% O2"
    },
    {
        "code": 50,
        "value": "U/min"
    },
    {
        "code": 53,
        "value": "Hz"
    },
    {
        "code": 55,
        "value": "Impulse"
    },
    {
        "code": 60,
        "value": "m/s"
    },
    {
        "code": 61,
        "value": "km/h"
    },
    {
        "code": 62,
        "value": "mph"
    },
    {
        "code": 63,
        "value": "Knoten"
    },
    {
        "code": 70,
        "value": "mm"
    },
    {
        "code": 71,
        "value": "m"
    },
    {
        "code": 72,
        "value": "inch"
    },
    {
        "code": 73,
        "value": "ft"
    },
    {
        "code": 74,
        "value": "cm"
    },
    {
        "code": 75,
        "value": "km"
    },
    {
        "code": 79,
        "value": "l/s"
    },
    {
        "code": 80,
        "value": "l/h"
    },
    {
        "code": 81,
        "value": "l/min"
    },
    {
        "code": 82,
        "value": "m³/h"
    },
    {
        "code": 83,
        "value": "m³/min"
    },
    {
        "code": 84,
        "value": "nm³/h"
    },
    {
        "code": 85,
        "value": "ml/s"
    },
    {
        "code": 86,
        "value": "ml/min"
    },
    {
        "code": 87,
        "value": "ml/h"
    },
    {
        "code": 88,
        "value": "m³/3"
    },
    {
        "code": 90,
        "value": "g"
    },
    {
        "code": 91,
        "value": "kg"
    },
    {
        "code": 92,
        "value": "N"
    },
    {
        "code": 93,
        "value": "Nm"
    },
    {
        "code": 94,
        "value": "t"
    },
    {
        "code": 100,
        "value": "A"
    },
    {
        "code": 101,
        "value": "mA"
    },
    {
        "code": 102,
        "value": "μA"
    },
    {
        "code": 105,
        "value": "V"
    },
    {
        "code": 106,
        "value": "mV"
    },
    {
        "code": 107,
        "value": "μV"
    },
    {
        "code": 111,
        "value": "W"
    },
    {
        "code": 112,
        "value": "kW"
    },
    {
        "code": 115,
        "value": "Wh"
    },
    {
        "code": 116,
        "value": "kWh"
    },
    {
        "code": 117,
        "value": "mW/cm²"
    },
    {
        "code": 119,
        "value": "Wh/m²"
    },
    {
        "code": 120,
        "value": "mΩ"
    },
    {
        "code": 121,
        "value": "Ω"
    },
    {
        "code": 122,
        "value": "kΩ"
    },
    {
        "code": 123,
        "value": "MΩ"
    },
    {
        "code": 125,
        "value": "kΩ*cm"
    },
    {
        "code": 126,
        "value": "MΩ*cm"
    },
    {
        "code": 130,
        "value": "cd"
    },
    {
        "code": 131,
        "value": "lx"
    },
    {
        "code": 132,
        "value": "lm"
    },
    {
        "code": 150,
        "value": "%"
    },
    {
        "code": 151,
        "value": "°"
    },
    {
        "code": 152,
        "value": "ppm"
    },
    {
        "code": 153,
        "value": "ppb"
    },
    {
        "code": 160,
        "value": "g/kg"
    },
    {
        "code": 161,
        "value": "g/m³"
    },
    {
        "code": 162,
        "value": "mg/m³"
    },
    {
        "code": 163,
        "value": "μg/m³"
    },
    {
        "code": 170,
        "value": "kJ/kg"
    },
    {
        "code": 171,
        "value": "kcal/kg"
    },
    {
        "code": 172,
        "value": "mg/l"
    },
    {
        "code": 173,
        "value": "g/l"
    },
    {
        "code": 175,
        "value": "dB"
    },
    {
        "code": 176,
        "value": "dBm"
    },
    {
        "code": 177,
        "value": "dBA"
    },
    {
        "code": 190,
        "value": "sone"
    },
    {
        "code": 191,
        "value": "phon"
    },
    {
        "code": 192,
        "value": "μPa"
    },
    {
        "code": 196,
        "value": "dB(SPL)"
    }
]


class Config(object):

    def __init__(self):
        self.error: List[Error] = []
        self.units: List[Unit] = []

        for item in _error:
            self.error.append(Error(item))

        for item in _units:
            self.units.append(Unit(item))
        return

    def get_error(self, code: int) -> Union[None, Error]:
        for item in self.error:
            if item.code == code:
                return item
        return None

    def get_unit(self, code: int) -> Union[None, Unit]:
        for item in self.units:
            if item.code == code:
                return item
        return None

    @staticmethod
    def create_status(status_list: List[Status]):
        for item in _status:
            status_list.append(Status(item))
        return
