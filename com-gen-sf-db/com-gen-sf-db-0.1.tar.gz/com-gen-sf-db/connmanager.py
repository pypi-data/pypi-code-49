import sqlalchemy
from sqlalchemy import tuple_, text
import logging
import os
from sys import platform

class DB():
    db=None
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        logging.info('conectando...')
        db_user = os.environ.get("DB_USER")
        db_pass = os.environ.get("DB_PASS")
        db_name = os.environ.get("DB_NAME")
        cloud_sql_connection_name = os.environ.get("CLOUD_SQL_CONNECTION_NAME")
        # inicializaciòn de conexion con db son server LOCAL
    
        if platform == "win32":
            self.db = sqlalchemy.create_engine(
            sqlalchemy.engine.url.URL(
                drivername="mysql+pymysql",
                username='root',
                password='Compar30#',
                database='sales_flow_dev',
                host='127.0.0.1',#host='34.73.187.163',
                port='3307'
                #query={"unix_socket": "/cloudsql/{}".format(cloud_sql_connection_name)},
            ),pool_size=5,max_overflow=2,pool_timeout=30, pool_recycle=1800 ) 
        else:
            self.db = sqlalchemy.create_engine(
            sqlalchemy.engine.url.URL(
                drivername="mysql+pymysql",
                username=db_user,
                password=db_pass,
                database=db_name,
                query={"unix_socket": "/cloudsql/{}".format(cloud_sql_connection_name)},
            ),pool_size=5,max_overflow=2,pool_timeout=30, pool_recycle=1800 )

    def get_connection(self):
        con= self.db.raw_connection()
        logging.info('conectado!')
        return con

DB().get_connection()