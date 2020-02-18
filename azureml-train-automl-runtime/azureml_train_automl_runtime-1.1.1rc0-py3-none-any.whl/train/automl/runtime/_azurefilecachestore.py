# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Cache store implementation that utilizes Azure files for backend storage."""
import logging
import os
from typing import Any, Dict, Callable

import numpy as np
from azureml._vendor.azure_storage.file import FileService, models, ContentSettings
from scipy import sparse

from automl.client.core.common.activity_logger import DummyActivityLogger
from automl.client.core.runtime.cache_store import CacheStore, CacheException, _create_temp_dir, _SavedAsProtocol, \
    _CacheConstants
from automl.client.core.common import logging_utilities
from automl.client.core.runtime.pickler import DefaultPickler
from azureml import _async


class AzureFileCacheStore(CacheStore):
    """Cache store based on azure file system."""

    def __init__(self,
                 path,
                 account_name=None,
                 account_key=None,
                 pickler=None,
                 task_timeout=_CacheConstants.DEFAULT_TASK_TIMEOUT_SECONDS,
                 module_logger=logging.getLogger(__name__),
                 temp_location=None,
                 file_service=None):
        """
        Cache based on azure file system.

        :param path: path of the store
        :param account_name: account name
        :param account_key: account key
        :param pickler: pickler, default is cPickler
        :param task_timeout: task timeout
        :param module_logger: logger
        :param temp_location: temporary location to store the files
        :param file_service: file service instance if provided
        """
        super(AzureFileCacheStore, self).__init__(module_logger=module_logger)

        if pickler is None:
            pickler = DefaultPickler()

        self.task_timeout = task_timeout
        self.pickler = pickler
        self.account_name = account_name
        self.account_key = account_key
        self.cache_items = dict()  # type: Dict[str, str]
        self.module_logger = module_logger if module_logger is not None else logging.getLogger()
        self.temp_location = _create_temp_dir(temp_location)
        self.file_service = file_service if file_service is not None else \
            FileService(account_name=account_name, account_key=account_key)
        self.path = path.lower().replace('_', '-')
        self.file_service.create_share(self.path)
        self.saved_as = dict()  # type: Dict[str, _SavedAsProtocol]
        self._saved_as_file_name = _CacheConstants.SAVED_AS_FILE_NAME

    def __getstate__(self):
        return {'task_timeout': self.task_timeout,
                'pickler': self.pickler,
                'account_name': self.account_name,
                'account_key': self.account_key,
                'cache_items': self.cache_items,
                'module_logger': None,
                'temp_location': self.temp_location,
                'path': self.path,
                'max_retries': self.max_retries,
                'saved_as': self.saved_as,
                '_saved_as_file_name': self._saved_as_file_name}

    def __setstate__(self, state):
        self.path = state['path']
        self.pickler = state['pickler']
        self.account_name = state['account_name']
        self.account_key = state['account_key']
        self.cache_items = state['cache_items']
        self.module_logger = logging.getLogger()
        self.task_timeout = state['task_timeout']
        self.max_retries = state['max_retries']
        self.saved_as = state['saved_as']
        self._saved_as_file_name = state['_saved_as_file_name']
        self.activity_logger = DummyActivityLogger()
        self.file_service = FileService(account_name=self.account_name, account_key=self.account_key)

        try:
            temp_location = state['temp_location']
            os.makedirs(temp_location, exist_ok=True)
        except Exception:
            temp_location = os.getcwd()
            os.makedirs(temp_location, exist_ok=True)
        self.temp_location = temp_location

    def add(self, keys, values):
        """Add to azure file store.

        :param keys: keys
        :param values: values
        """
        self.module_logger.info('Adding {} to Azure file store cache'.format(keys))
        with self.log_activity():
            try:
                for k, v in zip(keys, values):
                    self._function_with_retry(self._serialize_and_upload,
                                              self.max_retries, self.module_logger, k, v)
            except Exception as e:
                logging_utilities.log_traceback(e, self.module_logger, is_critical=False)
                raise CacheException("Cache failure")

    def add_or_get(self, key, value):
        """
        Adds the key to the Azure File store. If it already exists, return the value.

        :param key:
        :param value:
        :return: deserialized object
        """
        val = self.cache_items.get(key, None)
        if val is None:
            self.add([key], [value])
            return {key: value}

        return self.get([key], None)

    def get(self, keys, default=None):
        """
        Get the deserialized object from azure file store

        :param default: default value
        :param keys: store key
        :return: deserialized object
        """
        self.module_logger.info('Getting {} from Azure file store cache'.format(keys))
        with self.log_activity():
            ret = dict()
            self.module_logger.debug("saved_as object: " + str(self.saved_as.keys()))
            self.module_logger.info("Currently available items in cache: " + str(self.cache_items.keys()))
            for key in keys:
                try:
                    ret[key] = self._function_with_retry(self._download_and_deserialize, self.max_retries,
                                                         self.module_logger, key)[key]
                except Exception as e:
                    logging_utilities.log_traceback(e, self.module_logger, is_critical=False)
                    self.module_logger.warning('Failed to retrieve key "{}" from cache'.format(key))
                    ret[key] = default

        return ret

    def set(self, key, value):
        """
        Set values to store.

        :param key: key
        :param value: value
        """
        self.add([key], [value])

    def remove(self, key):
        """
        Remove from store.

        :param key: store key
        """
        with self.log_activity():
            self._remove(self.path, [key])

    def remove_all(self):
        """Remove all the file from cache."""
        with self.log_activity():
            self._remove(self.path, self.cache_items.keys())

    def load(self):
        """Load from azure file store."""
        with self.log_activity():
            self._function_with_retry(self._get_azure_file_lists,
                                      self.max_retries, self.module_logger, self.path)

    def unload(self):
        """Unload the cache."""
        import shutil
        try:
            self.file_service.delete_share(share_name=self.path)
        except Exception as e:
            logging_utilities.log_traceback(e, self.module_logger, is_critical=False)
            self.module_logger.warning('Failed to delete share "{}"'.format(self.path))

        self.cache_items.clear()
        shutil.rmtree(self.temp_location)

    def _remove(self, path, files):
        worker_pool = _async.WorkerPool(max_workers=os.cpu_count())
        tasks = []

        with _async.TaskQueue(worker_pool=worker_pool, _ident=__name__,
                              flush_timeout_seconds=self.task_timeout,
                              _parent_logger=self.module_logger) as tq:
            for file in files:
                tasks.append(tq.add(self._function_with_retry,
                                    self._remove_from_azure_file_store,
                                    self.max_retries,
                                    self.module_logger,
                                    path,
                                    file))

        for task in tasks:
            task.wait()
        worker_pool.shutdown()

    def _remove_from_azure_file_store(self, path, key):
        self.file_service.delete_file(path, directory_name=None, file_name=key)
        self.cache_items.pop(key)

    def _get_azure_file_lists(self, path):
        """
        Get list of files available from azure file store. similar to dir.

        :param path: path
        """
        self.module_logger.debug('Getting list of files in "{}" in Azure file store'.format(path))
        for dir_or_file in self.file_service.list_directories_and_files(share_name=path):
            if isinstance(dir_or_file, models.File):
                if dir_or_file.name != self._saved_as_file_name:
                    self.cache_items[dir_or_file.name] = dir_or_file.name
                else:
                    self._load_saved_as_object_from_file()

    def _try_remove_temp_file(self, path):
        self.module_logger.debug('Removing temp file "{}"'.format(path))
        try:
            os.remove(path)
        except OSError as e:
            logging_utilities.log_traceback(e, self.module_logger, is_critical=False)
            self.module_logger.warning("failed to remove temp file")

    def _load_saved_as_object_from_file(self):
        self.module_logger.info("Loading the saved_as object from cache.")
        with self.log_activity():
            saved_as_temp_file = os.path.join(self.temp_location, '_saved_as_tmp')
            self.file_service.get_file_to_path(share_name=self.path,
                                               directory_name=None,
                                               file_name=self._saved_as_file_name,
                                               file_path=saved_as_temp_file)
            self.saved_as = self.pickler.load(saved_as_temp_file)
        self._try_remove_temp_file(saved_as_temp_file)
        self.module_logger.info("The saved_as object is: " + str(self.saved_as))

    def _persist_saved_as_file(self) -> None:
        with self.log_activity():
            path = os.path.join(self.temp_location, self._saved_as_file_name)
            self.pickler.dump(self.saved_as, path=path)
            self.file_service.create_file_from_path(share_name=self.path,
                                                    directory_name=None,
                                                    file_name=self._saved_as_file_name,
                                                    local_file_path=path,
                                                    content_settings=ContentSettings('application/x-binary'))
        self._try_remove_temp_file(path)
        self.module_logger.info("The saved_as object is: " + str(self.saved_as))

    def _serialize_numpy_ndarray(self, file_name: str, obj: np.ndarray) -> Any:
        assert isinstance(obj, np.ndarray)
        self.module_logger.debug('Numpy saving and uploading "{}" to cache'.format(file_name))
        path = os.path.join(self.temp_location, file_name)
        np.save(path, obj, allow_pickle=False)
        return path

    def _serialize_scipy_sparse_matrix(self, file_name: str, obj: Any) -> Any:
        assert sparse.issparse(obj)
        self.module_logger.debug('Scipy saving and uploading "{}" to cache'.format(file_name))
        path = os.path.join(self.temp_location, file_name)
        sparse.save_npz(path, obj)
        return path

    def _serialize_object_as_pickle(self, file_name: str, obj: Any) -> Any:
        self.module_logger.debug('Pickling and uploading "{}" to cache'.format(file_name))
        path = os.path.join(self.temp_location, file_name)
        self.pickler.dump(obj, path=path)
        return path

    def _serialize_and_upload(self, file_name: str, obj: Any) -> None:
        with self.log_activity():
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

            self.file_service.create_file_from_path(share_name=self.path,
                                                    directory_name=None,
                                                    file_name=key_name,
                                                    local_file_path=local_file_path,
                                                    content_settings=ContentSettings('application/x-binary'))
            self.cache_items[file_name] = file_name
            self._persist_saved_as_file()
            self._try_remove_temp_file(local_file_path)

    def _deserialize_object(self, file_name: str, deserialization_fn: Callable[[str], Any]) -> Any:
        downloaded_path = os.path.join(self.temp_location, file_name)
        # Optimize to skip downloading the file if we already have it locally (e.g. from a previous call to get it)
        if not os.path.exists(downloaded_path):
            self.file_service.get_file_to_path(share_name=self.path,
                                               directory_name=None,
                                               file_name=file_name,
                                               file_path=downloaded_path)
        return deserialization_fn(downloaded_path)

    def _download_and_deserialize(self, file_name: str) -> Dict[str, Any]:
        self.cache_items[file_name] = file_name
        saved_as = self.saved_as.get(file_name, None)
        if saved_as == _SavedAsProtocol.SCIPY:
            self.module_logger.debug('Downloading and de-serializing "{}" via. Scipy from cache'.format(file_name))
            deserialized_obj = self._deserialize_object(
                '.'.join([file_name, _CacheConstants.SCIPY_SPARSE_FILE_EXTENSION]), sparse.load_npz)
        elif saved_as == _SavedAsProtocol.NUMPY:
            self.module_logger.debug('Downloading and de-serializing "{}" via. Numpy from cache'.format(file_name))
            deserialized_obj = self._deserialize_object(
                '.'.join([file_name, _CacheConstants.NUMPY_FILE_EXTENSION]), np.load)
        else:
            self.module_logger.debug('Downloading and unpickling "{}" from cache'.format(file_name))
            deserialized_obj = self._deserialize_object(file_name, self.pickler.load)
        return {file_name: deserialized_obj}
