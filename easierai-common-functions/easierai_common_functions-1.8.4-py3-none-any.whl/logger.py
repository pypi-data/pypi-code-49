import logging
from logging.handlers import TimedRotatingFileHandler
import datetime as dt
import time
import inspect
import os
import sys
from copy import copy

import logstash

import json

import common_functions.constants as constants

class ConsoleFormatter(logging.Formatter):
    
    def __init__(self):
        fmt = '%(asctime)s [%(levelname)-7s - %(filename)s] %(message)s %(add_info)s'
        datefmt = '%Y-%m-%d %H:%M:%S'
        logging.Formatter.__init__(self, fmt, datefmt)

    def format(self, record):
        record_copy = copy(record)
        record_copy.msg = record.msg
        record_copy.filename = record.source_file
        if hasattr(record, 'additional_info'):
            record_copy.add_info = '-> '+ str(record.additional_info)
        else:
            record_copy.add_info = ''
        return super().format(record_copy)

class Logger:

    def __init__(self, service, source_file):
        self.service = service
        self.source_file = source_file
        logstash_host = os.getenv('LOGSTASH_HOST')
        logstash_port = os.getenv('LOGSTASH_PORT')
        self.init_log_file(source_file, logstash_host, logstash_port)

    def lineno(self):
        f = inspect.currentframe()
        filename = os.path.normcase(f.f_code.co_filename)
        # Traverse the stack until the function has been called by a different file, then get that line number
        while filename == __file__:
            f = f.f_back
            filename = os.path.normcase(f.f_code.co_filename)

        return f.f_lineno

    def init_log_file(self, source_file, logstash_host=None, logstash_port=None):
        streamHandler = logging.StreamHandler(sys.stdout)
        streamHandler.setFormatter(ConsoleFormatter())
        self.logger = logging.getLogger(source_file)
        if logstash_host and logstash_port:
            self.logger.addHandler(logstash.TCPLogstashHandler(logstash_host, int(logstash_port), version=1))
        self.logger.addHandler(streamHandler)
        # By default, level is ERROR. If not recognized, level is also ERROR
        logging_level = os.getenv('LOGGING_LEVEL', 'ERROR').upper()
        if logging_level == 'WARN' or logging_level == 'WARNING':
            self.logger.setLevel(logging.WARNING)
        elif logging_level == 'DEBUG':
            self.logger.setLevel(logging.DEBUG)
        elif logging_level == 'INFO':
            self.logger.setLevel(logging.INFO)
        else:
            self.logger.setLevel(logging.ERROR)
        
    def generate_extra_doc(self, level, additional_info=None):
        doc = {
            'service': self.service,
            'source_file': self.source_file + ':' + str(self.lineno()),
            '@timestamp': dt.datetime.now().isoformat(),
            'debug_level': level
        }
        if additional_info:
            doc['additional_info'] = additional_info
        return doc

    def debug(self, message, additional_info=None):
        self.logger.debug(message, extra=self.generate_extra_doc(constants.DEBUG, additional_info))

    def info(self, message, additional_info=None):
        self.logger.info(message, extra=self.generate_extra_doc(constants.INFO, additional_info))

    def warning(self, message, additional_info=None):
        self.logger.warning(message, extra=self.generate_extra_doc(constants.WARNING, additional_info))

    def error(self, message, additional_info=None):
        self.logger.error(message, extra=self.generate_extra_doc(constants.ERROR, additional_info))

    def perf(self, message, additional_info=None):
        self.logger.info(message, extra=self.generate_extra_doc(constants.PERFORMANCE, additional_info))