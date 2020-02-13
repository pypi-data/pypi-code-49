import os
import sys
import threading
from uuid import uuid4

from azureml.dataprep import read_preppy
from azureml.dataprep.api._loggerfactory import _LoggerFactory


log = _LoggerFactory.get_logger('dprep.fuse._cached_dataflow')


class CachedDataflow:
    def __init__(self, dataflow, cache_dir):
        self._dataflow = dataflow
        self._cache_dir = os.path.join(cache_dir, '__dprep_preppy_{}__'.format(str(uuid4())))
        self._cache_lock = threading.Lock()
        self._preppy_dataflow = None

    @property
    def dataflow(self):
        try:
            self._cache_lock.acquire()
            if self._preppy_dataflow is None:
                self._dataflow.write_to_preppy(self._cache_dir).run_local()
                self._preppy_dataflow = read_preppy(self._cache_dir, include_path=True, verify_exists=True)
            return self._preppy_dataflow
        except Exception as e:
            log.warning('Error encountered while caching dataflow', exc_info=sys.exc_info())
            self._preppy_dataflow = None
            # fallback to use raw dataflow without cache
            return self._dataflow
        finally:
            self._cache_lock.release()
