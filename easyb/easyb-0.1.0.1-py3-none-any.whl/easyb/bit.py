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

import easyb
import sys

from typing import List
from easyb.definitions import Error

import math

__all__ = [
    "debug_data",
    "convert_unsigned",
    "to_signed32",
    "to_unsigned32",
    "decode_u16",
    "decode_u32",
    "crop_u8",
    "crop_u16",
    "crop_u32",
    "create_crc",
    "check_crc",

    "Value"
]


def debug_data(data: bytes) -> str:
    debug = ""
    for item in data:
        value = int(item)
        if debug == "":
            debug = "0x{:02x}".format(value)
        else:
            debug = debug + " 0x{:02x}".format(value)

    return debug


def convert_unsigned(unsigned_value, bitsize) -> int:
    signed_value = unsigned_value if unsigned_value < (1 << bitsize - 1) else unsigned_value - (1 << bitsize)
    return signed_value


def to_signed32(value):
    value = value & 0xffffffff
    return (value ^ 0x80000000) - 0x80000000


def to_unsigned32(value):
    value = value & 0xffffffff
    return value


def decode_u16(bytea: int, byteb: int) -> int:
    data = (255 - bytea) << 8
    data = data | byteb
    return data


def decode_u32(inputa: int, inputb: int) -> int:
    data = (inputa << 16) | inputb
    return data


def crop_u8(value: int) -> int:
    size = sys.getsizeof(value)
    result = value

    if size <= 16:  # pragma: no cover
        result = value & 0x00ff

    if (size > 16) and (size <= 32):
        result = value & 0x000000ff

    if (size > 32) and (size <= 64):
        result = value & 0x00000000000000ff
    return result


def crop_u16(value: int) -> int:
    size = sys.getsizeof(value)
    result = value

    if (size > 16) and (size <= 32):
        result = value & 0x0000ffff

    if (size > 32) and (size <= 64):
        result = value & 0x000000000000ffff
    return result


def crop_u32(value: int) -> int:
    size = sys.getsizeof(value)
    result = value

    if size > 32:
        result = value & 0x00000000ffffffff
    return result


def create_crc(byte1: int, byte2: int) -> int:
    ui16_integer = (byte1 << 8) | byte2

    counter = 0
    while counter < 16:
        check_value = crop_u16(ui16_integer & 0x8000)
        if check_value == 0x8000:
            ui16_integer = ui16_integer << 1
            ui16_integer = ui16_integer ^ 0x0700
        else:
            ui16_integer = ui16_integer << 1

        counter += 1

    crop = crop_u8(ui16_integer >> 8)
    crc = 255 - crop
    return crc


def check_crc(byte1: int, byte2: int, crc: int) -> bool:
    value_crc = create_crc(byte1, byte2)

    if value_crc == crc:
        return True

    error_text = "CRC check failed: {0:s} {1:s}, crc {2:s}, calculated {3:s}".format(hex(byte1), hex(byte2),
                                                                                     hex(crc),
                                                                                     hex(value_crc))
    easyb.log.error(error_text)
    return False


class Value(object):

    def __init__(self, **kwargs):
        self.data: List[int] = []
        self.value: float = 0.0

        # noinspection PyTypeChecker
        self.error: Error = None

        item = kwargs.get("data", None)
        if item is not None:
            self.data = item

        item = kwargs.get("value", None)
        if item is not None:
            self.value = item
        return

    def decode16(self) -> bool:
        byte3: int = self.data[3]
        byte4: int = self.data[4]

        u16_integer = decode_u16(byte3, byte4)

        float_pos = crop_u16(u16_integer & 0xc000)

        float_pos = crop_u16(float_pos >> 14)

        u16_integer = crop_u16(u16_integer & 0x3fff)

        if (u16_integer >= 0x3fe0) and (u16_integer <= 0x3fff):
            # error = int(u16_integer) - 16352
            self.error = easyb.conf.get_error(int(u16_integer))
            self.value = 0.0
            return False

        nenner = 10 ** int(float_pos)
        zaehler = float(u16_integer) - 2048.0

        self.value = float(zaehler / nenner)
        return True

    def encode16(self):
        float_value = self.value
        floor_value = math.floor(float_value)
        floor_str = str(floor_value)

        pos = len(floor_str)

        i16_integer = int(float_value * float(float(10.0) ** pos)) + 2048
        i16_integer = crop_u16(i16_integer)
        u16_integer = convert_unsigned(i16_integer, 16)

        float_pos = crop_u16(pos << 14)
        u16_integer = u16_integer | float_pos

        byte3 = u16_integer >> 8
        byte3 = 255 - byte3

        byte4 = crop_u8(u16_integer & 0x00ff)
        byte5 = create_crc(byte3, byte4)

        self.data = [byte3, byte4, byte5]
        return

    def decode32(self) -> bool:
        byte3: int = self.data[3]
        byte4: int = self.data[4]
        byte6: int = self.data[6]
        byte7: int = self.data[7]

        u16_integer1 = decode_u16(byte3, byte4)
        u16_integer2 = decode_u16(byte6, byte7)
        u32_integer = decode_u32(u16_integer1, u16_integer2)

        float_pos = 0xff - byte3
        float_pos = (float_pos >> 3) - 15

        u32_integer = crop_u32(u32_integer & 0x07ffffff)

        if (100000000 + 0x2000000) > u32_integer:
            compare = crop_u32(u32_integer & 0x04000000)

            if 0x04000000 == compare:
                u32_integer = crop_u32(u32_integer | 0xf8000000)

            u32_integer = crop_u32(u32_integer + 0x02000000)
        else:
            error_num = u32_integer - 0x02000000 - 100000000

            self.error = easyb.conf.get_error(error_num)
            self.value = 0.0
            return False

        i32_integer = to_signed32(u32_integer)
        self.value = float(i32_integer) / float(float(10.0) ** float_pos)
        return True

    def encode32(self):
        float_value = self.value

        float_pos = len(str(math.floor(float_value)))

        i32_integer = int(float_value * float(float(10.0) ** float_pos))
        u32_integer = to_unsigned32(i32_integer)

        u32_integer = crop_u32(u32_integer - 0x02000000)

        check_integer = u32_integer & 0x7FFFFFF
        compare = crop_u32(check_integer & 0x04000000)

        if 0x04000000 == compare:
            u32_integer = check_integer

        float_value = crop_u16((float_pos + 15) << 3) << 24

        u32_integer = u32_integer | float_value

        byte3 = 255 - ((u32_integer & 0xff000000) >> 24)
        byte4 = (u32_integer & 0x00ff0000) >> 16
        byte5 = create_crc(byte3, byte4)

        byte6 = 255 - ((u32_integer & 0x0000ff00) >> 8)
        byte7 = u32_integer & 0x000000ff
        byte8 = create_crc(byte6, byte7)

        self.data = [byte3, byte4, byte5, byte6, byte7, byte8]
        return
