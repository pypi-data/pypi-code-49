#!/usr/bin/python
# coding: utf8

# Copyright 2019 Skiply

from __future__ import unicode_literals


from .base import db_session, SkiplyBase

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, JSON

import datetime


class InstallationInstruction(SkiplyBase):
    ''' Event Log '''
    __tablename__ = 'i_install_instructions'

    id = Column(Integer, primary_key=True, autoincrement=True)

    inst_label = Column('label', String(200), nullable=False)
    inst_created_on = Column('created_on', DateTime, default=datetime.datetime.utcnow, nullable=False)
    inst_product_type = Column('product_type',String(20), default='SATISFACTION', nullable=False)

    def __init__(self, inst_label):
        self.inst_label = inst_label

    def __repr__(self):
        return '<Installation instruction %r>' % (self.inst_label)


def get_installation_instruction(install_inst_id):
    session = db_session()
    try:
        results = session.query(InstallationInstruction).filter(InstallationInstruction.id == install_inst_id).first()
    except:
        print("DB Request get_installation_instruction(install_inst_id) Failed")
        results = None
    finally:
        session.close()

    return results

def get_installation_instruction_from_type(type):
    session = db_session()
    try:
        results = session.query(InstallationInstruction).filter(InstallationInstruction.inst_product_type == type).first()
    except:
        print("DB Request get_installation_instruction_from_type(type) Failed")
        results = None
    finally:
        session.close()

    return results

def get_installation_instructions():
    session = db_session()
    try:
        session.query(InstallationInstruction).all()
    except:
        print("DB Request get_installation_instructions() Failed")
        results = None
    finally:
        session.close()

    return results