import requests
import logging
from datetime import timedelta
from prefect.utilities.tasks import defaults_from_attrs
from .query_service import Query


class QueryGSheet(Query):
    """
    Base class for querying CA
    """
    def __init__(self, key, url=None, a_range=None, sheet_id=None, sheet_name=None,
                 max_retries=3, retry_delay=timedelta(minutes=1)):
        super().__init__(key, url, max_retries, retry_delay)
        self.name = "Query GSheet"
        self.a_range = a_range
        self.sheet_id = sheet_id
        self.sheet_name = sheet_name
        self.log_prefix = self.build_log_prefix()

    @staticmethod
    def prep(url, a_range, sheet_id, sheet_name):
        url = "{url}/{sheet_id}/values/{sheet_name}!{a_range}".format(
            url=url, sheet_id=sheet_id, sheet_name=sheet_name, a_range=a_range)
        return url

    def query(self, url):
        logging.debug("Querying %s", url)
        url += "?key={key}".format(key=self.key)
        return requests.get(url, params={}, headers={})

    def post_process(self, result, collapse=True):
        companies = []
        if "values" not in result:
            return []
        values = result["values"]
        if not collapse:  # return early & don't collapse lists
            return values
        for company in values:
            companies += company
        logging.debug("{}: {} companies returned".format(self.log_prefix, len(companies)))
        companies = [x for x in companies if x != ""]
        return companies

    @defaults_from_attrs('url', 'a_range', 'sheet_id', 'sheet_name')
    def run(self, url=None, a_range=None, sheet_id=None, sheet_name=None, collapse=True):
        full_url = self.prep(url, a_range, sheet_id, sheet_name)
        response = self.query(full_url)
        result = self.process("", full_url, response)
        ids = self.post_process(result, collapse)
        return ids


class MapIDs(QueryGSheet):
    def __init__(self, key, url=None, a_range=None, sheet_id=None, sheet_name=None, key_idx=None, value_idx=None,
                 max_retries=3, retry_delay=timedelta(minutes=1)):
        super().__init__(key, url, a_range, sheet_id, sheet_name, max_retries, retry_delay)
        self.name = "Map IDS"
        self.key_idx = key_idx
        self.value_idx = value_idx

    @staticmethod
    def create_map(values, key_idx, value_idx) -> dict:
        maps = {}
        if len(values) < 2:
            logging.error("No maps %s", values)
            return maps
        for lst in values[1:]:
            if len(lst) < key_idx or len(lst) < value_idx:
                break
            maps[lst[key_idx]] = lst[value_idx]  # NOTE: hardcoded location of mapping
        return maps

    def mapped(self, ids, result, key_idx, value_idx):
        if "values" not in result:
            return []
        id_map = self.create_map(result["values"], key_idx, value_idx)
        try:
            return [id_map[x] for x in ids]
        except KeyError as err:
            logging.error("Key Error %s", err)
            return []

    @defaults_from_attrs('url', 'a_range', 'sheet_id', 'sheet_name', 'key_idx', 'value_idx')
    def run(self, ids, url=None, a_range=None, sheet_id=None, sheet_name=None, key_idx=None, value_idx=None):
        full_url = self.prep(url, a_range, sheet_id, sheet_name)
        response = self.query(full_url)
        result = self.process("", full_url, response)
        ids = self.mapped(ids, result, key_idx, value_idx)
        return ids
