import multiprocessing as mp
import random
import math
from inspect import isfunction
from abc import ABC

class Parallelizer(ABC):

    def __init__(self, task, post_processor = None, n_threads = -1):
        # check arguments
        if not isfunction(task):
            raise ValueError('task argument is not a callable')
        if post_processor is not None and not isfunction(post_processor):
            raise ValueError('post_processor argument is not a callable')
        if not isinstance(n_threads, int) or n_threads == 0:
            raise ValueError('invalid n_threads value')
        # constructor objects
        self._task = task
        self._post_processor = post_processor
        cpu_threads = mp.cpu_count()
        if n_threads < 0 or n_threads > cpu_threads:
            self._n_threads = cpu_threads
        else:
            self._n_threads = n_threads
        # objects for later use
        self._task_args = list()
        self._task_kwargs = dict()
        self._post_processor_args = list()
        self._post_processor_kwargs = dict()
        self._manager = mp.Manager()
        self._shared_memory = None

    @property
    def task(self):
        return self._task

    @property
    def post_processor(self):
        return self._post_processor

    @property
    def n_threads(self):
        return self._n_threads

    def _parse_arguments(self, args, kwargs):
        if args is not None:
            for e in args:
                if e.startswith(self._task.__name__ + '_'):
                    arg = e.replace(self._task.__name__ + '_', '')
                    self._task_args.append(arg)
                if e.startswith(self._post_processor.__name__ + '_'):
                    arg = e.replace(self._post_processor.__name__ + '_', '')
                    self._post_processor_args.append(arg)
        if kwargs is not None:
            for k, v in kwargs.items():
                if k.startswith(self._task.__name__ + '_'):
                    arg = k.replace(self._task.__name__ + '_', '')
                    self._task_kwargs[arg] = v
                if k.startswith(self._post_processor.__name__ + '_'):
                    arg = k.replace(self._post_processor.__name__ + '_', '')
                    self._post_processor_kwargs[arg] = v

    def _split_data(self, data, shuffle = False):
        if shuffle:
            random.shuffle(data)
        q = math.floor(len(data) / self._n_threads)
        sizes = [q for _ in range(self._n_threads)]
        for i in range(len(data) % self._n_threads):
            sizes[i] += 1
        sizes = [size for size in sizes if size != 0]
        data_chunks = list()
        i = 0
        for size in sizes:
            data_chunks.append(data[i:i + size])
            i += size
        return data_chunks
    
    def _target_wrapper(self, data):
        raise NotImplementedError

    def _post_process(self):
        raise NotImplementedError
    
    def _run(self, data, shuffle_data = False, *args, **kwargs):
        # check arguments
        if not isinstance(data, list):
            raise ValueError('invalid data argument: expecting a list')
        if not isinstance(shuffle_data, bool):
            raise ValueError('invalid shuffle_data value: expecting a boolean')
        # parse args and kwargs
        self._parse_arguments(args, kwargs)
        # initialize the shared memory
        self._shared_memory = self._manager.list()
        # split data
        data_chunks = self._split_data(data, shuffle_data)
        # execute jobs
        processes = list()
        for data_chunk in data_chunks:
            process = mp.Process(target = self._target_wrapper, 
                                 args = (data_chunk,), kwargs = {})
            processes.append(process)
        for process in processes:
            process.start()
        for process in processes:
            process.join()

    def process(self):
        raise NotImplementedError

class FunctionParallelizer(Parallelizer):

    def _target_wrapper(self, data):
        rv = self._task(data, *self._task_args, **self._task_kwargs)
        self._shared_memory.append(rv)

    def _post_process(self):
        if self._post_processor is None:
            rv = list(self._shared_memory)
        else:
            rv = self._post_processor(self._shared_memory,
                                      *self._post_processor_args, 
                                      **self._post_processor_kwargs)
        return rv

    def process(self, data, shuffle_data = False, *args, **kwargs):
        super()._run(data, shuffle_data = shuffle_data, *args, **kwargs)
        return self._post_process()

class ProcedureParallelizer(Parallelizer):

    def _target_wrapper(self, data):
        self._task(data, *self._task_args, **self._task_kwargs)

    def _post_process(self):
        if self._post_processor is not None:
            self._post_processor(self._shared_memory, 
                                 *self._post_processor_args, 
                                 **self._post_processor_kwargs)

    def process(self, data, shuffle_data = False, *args, **kwargs):
        super()._run(data, shuffle_data = shuffle_data, *args, **kwargs)
        self._post_process()

def ll_func(task, 
            data, 
            shuffle_data = False, 
            post_processor = None, 
            n_threads = -1, 
            *args, **kwargs):
    ll = FunctionParallelizer(task, 
                              post_processor = post_processor, 
                              n_threads = n_threads)
    return ll.process(data, shuffle_data = shuffle_data, *args, **kwargs)

def ll_proc(task, 
            data, 
            shuffle_data = False, 
            post_processor = None, 
            n_threads = -1, 
            *args, **kwargs):
    ll = ProcedureParallelizer(task, 
                               post_processor = post_processor, 
                               n_threads = n_threads)
    ll.process(data, shuffle_data = shuffle_data, *args, **kwargs)
