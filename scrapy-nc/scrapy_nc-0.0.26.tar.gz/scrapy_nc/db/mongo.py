import os
from pymongo import MongoClient

MONGO_HOST = os.environ.get('CRAWLAB_MONGO_HOST')
MONGO_PORT = int(os.environ.get('CRAWLAB_MONGO_PORT', '27017'))
MONGO_DB = os.environ.get('CRAWLAB_MONGO_DB')
MONGO_USERNAME = os.environ.get('CRAWLAB_MONGO_USERNAME')
MONGO_PASSWORD = os.environ.get('CRAWLAB_MONGO_PASSWORD')
MONGO_AUTHSOURCE = os.environ.get('CRAWLAB_MONGO_AUTHSOURCE')
COLLECTION = os.environ.get('CRAWLAB_COLLECTION')

mongo_conn = MongoClient(
    host=MONGO_HOST,
    port=MONGO_PORT,
    username=MONGO_USERNAME,
    password=MONGO_PASSWORD,
    authSource=MONGO_AUTHSOURCE,
) if MONGO_HOST else None
mongo_db = mongo_conn.get_database(MONGO_DB) if mongo_conn else None
spider_collection = mongo_db.get_collection(COLLECTION) if mongo_db else None
