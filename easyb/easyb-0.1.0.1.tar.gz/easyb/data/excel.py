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

import os
import easyb
from typing import Any

from easyb.data.base import Storage, Type, Collection
import xlsxwriter

__all__ = [
    "ExcelStorage"
]


class ExcelStorage(Storage):

    # noinspection PyTypeChecker
    def __init__(self, data: Collection):
        self.workbook: xlsxwriter.Workbook = None
        self.info_sheet: xlsxwriter.workbook.Worksheet = None
        self.data_sheet: xlsxwriter.workbook.Worksheet = None
        self.row: int = 0

        Storage.__init__(self, "EXCEL", data)
        return

    def _prepare(self):

        self.data.filename = os.path.abspath(os.path.normpath(self.data.filename + ".xlsx"))
        easyb.log.inform(self.name, "Open {0:s}".format(self.data.filename))
        self.workbook = xlsxwriter.Workbook(self.data.filename, {'constant_memory': True})
        self.info_sheet = self.workbook.add_worksheet("Information")
        self.data_sheet = self.workbook.add_worksheet("Data")
        return

    def _create_header(self):
        cell_format = self.workbook.add_format()
        cell_format.set_bottom(5)
        cell_format.set_font_name("Arial")
        cell_format.set_font_size(10)
        cell_format.set_bold()

        for column in self.data.columns:
            self.data_sheet.write_string(self.row, column.index, column.description, cell_format)

        self.data_sheet.freeze_panes(1, 0)
        self.row += 1
        return

    @staticmethod
    def _get_writer(sheet: xlsxwriter.workbook.Worksheet, data_type: Type) -> Any:
        writer = None
        if data_type is Type.datetime:
            writer = sheet.write_datetime

        if data_type is Type.float:
            writer = sheet.write_number

        if data_type is Type.integer:
            writer = sheet.write_number

        if data_type is Type.string:
            writer = sheet.write_string

        if data_type is Type.bool:
            writer = sheet.write_boolean

        if writer is None:  # pragma: no cover
            raise ValueError("Unknown type: {0:s}".format(data_type.name))

        return writer

    def _write_cell(self, row: int, column: int, data_type: Type, value: Any, writer: Any):
        cell_format = self.workbook.add_format()
        cell_format.set_font_name("Arial")
        cell_format.set_font_size(10)

        if data_type is Type.datetime:
            cell_format.set_num_format('hh:mm:ss')

        if data_type is Type.float:
            cell_format.set_num_format('0.00')

        writer(row, column, value, cell_format)
        return

    def _write_data(self):
        for row in self.data.rows:

            for column in self.data.columns:
                writer = self._get_writer(self.data_sheet, column.type)
                value = getattr(row, column.name)

                self._write_cell(self.row, column.index, column.type, value, writer)
            self.row += 1
        return

    def _write_infos(self):
        header = self.workbook.add_format()
        header.set_bottom(5)
        header.set_font_name("Arial")
        header.set_font_size(10)
        header.set_bold()

        value_text = self.workbook.add_format()
        value_text.set_font_name("Arial")
        value_text.set_font_size(10)
        value_text.set_bold()

        self.info_sheet.write_string(0, 0, "Name", header)
        self.info_sheet.write_string(0, 1, "Value", header)

        row = 1

        for item in self.data.infos:
            writer = self._get_writer(self.info_sheet, item.type)
            self.info_sheet.write_string(row, 0, item.name, value_text)
            self._write_cell(row, 1, item.type, item.value, writer)
            row += 1

        row += 1

        for item in self.data.status:
            writer = self._get_writer(self.info_sheet, item.type)
            self.info_sheet.write_string(row, 0, item.name, value_text)
            self._write_cell(row, 1, item.type, item.value, writer)
            row += 1
        return

    def _close(self):
        easyb.log.inform(self.name, "Write number of rows {0:d}".format(self.row))
        self.workbook.close()
        return

    def store(self) -> bool:
        self._prepare()
        self._write_infos()
        self._create_header()
        self._write_data()
        self._close()
        return True
