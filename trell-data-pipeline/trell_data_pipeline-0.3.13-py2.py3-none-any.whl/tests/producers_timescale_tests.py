from datetime import datetime
import asyncio
import pytest

from pipeline.producers.timescale import _map_value, _map_values


@pytest.mark.asyncio
async def test_map_value():
    epoch_to_datetime = await _map_value(value=1581412003, value_type='timestamptz')
    assert datetime(2020, 2, 11, 10, 6, 43) == epoch_to_datetime

    str_to_text = await _map_value(value="abc123", value_type='text')
    assert "'abc123'" == str_to_text


@pytest.mark.asyncio
async def test_map_values():
    values = [
        (25.1, 'double'),
        ('abc123', 'text'),
        (1581412003, 'timestamptz')
    ]
    res = await _map_values(values=values)
    assert datetime(2020, 2, 11, 10, 6, 43) == epoch_to_datetime
