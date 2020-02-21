import logging

from .podder_task_logger import PodderTaskLogger
from .podder_task_logger import task_name, job_id, host_name

logging.setLoggerClass(PodderTaskLogger)

logging.getLogger().__class__ = PodderTaskLogger
