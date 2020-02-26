import logging

import wrapt

from scopeagent.tracer import tags
from . import run_once

logger = logging.getLogger(__name__)

NANOSECONDS_IN_SECOND = 1e9


@run_once
def patch(tracer):
    def wrapper(wrapped, instance, args, kwargs):
        result = wrapped(*args, **kwargs)
        active_span = tracer.active_span
        stats = instance.stats.stats
        active_span.set_tag(tags.TEST_TYPE, tags.BENCHMARK_TYPE)
        active_span.set_tag(tags.BENCHMARK_RUNS, stats.rounds)
        active_span.set_tag(tags.BENCHMARK_DURATION_MEAN, stats.mean * NANOSECONDS_IN_SECOND)
        active_span.set_tag(tags.BENCHMARK_DURATION_MIN, stats.min * NANOSECONDS_IN_SECOND)
        active_span.set_tag(tags.BENCHMARK_DURATION_MAX, stats.max * NANOSECONDS_IN_SECOND)
        active_span.set_tag(tags.BENCHMARK_DURATION_STDDEV, stats.stddev * NANOSECONDS_IN_SECOND)
        active_span.set_tag(tags.BENCHMARK_DURATION_MEDIAN, stats.median * NANOSECONDS_IN_SECOND)
        active_span.set_tag(tags.BENCHMARK_DURATION_Q1, stats.q1 * NANOSECONDS_IN_SECOND)
        active_span.set_tag(tags.BENCHMARK_DURATION_Q3, stats.q3 * NANOSECONDS_IN_SECOND)

        return result

    try:
        logger.debug("patching module=pytest_benchmark.fixture.BenchmarkFixture name=_raw")
        # Function being wrapped
        # https://github.com/ionelmc/pytest-benchmark/blob/c91293b94e3b64a4fd7d89dd35e4d2b3ebc3d190/src/pytest_benchmark/fixture.py#L145
        wrapt.wrap_function_wrapper('pytest_benchmark.fixture', 'BenchmarkFixture._raw', wrapper)
    except ImportError:
        logger.debug("module not found module=pytest_benchmark.fixture.BenchmarkFixture")
