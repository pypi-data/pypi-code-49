import os
import pymongo as pym

from collections import OrderedDict
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional
from urllib import parse

from cvplotlib.data_source import base


class MongoDBDataSource(base.BaseDataSource):
    """docstring for MongoDBDataSource

    Args:
        metrics
        setups
        query_factory
        metric_prefix
        creds
        host

    Attributes:
        client:
        db:
        metrics:
        runs:
        data:

    """

    def __init__(self,
                 metrics: List[str],
                 setups: List[Optional[str]],
                 query_factory: Callable,
                 metric_prefix: str = '',
                 creds: Dict[str, str] = {},
                 host: str = 'localhost'):
        creds = creds or MongoDBDataSource.get_creds()
        self.client = pym.MongoClient(MongoDBDataSource.auth_url(creds, host))
        self.db = self.client[creds['db_name']]
        self.metrics = self.db['metrics']
        self.runs = self.db['runs']

        self._metric_list = metrics
        if metric_prefix:
            self._metric_list = [metric_prefix + m for m in self._metric_list]

        self._setup_list = setups
        self._query_factory = query_factory

        super(MongoDBDataSource, self).__init__()

    @staticmethod
    def get_creds() -> Dict[str, str]:
        return dict(
            user=parse.quote_plus(os.environ['MONGODB_USER_NAME']),
            password=parse.quote_plus(os.environ['MONGODB_PASSWORD']),
            db_name=parse.quote_plus(os.environ['MONGODB_DB_NAME']),
        )

    @staticmethod
    def auth_url(creds: Dict[str, str], host) -> str:
        url = 'mongodb://{user}:{password}@{host}:27017/{db_name}?authSource=admin'.format(
            host=host, **creds)
        return url

    def load_setup_data(self, metric: str, query: Dict[str, Any]) -> None:

        query["status"] = {"$in": ["COMPLETED"]}
        selected_runs = list(self.runs.find(query))

        for run in selected_runs:
            values = self.metrics.find_one(dict(
                name=metric,
                run_id=run['_id'],
            ))

            if values is None or values['values'] is None:
                continue

            self.data.setup_data.append(values['values'])

        if len(selected_runs) == 0:
            warnings.warn(f"No runs were selected for metric \"{metric}\" with query \"{query}\"!")

    def load_metric_data(self, metric: str) -> None:

        for setup, query in self._queries.items():
            with self.data.using_setup(setup):
                self.load_setup_data(metric, query)

    def load_data(self) -> None:
        self.data.clear()

        for metric in self._metric_list:
            with self.data.using_metric(metric):
                self.load_metric_data(metric)

    def preprocess(self) -> None:
        self._queries = {
            setup: self._query_factory(setup) for setup in self._setup_list
        }

    def postprocess(self) -> None:
        pass
