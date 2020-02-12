"""
Define all the constant and hard code value
"""
import pathlib

DEBUG = False
ENABLE_SIMULATOR = True


BASE_DIR = pathlib.Path.home()
RELATIVE_PROJECT_DIR = '.local/py2pip'

PATH_STATS_FILE = BASE_DIR / RELATIVE_PROJECT_DIR / 'stats.txt'

SUFFIX_LOG_FILE = 'py2pip_status.log'
PATH_LOG_FILE = BASE_DIR / RELATIVE_PROJECT_DIR / SUFFIX_LOG_FILE


PATH_PIP_COMMAND = 'pip'


class LookupTags():
    GRAND_PARENT = 'div'
    PARENT = 'div'
    TARGET_VERSION = 'p'
    TARGET_URL = 'a'
    TARGET_TIME = 'time'


class LookupClass():
    GRAND_PARENT = 'release-timeline'
    PARENT = 'release'
    TARGET_VERSION = 'release__version'
    TARGET_URL = ['release__card', 'card']  # Precise way to check


class PIPServer():
    HOST = 'https://pypi.org/'
    PATH = 'project/{project}/#history'
