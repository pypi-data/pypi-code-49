
from enum import Enum
import io
import logging
from pathlib import Path
from typing import List, Optional

__all__ = ['Level', 'Logger']


Level =  Enum('Level', 'DEBUG INFO WARNING ERROR CRITICAL')


def level_to_logging(level: Level) -> int:
    return {
        Level.DEBUG: logging.DEBUG,
        Level.INFO: logging.INFO,
        Level.WARNING: logging.WARNING,
        Level.ERROR: logging.ERROR,
        Level.CRITICAL: logging.CRITICAL,
    }[level]


class FileHandlerWithExtras(logging.FileHandler):

    def __init__(self, extras, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.extras = extras

    def add_global(self, key: str, value: str):
        self.extras[key] = value

    def emit(self, record):
        for k, v in self.extras.items():
            record.__dict__[k] = v
        return super().emit(record)


class StreamHandlerWithExtras(logging.StreamHandler):

    def __init__(self, extras, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.extras = extras

    def add_global(self, key: str, value: str):
        self.extras[key] = value

    def emit(self, record):
        for k, v in self.extras.items():
            record.__dict__[k] = v
        return super().emit(record)


class Logger:

    def __init__(
        self,
        level: Level = Level.DEBUG,
        name: Optional[str] = None,
        log_format: Optional[str] = None,
        date_format: Optional[str] = None,
    ):
        self.level = level
        self.name = name
        self._logger = logging.getLogger(name)
        self._logger.setLevel(level_to_logging(level))
        l = log_format or '%(asctime)s:%(levelname)s:%(name)s:%(message)s'
        d = date_format or '%Y-%m-%d %H:%M:%S %z'
        f = logging.Formatter(l, datefmt=d)
        self.log_formats = {'default': l}
        self.date_formats = {'default': d}
        self.formatters = {}
        self.stream_handlers = {}
        self.file_handlers = {}
        self.create_formatter('simple', ' %(levelname)-8s %(message)s')
        self.create_formatter('default', l)
        self.extras = {}

    def add_global(self, key: str, value: str):
        self.extras[key] = value
        for handler in self.file_handlers.values():
            handler.add_global(key, value)
        for handler in self.stream_handlers.values():
            handler.add_global(key, value)

    def create_formatter(self, name: str, log_format: str, date_format: Optional[str] = None) -> logging.Formatter:
        d = date_format or self.date_formats['default']
        f = logging.Formatter(log_format, datefmt=d)
        self.formatters[name] = f
        return f

    def log_to_file(
        self,
        filename: Path,
        mode: str = 'a',
        encoding: Optional[str] = None,
        level: Optional[Level] = None,
        log_format: Optional[str] = None,
        date_format: Optional[str] = None,
    ) -> None:
        if filename in self.file_handlers:
            return
        lf = log_format or self.log_formats['default']
        df = date_format or self.date_formats['default']
        fh = FileHandlerWithExtras(self.extras, filename, mode, encoding)
        fh.setLevel(level_to_logging(level or self.level))
        fh.setFormatter(logging.Formatter(lf, datefmt=df))
        self._logger.addHandler(fh)
        self.file_handlers[filename] = fh
        return

    def stop_logging_to_file(self, filename: str):
        raise NotImplementedError('Have not completed yet')

    def log_to_stream(
        self,
        stream: Optional[io.IOBase] = None,
        level: Optional[Level] = None,
        log_format: Optional[str] = None,
    ) -> None:
        if stream in self.stream_handlers:
            return
        sh = StreamHandlerWithExtras(self.extras, stream)
        sh.setLevel(level_to_logging(level or self.level))
        sh.setFormatter(logging.Formatter(log_format) if log_format else self.formatters['simple'])
        self._logger.addHandler(sh)
        self.stream_handlers[stream] = sh
        return
    log_to_console = log_to_stream

    def stop_logging_to_stream(self, stream: Optional[io.IOBase] = None):
        raise NotImplementedError('Have not completed yet')

    def info(self, msg, *args):
        return self._logger.info(msg, *args)

    def debug(self, msg, *args):
        return self._logger.debug(msg, *args)

    def warning(self, msg, *args):
        return self._logger.warning(msg, *args)

    def critical(self, msg, *args):
        return self._logger.critical(msg, *args)

    def error(self, msg, *args):
        return self._logger.error(msg, *args)
