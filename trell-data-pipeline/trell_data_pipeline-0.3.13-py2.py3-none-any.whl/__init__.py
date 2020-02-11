__version__ = '0.3.13'

import asyncio
from typing import Optional
import logging
import logging.handlers
from pathlib import Path
import sys
from datetime import datetime

from pipeline import settings


STOP = asyncio.Event()


class DebugOnlyFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.DEBUG


class FileFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        created = datetime.utcfromtimestamp(record.created)
        return created.strftime('%Y-%m-%d %H:%M:%S:%f')


def init_logging() -> None:
    console_formatter = logging.Formatter(
        fmt='{asctime:s} {name:42s} {levelname:8s} {message:s}',
        style='{',
    )
    file_formatter = FileFormatter(
        fmt='{asctime:s} {name:s} {levelname:s} {message:s}',
        style='{',
    )

    # root logger
    root = logging.getLogger()
    root.setLevel(settings.LOG_LEVEL)

    # console output
    stdout = logging.StreamHandler(stream=sys.stdout)
    stdout.setFormatter(console_formatter)
    stdout.setLevel(logging.DEBUG)
    root.addHandler(stdout)

    # log files
    if settings.LOG_DIR is not None:
        log_dir = Path(settings.LOG_DIR)

        # debug file
        debug_file = logging.handlers.RotatingFileHandler(
            filename=log_dir / 'trell-data-pipeline.debug.log',
            maxBytes=5 * 1000 * 1000,
            backupCount=2,
        )
        debug_file.setFormatter(file_formatter)
        debug_file.setLevel(logging.DEBUG)
        root.addHandler(debug_file)

        # info file
        info_file = logging.handlers.RotatingFileHandler(
            filename=log_dir / 'trell_lora_pipeline.info.log',
            maxBytes=5 * 1000 * 1000,
            backupCount=2,
        )
        info_file.setFormatter(file_formatter)
        info_file.setLevel(logging.INFO)
        root.addHandler(info_file)

    # disable asyncio debug log
    asyncio_logger = logging.getLogger('asyncio')
    asyncio_logger.setLevel(logging.WARNING)

    # disable gmqtt debug log
    gmqtt_logger = logging.getLogger('gmqtt')
    gmqtt_logger.setLevel(logging.WARNING)

    # disable aiokafka debug log
    aiokafka_logger = logging.getLogger('aiokafka')
    aiokafka_logger.setLevel(logging.WARNING)
