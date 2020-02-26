import asyncio
import inspect

import pytest
from _pytest.config import hookimpl


@pytest.yield_fixture
def event_loop():
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@hookimpl(tryfirst=True)
def pytest_pyfunc_call(pyfuncitem):
    testfunction = pyfuncitem.obj
    is_coroutine = False
    if inspect.iscoroutinefunction(testfunction):
        is_coroutine = True
    funcargs = pyfuncitem.funcargs
    testargs = {arg: funcargs[arg] for arg in pyfuncitem._fixtureinfo.argnames}
    result = testfunction(**testargs)
    if is_coroutine:
        asyncio.run(result)
    # if hasattr(result, "__await__") or hasattr(result, "__aiter__"):
    #     async_warn()
    return True
