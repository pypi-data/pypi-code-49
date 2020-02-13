import logging
from datetime import timedelta

import requests
from prefect.engine.result_handlers import JSONResultHandler
from prefect.utilities.tasks import defaults_from_attrs

from commontaskz import errors
from requests import Response

from .query_service import Query
from datamodelz.error import Error


class GenericTimeseries(Query):
    """
    Basic
    """
    def __init__(self, key, url=None, timeseries=None, max_retries=3, retry_delay=timedelta(minutes=1), **kwargs):
        super().__init__(key, url, max_retries, retry_delay, **kwargs)
        self.name = "Generic Timeseries"
        self.url = url
        self.timeseries = timeseries
        self.key = "apiKey {}".format(key)
        self.log_prefix = self.build_log_prefix()

    def query(self, data, full_url, timeseries="", **kwargs):
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
                Error(check_name="Query",
                      timeseries_code=timeseries,
                      value="Bad request: {}".format(err),
                      company=data,
                      api_call=full_url)
            )

    def process(self, data, full_url, response, timeseries=None, **kwargs):
        if "error" in response:
            return response
        try:
            if type(response) == str:
                return self.error(Error(check_name=self.log_prefix, value=response,
                                        timeseries_code=timeseries, company=data, api_call=full_url))
            if type(response) != Response:
                return self.error(Error(check_name=self.log_prefix, value="Bad Response",
                                        timeseries_code=timeseries, company=data, api_call=full_url))
            if response.status_code != 200:
                return self.error(Error(check_name=self.log_prefix, value=str(response.status_code),
                                        timeseries_code=timeseries, company=data, api_call=full_url))
            doc = response.json()
            if doc is None or not doc or doc == {}:
                return self.error(Error(check_name=self.log_prefix, value="Empty Response",
                                        timeseries_code=timeseries, company=data, api_call=full_url))
            return doc
        except Exception as err:
            return self.error(Error(check_name=self.log_prefix, value="Bad Response: {}".format(str(err)),
                                    timeseries_code=timeseries, company=data, api_call=full_url))


class QueryTimeseries(Query):
    def __init__(self, key, url=None, timeseries=None, max_retries=3, retry_delay=timedelta(minutes=1), **kwargs):
        super().__init__(key, url, timeseries, max_retries, retry_delay, **kwargs)
        self.name = "Query Timeseries"
        self.key = "apiKey {}".format(key)
        self.log_prefix = self.build_log_prefix()

    def prep(self, data: str, url: str, timeseries: str):
        if "error" in data:
            return data
        new_url = "{url}/timeseries/{timeseries}/{ca_id}" \
            .format(url=url, ca_id=data, timeseries=timeseries)
        return new_url

    @defaults_from_attrs('url', 'timeseries')
    def run(self, data, timeseries=None, url=None, **kwargs):
        full_url = self.prep(data=data, url=url, timeseries=timeseries)
        response = self.query(data=data, full_url=full_url, timeseries=timeseries)
        result = self.process(data=data, full_url=full_url, response=response, timeseries=timeseries)
        return result


class GetTimeseriesData(GenericTimeseries):
    def __init__(self, key, url=None, order=None, max_retries=3, retry_delay=timedelta(minutes=1), **kwargs):
        super().__init__(key, url, max_retries, retry_delay, **kwargs)
        self.name = "Get Timeseries Data"
        self.order = order
        self.key = "apiKey {}".format(key)
        self.log_prefix = self.build_log_prefix()

    @staticmethod
    def prep(data: str,
             url: str,
             timeseries: str,
             skip: int,
             limit: int,
             order: str,
             collapse: str,
             aggregate: str,
             transform: str):
        new_url = "{url}/timeseries/{timeseries}/{data}?skip={skip}&limit={limit}"\
            .format(url=url, data=data.lower(), timeseries=timeseries.lower(), skip=skip, limit=limit)
        if order:
            new_url += "&order={}".format(order.lower())
        if collapse:
            new_url += "&collapse={}".format(collapse.lower())
        if aggregate:
            new_url += "&aggregate={}".format(aggregate.lower())
        if transform:
            new_url += "&transform={}".format(transform.lower())
        return new_url

    @staticmethod
    def join(final, result):
        if "error" in result:
            return result
        if "data" in result:
            final["data"] = final["data"] + result["data"]
        return final

    def done(self, final, result, skip):
        # make data dict
        if "data" not in final:
            final = result
        else:
            final = self.join(final, result)
        if "error" in result or skip >= result["totalCount"]:  # stop because bad response or done getting results
            return final, True
        return final, False  # still more to go and no errors

    @defaults_from_attrs('url', 'order')
    def run(self, data, timeseries=None, url=None, order=None, collapse=None, aggregate=None, transform=None, **kwargs):
        """
        Repeats API call to get all data via paging for given timeseries type & company id
        :param aggregate:
        :param order:
        :param data:
        :param timeseries:
        :param url:
        :param collapse:
        :param aggregation:
        :param transform:
        :return: will return error or final results
        """
        if "error" in data:
            return data
        final = {}
        skip, limit = 0, 500
        done = False
        while not done:
            full_url = self.prep(data, url, timeseries, skip, limit, order, collapse, aggregate, transform)
            response = self.query(data=data, full_url=full_url, timeseries=timeseries)
            result = self.process(data, full_url, response, timeseries)
            skip += limit  # adding offset for next query
            final, done = self.done(final, result, skip)
            final = self.add_api_call(full_url, final)
        return final


class GetAllTimeseries(Query):
    def __init__(self, key, url=None, max_retries=3, retry_delay=timedelta(minutes=1), **kwargs):
        super().__init__(key, url, max_retries, retry_delay)
        self.name = "Get All Timeseries Metadata"
        self.key = "apiKey {}".format(key)
        self.url = url
        self.log_prefix = self.build_log_prefix()

    @staticmethod
    def prep(url: str, **kwargs):
        print("url is", url)
        return "{url}/timeseries".format(url=url)

    def post_process(self, full_url, result, **kwargs):
        if "data" not in result:
            return [self.error(Error(check_name=self.log_prefix, value="No Timeseries Data", api_call=full_url))]
        print(result)
        return result["data"]

    @staticmethod
    def add_api_call(full_url, result, **kwargs):
        for i in range(len(result)):
            print(result[i])
            result[i]["apiCall"] = full_url
        return result

    @defaults_from_attrs('url')
    def run(self, url=None, **kwargs):
        full_url = self.prep(url=url)
        response = self.query(data="", full_url=full_url)
        result = self.process(data="", full_url=full_url, response=response)
        result = self.post_process(full_url=full_url, result=result)
        result = self.add_api_call(full_url=full_url, result=result)
        return result  # data has key data


class SearchCompany(Query):
    def __init__(self, key, url=None, max_retries=3, retry_delay=timedelta(minutes=1), **kwargs):
        super().__init__(key, url, max_retries, retry_delay, **kwargs)
        self.name = "TimeseriesCompany"
        self.key = "apiKey {}".format(key)
        self.log_prefix = self.build_log_prefix()

    @staticmethod
    def prep(timeseries_id: str, url: str):
        if "error" in timeseries_id:
            return timeseries_id
        return "{url}/companies?name={timeseries_id}".format(url=url, timeseries_id=timeseries_id)

    @defaults_from_attrs('url')
    def run(self, data, url=None, **kwargs):
        full_url = self.prep(timeseries_id=data, url=url)
        response = self.query(data=data, full_url=full_url)
        result = self.process(data="", full_url=full_url, result=response, timeseries=data)
        result = self.add_api_call(full_url=full_url, result=result)
        return result
