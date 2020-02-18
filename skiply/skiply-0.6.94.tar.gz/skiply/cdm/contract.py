#!/usr/bin/python
# coding: utf8

# Copyright 2019 Skiply

from __future__ import unicode_literals


from .base import db_session, SkiplyBase

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from skiply.cdm.associationContractService import AssociationContractService
from skiply.cdm.service import Service

import skiply.cdm.service


class Contract(SkiplyBase):
    ''' Device '''
    __tablename__ = 'so_contract'
    
    id = Column(Integer, primary_key=True, autoincrement=True)

    entity_id = Column('client_id', Integer, ForeignKey("so_client.id"), nullable=False)

    external_id = Column('external_id', String())

    contract_start_date = Column('start', DateTime())
    contract_end_date = Column('end', DateTime())

    contract_label = Column('description', String())

    services = relationship('AssociationContractService', back_populates="contract")

    def __init__(self, entity_id, external_id, contract_start_date, contract_end_date, contract_label, service):
        self.entity_id = entity_id

        self.external_id = external_id

        self.contract_start_date = contract_start_date
        self.contract_end_date = contract_end_date

        self.contract_label = contract_label

        self.services = services

    def __repr__(self):
        return '<Contract %r>' % (self.contract_label)

def get_contract(contract_id):
    session = db_session()
    try:
        results = session.query(Contract).filter(Contract.id == contract_id).first()
    except Exception as e:
        print("DB Request get_contract(contract_id) Failed with error : {}".format(e))
        results=None
    finally:
        session.close()

    return results

def get_contract(contract_id):
    session = db_session()
    try:
        results = session.query(Contract).filter(Contract.id == contract_id).first()
    except Exception as e:
        print("DB Request get_contract(contract_id) Failed with error : {}".format(e))
        results=None
    finally:
        session.close()

    return results

def get_contracts_for_service(service_id):
    session = db_session()
    try:
        if service_id != None:
            results = session.query(AssociationContractService).join(Contract).join(Service).filter(Service.id == service_id).all()
        else: 
            results = None
    except Exception as e:
        print("DB Request get_contracts_for_services(service_ids) Failed with error : {}".format(e))
        results = None
    finally:
        session.close()

    return results

def get_contract_with_service_code(service_code):
    session = db_session()
    try:
        print("DB Request get_contract_with_service_code(service_code) : %s" % service_code)
        # Get service with code <service_code>
        service_results = skiply.cdm.service.get_service_from_code(service_code);
        if service_results != None and len(service_results)==1:
            service_id = service_results[0].id;

            # Get contract_id 
            assoc_results = get_contracts_for_service(service_id);

            if assoc_results != None and len(assoc_results) == 1:
                results = session.query(Contract).filter(Contract.id == assoc_results[0].contract_id).all()
            else:
                print("DB Request get_contract_with_service_code(service_code) : No contract associated to service {}".format(service_code))
                results = None
        else:
            print("DB Request get_contract_with_service_code(service_code) : No service {} found".format(service_code))
            results = None
    except Exception as e:
        print("DB Request get_contract_with_service_code(service_code) Failed with error : {}".format(e))
        results = None
    finally:
        session.close()

    return results
