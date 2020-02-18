#!/usr/bin/python
# coding: utf8

# Copyright 2019 Skiply

from __future__ import unicode_literals


from .base import db_session, SkiplyBase

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from skiply.cdm.associationContractService import AssociationContractService


class Service(SkiplyBase):
    ''' Device '''
    __tablename__ = 'so_service'
    
    id = Column(Integer, primary_key=True, autoincrement=True)

    created_date = Column('createdAt', DateTime())

    service_code = Column('code', String(255))
    service_enabled = Column('enabled', Boolean())
    service_label = Column('description', String())
    service_type = Column('type', String(255))

    contracts = relationship('AssociationContractService', back_populates="service")


    def __init__(self, created_date, service_code, service_enabled, service_label, service_type):
        self.created_date = created_date

        self.service_code = service_code
        self.service_enabled = service_enabled
        self.service_label = service_label
        self.service_type = service_type

    def __repr__(self):
        return '<Service %r>' % (self.service_label)

def get_service(service_id):
    session = db_session()
    try:
        results = session.query(Service).filter(Service.id == service_id).first()
    except Exception as e:
        print("DB Request get_service(service_id) Failed with error : {}".format(e))
        results=None
    finally:
        session.close()

    return results

def get_service_from_code(service_code):
    session = db_session()
    try:
        results = session.query(Service).filter(Service.service_code == service_code).all()
    except Exception as e:
        print("DB Request get_service_from_code(service_code) Failed with error : {}".format(e))
        results=None
    finally:
        session.close()

    return results
        