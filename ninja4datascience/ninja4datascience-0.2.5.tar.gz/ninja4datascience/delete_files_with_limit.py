import logging
import os
from datetime import datetime, timedelta
from glob import glob


# from ninja4datascience.logwriter import *


def delete_all_extension_files_with_limit(logging_file_path, file_extension, number_days):
    try:
        if str(file_extension).strip() in ["*.*", ".*", ""]:
            return
        file_count = 0
        # process_name = (os.path.splitext(os.path.basename(inspect.getfile(inspect.currentframe())))[0])
        # get_job_name_log_file_path(process_name, logging_file_path)
        # log_write(process_name + " started")
        cutoff = datetime.now() - timedelta(days=number_days)
        for file_name in glob(file_extension):
            t = os.stat(file_name)
            c = datetime.fromtimestamp(t.st_ctime)
            if c < cutoff:
                os.remove(file_name)
                file_count += 1
                # log_write(file_name + " deleted")
        # log_write(process_name + " finished")
        return 'No file(s) found to delete' if file_count == 0 else str(file_count) + ' file(s) deleted'
    except Exception as e:
        logging.exception(e)
