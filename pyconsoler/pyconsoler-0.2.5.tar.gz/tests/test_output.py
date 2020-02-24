import logging

import pytest

from pyconsoler.output import print_waiting_countdown

_LOGGER = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_print_waiting_countdown():
    await print_waiting_countdown(4)
