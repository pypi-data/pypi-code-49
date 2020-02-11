import logging
import os
import inspect
import time

import openlab.credentials as credentials

#import user settings
log = credentials.log #Boolean whether or not to log
log_level = credentials.log_level #ENUM 

# for other modules to identify
logger_name = 'Openlab_Logger'

#Get the location of the installed OpenLab Library
current_directory = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))


#Save log to same directory tree as openlab module
log_file = "openlab_log.txt"
log_path = os.path.join(current_directory, log_file)

# Create and configure logger
LOG_FORMAT = "%(asctime)s [%(levelname)s] - %(message)s"
logging.basicConfig(filename = log_path,
                    format=LOG_FORMAT,
                    level = log_level)

if not log:
    logging.disable(logging.CRITICAL) #disables logging for critical and below, effectivaly disabling all logging 
else:
    logger = logging.getLogger(logger_name)
    logger.info("Logger Initalized at path: {}".format(log_path))
