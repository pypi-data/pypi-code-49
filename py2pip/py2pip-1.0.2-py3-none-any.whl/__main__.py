#!/usr/bin/env python3

import argparse
import logging
import pathlib
import time
import sys

from logging.handlers import RotatingFileHandler

import py2pip.config
import py2pip.utils
from py2pip.process import Py2PIPManager


MAX_FILE_SIZE = 2 * 1024 * 1024  # 2 MiB
MAX_BACKUP_FILE = 5


def get_logger(log_file, enable_debug):
    """
    Creates a rotating log
    """
    # Create parent dir if not exists already.
    if not log_file.parent.exists():
        log_file.parent.mkdir(parents=True)

    formatter = logging.Formatter('%(asctime)s.%(msecs)03d %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    logger = logging.getLogger("Py2pip process handler")
    logger.setLevel(logging.DEBUG if enable_debug else logging.INFO)

    # add a rotating handler
    handler = RotatingFileHandler(str(log_file), maxBytes=MAX_FILE_SIZE, backupCount=MAX_BACKUP_FILE, encoding='UTF-8')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def options():
    parser = argparse.ArgumentParser('Verify-And-Install-Package')
    parser.add_argument('-i', '--install', action='store_true',
            help="Pass if you want to install package of supported Python version")
    parser.add_argument('--py-version', dest='python_support', type=str, required=True,
            help="Find Support Python Version i.e 2.6, 2.7, 3.1, 3.5 etc.")
    parser.add_argument('-p', '--package', type=str, help="Python Package Name registered to PIP", required=True)
    parser.add_argument('-d', '--debug', dest="enable_debug", action="store_true", default=py2pip.config.DEBUG,
                        help="Enable Debug")
    parser.add_argument('-l', '--log-file', dest='log_file_name', type=str, default=str(py2pip.config.PATH_LOG_FILE),
                        help="Log file path. Set default to app level")
    
    args = parser.parse_args()
    return args


def main():
    try:
        option = options()
        if not py2pip.utils.validPySupportVersion(option.python_support):
            raise ValueError(f"Must pass support python version '--py-version'.")

        log_file_path = pathlib.Path(option.log_file_name)
        log = get_logger(log_file_path, option.enable_debug)

        py2pip_manager = Py2PIPManager(option.package, option.python_support, option.install, log, show_progress=True)
        
        stime = time.time()
        result = py2pip_manager.run()
        etime = time.time()
        print(f'Execution time: {etime - stime}\nSupported Version: {result}\n')

    except ValueError as e:
        print(f'Error: {str(e)}')

if __name__ == '__main__':
    sys.exit(main())
