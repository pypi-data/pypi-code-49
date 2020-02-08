#!/usr/bin/python3
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

import abc

from typing import List, Any

from enum import Enum
from abc import ABCMeta

__all__ = [
    "Type",
    "FormatInfo",
    "Column",
    "convert_data",
    "Info",
    "Row",
    "Collection",
    "Storage"
]


class Type(Enum):

    datetime = 0
    integer = 1
    float = 2
    string = 3
    bool = 4


class FormatInfo(object):

    def __init__(self, name: str = "", path: str = "", classname: str = ""):
        self.name = name
        self.path = path
        self.classname = classname
        return


class Column(object):

    def __init__(self, index: int, name: str, desc: str, column_type: Type):
        self.index: int = index
        self.name: str = name
        self.description: str = desc
        self.type: Type = column_type
        return


def convert_data(data_type: Type, data: Any) -> Any:
    value = data

    if data_type is Type.bool:
        if data is True:
            value = "True"
        else:
            value = "False"

    if data_type is Type.float:
        value = "{0:.2f}".format(data)

    if data_type is Type.integer:
        value = str(data)

    if data_type is Type.datetime:
        value = "{0:s}".format(data.strftime("%H:%M:%S"))

    return value


class Info(object):

    def __repr__(self) -> str:
        value = convert_data(self.type, self.value)
        return value

    def __init__(self, name: str, data_type: Type, value: Any):
        self.name: str = name
        self.type: Type = data_type
        self.value: Any = value
        return


class Row(object):

    def __init__(self, keys, values):
        for (key, value) in zip(keys, values):
            self.__dict__[key] = value
        return


class Collection(object):

    def __init__(self):
        self.rows: List[Row] = []
        self.columns: List[Column] = []
        self.infos: List[Info] = []
        self.status: List[Info] = []
        self.filename: str = ""
        return


class Storage(metaclass=ABCMeta):

    def __init__(self, name: str, data: Collection):
        self.name: str = name
        self.data: Collection = data
        return

    @abc.abstractmethod
    def store(self) -> bool:  # pragma: no cover
        return True
