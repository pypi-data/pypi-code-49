from functools import wraps

from pymongo import UpdateOne, MongoClient, ASCENDING, DESCENDING
from pymongo.errors import BulkWriteError

from .queryset import MongoQuery

def db_from_mongo_uri(mongo_uri, database_name):
    client = MongoClient(mongo_uri)
    return client[database_name]


class MongoOperations(object):
    def __init__(self, mongo_collection):
        self.ops = mongo_collection
        
    def find(self, query):
        query_dict = MongoQuery(query).build()
        return self.ops.find(query_dict)
        
    def insert_many(self, objs):
        return self.ops.insert_many(objs)
    
    def update_many(self, objs, by='_id'):
        updates = [
            UpdateOne({by: obj[by]}, {'$set': obj}) for obj in objs
        ]
        return self.ops.bulk_write(updates)
    
    def delete_many(self, query):
        query_dict = MongoQuery(query).build()
        return self.ops.delete_many(query_dict)
        
    def create_index(self, fields_and_direction, unique=False):
        self.ops.create_index(fields_and_direction, unique=unique)