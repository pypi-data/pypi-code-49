import logging
from contextlib import contextmanager
from typing import Any, Callable, Iterable, Iterator, List

import ray

from prefect import context
from prefect.engine.executors.base import Executor


class RayExecutor(Executor):
    """
    An executor that runs all functions using the `dask.distributed` scheduler on
    a (possibly local) dask cluster.  If you already have one running, simply provide the
    address of the scheduler upon initialization; otherwise, one will be created
    (and subsequently torn down) within the `start()` contextmanager.

    Note that if you have tasks with tags of the form `"dask-resource:KEY=NUM"` they will be parsed
    and passed as [Worker Resources](https://distributed.dask.org/en/latest/resources.html) of the form
    `{"KEY": float(NUM)}` to the Dask Scheduler.

    Args:
        - address (string, optional): address of a currently running dask
            scheduler; if one is not provided, a `distributed.LocalCluster()` will be created in `executor.start()`.
            Defaults to `None`
        - local_processes (bool, optional): whether to use multiprocessing or not
            (computations will still be multithreaded). Ignored if address is provided.
            Defaults to `False`.
        - debug (bool, optional): whether to operate in debug mode; `debug=True`
            will produce many additional dask logs. Defaults to the `debug` value in your Prefect configuration
        - **kwargs (dict, optional): additional kwargs to be passed to the
            `dask.distributed.Client` upon initialization (e.g., `n_workers`)
    """

    def __init__(self, **kwargs: Any):
        self.kwargs = kwargs
        super().__init__()

    @contextmanager
    def start(self) -> Iterator[None]:
        """
        Context manager for initializing execution.

        Creates a `dask.distributed.Client` and yields it.
        """
        ray.init(**self.kwargs)
        yield
        ray.shutdown()

    def submit(self, fn: Callable, *args: Any, **kwargs: Any) -> Any:
        """
        Submit a function to the executor for execution. Returns a Future object.

        Args:
            - fn (Callable): function that is being submitted for execution
            - *args (Any): arguments to be passed to `fn`
            - **kwargs (Any): keyword arguments to be passed to `fn`

        Returns:
            - Future: a Future-like object that represents the computation of `fn(*args, **kwargs)`
        """

        try:
            future = ray.remote(fn).remote(*args, **kwargs)
        except Exception as exc:
            from IPython import embed

            embed()
        return future

    def map(self, fn: Callable, *args: Any, **kwargs: Any) -> List[Any]:
        """
        Submit a function to be mapped over its iterable arguments.

        Args:
            - fn (Callable): function that is being submitted for execution
            - *args (Any): arguments that the function will be mapped over
            - **kwargs (Any): additional keyword arguments that will be passed to the Dask Client

        Returns:
            - List[Future]: a list of Future-like objects that represent each computation of
                fn(*a), where a = zip(*args)[i]

        """
        results = []
        for args_i in zip(*args):
            results.append(self.submit(fn, *args_i))
        return results

    def wait(self, futures: Any) -> Any:
        """
        Resolves the Future objects to their values. Blocks until the computation is complete.

        Args:
            - futures (Any): single or iterable of future-like objects to compute

        Returns:
            - Any: an iterable of resolved futures with similar shape to the input
        """
        return ray.get(futures)
