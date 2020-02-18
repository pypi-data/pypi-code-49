import os
import time
import traceback
from datetime import datetime

from starling.config import CONFIG
from starling.exception import RetryTaskExitError, RetryTaskError, RetryTaskSkipAuthError
from starling.helper import retry_task
from starling.types import ScrapperData, TaskData
from .blueprint_scrapper import BlueprintScrapper


class Scrapper:
    @staticmethod
    def _run_task(task: TaskData, scrapper_data: ScrapperData):
        package_name, classname = task.action.rsplit('.', 1)
        blueprint = getattr(__import__(package_name, fromlist=[package_name]), classname)(scrapper_data, task)
        fetched_data = blueprint.fetch()
        time.sleep(os.getenv('INTERVAL', blueprint.interval()))
        scrapper_data.message.fetched_at = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
        return fetched_data

    @staticmethod
    @retry_task()
    def _run(scrapper: BlueprintScrapper, is_auth=True):
        if is_auth:
            scrapper.authenticate()

        for action in scrapper.valid_actions:
            for task in [task for task in [tasks for tasks in scrapper.data.actions[action]]
                         if task.fetched_data is None]:
                task.fetched_data = Scrapper._run_task(task, scrapper.data)

    @staticmethod
    def run(scrapper: BlueprintScrapper, **kwargs):
        CONFIG.update(kwargs)
        try:
            Scrapper._run(scrapper)
        except (RetryTaskExitError, RetryTaskError, RetryTaskSkipAuthError) as e:
            scrapper.data.is_valid = e.extra.get('is_valid', False)
            scrapper.data.error_message = e.message
            scrapper.data.error_extra = e.extra
        except Exception as e:
            scrapper.data.is_valid = False
            scrapper.data.error_message = '__UNEXPECTED_SCRAPPER_ERROR__'
            scrapper.data.error_extra = dict(traceback=traceback.format_exc(), name=type(e).__name__)
        return scrapper.data
