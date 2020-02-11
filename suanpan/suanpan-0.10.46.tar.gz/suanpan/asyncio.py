# coding=utf-8
from __future__ import absolute_import, print_function

import multiprocessing
import multiprocessing.dummy

from suanpan import utils
from suanpan.utils import pbar as spbar

WORKERS = multiprocessing.cpu_count()


class GlobalPool(object):
    def __init__(self, workers=WORKERS):
        super(GlobalPool, self).__init__()
        self._workers = workers

    @property
    def workers(self):
        return self._workers

    @workers.setter
    def workers(self, value):
        self._workers = value

    @utils.lazyproperty
    def threads(self):
        return Pool(thread=True, workers=self.workers)

    @utils.lazyproperty
    def processes(self):
        return Pool(thread=False, workers=self.workers)

    def pool(self, thread=False):
        return self.threads if thread else self.processes

    def imap(self, func, iterable, chunksize=1, pbar=None, total=None, thread=False):
        return self.pool(thread=thread).imap(
            func, iterable, chunksize=chunksize, pbar=pbar, total=total
        )

    def map(self, func, iterable, chunksize=1, pbar=None, total=None, thread=False):
        return self.pool(thread=thread).map(
            func, iterable, chunksize=chunksize, pbar=pbar, total=total
        )

    def istarmap(
        self, func, iterable, chunksize=1, pbar=None, total=None, thread=False
    ):
        return self.pool(thread=thread).istarmap(
            func, iterable, chunksize=chunksize, pbar=pbar, total=total
        )

    def starmap(self, func, iterable, chunksize=1, pbar=None, total=None, thread=False):
        return self.pool(thread=thread).starmap(
            func, iterable, chunksize=chunksize, pbar=pbar, total=total
        )

    def run(self, funcs, args=(), kwds=None, thread=False, **kwargs):
        return self.pool(thread=thread).run(funcs, args=args, kwds=kwds, **kwargs)

    def lock(self, thread=False):
        return self.pool(thread=thread).lock()

    def wait(self, results):
        wait(results)


class StarmapRunner(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, args):
        return self.func(*args)


class Pool(object):
    def __init__(self, workers=None, thread=False, join=False):
        super(Pool, self).__init__()
        self.workers = workers or WORKERS
        self.thread = thread
        self.join = join

    @utils.lazyproperty
    def pool(self):
        PoolClass = multiprocessing.dummy.Pool if self.thread else multiprocessing.Pool
        return PoolClass(processes=self.workers)

    def close(self):
        self.pool.close()
        if self.join:
            self.pool.join()

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        self.close()

    def imap(self, func, iterable, chunksize=1, pbar=None, total=None):
        iterable, total = spbar.getIterableLen(iterable, config=pbar, total=total)
        return spbar.one(
            self.pool.imap(func, iterable, chunksize=chunksize),
            config=pbar,
            total=total,
        )

    def map(self, func, iterable, chunksize=1, pbar=None, total=None):
        return list(
            self.imap(func, iterable, chunksize=chunksize, pbar=pbar, total=total)
        )

    def istarmap(self, func, iterable, chunksize=1, pbar=None, total=None):
        return self.imap(
            StarmapRunner(func), iterable, chunksize=chunksize, pbar=pbar, total=total
        )

    def starmap(self, func, iterable, chunksize=1, pbar=None, total=None):
        return list(
            self.istarmap(func, iterable, chunksize=chunksize, pbar=pbar, total=total)
        )

    def run(self, funcs, args=(), kwds=None, **kwargs):
        kwds = kwds or {}
        single = not isinstance(funcs, (list, tuple))
        funcs = [funcs] if single else funcs
        results = [
            self.pool.apply_async(func, args=args, kwds=kwds, **kwargs)
            for func in funcs
        ]
        return results[0] if single else results

    def lock(self):
        return multiprocessing.dummy.Lock() if self.thread else multiprocessing.Lock()

    def wait(self, results):
        wait(results)


pool = GlobalPool()


def GLOBAL_WORKERS(workers):
    pool.workers = workers


def imap(
    func, iterable, chunksize=1, pbar=None, total=None, thread=False, workers=None
):
    if workers is not None:
        with Pool(workers=workers, thread=thread) as _pool:
            return _pool.imap(
                func, iterable, chunksize=chunksize, pbar=pbar, total=total
            )
    return pool.imap(
        func, iterable, chunksize=chunksize, pbar=pbar, total=total, thread=thread
    )


def map(func, iterable, chunksize=1, pbar=None, total=None, thread=False, workers=None):
    if workers is not None:
        with Pool(workers=workers, thread=thread) as _pool:
            return _pool.map(
                func, iterable, chunksize=chunksize, pbar=pbar, total=total
            )
    return pool.map(
        func, iterable, chunksize=chunksize, pbar=pbar, total=total, thread=thread
    )


def istarmap(
    func, iterable, chunksize=1, pbar=None, total=None, thread=False, workers=None
):
    if workers is not None:
        with Pool(workers=workers, thread=thread) as _pool:
            return _pool.istarmap(
                func, iterable, chunksize=chunksize, pbar=pbar, total=total
            )
    return pool.istarmap(
        func, iterable, chunksize=chunksize, pbar=pbar, total=total, thread=thread
    )


def starmap(
    func, iterable, chunksize=1, pbar=None, total=None, thread=False, workers=None
):
    if workers is not None:
        with Pool(workers=workers, thread=thread) as _pool:
            return _pool.starmap(
                func, iterable, chunksize=chunksize, pbar=pbar, total=total
            )
    return pool.starmap(
        func, iterable, chunksize=chunksize, pbar=pbar, total=total, thread=thread
    )


def run(funcs, args=(), kwds=None, thread=False, workers=None):
    if workers is not None:
        workers = min(len(funcs), workers)
        with Pool(workers=workers, thread=thread) as _pool:
            return _pool.run(funcs, args=args, kwds=kwds)
    return pool.run(funcs, args=args, kwds=kwds, thread=thread)


def lock(thread=False):
    return pool.lock(thread=thread)


def wait(results):
    single = not isinstance(results, (list, tuple))
    results = [results] if single else results
    results = [r.get() for r in results]
    return results[0] if single else results
