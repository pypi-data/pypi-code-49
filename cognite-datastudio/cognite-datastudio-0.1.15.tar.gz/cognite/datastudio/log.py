import logging
import os
import sys


"""Logging module to datastudio
-------------------------------
Importing this module will tag a call id from a cognite function
onto any print statement or error/exception so that it can be fetched by
the logs. This module can be attached to any handler.py file by default
to enable us to fetch logs by call id."""


class StreamToLogger(object):
    """
    Fake file-like stream object that redirects writes to a logger instance.
    """

    def __init__(self, logger, log_level=logging.INFO):
        self.call_id = os.environ.get("Http_X_Call_Id")
        self.logger = logger
        self.log_level = log_level
        self.linebuf = ""

    def write(self, buf):
        for line in buf.rstrip().splitlines():
            self.logger.log(self.log_level, f"Call ID:{self.call_id}: {line.rstrip()}")

    def flush(self):
        if self.log_level == logging.INFO or self.log_level == logging.WARNING:
            self.logger.log(self.log_level, sys.stdout)
        else:
            self.logger.log(self.log_level, sys.stderr)


logging.basicConfig(level=logging.DEBUG, format="%(levelname)s:%(name)s:%(message)s")

stdout_logger = logging.getLogger("STDOUT")
sl = StreamToLogger(stdout_logger, logging.INFO)
sys.stdout = sl

stderr_logger = logging.getLogger("STDERR")
sl = StreamToLogger(stderr_logger, logging.ERROR)
sys.stderr = sl
