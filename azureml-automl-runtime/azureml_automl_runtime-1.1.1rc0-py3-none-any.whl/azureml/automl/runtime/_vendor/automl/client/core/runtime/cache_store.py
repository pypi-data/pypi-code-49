# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Classes for automl cache store."""
import errno
import pickle
from enum import Enum
from typing import Any, Callable, cast, Dict, Iterable, Optional
import logging
import numpy as np
import os
import sys  # noqa F401 # dynamically evaluated to get caller
import tempfile
import copy

from abc import ABC, abstractmethod

from scipy import sparse

from .pickler import DefaultPickler
from automl.client.core.common.activity_logger import ActivityLogger, DummyActivityLogger


class CacheStore(ABC):
    """ABC for cache store."""

    def __init__(self,
                 max_retries: int = 3,
                 module_logger: Optional[logging.Logger] = None,
                 activity_logger: Optional[ActivityLogger] = None) -> None:
        """
        Cache store constructor.

        :param max_retries: max retries to get/put from/to store
        :param module_logger: logger
        :param activity_logger: activity logger
        """
        self.cache_items = {}  # type: Dict[Any, Any]
        self.max_retries = max_retries
        self.module_logger = module_logger or logging.getLogger()
        self.activity_logger = activity_logger or DummyActivityLogger()

    def __getstate__(self) -> Dict[str, Optional[Any]]:
        """
        Get this cache store's state, removing unserializable objects in the process.

        :return: a dict containing serializable state.
        """
        return {'module_logger': None,
                'activity_logger': None,
                'cache_items': self.cache_items,
                'max_retries': self.max_retries}

    def __setstate__(self, state: Dict[str, Optional[Any]]) -> None:
        """
        Deserialize this cache store's state, using the default logger.

        :param state: dictionary containing object state
        :type state: dict
        """
        self.module_logger = logging.getLogger()
        self.activity_logger = DummyActivityLogger()
        self.cache_items = cast(Dict[Any, Any], state['cache_items'])
        self.max_retries = cast(int, state['max_retries'])

    @abstractmethod
    def load(self):
        """Load - abstract method."""
        pass

    @abstractmethod
    def unload(self):
        """Unload - abstract method."""
        pass

    def add(self, keys: Iterable[Any], values: Iterable[Any]) -> None:
        """Add to store.

        :param keys: store key
        :param values: store value
        """
        for k, v in zip(keys, values):
            self.cache_items[k] = v

    def add_or_get(self, key: Any, value: Any) -> Any:
        """
        Add or get from store.

        :param key: store key
        :param value: store value
        :return: value
        """
        val = self.cache_items.get(key, None)
        if val is not None:
            return val

        self.add([key], [value])
        return value

    def get(self, keys: Iterable[Any], default: Optional[Any] = None) -> Dict[Any, Optional[Any]]:
        """
        Get value from store.

        :param default: default value
        :param keys: store keys
        :return: values
        """
        return {k: self.cache_items.get(k, default) for k in keys}

    def set(self, key, value):
        """
        Set value to store.

        :param key: store key
        :param value: store value
        """
        self.add([key], [value])

    def remove(self, key):
        """
        Remove from store.

        :param key: store key
        """
        obj = self.cache_items.pop(key)
        del obj

    def remove_all(self):
        """Remove all entry from store."""
        for k, v in self.cache_items.items():
            del v

        self.cache_items.clear()

    def __iter__(self):
        """
        Store iterator.

        :return: cache items
        """
        return iter(self.cache_items.items())

    @staticmethod
    def _function_with_retry(fn: 'Callable[..., Optional[Any]]',
                             max_retries: int,
                             logger: logging.Logger,
                             *args: Any,
                             **kwargs: Any) -> Optional[Any]:
        """
        Call function with retry capability.

        :param fn: function to be executed
        :param max_retries: number of retries
        :param logger: logger
        :param args: args
        :param kwargs: kwargs
        :return: Exception if failure, otherwise returns value from function call
        """
        retry_count = 0
        ex = None
        while retry_count < max_retries:
            try:
                return fn(*args, **kwargs)
            except Exception as e:
                logger.warning("CacheStore: Execution failed.")
                ex = e
            finally:
                retry_count += 1

        error_raised = cast(BaseException, ex)
        raise error_raised.with_traceback(error_raised.__traceback__)

    # Need to disable type checking because ContextManager is not available in typing before Python 3.5.4
    def log_activity(self, custom_dimensions: Optional[Dict[str, Any]] = None) -> Any:
        """
        Log activity collects the execution latency.

        :param custom_dimensions: custom telemetry dimensions
        :return: log activity
        """
        get_frame_expr = 'sys._getframe({}).f_code.co_name'
        caller = eval(get_frame_expr.format(2))
        telemetry_values = dict()
        telemetry_values['caller'] = caller

        if custom_dimensions is not None:
            telemetry_values.update(custom_dimensions)

        return self.activity_logger.log_activity(
            logger=self.module_logger, activity_name=caller, custom_dimensions=telemetry_values)


