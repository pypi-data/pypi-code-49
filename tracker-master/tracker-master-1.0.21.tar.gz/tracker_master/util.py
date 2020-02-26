import logging
import logging.config
import os
import json
import tracker_master.config as CFG

__COM_PORT_LOGGER_NAME = 'com_port'


def setup_logging(default_path='logging.json', default_level=logging.INFO, env_key='LOG_CFG'):
    # Setup logging configuration
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)

        # Read log file name from app configuration
        config['handlers']['app_log']['filename'] = CFG.log_file()
        config['handlers']['com_port']['filename'] = CFG.com_port_log_file()
        logging.config.dictConfig(config)

    else:
        logging.basicConfig(level=default_level)


def get_com_port_logger():
    return logging.getLogger(__COM_PORT_LOGGER_NAME)
