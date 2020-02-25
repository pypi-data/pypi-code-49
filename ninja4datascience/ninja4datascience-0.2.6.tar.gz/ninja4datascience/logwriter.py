import logging
from logging.handlers import TimedRotatingFileHandler
import platform
import os

JobName = ''
file_handler_path = ''


# procedure_name = (os.path.splitext(os.path.basename(inspect.getfile(inspect.currentframe())))[0])
# logging_file_path = os.getcwd()
# get_job_name_log_file_path(procedure_name, os.getcwd())

def get_job_name_log_file_path(job_name, logging_file_path):
    global JobName, Logging_file_name, file_handler_path
    JobName = job_name
    file_handler_path = os.path.join(logging_file_path, 'Logs', JobName + ".log")


class AppFilter(logging.Filter):
    def filter(self, record):
        record.app_name = platform.node()
        return True


def get_file_handler():
    FORMATTER = logging.Formatter(
        '\n' + "-" * 100 + '\nTimestamp: %(asctime)s\n%(name)s: %(message)s \nMachine: %(app_name)s \n' + "-" * 100,
        '%m/%d/%Y %I:%M:%S %p')
    if not os.path.isdir((os.path.dirname(file_handler_path))):
        os.mkdir((os.path.dirname(file_handler_path)))
    file_handler = TimedRotatingFileHandler(file_handler_path, when='D', interval=1)
    file_handler.suffix = "%Y-%m-%d-%H%M%S.log"
    file_handler.setFormatter(FORMATTER)
    return file_handler


def get_logger(logger_name):
    if file_handler_path != '':
        logger = logging.getLogger(logger_name)
        logger.addFilter(AppFilter())
        logger.setLevel(logging.DEBUG)
        logger.addHandler(get_file_handler())
        return logger


def LogCacheOutput(child):
    global get_file_log_writer
    # Log all console output responses  here
    logCacheOutput = ''
    logCacheOutput += 'Console log of responses ' + "\n"
    logCacheOutput += '********start' + "\n"
    for line in child:
        logCacheOutput += 'Output: ' + str(line) + "\n"
    logCacheOutput += '********end' + "\n"
    if get_file_log_writer is None:
        get_file_log_writer = get_logger("Message")
    get_file_log_writer.debug(logCacheOutput)


get_file_log_writer = get_logger("Message")
JobLogId = 0


def log_write(message, is_end=''):
    global JobLogId, JobName, get_file_log_writer
    log_file = "file"
    if log_file.strip().upper() == "FILE":
        if get_file_log_writer is None:
            get_file_log_writer = get_logger("Message")
        get_file_log_writer.debug(message)
    else:
        if JobLogId == 0:
            obj_job_log = JobLog(JobName)
            JobLogId = insert_job_log(obj_job_log)
        obj_job_log_details = JobLogDetails(JobLogId, message)
        insert_job_log_details(obj_job_log_details)
        if is_end != '':
            obj_update_job_log_end_date = JobLogEndDate(JobLogId)
            update_job_log_end_date(obj_update_job_log_end_date)
