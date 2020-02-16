"""
Test for timing module.
"""
import pytest
import time

import test_common.benchmark.timing as timing


@pytest.mark.timing
def test_timeit():
    TIME_TO_SLEEP = 1  # seconds
    elapsed_time = []
    with timing.timeit(elapsed_time):
        time.sleep(TIME_TO_SLEEP)
    assert TIME_TO_SLEEP <= elapsed_time[0]
