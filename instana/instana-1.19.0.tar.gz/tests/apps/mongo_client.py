from __future__ import absolute_import

from flask import Flask, render_template

import pymongo
#import psycopg2
from datetime import datetime

conn = pymongo.MongoClient()
db = conn.test

#conn = psycopg2.connect(user='postgres', database='postgres')
#pg_db = conn.cursor()

app = Flask(__name__)

@app.route('/')
def hello():
#    pg_db.execute("SELECT 1;")
#    pg_db.fetchone()
    return "{} documents".format(db.records.count_documents({}))

app.run(debug=False)
