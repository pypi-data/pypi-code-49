# coding=utf-8
from __future__ import absolute_import, print_function

import logging
import logging.handlers
import os
import platform
import time

import suanpan
from suanpan import path, g
from suanpan.utils import functional


class Formatter(logging.Formatter):

    converter = time.gmtime

    def __init__(
        self,
        fmt="%(asctime)s.%(msecs)06d :: %(levelname)-10s :: %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    ):
        super(Formatter, self).__init__(fmt=fmt, datefmt=datefmt)


class Logger(logging.Logger):

    FORMATTER = Formatter()
    STREAM_LOG_LEVEL = logging.DEBUG
    FILE_LOG_LEVEL = logging.DEBUG
    LOG_FILE_MAX_SIZE = 1024 * 1024 * 1024
    BACKUP_COUNT = 5
    LOG_PATH = "logs"
    LOG_FILE = None

    def __init__(self, name="suanpan"):
        super(Logger, self).__init__(name=name)
        self.addStreamHandler(level=logging.DEBUG if g.debug else logging.INFO)
        # self.addFileHandler()

    def addStreamHandler(self, level=STREAM_LOG_LEVEL, formatter=FORMATTER):
        streamHandler = logging.StreamHandler()
        streamHandler.setLevel(level)
        streamHandler.setFormatter(formatter)
        self.addHandler(streamHandler)
        return streamHandler

    def addFileHandler(
        self,
        level=FILE_LOG_LEVEL,
        formatter=FORMATTER,
        logPath=LOG_PATH,
        logFile=LOG_FILE,
        logFileMaxSize=LOG_FILE_MAX_SIZE,
        backupCount=BACKUP_COUNT,
    ):
        logFile = logFile or f"{self.name}.log"
        logFilePath = os.path.join(logPath, logFile)
        path.mkdirs(logFilePath, parent=True)
        fileHandler = logging.handlers.RotatingFileHandler(
            logFilePath, maxBytes=logFileMaxSize, backupCount=backupCount
        )
        fileHandler.setLevel(level)
        fileHandler.setFormatter(formatter)
        self.addHandler(fileHandler)
        return fileHandler

    @functional.onlyonce
    def logDebugInfo(self):
        self.logPythonVersion()
        self.logSdkVersion()

    @functional.onlyonce
    def logSdkVersion(self):
        self.debug(f"Suanpan SDK (ver: {suanpan.__version__})")

    @functional.onlyonce
    def logPythonVersion(self):
        self.debug(f"Python (ver: {platform.python_version()})")


class LoggerProxy(object):
    def __init__(self, loggerOrName):
        self.setLogger(loggerOrName)

    def __getattr__(self, key):
        return getattr(self.logger, key)

    def setLogger(self, loggerOrName):
        self.logger = (
            loggerOrName if isinstance(loggerOrName, Logger) else Logger(loggerOrName)
        )


rootLogger = Logger("suanpan")
logger = LoggerProxy(rootLogger)
