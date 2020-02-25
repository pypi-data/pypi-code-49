import logging
import os


def num_of_records(file):
    try:
        if os.path.isfile(file):
            return int(len(open(file, encoding="utf-8", errors="ignore").readlines()))
        else:
            return 0
    except Exception as exception:
        logging.exception(exception)
