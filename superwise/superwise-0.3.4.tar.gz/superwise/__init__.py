__version__ = '0.3.4'
import logging.config
import os

import yaml

from superwise.project_root import PROJECT_ROOT

with open(os.path.join(PROJECT_ROOT, "resources", "logger_config.yml"), 'r') as f:
    log_cfg = yaml.safe_load(f.read())


logging.config.dictConfig(log_cfg)
logger = logging.getLogger('superwise')
