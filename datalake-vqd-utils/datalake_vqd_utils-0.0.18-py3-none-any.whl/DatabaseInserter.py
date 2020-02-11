import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy.types import (Integer, String, DateTime, TypeDecorator,
                              JSON, TEXT, Enum, TIMESTAMP, Float, Unicode,
                             Boolean, Numeric)
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import FlushError
import hashlib
from models import Base, User, Person, PersonAddress, Transaction, Block
import pandas as pd

class SQLAlchemyInserter:
    """
    Takes records (list of dictionaries) and inserts them into a database using a list of targets
    """
    def __init__(self, database_url):
        self.database_url = database_url
        self.engine = self.set_engine()
        self.connection = self.engine.connect()
        self.session = self.make_database_session()
        self.upload_queue = []

    def set_engine(self):
        """
        Set engine
        """
        return create_engine(self.database_url)

    def make_database_session(self):
        """
        Make database session from sqlalchemy engine
        """
        return Session(bind=self.engine)

    def add_to_upload_queue(self, records, table, orm_model=None):
        if orm_model == None:
            orm_model = self.infer_orm_model(table)

        upload_object = {
            'records_hash' : self.compute_hash(records),
            'records_count' : self.count_records(records),
            'records_size' : self.get_size(records),
            'data' : records,
            'table' : table,
            'orm_model' : orm_model
        }
        self.upload_queue.append(upload_object)

    def infer_orm_model(self, table):
        """
        Infers SQLAlchemy ORM model from database schema of table
        """
        Base = automap_base()
        Base.prepare(self.engine, reflect=True)
        orm_model = Base.classes[table]
        return orm_model

    def get_orm_dtypes(self, orm_model):
        """
        Takes SQLAlchemy ORM model and returns dictionary of python datatypes { column_name : column_type }
        """
        orm_dtypes = { cName : self.convert_orm_dtypes(cValue.type) for cName, cValue in orm_model.__table__.columns.items()}
        return orm_dtypes

    def convert_orm_dtypes(self, SQLAlchemyDatatype):
        """
        Converts SQLAlchemy datatype to pandas datatype
        """
        if isinstance(SQLAlchemyDatatype, Integer):
            return "int64"
        elif isinstance(SQLAlchemyDatatype, DateTime):
            return "datetime64[ns]"
        elif isinstance(SQLAlchemyDatatype, Float):
            return "float64"
        elif isinstance(SQLAlchemyDatatype, Unicode):
            return "unicode"
        elif isinstance(SQLAlchemyDatatype, String):
            return "unicode"
        else:
            raise ValueError("Datatype {} not recognized".format(SQLAlchemyDatatype))

    def get_orm_columns(self, orm_model):
        """
        Retrieve columns from ORM model
        """
        return list(orm_model.__table__.columns.keys())

    def insert_or_update_to_database(self, record, orm_model):
        instance = orm_model(**record)
        try:
            print(f"Adding instance to table, table {orm_model.__tablename__}")
            self.session.add(instance)
            self.session.commit()
        except (IntegrityError, FlushError) as e:
            print(f"Exception {e} caused rollback, checking chronology of events")
            self.session.rollback()
            try:
                primary_key = instance.id
                if primary_key is None:
                    print(f"Record with ID None: {record}")
                print(f"ID {primary_key} was already present in table {orm_model.__tablename__}, checking chronology")
                row = self.session.query(orm_model).filter(orm_model.id == primary_key).first()
                try:
                    old_event_time = pd.to_datetime(row.modified).replace(tzinfo=None)
                    current_event_time = pd.to_datetime(instance.modified).replace(tzinfo=None)
                    print(f"Current event was modified at {current_event_time}, old event was modified at {old_event_time}")
                except Exception:
                    print(f"Event {orm_model.__tablename__} does not have a modified field, using created instead.")
                    old_event_time = pd.to_datetime(row.created).replace(tzinfo=None)
                    current_event_time = pd.to_datetime(instance.created).replace(tzinfo=None)
                    print(f"Current event was created at {current_event_time}, old event was created at {old_event_time}")
                newer = current_event_time > old_event_time
                self.session.query(orm_model).filter(orm_model.id == primary_key).update(record)
                self.session.commit()
                if not newer:
                    print(f"event was older than previously inserted data, event has been discarded")
            except Exception as e:
                print(record)
                print("Instance is missing fields")
                self.session.rollback()
                raise(e)
                        
    def insert_or_update_all(self):
        total_len = len(self.upload_queue)
        counter = 0
        for upload_object in self.upload_queue:
            counter = counter + 1 
            print(f"Uploading object {counter} out of {total_len}")
            for record in upload_object['data']:
                self.insert_or_update_to_database(
                    record=record,
                    orm_model=upload_object['orm_model']
                )
            print("All objects in queue have been processed.")


    def push_to_database(self, records, orm_model, table, record_count):
        """
        Push records to database
        """
        try:
            self.session.bulk_insert_mappings(orm_model, records)
            self.session.commit()
            print('Inserted {} records of size into table "{}"'.format(record_count, table))
        except:
            self.session.rollback()
            raise
        finally:
            self.session.close()

    def push_all_to_database(self):
        """
        Push all records of SQLAlchemyInsert instance to database
        """
        for upload_object in self.upload_queue:
            self.push_to_database(
                    records = upload_object['data'],
                    orm_model = upload_object['orm_model'],
                    table = upload_object['table'],
                    record_count = upload_object['records_count']
            )

    def sort_upload_queue(self, ascending=True, key='record_count'):
        if ascending == True:
            reverse = False
        elif ascending == False:
            reverse = True

        sorted_queue = sorted(self.upload_queue, key=lambda k: k[key], reverse=reverse)
        self.upload_queue = sorted_queue

    def count_records(self, records):
        return len(records)

    def get_size(self, obj, seen=None, unit=None):
        """
        Recursively finds size of objects and returns bytes
        """
        size = sys.getsizeof(obj)
        if seen is None:
            seen = set()
        obj_id = id(obj)
        if obj_id in seen:
            return 0
        # Important mark as seen *before* entering recursion to gracefully handle
        # self-referential objects
        seen.add(obj_id)
        if isinstance(obj, dict):
            size += sum([self.get_size(v, seen) for v in obj.values()])
            size += sum([self.get_size(k, seen) for k in obj.keys()])
        elif hasattr(obj, '__dict__'):
            size += self.get_size(obj.__dict__, seen)
        elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
            size += sum([self.get_size(i, seen) for i in obj])

        return self.transform_byte_size(size, unit=unit)

    def transform_byte_size(self, byte_size, unit=None):
        byte_size = float(byte_size)
        if unit == None:
            return byte_size
        elif unit == 'kb':
            return byte_size / 10**3
        elif unit == 'Mb':
            return byte_size / 10**6
        elif unit == 'Gb':
            return byte_size / 10**9
        elif unit == 'Tb':
            return byte_size / 10**12
        else:
            raise ValueError("Unit unknown to function")

    def compute_hash(self, obj):
        """
        Compute Sha1 hexadecimal hash string from object
        """
        hash_object = hashlib.sha1(str(obj).encode())
        return hash_object.hexdigest()

    @property
    def queue_size(self, unit=None):
        size = 0.0
        for upload_object in self.upload_queue:
            size += self.transform_byte_size(upload_object['records_size'], unit=unit)
        return size

    @property
    def queue_tables(self):
        return [upload_object['table'] for upload_object in self.upload_queue]

    @property
    def queue_length(self):
        return len(self.upload_queue)

class PyMongoInserter(SQLAlchemyInserter):
    def push_bulk_to_database(self):
        return True   
