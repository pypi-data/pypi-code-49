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

__all__ = [
    "data",
    "devices",
    "message",

    "bit",
    "command",
    "config",
    "console",
    "definitions",
    "device"
]


#: package name
__name__ = "easyb"

#: package author
__author__ = "Kai Raphahn"

#: email of package maintainer
__email__ = "kai.raphahn@laburec.de"

#: copyright year
__year__ = 2020

#: package copyright
__copyright__ = "Copyright (C) {0:d}, {1:s} <{2:s}>".format(__year__, __author__, __email__)

#: package description
__description__ = "Python tools for EASYBus Sensor modules from GMH Messtechnik GmbH"

#: package license
__license__ = "Apache License, Version 2.0"

#: package credits
__credits__ = [__author__]

#: version milestone
__milestone__ = 0

#: version major
__major__ = 1

#: version minor
__minor__ = 0

#: version patch
__patch__ = 1

#: package version
__version__ = "{0:d}.{1:d}.{2:d}.{3:d}".format(__milestone__, __major__, __minor__, __patch__)

#: package maintainer
__maintainer__ = __author__


from easyb.logging import SerialLogging
import easyb.config

log: SerialLogging = SerialLogging()
conf = easyb.config.Config()


def set_logging(new_log):
    global log
    log = new_log
