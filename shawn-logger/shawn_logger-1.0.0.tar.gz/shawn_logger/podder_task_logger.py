import logging
import socket

host_name = socket.gethostname()
job_id = 'JOB_ID'
task_name = 'TASK_NAME'


class PodderTaskLogger(logging.Logger):
    def _log(self, level, msg, args, exc_info=None, extra=None, stack_info=False):
        message = f'[{task_name}][{host_name}][{job_id}] - {msg}'
        super(PodderTaskLogger, self)._log(level, message, args, exc_info, extra)
