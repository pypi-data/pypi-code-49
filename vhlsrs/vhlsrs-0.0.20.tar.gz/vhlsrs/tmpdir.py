"""
Utilitaries to execute commands inside a temporary directory
"""

import logging
import shutil
import tempfile
from os import chdir
from pathlib import Path

class TmpDirManager:
    def __init__(self, exp_name, destruct=True):
        logger = logging.getLogger("vrs_log")
        self.destruct = destruct
        self.work_dir = Path.cwd()
        self.path = Path(tempfile.mkdtemp(suffix=exp_name, prefix="vhlsrs"))
        logger.info("Creating temporary directory in {}".format(self.path))
        logger.debug("work_dir : {}".format(self.work_dir))
        logger.debug("self_destruct : {}".format(self.destruct))

    def __enter__(self):
        logging.getLogger("vrs_log").debug("Changing current dir to {}".format(self.path)) 
        chdir(self.path)

    def __exit__(self, _, __, ___):
        logger = logging.getLogger("vrs_log")
        logger.debug("leaving temporary dir and switching to {}".format(self.work_dir))
        chdir(self.work_dir)
        if self.destruct:
            logger.debug("Removing temporary directory")
            shutil.rmtree(self.path)
        pass
