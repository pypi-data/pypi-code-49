#!/usr/bin/python
# coding: utf8

# Copyright 2019 Skiply

from __future__ import unicode_literals


from .base import db_session, SkiplyBase

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, JSON

import datetime


class EventLog(SkiplyBase):
    ''' Event Log '''
    __tablename__ = 'so_event_log'
    

    LOG = 'Log'
    EXCEPTION = 'Exception'

    TYPE_INSTALLATION = 'Installation'

    id = Column(Integer, primary_key=True, autoincrement=True)

    log_flag = Column('log_flag', String(64), nullable=False)
    log_message = Column('log_message', JSON)
    log_timestamp = Column('log_timestamp', DateTime, default=datetime.datetime.utcnow, nullable=False)
    log_type = Column('event_type', String(64), nullable=False)

    device_skiply_id = Column('device_skiply_id', String(255), nullable=False)

    def __init__(self, device_id, log_type, log_flag, log_message):
        self.device_skiply_id = device_id

        self.log_type = log_type
        self.log_flag = log_flag

        self.log_message = log_message

    def __repr__(self):
        return '<EventLog %r>' % (self.id)

def get_log(log_id):
    session = db_session()
    try:
        results = session.query(EventLog).filter(EventLog.id == log_id).first()
    except:
        print("DB Request get_log(log_id) Failed")
        results=None
    finally:
        session.close()

    return results

def get_logs(log_type, nb_log):
    session = db_session()
    try:
        results = session.query(EventLog).filter(EventLog.log_type == log_type).order_by(EventLog.log_timestamp.desc()).limit(nb_log).all()
    except:
        print("DB Request get_logs(log_type, nb_log) Failed")
        results=None
    finally:
        session.close()

    return results

def add_log(device_id, log_type, log_flag, log_message):
    session = db_session()
    try:
        log = EventLog(device_id, log_type, log_flag, log_message)
        session.add(log)
        session.commit()
    except:
        print("DB Request add_log(device_id, log_type, log_flag, log_message) Failed - ROLLBACK")
        session.rollback()
    finally:
        session.close()