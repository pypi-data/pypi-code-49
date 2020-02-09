from datetime import timedelta

from datamodelz.error import Error
from prefect.utilities.tasks import defaults_from_attrs
from .query_service import Query


class QueryDatasysCompany(Query):
    def __init__(self, key, url=None, max_retries=3, retry_delay=timedelta(minutes=1), **kwargs):
        super().__init__(key, url, max_retries, retry_delay, **kwargs)
        self.name = "Query Datasys Company"
        self.log_prefix = self.build_log_prefix()

    @staticmethod
    def prep(datasys_id: dict, url: str):
        return "{}/repository/company/{}?trace=false".format(url, datasys_id)

    @defaults_from_attrs('url')
    def run(self, data, url=None, **kwargs):
        if "error" in data:
            return data
        if "biid" not in data:
            return self.error(Error(check_name="QueryDatasys", value="No Datasys id",
                                    company=data, api_call=data["apiCall"]))
        biid = data["biid"]
        full_url = self.prep(datasys_id=biid, url=url)
        response = self.query(data=biid, full_url=full_url)
        result = self.process(data=biid, full_url=full_url, response=response)
        result = self.add_api_call(full_url=full_url, result=result)
        return result
