from pymongo import MongoClient
from pvlv_database.configurations.configuration import MONGO_CONNECTION_STRING


class Connector(object):

    def __init__(self):
        self.client = MongoClient(MONGO_CONNECTION_STRING)

    def pull_data(self, database, table, id_in_table):
        collection = self.client[database][table]
        cursor = collection.find({'unique_id': id_in_table})
        data = None
        for doc in cursor:
            data = doc
        if data is None:
            return {}
        else:
            return data

    def push_data(self, database, table, id_in_table, data):
        collection = self.client[database][table]
        query = {'unique_id': id_in_table}
        cursor = collection.find(query)
        user_data_in_db = None
        for doc in cursor:
            user_data_in_db = doc
        if user_data_in_db is not None:
            collection.update_one(query, {'$set': data})
        else:
            collection.insert_one(data)
