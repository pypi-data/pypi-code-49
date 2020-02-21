import logging
import socket

host_name = socket.gethostname()
job_id = 'JOB_ID'
task_name = 'TASK_NAME'


def set_job_id(id: str):
    global job_id
    job_id = id


def set_host_name(name: str):
    global host_name
    host_name = name


def set_task_name(name: str):
    global task_name
    task_name = name


class PodderTaskLogger(logging.Logger):
    def _log(self, level, msg, args, exc_info=None, extra=None, stack_info=False):
        message = f'[{task_name}][{host_name}][{job_id}] - {msg}'
        super(PodderTaskLogger, self)._log(level, message, args, exc_info, extra)


logging.setLoggerClass(PodderTaskLogger)

logging.getLogger().__class__ = PodderTaskLogger
