from typing import Any

import requests
import logging
from prefect import task, Task
from prefect.utilities.tasks import defaults_from_attrs
from prefect.client import Secret
from prefect.utilities.notifications import slack_notifier
from prefect.engine.state import Failed
from datetime import timedelta
from . import errors
from datamodelz.error import Error


class Query(Task):
    def __init__(self, key, url=None, max_retries=3, retry_delay=timedelta(minutes=1), **kwargs: Any):
        super().__init__(max_retries, retry_delay, **kwargs)
        self.name = "Query"
        self.key = key
        self.url = url
        self.log_prefix = self.build_log_prefix()

    def query(self, data, full_url, **kwargs):
        if "error" in full_url:
            return full_url
        logging.debug("{}: url {}".format(self.log_prefix, full_url))
        try:
            response = requests.get(
                url=full_url,
                params={},
                headers={'Authorization': self.key},
            )
            return response
        except Exception as err:
            return self.error(
                Error(check_name="Query", value="Bad request: {}".format(err), company=data, api_call=full_url))

    def process(self, data, full_url, response, **kwargs):
        logging.debug("queried {} with response {}".format(full_url, response))
        if "error" in response:
            return response
        try:
            if response.status_code != 200:
                return self.error(Error(check_name="Query", value=errors.response_code(str(response.status_code)),
                                        company=data, api_call=full_url))
            doc = response.json()
            if doc is None or not doc or doc == {}:
                return self.error(Error(check_name="Query", value=errors.bad_response, company=data, api_call=full_url))
            return doc
        except Exception as err:
            return self.error(Error(check_name="Query", value="{}: {}".format(errors.bad_response, err), company=data,
                                    api_call=full_url))

    @staticmethod
    def add_api_call(full_url, result):
        result["apiCall"] = full_url
        return result

    def error(self, error) -> dict:
        full_msg = "{}: {}".format(self.log_prefix, error)
        logging.error(full_msg)
        return {"error": [error]}

    def build_log_prefix(self) -> str:
        return self.name.title().replace(' ', '')

    @defaults_from_attrs('url')
    def run(self, data, url=None, **kwargs):
        response = self.query(data, url)
        result = self.process(data, url, response)
        return result
