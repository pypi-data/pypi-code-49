# import pyodbc 
import pymysql
from .settings import Settings
from .helpers import Helpers
from datetime import datetime, timedelta





class _Model():
    DBConnection = None
    DBCursor = None

    def __reconnect(self):
        raise NotImplementedError

    def __execute(self, query, retry = True):
        try:
            self.DBCursor.execute(query)
        except (pymysql.err.OperationalError, pymysql.err.InterfaceError) as e:
            print("An issue with the connection was identified.", e)
            if retry:
                print(" - Attempting to resolve by rebooting connection... Standby...")
                self.__reconnect()
                print("Attempting to retry query: ", query)
                self.__execute(query, False)
            else:
                print(" - Was unable to resolve the issue, query cannot be executed. Query: ", query)

    def insert(self, query):
        """Insert data into the database"""
        self.DBCursor.execute(query)
        self.DBConnection.commit()

    def truncate(self, query):
        """Truncate a table in the database"""
        self.DBCursor.execute(query)
        self.DBConnection.commit()

    def update(self, query):
        """Insert data into the database"""
        self.DBCursor.execute(query)
        self.DBConnection.commit()
    
    def delete(self, query):
        """Delete data from the database"""
        self.DBCursor.execute(query)
        self.DBConnection.commit()

    def fetchOne(self, query):
        """Return the first record from the query"""
        self.__execute(query)
        self.DBConnection.commit()
        return self.DBCursor.fetchone()
    
    def fetchAll(self, query):
        """Return all records from the query"""
        self.__execute(query)
        self.DBConnection.commit()
        return self.DBCursor.fetchall()

    def get_timestamp_from_datetime(self, timestamp: datetime):
        """return a formatted date string for a given timestamp"""
        return Helpers().get_timestamp_from_datetime(timestamp)
        
    def get_timestamp(self):
        return Helpers().get_timestamp()
    
    def get_utc_timestamp(self):
        return Helpers().get_utc_timestamp()

    def utc_from_timestamp(self, utc_timestamp):
        return Helpers().utc_from_timestamp(utc_timestamp)

    def utc_from_timestamp_to_localtime_timestamp(self, utc_timestamp: str):
        return Helpers().utc_from_timestamp_to_localtime_timestamp(utc_timestamp)
    
    def sanitise(self, target):
        """Sanitise the input from undesirable data"""
        return target.replace("'", "''").replace("\"", "\"\"").replace(";", "")


# class MSSQLModel(_Model):
#     """A Model abstraction for interacting with Microsoft SQL Server."""
#     def __init__(self):
#         setting = Settings()
#         self.DBConnection = pyodbc.connect(setting.get_setting("database.string"))
#         self.DBCursor = self.DBConnection.cursor()

class MySQLModel(_Model):
    """A Model abstraction for interacting with MySQL."""
    __user: str
    __pass: str
    __database: str
    __host: str

    def __init__(self, user, password, database="jarvis", host="127.0.0.1"):
        self.DBConnection = pymysql.connect(host=host, 
                                    charset='utf8mb4',
                                    user=user, 
                                    password=password, 
                                    db=database,
                                    autocommit=True)
        self.DBCursor = self.DBConnection.cursor()
        self.__user = user
        self.__pass = password
        self.__database = database
        self.__host = host

    def __reconnect(self):
        self.DBConnection = pymysql.connect(host=self.__host, 
                                    charset='utf8mb4',
                                    user=self.__user, 
                                    password=self.__pass, 
                                    db=self.__database,
                                    autocommit=True)
        self.DBCursor = self.DBConnection.cursor()


class Model(MySQLModel):
    """Default Model Class for Jarvis, preconfigured"""
    def __init__(self, user, password):
        MySQLModel.__init__(self, user, password)