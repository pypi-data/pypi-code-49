"""
Functions to measure times.
"""
import contextlib
import time
import typing


@contextlib.contextmanager
def timeit(returned_time: typing.List[float]) -> None:
    """ Context manager to measure elapsed time to execute code it encloses.

    To pass back elapsed time, and empty list should be entered as
    *returned_time* parameter. After context manager ends, elapsed time
    is going to be in its first position.

    Example::

        import time
        import test_common.benchmark.timing as timing

        elapsed_time = []
        with timing.timeit(elapsed_time):
            time.sleep(2)
        print(f"Elapsed time was: {elapsed_time[0]}")


    :param returned_time: Empty list to pass back elapsed time in its first
     element.
    """
    start_time = time.time()
    yield
    end_time = time.time()
    elapsed_time = end_time - start_time
    returned_time.append(elapsed_time)
