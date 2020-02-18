#!/usr/bin/python
# coding: utf8

# Copyright 2019 Skiply

from __future__ import unicode_literals


from .base import db_session, SkiplyBase

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, JSON

import datetime


class AssociationInstallDeviceGroup(SkiplyBase):
    ''' Event Log '''
    __tablename__ = 'i_install_device'

    install_id = Column(Integer, ForeignKey("i_installs.id"), primary_key=True)

    device_skiply_id = Column(String(255), ForeignKey('so_boitier.devicename'), primary_key=True)

    last_checkNetwork = Column(DateTime, default=None)
    last_checkNetwork_quality = Column(String(10), default=None)

    def __init__(self, install_id, device_skiply_id):
        self.install_id = install_id
        self.device_skiply_id = device_skiply_id

    def __repr__(self):
        return '<Association installation/device %r/%s>' % (self.install_id, self.device_skiply_id)


def addAssociationInstallDeviceGroup(install_id, device_id, checkNetowk=False, checkNetowk_quality=None):
    session = db_session()
    ass = session.query(AssociationInstallDeviceGroup).filter(AssociationInstallDeviceGroup.install_id == install_id, AssociationInstallDeviceGroup.device_skiply_id == device_id)
    
    if (ass.count() == 0):
        try:
            ass = AssociationInstallDeviceGroup(install_id,device_id)
            
            session.merge(ass)
            session.commit()
        except:
            session.rollback()
        finally:
            session.close()
    elif ass.count() == 1 and checkNetowk:
        a = ass.first()
        try:
            a.last_checkNetwork = datetime.datetime.utcnow()
            if a.last_checkNetwork_quality != checkNetowk_quality:
                a.last_checkNetwork_quality = checkNetowk_quality
            session.commit()
        except:
            session.rollback()
        finally:
            session.close()

def getDeviceForInstall(install_id, device_id):
    session = db_session()
    try:
        results = session.query(AssociationInstallDeviceGroup).filter(AssociationInstallDeviceGroup.install_id == install_id, AssociationInstallDeviceGroup.device_skiply_id == device_id).first()
    except:
        print("DB Request getDeviceForInstall(install_id, device_id) Failed")
        results = None
    finally:
        session.close()

    return results

def getDevicesForInstall(install_id):
    session = db_session()
    try:
        results = session.query(AssociationInstallDeviceGroup).filter(AssociationInstallDeviceGroup.install_id == install_id).all()
    except:
        print("DB Request getDevicesForInstall(install_id) Failed")
        results = None
    finally:
        session.close()

    return results
