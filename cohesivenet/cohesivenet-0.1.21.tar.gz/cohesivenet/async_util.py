import asyncio
import functools


def force_async(fn):
    """Turns a sync function to async function using threads

    Arguments:
        fn {function}

    Returns:
        function - awaitable function
    """
    from concurrent.futures import ThreadPoolExecutor

    pool = ThreadPoolExecutor()

    @functools.wraps(fn)
    def async_wrapper(*args, **kwargs):
        future = pool.submit(fn, *args, **kwargs)
        return asyncio.wrap_future(future)  # make it awaitable

    return async_wrapper


def run_parallel(*coroutines):
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(asyncio.gather(*coroutines))
    return results
