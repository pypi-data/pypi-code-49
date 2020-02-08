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
from typing import List

from easyb.definitions import Length


class Command(object):

    def call(self, message) -> bool:
        check = self._func_call(message)
        return check

    def __init__(self, **kwargs):
        self.number = 0
        self.address = 1

        self.name: str = ""
        self.code: int = 0
        self.length: Length = Length.Byte3
        self.param: List[int] = []
        self._func_call = None

        item = kwargs.get("name", "")
        if item is not None:
            self.name = item

        item = kwargs.get("address", None)
        if item is not None:
            self.address = item

        item = kwargs.get("number", None)
        if item is not None:
            self.number = item

        item = kwargs.get("code", 0)
        if item is not None:
            self.code = item

        item = kwargs.get("length", Length.Byte3)
        if item is not None:
            self.length = item

        item = kwargs.get("param", [])
        if item is not None:
            self.param = item

        item = kwargs.get("func_call", None)
        if item is not None:
            self._func_call = item
        return
