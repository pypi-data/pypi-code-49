#!/usr/bin/python3
# -*- coding: utf-8 -*-

from logging import Formatter

from datetime import datetime
import os
import sys
import json

class JsonFormatter(Formatter):
    """ Outputs log records in JSON format. """

    def __init__(self, attributes=None,
                 resolve_args=True, datefmt=None, style='%'):
        """ Construct a new JSON formatter.
        :param datefmt: Date format. See Python docs.

        :param style: Formatter style. See Python docs.

        :param resolve_args: Whether to inject `args` into `message`. Default
            is `True`. Setting to `False` will result in the json log entry
            to include both a `msg` and `args` item.
        """
        self.attributes = attributes
        self.resolve_args = resolve_args
        self.application = os.path.basename(sys.argv[0])
        super(JsonFormatter, self).__init__(datefmt=datefmt, style=style)

    def format(self, record):
        """ Format a record in JSON format.

        :param record: LogRecord to format.

        :return: String formatted as a json object.
        """
        # datetime.now().isoformat()
        # datetime.datetime.fromtimestamp(1347517370)
        log = {'time': datetime.fromtimestamp(record.created).isoformat(),
               'level': record.levelname,
               'application': self.application,
               'message': record.msg}
        return json.dumps(log)



