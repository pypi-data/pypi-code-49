import os
import time
from stat import S_ISREG, ST_CTIME, ST_MODE

# from ninja4datascience.logwriter import *
from dateutil import parser


def get_filelistwithdate(logging_file_path, dirpath):
    # process_name = (os.path.splitext(os.path.basename(inspect.getfile(inspect.currentframe())))[0])
    # get_job_name_log_file_path(process_name, logging_file_path)
    # log_write(process_name + " started")
    # path to the directory (relative or absolute)
    # dirpath = Path(sampledirectory')
    # get all entries in the directory w/ stats
    if os.path.isdir(dirpath):
        entries = (os.path.join(dirpath, fn) for fn in os.listdir(dirpath))
        entries = ((os.stat(path), path) for path in entries)
        # leave only regular files, insert creation date
        entries = ((stat[ST_CTIME], path, os.stat(path).st_size)
                   for stat, path in entries if S_ISREG(stat[ST_MODE]))

        listData = []
        for cdate, path, size in sorted(entries):
            listData.append(parser.parse(time.ctime(cdate)).strftime('%d-%m-%Y %H:%M:%S') + ' ' + path
                            + ' ' + str(size))

        # log_write(process_name + " finished")
        return listData
    else:
        return ""
