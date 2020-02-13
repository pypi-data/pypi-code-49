"""
Constants and Enum used by the sdk
"""
import enum
import pathlib

REST_API_SUFFIX = '/api/v1'
DEFAULT_BASE_URL = 'https://app.dis.co'
DISCO_CONFIG_PATH = pathlib.Path.home() / '.disco_py'
ENV_VAR_BASE_URL_NAME = 'DISCO_BASE_URL'
ENV_VAR_EMAIL_NAME = 'DISCO_EMAIL'
ENV_VAR_PASSWORD_NAME = 'DISCO_PASSWORD'
ENV_VAR_DISABLE_PROGRESS_BAR = 'DISCO_DISABLE_PROGRESS_BAR'

SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR


class JobStatus(enum.Enum):
    """Job statuses"""
    unknown = 'Unknown'
    listed = 'Listed'
    working = 'Working'
    stopped = 'Stopped'
    done = 'Done'
    failed = 'Failed'
    deleted = 'Deleted'


JOB_RUNNING_STATES = {JobStatus.listed, JobStatus.working}
JOB_TERMINAL_STATES = {x for x in JobStatus if x not in JOB_RUNNING_STATES}


class TaskStatus(enum.Enum):
    """Task statuses"""
    unknown = 'Unknown'
    listed = 'Listed'
    running = 'Running'
    stopped = 'Stopped'
    success = 'Success'
    failed = 'Failed'
    deleted = 'Deleted'


class ClusterType(enum.Enum):
    """Cluster types"""
    AWS = 'aws'
    Azure = 'azure'
    GCP = 'gcp'
    Packet = 'packet'
    OnPremise = 'onPremise'
