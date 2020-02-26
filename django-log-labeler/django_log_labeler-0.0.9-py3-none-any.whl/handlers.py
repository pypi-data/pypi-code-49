import logging
import structlog

class StructlogRawMessageHandler(logging.StreamHandler):
    level = logging.DEBUG
    filters = []
    lock = None
    _name = "StructlogRawMessageHandler"

    def __init__(self):
        self._log = structlog.get_logger()

    def emit(self, record):
        self._log.log(record.levelno, record.msg, name=record.name)
