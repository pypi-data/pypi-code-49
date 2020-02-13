from datetime import timedelta

from datamodelz.error import Error
from prefect.engine.result_handlers import JSONResultHandler
from prefect.utilities.tasks import defaults_from_attrs
from .query_service import Query


class QueryRankingsCompany(Query):
    def __init__(self, key, url=None, max_retries=3, retry_delay=timedelta(minutes=1), **kwargs):
        super().__init__(key, url, max_retries, retry_delay, **kwargs)
        self.name = "Query Rankings Company"
        self.log_prefix = self.build_log_prefix()

    @staticmethod
    def prep(rankings_id: str, url: str):
        return "{}/companies?company={}".format(url, rankings_id)

    @defaults_from_attrs('url')
    def run(self, data, url=None, **kwargs):
        if "error" in data:
            return data
        if "biid" not in data:
            return self.error(Error(check_name="QueryRankings", value="No Rankings id",
                                    company=data, api_call=data["apiCall"]))
        biid = data["biid"]
        full_url = self.prep(rankings_id=biid, url=url)
        response = self.query(data=biid, full_url=full_url)
        result = self.process(data=biid, full_url=full_url, response=response)
        result = self.add_api_call(full_url=full_url, result=result)
        return result
