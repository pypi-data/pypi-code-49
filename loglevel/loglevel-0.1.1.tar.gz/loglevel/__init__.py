"""loglevel - """

__version__ = '0.1.1'
__author__ = 'fx-kirin <fx.kirin@gmail.com>'
__all__ = ['set_loglevel']

import logging
import yaml
from pathlib import Path


def set_loglevel(yml_file_path):
    loglevels = yaml.safe_load(Path(yml_file_path).read_text())
    for key, value in loglevels.items():
        logging.getLogger(key).setLevel(getattr(logging, value))
