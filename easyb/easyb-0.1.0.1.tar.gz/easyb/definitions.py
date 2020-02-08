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

from typing import Union
from enum import Enum

__all__ = [
    "Direction",
    "get_direction",

    "Priority",
    "get_priority",

    "Length",
    "get_length",

    "Error",
    "Status",
    "Unit"
]

from bbutil.utils import check_dict


class Direction(Enum):

    FromSlave = 1
    FromMaster = 0


def get_direction(value: int) -> Union[None, Direction]:
    for item in Direction:
        if item.value == value:
            return item
    return None


class Priority(Enum):

    Priority = 1
    NoPriority = 0


def get_priority(value: int) -> Union[None, Priority]:
    for item in Priority:
        if item.value == value:
            return item
    return None


class Length(Enum):

    Byte3 = 0
    Byte6 = 1
    Byte9 = 2
    Variable = 3


def get_length(value: int) -> Union[None, Length]:
    for item in Length:
        if item.value == value:
            return item
    return None


class Error(object):

    def __init__(self, data: dict):
        self.code: int = 0
        self.text: str = ""

        check = check_dict(data, ["code", "text"])
        if check is False:
            raise ValueError("Invalid error code: {0:s}".format(str(data)))

        self.code = data["code"]
        self.text = data["text"]
        return


class Status(object):

    def __init__(self, data: dict):
        self.bit: int = 0
        self.text: str = ""
        self.is_set: bool = False

        check = check_dict(data, ["bit", "text"])
        if check is False:
            raise ValueError("Invalid status code: {0:s}".format(str(data)))

        self.bit = data["bit"]
        self.text = data["text"]
        return


class Unit(object):

    def __init__(self, data: dict):
        self.code: int = 0
        self.value: str = ""

        check = check_dict(data, ["code", "value"])
        if check is False:
            raise ValueError("Invalid unit code: {0:s}".format(str(data)))

        self.code = data["code"]
        self.value = data["value"]
        return
