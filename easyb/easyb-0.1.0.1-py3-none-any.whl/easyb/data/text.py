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

import os
import easyb

from easyb.data.base import Storage, Collection, convert_data
from io import FileIO

__all__ = [
    "TextStorage"
]


class TextStorage(Storage):

    # noinspection PyTypeChecker
    def __init__(self, data: Collection):
        self.file: FileIO = None
        Storage.__init__(self, "TEXT", data)
        return

    def _prepare(self) -> bool:
        filename = os.path.abspath(os.path.normpath(self.data.filename + ".csv"))
        easyb.log.inform(self.name, "Open {0:s}".format(filename))
        try:
            self.file = open(filename, mode="w")
        except OSError as e:
            easyb.log.exception(e)
            return False
        return True

    def _write_info(self):

        self.file.write("Name\tValue\n")

        for item in self.data.infos:
            line = "{0:s}\t{1:s}\n".format(item.name, str(item))
            self.file.write(line)

        self.file.write("\n")
        return

    def _write_status(self):

        self.file.write("State\tValue\n")

        for item in self.data.status:
            line = "{0:s}\t{1:s}\n".format(item.name, str(item))
            self.file.write(line)

        self.file.write("\n")
        return

    def _write_data(self):

        line = ""
        for column in self.data.columns:
            if line == "":
                line = column.description
            else:
                line += "\t{0:s}".format(column.description)

        line += "\n"
        self.file.write(line)

        for row in self.data.rows:

            line = ""
            for column in self.data.columns:
                data = getattr(row, column.name)
                value = convert_data(column.type, data)

                if line == "":
                    line = value
                else:
                    line += "\t{0:s}".format(value)

            line += "\n"
            self.file.write(line)

        return

    def store(self) -> bool:
        check = self._prepare()
        if check is False:
            return False

        self._write_info()
        self._write_status()
        self._write_data()

        if self.file is not None:
            self.file.close()
        return True
