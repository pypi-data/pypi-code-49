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
import sys
import easyb

from bbutil.utils import full_path

from easyb.console import Console

if __name__ == '__main__':

    easyb.log.setup(app="easyb-tool", level=2)

    console = easyb.log.get_writer("console")
    fileio = easyb.log.get_writer("file")
    filename = full_path("{0:s}/run-tests.log".format(os.getcwd()))

    console.setup(text_space=15, error_index=["ERROR", "EXCEPTION"])
    fileio.setup(text_space=15, error_index=["ERROR", "EXCEPTION"], filename=filename)
    easyb.log.register(console)
    easyb.log.register(fileio)

    easyb.log.open()

    main = Console()

    if main.prepare() is False:
        sys.exit(1)

    if main.run() is False:
        sys.exit(1)

    if main.close() is False:
        sys.exit(1)

    sys.exit(0)
