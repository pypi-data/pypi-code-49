#!/usr/bin/env python3

""" Derived from the following, but changed by rsyslog_pseudonymizer project:
        https://github.com/rsyslog/rsyslog/blob/master/plugins/external/skeletons/python/plugin.py
        A skeleton for a python rsyslog output plugin
        Copyright (C) 2014 by Adiscon GmbH
        This file is part of rsyslog.
        Licensed under the Apache License, Version 2.0 (the "License");
        you may not use this file except in compliance with the License.
        You may obtain a copy of the License at

                http://www.apache.org/licenses/LICENSE-2.0
                -or-
                see COPYING.ASL20 in the source distribution

        Unless required by applicable law or agreed to in writing, software
        distributed under the License is distributed on an "AS IS" BASIS,
        WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
        See the License for the specific language governing permissions and
        limitations under the License.
"""

import sys
import json

from .pseudonymizer.PseudonymReplacer import (
    PseudonymReplacer,
    get_default_identifier_types
)

def main():
    keepRunning = 1
    while keepRunning == 1:
        msg = sys.stdin.readline()
        if msg:
            msg = msg[:-1]  # remove LF
            onReceive(msg)
            sys.stdout.flush()  # very important, Python buffers far too much!
        else:  # an empty line means stdin has been closed
            keepRunning = 0
    sys.stdout.flush()  # very important, Python buffers far too much!

pseudonym_replacer = PseudonymReplacer(get_default_identifier_types())

def onReceive(encoded):
    """This is the entry point where actual work needs to be done. It receives
       the messge from rsyslog and now needs to examine it, do any processing
       necessary. The to-be-modified properties (one or many) need to be pushed
       back to stdout, in JSON format, with no interim line breaks and a line
       break at the end of the JSON. If no field is to be modified, empty
       json ("{}") needs to be emitted.
       Note that no batching takes place (contrary to the output module
       skeleton) and so each message needs to be fully processed (rsyslog will
       wait for the reply before the next message is pushed to this module).
    """
    msg = json.loads(encoded)["msg"]
    try:
        processed = pseudonym_replacer.pseudonymize_text(msg)
    except Exception as e:
        processed = "[Pseudonymization error: " + \
            str(e).replace("\\", "\\\\").replace("\n", "\\n") + "] " + encoded
    print(json.dumps({'msg': processed}))

if __name__ == "__main__":
    main()
