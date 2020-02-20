# Description:Clean files

import os
import re
from .log import logger
from . import workers

MAX_ITER_TIMES = 10


def cleanwork(fromPath, toPath, pattern, command, iscrawl=False, iter_times=0):
    """
    Parameters
    ----------
    fromPath:string
        Source folder
    toPath:string
        Target folder
    pattern:string
        Regular expression partern for file match
    command:string
        delete, move or copy
    iscrawl:bool,default is False
        is crawl fodler if exists nesting folders

    Returns
    -------
    None
    """
    taskName = f"from {fromPath} {command} to {toPath}"
    logger.info(f"Start task: {taskName}")
    try:
        filenameList = os.listdir(fromPath)
        nfiles = len(filenameList)
        if nfiles == 0:
            logger.warning(f"{nfiles} files found in {fromPath}.")
    except Exception as e:
        logger.info("Open %s error." % fromPath)
        logger.error(e)
        return None
    for filename in filenameList:
        newPath = os.path.join(fromPath, filename)
        # Handling recursive problems with folders
        if (
            os.path.isdir(newPath)
            and bool(int(iscrawl))
            and iter_times < MAX_ITER_TIMES
        ):
            iter_times += 1
            logger.info(newPath, iter_times)
            cleanwork(newPath, toPath, pattern, command, iscrawl, iter_times)
        elif re.match(pattern, filename, flags=re.IGNORECASE):
            Worker = workers.selectWorker(command)
            worker = Worker(newPath, toPath, pattern)
            worker.work()
