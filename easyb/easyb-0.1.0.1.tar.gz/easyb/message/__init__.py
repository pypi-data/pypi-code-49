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

from typing import List

from easyb.command import Command
from easyb.message.stream import Stream

from easyb.definitions import Direction, get_direction, Length, get_length, Priority, get_priority
from easyb.bit import crop_u8

__all__ = [
    "stream",

    "Message"
]


class Message(object):

    def __init__(self, **kwargs):

        self.address: int = 0
        self.code: int = 0
        self.priority: Priority = Priority.NoPriority
        self.length: Length = Length.Byte3
        self.direction: Direction = Direction.FromMaster
        self.param: List[int] = []

        # noinspection PyTypeChecker
        self.stream: Stream = None

        item = kwargs.get("address", None)
        if item is not None:
            self.address = item

        item = kwargs.get("code", None)
        if item is not None:
            self.code = item

        item = kwargs.get("priority", None)
        if item is not None:
            self.priority = item

        item = kwargs.get("length", None)
        if item is not None:
            self.length = item

        item = kwargs.get("direction", None)
        if item is not None:
            self.direction = item

        item = kwargs.get("param", None)
        if item is not None:
            self.param = item
        return

    def command(self, command: Command) -> bool:
        self.address = command.address
        self.code = command.code
        self.priority = Priority.NoPriority
        self.length = command.length
        self.direction = Direction.FromMaster
        self.param = command.param
        return True

    def _verify_param(self) -> bool:
        length = len(self.param)

        if (self.length is Length.Byte3) and (length == 0):
            return True

        check = length % 2
        if check != 0:
            easyb.log.error("Data size is not a pair! ({0:d})".format(length))
            return False

        if (self.length is Length.Byte6) and (length != 2):
            easyb.log.error("Invald data size for Byte6: {0:d}".format(length))
            return False

        if (self.length is Length.Byte9) and (length != 4):
            easyb.log.error("Invald data size for Byte4: {0:d}".format(length))
            return False

        return True

    def _encode_header(self, data: List[int]):
        u8 = 0

        direction = crop_u8(self.direction.value)
        length = crop_u8(self.length.value << 1)
        priority = crop_u8(self.priority.value << 3)
        code = crop_u8(self.code << 4)

        u8 = crop_u8(u8 | direction)
        u8 = crop_u8(u8 | length)
        u8 = crop_u8(u8 | priority)
        u8 = crop_u8(u8 | code)

        byte = crop_u8(self.address)
        data.append(byte)

        result = int(u8)
        data.append(result)

        data.append(0)
        return

    def _encode_data(self, data: List[int]):
        length = len(self.param)

        pos_set = 0
        n = 0
        while True:
            if pos_set >= length:
                break

            pos1 = pos_set + 0
            pos2 = pos_set + 1

            data.append(self.param[pos1])
            data.append(self.param[pos2])
            data.append(0)

            pos_set += 2
            n += 3
        return

    def _decode_header(self):
        byte0 = self.stream.data[0]
        byte1 = self.stream.data[1]

        self.address = 255 - byte0
        self.code = (byte1 & 0xf0) >> 4

        priority = (byte1 & 0x8) >> 3
        length = (byte1 & 0x6) >> 1
        direction = byte1 & 0x1

        self.priority = get_priority(priority)
        self.length = get_length(length)
        self.direction = get_direction(direction)
        return

    def encode(self) -> bool:
        check = self._verify_param()
        if check is False:
            return False

        data = []
        self._encode_header(data)
        self._encode_data(data)

        out = Stream(self.length)
        out.set_data(data)
        out.encode()
        self.stream = out
        return True

    def decode(self, data: bytes) -> bool:
        self.stream = Stream(Length.Byte3)
        check = self.stream.decode(data)
        if check is False:
            easyb.log.error("Header is not valid!")
            return False

        self._decode_header()
        return True

    def info(self, debug: str):
        line = "Address {0:d}, Code {1:d}, {2:s}, {3:s}, {4:s}"
        logging = line.format(self.address, self.code, self.priority.name, self.length.name, self.direction.name)
        easyb.log.debug2(debug, logging)
        return
