import asyncio
import contextlib


def create_task(coro):
	if not hasattr(asyncio, 'create_task'): # pragma: no cover
		return asyncio.get_event_loop().create_task(coro)
	return asyncio.create_task(coro)

def AsyncExitStack(*args, **kwargs):
	if not hasattr(contextlib, 'AsyncExitStack'): # pragma: no cover
		import async_exit_stack
		return async_exit_stack.AsyncExitStack(*args, **kwargs)
	return contextlib.AsyncExitStack(*args, **kwargs)