class MemoryCacheStore(CacheStore):
    """MemoryCacheStore - stores value in memory."""

    def load(self):
        """Load from memory - NoOp."""
        pass

    def add(self, keys, values):
        """
        Add to store by creating a deep copy.

        :param keys: store key
        :param values: store value
        """
        for k, v in zip(keys, values):
            self.cache_items[k] = copy.deepcopy(v)

    def unload(self):
        """Unload from memory."""
        self.cache_items.clear()


class _SavedAsProtocol(Enum):
    PICKLE = 1
    NUMPY = 2
    SCIPY = 3


class _CacheConstants:
    # default task timeout
    DEFAULT_TASK_TIMEOUT_SECONDS = 900

    # Extension name for files that are saved by Numpy.save()
    NUMPY_FILE_EXTENSION = 'npy'

    # Extension name for files that are saved by SciPy.save()
    SCIPY_SPARSE_FILE_EXTENSION = 'npz'

    # File name for metadata file (which stores mapping of what was stored and in what format)
    SAVED_AS_FILE_NAME = 'saved_as'


class FileCacheStore(CacheStore):
    """FileCacheStore - cache store based on file system."""

    def __init__(self, path=None,
                 task_timeout=_CacheConstants.DEFAULT_TASK_TIMEOUT_SECONDS,
                 module_logger=None):
        """
        File based cache store - constructor.

        :param path: store path
        :param task_timeout: task timeout
        :param module_logger:
        """
        super(FileCacheStore, self).__init__(module_logger=module_logger)

        self.task_timeout = task_timeout
        self.pickler = DefaultPickler()
        self._num_workers = os.cpu_count()
        self.path = path
        if not path:
            self.path = _create_temp_dir(os.getcwd())
        self.saved_as = dict()  # type: Dict[str, _SavedAsProtocol]
        self._saved_as_file_name = _CacheConstants.SAVED_AS_FILE_NAME

    def __getstate__(self):
        """
        Get this cache store's state, removing unserializable objects in the process.

        :return: a dict containing serializable state.
        """
        return super().__getstate__(), {
            'path': self.path,
            'pickler': self.pickler,
            'task_timeout': self.task_timeout,
            '_num_workers': self._num_workers,
            'saved_as': self.saved_as,
            '_saved_as_file_name': self._saved_as_file_name
        }

    def __setstate__(self, state):
        """
        Deserialize this cache store's state, using the default logger.

        :param state: dictionary containing object state
        :type state: dict
        """
        super_state, my_state = state
        self.path = my_state['path']
        self._num_workers = my_state['_num_workers']
        self.task_timeout = my_state['task_timeout']
        self.pickler = my_state['pickler']
        self.saved_as = my_state.get('saved_as') or dict()
        self._saved_as_file_name = my_state.get('_saved_as_file_name') or self._saved_as_file_name
        super().__setstate__(super_state)

    def log_debug_messages(self, message):
        """
        Log a message in the logfile.

        :param message: message to be logged
        """
        if self.module_logger:
            self.module_logger.info(message)

    def add(self, keys, values):
        """
        Pickles the object and adds to cache.

        :param keys: store keys
        :param values: store values
        """
        with self.log_activity():
            for k, v in zip(keys, values):
                self.log_debug_messages("Uploading key: " + k)
                self._upload(k, v)

    def add_or_get(self, key, value):
        """
        Add or gets from the store.

        :param key: store key
        :param value: store value
        :return: UnPickled object
        """
        val = self.cache_items.get(key, None)
        if val is not None:
            return self.get([key])

        self.add([key], [value])
        return value

    def _deserialize(self, key: str, path: str) -> Any:
        saved_as = self.saved_as.get(key, None)
        if saved_as == _SavedAsProtocol.SCIPY:
            self.module_logger.debug('Downloading and de-serializing "{}" via. Scipy from cache'.format(key))
            deserialized_obj = sparse.load_npz(path)
        elif saved_as == _SavedAsProtocol.NUMPY:
            self.module_logger.debug('Downloading and de-serializing "{}" via. Numpy from cache'.format(key))
            deserialized_obj = np.load(path)
        else:
            self.module_logger.debug('Downloading and unpickling "{}" from cache'.format(key))
            deserialized_obj = self.pickler.load(path)
        return deserialized_obj

    def get(self, keys, default=None):
        """
        Get unpickled object from store.

        :param keys: store keys
        :param default: returns default value if not present
        :return: unpickled objects
        """
        res = dict()

        with self.log_activity():
            for key in keys:
                path = self.cache_items.get(key, None)
                obj = default
                self.log_debug_messages("Getting data for key: " + key)
                if path is not None:
                    obj = self._deserialize(key, path)
                res[key] = obj

        return res

    def set(self, key, value):
        """
        Set to store.

        :param key: store key
        :param value: store value
        """
        self.add([key], [value])

    def remove(self, key):
        """
        Remove from store.

        :param key: store key
        """
        self.log_debug_messages("Deleting data for key: " + key)
        with self.log_activity():
            try:
                self.cache_items.pop(key)
                os.remove(key)
            except OSError as e:
                err_msg = "Failed to remove {} from store: {}".format(key, e)
                if e.errno != errno.ENOENT:
                    self.module_logger.error(err_msg)
                    raise
                else:
                    self.module_logger.warning(err_msg)
            except KeyError as e:
                self.module_logger.warning("Failed to remove {} from store: {}".format(key, e))
            except Exception:
                self.module_logger.warning("Remove from store failed.")

    def remove_all(self):
        """Remove all the cache from store."""
        length = self.cache_items.__len__()

        with self.log_activity():
            while length > 0:
                length -= 1
                k, v = self.cache_items.popitem()
                try:
                    # For back compatibility (e.g. with continue_runs), if saved_as file is absent, delete the file
                    if not self.saved_as:
                        os.remove(v)
                    elif k in self.saved_as:
                        # Delete the file only if it was cached via the cache store (e.g. files saved outside the
                        # context of cache_store, such as outputs, shouldn't be removed
                        os.remove(v)
                except OSError as e:
                    self.module_logger.warning('Failed to remove {} from cache store: {}'.format(v, e))
                    if e.errno != errno.ENOENT:
                        raise

    def load(self):
        """Load from store."""
        self.log_debug_messages("Loading from file cache")
        with self.log_activity():
            self._try_loading_saved_as_object()
            for f in os.listdir(self.path):
                key = self.pickler.get_name_without_extn(f)
                val = os.path.join(self.path, f)
                self.cache_items[key] = val

    def unload(self):
        """Unload from store."""
        # load to make sure all the meta files are loaded
        self.load()

        self.log_debug_messages("Unloading from file cache")
        self.remove_all()
        try:
            os.remove(os.path.join(self.path, self._saved_as_file_name))
        except OSError as e:
            self.module_logger.warning('Failed to remove the "saved_as" file: {}'.format(e))
            if e.errno != errno.ENOENT:
                raise
        _try_remove_dir(self.path)

    def _try_loading_saved_as_object(self):
        self.module_logger.info("Loading the saved_as object from cache.")
        saved_as_file_path = os.path.join(self.path, self._saved_as_file_name)
        if os.path.exists(saved_as_file_path):
            with open(saved_as_file_path, 'rb') as f:
                self.saved_as = pickle.load(f)
            self.module_logger.info("The saved_as object is: " + str(self.saved_as))

    def _persist_saved_as_file(self) -> None:
        path = os.path.join(self.path, self._saved_as_file_name)
        with open(path, 'wb') as f:
            pickle.dump(self.saved_as, f)
        self.module_logger.info("The saved_as object is: " + str(self.saved_as))

    def _serialize_numpy_ndarray(self, file_name: str, obj: np.ndarray) -> Any:
        assert isinstance(obj, np.ndarray)
        self.module_logger.debug('Numpy saving and uploading "{}" to cache'.format(file_name))
        path = os.path.join(self.path, file_name)
        np.save(path, obj, allow_pickle=False)
        return path

    def _serialize_scipy_sparse_matrix(self, file_name: str, obj: Any) -> Any:
        assert sparse.issparse(obj)
        self.module_logger.debug('Scipy saving and uploading "{}" to cache'.format(file_name))
        path = os.path.join(self.path, file_name)
        sparse.save_npz(path, obj)
        return path

    def _serialize_object_as_pickle(self, file_name: str, obj: Any) -> Any:
        self.module_logger.debug('Pickling and uploading "{}" to cache'.format(file_name))
        path = os.path.join(self.path, file_name)
        self.pickler.dump(obj, path=path)
        return path

    def _serialize(self, file_name: str, obj: Any) -> Any:
        key_name = file_name
        if isinstance(obj, np.ndarray) and obj.dtype != np.object:
            key_name = '.'.join([file_name, _CacheConstants.NUMPY_FILE_EXTENSION])
            local_file_path = self._serialize_numpy_ndarray(key_name, obj)
            self.saved_as[file_name] = _SavedAsProtocol.NUMPY
        elif sparse.issparse(obj):
            key_name = '.'.join([file_name, _CacheConstants.SCIPY_SPARSE_FILE_EXTENSION])
            local_file_path = self._serialize_scipy_sparse_matrix(key_name, obj)
            self.saved_as[file_name] = _SavedAsProtocol.SCIPY
        else:
            local_file_path = self._serialize_object_as_pickle(key_name, obj)
            self.saved_as[file_name] = _SavedAsProtocol.PICKLE

        return local_file_path

    def _upload(self, key, obj):
        try:
            path = self._serialize(key, obj)
            self.cache_items[key] = path
            self._persist_saved_as_file()
            self.log_debug_messages("Uploaded key: " + key)
        except Exception:
            self.module_logger.error("Uploading {} failed.".format(key))
            raise


def _create_temp_dir(temp_location: str) -> str:
    """
    Create temp dir.

    :return: temp location
    """
    try:
        return tempfile.mkdtemp(dir=temp_location)
    except OSError as e:
        raise CacheException("Failed to create temp folder {}. You can disable the "
                             "cache if space is concern. Setting to disable cache enable_cache=False".format(e))


def _try_remove_dir(path):
    """
    Remove directory.

    :param path: path to be removed
    """
    try:
        os.rmdir(path)
    except OSError:
        return False

    return True


class CacheException(Exception):
    """Cache exceptions."""

    pass
