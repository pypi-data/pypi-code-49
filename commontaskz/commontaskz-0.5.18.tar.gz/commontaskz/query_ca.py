import requests
import logging
from datetime import timedelta

from datamodelz.error import Error
from prefect import Task
from prefect.engine.result_handlers import JSONResultHandler
from prefect.utilities.tasks import defaults_from_attrs
from .query_service import Query
from . import errors


class QueryCA(Query):
    """
    Base Query.
    """

    def __init__(self, key, url=None, service=None, max_retries=3, retry_delay=timedelta(minutes=1), **kwargs):
        super().__init__(key, url, max_retries, retry_delay, **kwargs)
        self.name = "Query CA"
        self.log_prefix = self.build_log_prefix()
        self.service = service

    def prep(self, ca_id, url: str):
        return "{url}/entity/{ca_id}?includeUnverified=true".format(url=url, ca_id=ca_id)

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
            if response is not None:
                return response
            return self.error(Error(check_name=self.log_prefix,
                                    value="Bad request",
                                    company=data,
                                    api_call=full_url))
        except Exception as err:
            return self.error(Error(check_name=self.log_prefix,
                                    value="Bad request: {}".format(err),
                                    company=data,
                                    api_call=full_url))

    @defaults_from_attrs('url', 'service')
    def run(self, data, url=None, service=None, **kwargs):
        full_url = self.prep(ca_id=data, url=url)
        response = self.query(data=data, full_url=full_url)
        result = self.process(data=data, full_url=full_url, response=response)
        result = self.add_api_call(full_url=full_url, result=result)
        return result


class QueryCACompany(QueryCA):
    """
    Query to get datasys or rankings id.
    """

    def __init__(self, key, url=None, service=None, max_retries=3, retry_delay=timedelta(minutes=1), **kwargs):
        super().__init__(key, url, max_retries, retry_delay, **kwargs)
        self.name = "Query CA Company"
        self.log_prefix = self.build_log_prefix()
        self.service = service

    def prep(self, ca_id, url: str):
        return "{url}/entity/{ca_id}?includeUnverified=true".format(url=url, ca_id=ca_id)

    def post_process(self, data, full_url, result, service):
        final = {}
        if "error" in result:
            return result
        if "biids" not in result:
            return self.error(Error(check_name=self.log_prefix,
                                    value=errors.service_name_dne("biids"),
                                    company=data,
                                    api_call=full_url))
        lst = result["biids"]
        for item in lst:
            if item["service"] == service:
                final["biid"] = item["value"]
                return final
        return self.error(Error(check_name=self.log_prefix,
                                value=errors.service_name_dne(service),
                                company=data,
                                api_call=full_url))

    @defaults_from_attrs('url', 'service')
    def run(self, data, url=None, service=None, **kwargs):
        full_url = self.prep(ca_id=data, url=url)
        response = self.query(data=data, full_url=full_url)
        result = self.process(data=data, full_url=full_url, response=response)
        result = self.post_process(data=data, full_url=full_url, result=result, service=service)
        result = self.add_api_call(full_url=full_url, result=result)
        return result
