import datetime
import logging
from multiprocessing import Process, Queue  # type: ignore
from typing import Text, Union, Dict, Optional

from apscheduler.job import Job
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import UnknownTimeZoneError, utc
from ragex.community import utils, config
from ragex.community.services.analytics_service import AnalyticsService

logger = logging.getLogger(__name__)

_job_queue = Queue()


def _schedule_background_jobs(scheduler: BackgroundScheduler) -> None:
    from ragex.community.services.git_service import GitService, GIT_BACKGROUND_JOB_ID

    # Schedule Git synchronization
    if utils.is_git_available():
        scheduler.add_job(
            GitService.run_background_synchronization,
            "cron",
            id=GIT_BACKGROUND_JOB_ID,
            next_run_time=datetime.datetime.now(),
            replace_existing=True,
            minute="*",
        )

    # Schedule analytics caching
    if utils.is_enterprise_installed():
        scheduler.add_job(
            AnalyticsService.run_analytics_caching,
            "cron",
            replace_existing=True,
            **config.analytics_update_kwargs,
        )


def _run_scheduler() -> None:
    try:
        logging.getLogger("apscheduler.scheduler").setLevel(logging.WARNING)
        scheduler = BackgroundScheduler()
        scheduler.start()
    except UnknownTimeZoneError:
        logger.warning(
            "apscheduler could not find a timezone and is "
            "defaulting to utc. This is probably because "
            "your system timezone is not set. "
            'Set it with e.g. echo "Europe/Berlin" > '
            "/etc/timezone"
        )
        scheduler = BackgroundScheduler(timezone=utc)
        scheduler.start()

    _schedule_background_jobs(scheduler)

    # Check regularly if a job should be executed right away
    while True:
        job_information = _job_queue.get()
        job_id = job_information.pop("job_id")
        existing_job: Optional[Job] = scheduler.get_job(job_id)

        if existing_job:
            _modify_job(existing_job, job_information)
        else:
            logger.warning(f"Did not find a scheduled job with id '{job_id}'.")


def _modify_job(background_job: Job, job_modification: Dict) -> None:
    changes = {}
    job_id = background_job.id
    run_immediately = job_modification.pop("run_immediately", False)

    if run_immediately:
        changes["next_run_time"] = datetime.datetime.now()
        logger.debug(f"Running job with id '{job_id}' immediately.")

    # Set keyword arguments to call scheduled job function with
    changes["kwargs"] = job_modification

    background_job.modify(**changes)
    logger.debug(f"Modifying job with id '{background_job.id}'.")


def run_job_immediately(job_id: Text, **kwargs: Union[bool, Text]) -> None:
    """Trigger a scheduled background job to run immediately.
    
    Args:
        job_id: ID of the job which should be triggered.
        kwargs: Keyword arguments to call scheduled job function with
        
    """

    modify_job(job_id, run_immediately=True, **kwargs)


def modify_job(job_id: Text, **kwargs: Union[bool, Text]) -> None:
    """Modify a scheduled background job.

    Args:
        job_id: ID of the job which should be modified.
        kwargs: Keyword arguments to call scheduled job function with
    """
    job_information = kwargs
    job_information["job_id"] = job_id
    _job_queue.put(job_information)


def start_background_scheduler() -> Process:
    """Start a background scheduler which runs periodic tasks."""

    # Start scheduler in a separate process so that we can create a process and thread
    # safe interface by using a `Queue` to communicate with it.
    process = Process(target=_run_scheduler)
    process.start()

    return process
