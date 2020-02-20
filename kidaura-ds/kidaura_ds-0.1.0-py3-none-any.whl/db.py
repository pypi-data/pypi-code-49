import pymongo
import os


def get_conn(database='kidaura_v1'):
    client = pymongo.MongoClient(os.environ['MONGO_URI'])
    return client.get_database(database)


def get_collection(coll, database='kidaura_v1'):
    client = pymongo.MongoClient(os.environ['MONGO_URI'])
    db = client.get_database(database)
    return db[coll]