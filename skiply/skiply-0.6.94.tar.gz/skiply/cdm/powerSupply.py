#!/usr/bin/python
# coding: utf8

# Copyright 2019 Skiply

from __future__ import unicode_literals

from datetime import datetime, timedelta

from .base import db_session, SkiplyBase

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy import and_, or_


class PowerSupply(SkiplyBase):
    ''' Device '''
    __tablename__ = 'so_power_supply'
    
    id = Column(Integer, primary_key=True, autoincrement=True)

    power_time = Column('time', DateTime, nullable=False)
    power_voltage = Column('voltage', Integer, nullable=False)
    power_voltage_idle = Column('voltage_idle', Integer, nullable=False)
    power_voltage_percentage = Column('voltage_percentage', Integer, nullable=False)

    device_id = Column('device_id', Integer, nullable=False)
    device_skiply_id = Column('device_name', String(255))

    def __init__(self, power_time, power_voltage, device_id, device_skiply_id):
        self.power_time = power_time
        self.power_voltage = power_voltage

        self.device_id = device_id
        self.device_skiply_id = device_skiply_id

    def __repr__(self):
        return '<Power Supply %s - %s>' % (self.power_time, self.power_voltage)

def get_powerSupply(powerSupply_id):
    session = db_session()
    try:
        results = session.query(PowerSupply).filter(PowerSupply.id == powerSupply_id).first()
    except:
        print("DB Request get_powerSupply(powerSupply_id) Failed")
        results = None
    finally:
        session.close()

    return results

def get_powerSupply_with_level_under(hours_start, hours_end, power_threshold, power_threshold_percent):
    deltatime_start = datetime.now() - timedelta(hours=hours_start)
    deltatime_end = datetime.now() - timedelta(hours=hours_end)
    
    session = db_session()
    try:
        results = session.query(func.max(PowerSupply.power_time), PowerSupply.power_voltage, PowerSupply.power_voltage_idle, PowerSupply.power_voltage_percentage, PowerSupply.device_id, PowerSupply.device_skiply_id).filter(PowerSupply.power_time >= deltatime_start).group_by(PowerSupply.device_skiply_id).having(or_(and_(PowerSupply.power_voltage <= power_threshold, PowerSupply.power_voltage > 0, PowerSupply.device_skiply_id.notlike('SA%')), and_(PowerSupply.power_voltage <= power_threshold, PowerSupply.power_voltage > 0, PowerSupply.device_skiply_id.like('SA%'), func.max(PowerSupply.power_time) < deltatime_end), and_(PowerSupply.power_voltage_percentage <= power_threshold_percent, PowerSupply.power_voltage_percentage > 0))).all()
    except:
        print("DB Request get_powerSupply(powerSupply_id) Failed")
        results = None
    finally:
        session.close()

    return results