import mongomock
import os
import pymongo as pym
import unittest

from cvplotlib import data_source as ds

HOST = "localhost"
CREDS = dict(MONGODB_USER_NAME="test",
             MONGODB_PASSWORD="test",
             MONGODB_DB_NAME="somedb")


def patch(func):
    global HOST, CREDS
    func = mongomock.patch(servers=((HOST, 27017),))(func)
    func = unittest.mock.patch.dict(os.environ, CREDS)(func)

    return func


class MongoDBSourceTests(unittest.TestCase):

    def init_database(self):
        creds = ds.MongoDBDataSource.get_creds()
        url = ds.MongoDBDataSource.auth_url(creds, host=HOST)
        self.db = pym.MongoClient(url).somedb
        runs = [dict(status="COMPLETED") for i in range(10)]
        self.db.runs.insert_many(runs)

        for run in self.db.runs.find():
            metrics = [
                dict(run_id=run["_id"],
                     name="accuracy",
                     values=[0.2, 0.1, 0.1, 0.1]),
                dict(run_id=run["_id"],
                     name="loss",
                     values=[0.3, 0.1, 0.2, 0.1]),
            ]
            self.db.metrics.insert_many(metrics)

    def init_source(self, metrics, setups, query_factory=lambda setup: dict()):
        return ds.MongoDBDataSource(metrics=metrics,
                                    setups=setups,
                                    query_factory=query_factory,
                                    host=HOST)

    @patch
    def test_connection(self):
        self.init_database()
        source = self.init_source(metrics=[], setups=[])

        self.assertEqual(source.runs.count_documents({}),
                         self.db.runs.count_documents({}))
        self.assertEqual(source.metrics.count_documents({}),
                         self.db.metrics.count_documents({}))

    @patch
    def test_data_load(self):
        self.init_database()
        metrics = ["accuracy", "loss"]
        # we check for only one setup!
        source = self.init_source(metrics=metrics, setups=["some_setup"])

        for metric in metrics:
            should = [
                res["values"] for res in self.db.metrics.find(dict(name=metric))
            ]
            # since we have only a single setup
            should = {"some_setup": should}

            read_data = source.data.get_metric(metric)

            self.assertDictEqual(
                read_data, should,
                f"Could not load values for \"{metric}\" correctly!")
