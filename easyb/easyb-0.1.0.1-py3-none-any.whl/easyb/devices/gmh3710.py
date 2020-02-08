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

from datetime import datetime

from easyb.data.base import Type, Info
from easyb.definitions import Length
from easyb.command import Command
from easyb.message import Message
from easyb.device import Device
from easyb.bit import Value, decode_u16, decode_u32

__all__ = [
    "GMH3710"
]

name = "GMH 3710"
device = "GMH3710"


class GMH3710(Device):

    def __init__(self, **kwargs):
        self.min_value: float = 0.0
        self.max_value: float = 0.0
        self.id_number: int = 0
        self.unit: str = ""

        # noinspection PyTypeChecker
        self.start_measure: datetime = None

        # noinspection PyTypeChecker
        self.end_measure: datetime = None

        Device.__init__(self, name="GMH 3710", **kwargs)

        self.data.add_column("value", "Temperature", Type.float)
        self.data.add_column("error", "Error", Type.string)
        return

    def messwert_lesen(self, message: Message) -> bool:
        data = message.stream.data
        bitio = Value(data=data)

        check = bitio.decode32()

        if check is False:
            easyb.log.warn(self.name, "Error: {0:s}".format(bitio.error.text))
        else:
            now = datetime.now()
            debug = "{0:s}: {1:.2f}".format(now.strftime("%Y-%m-%d %H:%M:%S"), bitio.value)
            easyb.log.inform(self.name, debug)
        return check

    def systemstatus_lesen(self, message: Message) -> bool:
        data = message.stream.data

        value = decode_u16(data[3], data[4])

        counter = self.set_status(value)

        n = 0
        for item in self.device_status:
            if item.is_set is False:
                n += 1
                continue
            line = "{0:d}: {2:s} (0x{1:04x})".format(n, item.bit, item.text)
            easyb.log.warn(self.name, line)
            n += 1

        if counter == 0:
            easyb.log.inform("Systemstatus", "Nothing to report!")
        return True

    def minwert_lesen(self, message: Message) -> bool:
        data = message.stream.data
        bitio = Value(data=data)

        check = bitio.decode32()

        if check is False:
            easyb.log.warn(self.name, "Error: {0:s}".format(bitio.error.text))
        else:
            easyb.log.inform("Min. value", str(bitio.value))
            self.min_value = bitio.value
        return check

    def maxwert_lesen(self, message: Message) -> bool:
        data = message.stream.data
        bitio = Value(data=data)

        check = bitio.decode32()

        if check is False:
            easyb.log.warn(self.name, "Error: {0:s}".format(bitio.error.text))
        else:
            easyb.log.inform("Max. value", str(bitio.value))
            self.max_value = bitio.value
        return check

    def id_nummer_lesen(self, message: Message) -> bool:
        data = message.stream.data
        input1 = decode_u16(data[3], data[4])
        input2 = decode_u16(data[6], data[7])
        value = decode_u32(input1, input2)

        self.id_number = value

        easyb.log.inform("ID", "ID: {0:x}".format(self.id_number))
        return True

    # noinspection PyUnusedLocal
    def anzeige_einheit_lesen(self, message: Message) -> bool:
        data = message.stream.data
        bitio = Value()

        value = decode_u16(data[6], data[7])

        unit = easyb.conf.get_unit(value)
        if unit is None:
            easyb.log.error("Unit is unknown: {0:d}".format(value))
            return False

        self.unit = unit.value

        column = self.data.get_column("value")
        column.description = "Temperature [{0:s}]".format(self.unit)

        logging = "{0:d}: {1:s}".format(value, self.unit)
        easyb.log.inform("Unit", logging)
        return True

    def init_commands(self):

        command = Command(name="Messwert lesen", code=0, func_call=self.messwert_lesen)
        self.add_command(command)

        command = Command(name="Systemstatus lesen", code=3, func_call=self.systemstatus_lesen)
        self.add_command(command)

        command = Command(name="Minwert lesen", code=6, func_call=self.minwert_lesen)
        self.add_command(command)

        command = Command(name="Maxwert lesen", code=7, func_call=self.maxwert_lesen)
        self.add_command(command)

        command = Command(name="ID-Nummer lesen", code=12, func_call=self.id_nummer_lesen)
        self.add_command(command)

        command = Command(name="Min. Messbereich lesen", code=15, length=Length.Byte6,
                          param=[176, 0], func_call=self.default_command)
        self.add_command(command)

        command = Command(name="Max. Messbereich lesen", code=15, length=Length.Byte6,
                          param=[177, 0], func_call=self.default_command)
        self.add_command(command)

        command = Command(name="Messbereich Einheit lesen", code=15, length=Length.Byte6,
                          param=[178, 0], func_call=self.default_command)
        self.add_command(command)

        command = Command(name="Messbereichs Messart lesen", code=15, length=Length.Byte6,
                          param=[180, 0], func_call=self.default_command)
        self.add_command(command)

        command = Command(name="Anzeige Messart lesen", code=15, length=Length.Byte6,
                          param=[199, 0], func_call=self.default_command)
        self.add_command(command)

        command = Command(name="Min. Anteigebereich lesen", code=15, length=Length.Byte6,
                          param=[200, 0], func_call=self.default_command)
        self.add_command(command)

        command = Command(name="Max. Anteigebereich lesen", code=15, length=Length.Byte6,
                          param=[201, 0], func_call=self.default_command)
        self.add_command(command)

        command = Command(name="Anzeige Einheit lesen", code=15, length=Length.Byte6,
                          param=[202, 0], func_call=self.anzeige_einheit_lesen)
        self.add_command(command)

        command = Command(name="Kanalzahl lesen", code=15, length=Length.Byte6,
                          param=[208, 0], func_call=self.default_command)
        self.add_command(command)

        command = Command(name="Steigungskorrektur lesen", code=15, length=Length.Byte6,
                          param=[214, 0], func_call=self.default_command)
        self.add_command(command)

        command = Command(name="Offset lesen", code=15, length=Length.Byte6,
                          param=[216, 0], func_call=self.default_command)
        self.add_command(command)

        command = Command(name="Abschaltverzoegerung lesen", code=15, length=Length.Byte6,
                          param=[222, 0], func_call=self.default_command)
        self.add_command(command)

        command = Command(name="Programmkennung lesen", code=15, length=Length.Byte6,
                          param=[254, 0], func_call=self.default_command)
        self.add_command(command)
        return

    def prepare(self) -> bool:
        self.start_measure = datetime.now()

        check = self.run_command(1)
        if check is False:
            return False

        status = self.get_status()
        if len(status) != 0:
            for item in status:
                easyb.log.warn("STATUS", item.text)
            return False

        check = self.run_command(4)
        if check is False:
            return False

        check = self.run_command(12)
        if check is False:
            return False
        return True

    def run(self) -> bool:
        command = self.get_command(0)

        message = self.execute(command)
        if message is None:
            return False

        data = message.stream.data
        bitio = Value(data=data)

        check = bitio.decode32()

        row = self.create_row()

        if check is False:
            easyb.log.warn(self.name, "Error: {0:s}".format(bitio.error.text))
            row.value = 0.0
            row.error = bitio.error.text
        else:
            row.value = bitio.value
            row.error = ""
            debug = "{0:06d} {1:s}: {2:.2f}".format(self.interval_counter, row.datetime.strftime("%H:%M:%S"), row.value)
            easyb.log.inform(self.name, debug)
        return check

    def close(self) -> bool:
        self.end_measure = datetime.now()

        check = self.run_command(1)
        if check is False:
            return False

        check = self.run_command(2)
        if check is False:
            return False

        check = self.run_command(3)
        if check is False:
            return False

        info = Info("Start", Type.datetime, self.start_measure)
        self.data.infos.append(info)

        info = Info("End", Type.datetime, self.end_measure)
        self.data.infos.append(info)

        delta = self.end_measure - self.start_measure

        info = Info("Duration", Type.datetime, delta)
        self.data.infos.append(info)

        info = Info("ID", Type.string, "{0:x}".format(self.id_number))
        self.data.infos.append(info)

        info = Info("Einheit", Type.string, self.unit)
        self.data.infos.append(info)

        _name = "Minwert [{0:s}]".format(self.unit)
        info = Info(_name, Type.float, self.min_value)
        self.data.infos.append(info)

        _name = "Maxwert [{0:s}]".format(self.unit)
        info = Info(_name, Type.float, self.max_value)
        self.data.infos.append(info)

        for item in self.device_status:
            info = Info(item.text, Type.bool, item.is_set)
            self.data.status.append(info)
        return True
