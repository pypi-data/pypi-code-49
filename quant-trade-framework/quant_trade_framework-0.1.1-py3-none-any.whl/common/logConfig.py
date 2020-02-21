import logging.config
from logging.handlers import TimedRotatingFileHandler
from os import path
import os
from .constant import SystemConfig
import re

debug_flag = True
class Logger:

    """
    python log module
    methods:
    add this import information:
    from common.logConfig import Logger
    logger = Logger.module_logger("com_control_device")
    """
    def __init__(self):
        pass

    @classmethod
    def module_logger(self,module_name):
        """
        output log to files
        :param module_name: log file module,you can define
        different file for different modules
        :return: logger object
        """

        try:
            if not os.path.exists(SystemConfig.LOG_FILE_FOLDER):
                os.makedirs(SystemConfig.LOG_FILE_FOLDER)
            if not os.path.exists(SystemConfig.LOG_FILE_PATH):
                os.makedirs(SystemConfig.LOG_FILE_PATH)
        except IOError as e:
            pass
        log_file_directory = path.join(SystemConfig.LOG_FILE_PATH, module_name + ".log")
        logger = logging.getLogger("logger")
        logger.setLevel(logging.INFO)

        formatter = logging.Formatter("%(asctime)s %(filename)s %(module)s %(funcName)s %(levelname)s %(message)s")

        if logger.hasHandlers():
            for handler in logger.handlers[:]:
                logger.removeHandler(handler)

        if not logger.hasHandlers():
            if debug_flag:
                handler = logging.StreamHandler()
                handler.setLevel(logging.INFO)
                handler.setFormatter(formatter)
                logger.addHandler(handler)
            # else:
            log_file_handler = TimedRotatingFileHandler(filename=log_file_directory, when="D", interval=1, backupCount=7)
            log_file_handler.suffix = "%Y-%m-%d_%H-%M.log"
            log_file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.log$")
            log_file_handler.setFormatter(formatter)
            log_file_handler.setLevel(logging.INFO)

            logger.addHandler(log_file_handler)
        return logger

    @classmethod
    def debug_logger(self):
        """
        output console log
        :return:
        """


        logger = logging.getLogger("logger")
        handler = logging.StreamHandler()
        logger.setLevel(logging.DEBUG)
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        return logger

