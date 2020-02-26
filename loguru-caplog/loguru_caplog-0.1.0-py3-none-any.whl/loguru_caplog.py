# pylint: disable=unused-import, redefined-outer-name
import logging
from typing import Iterator

import pytest
from _pytest.logging import caplog  # noqa: F401
from _pytest.logging import LogCaptureFixture
from loguru import logger


@pytest.fixture
def loguru_caplog(
    caplog: Iterator[LogCaptureFixture],  # noqa: F811
) -> Iterator[LogCaptureFixture]:
    class PropogateHandler(logging.Handler):
        def emit(self, record: logging.LogRecord) -> None:
            logging.getLogger(record.name).handle(record)

    handler_id = logger.add(PropogateHandler(), format="{message}")
    yield caplog
    logger.remove(handler_id)
