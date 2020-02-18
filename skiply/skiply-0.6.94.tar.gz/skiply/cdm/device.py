#!/usr/bin/python
# coding: utf8

# Copyright 2019 Skiply

from __future__ import unicode_literals

from datetime import datetime, timedelta

from .base import db_session, SkiplyBase

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy import and_, or_

import skiply.cdm.contract
import skiply.cdm.powerSupply


class Device(SkiplyBase):
    ''' Device '''
    __tablename__ = 'so_boitier'
    
    id = Column(Integer, primary_key=True, autoincrement=True)

    created_date = Column('dateajout', DateTime)

    device_skiply_id = Column('devicename', String(255))
    device_description = Column('description', String(500))

    lora_id = Column('lora_id', String(255))
    sigfox_id = Column('sf_id', String(255))

    device_latitude = Column('latitude', String(255))
    device_longitude = Column('longitude', String(255))
    device_battery_level = Column('battery_level', String(255))

    device_button1_label = Column('label_button1', String(255))
    device_button2_label = Column('label_button2', String(255))
    device_button3_label = Column('label_button3', String(255))
    device_button4_label = Column('label_button4', String(255))
    device_button5_label = Column('label_button5', String(255))

    device_last_swipe = Column('last_badge', DateTime)
    device_last_transmission = Column('last_transmission', DateTime)
    device_last_data_transmission = Column('last_data', DateTime)

    device_status = Column('status', String(100), default="IN-STOCK")

    device_type = Column('device_type', String(255), default="satisfaction")


    device_erp_ref = Column('skpf', String(255))


    billable = Column('billable', Boolean(), default=False)
    commissioning_on = Column('commissioning_on', DateTime, default=None)
    data_from_api = Column('data_from_api', Boolean(), default=False)


    entity_id = Column('client_id', Integer, ForeignKey("so_client.id"), nullable=False)

    group_id = Column('groupe_id', Integer, ForeignKey("so_groupe.id"), nullable=False)

    keyboard_id = Column('frontage_id', Integer, ForeignKey("so_frontage.id"), nullable=False)

    question_id = Column('question_id', Integer, ForeignKey("so_question.id"), nullable=False)

    network_id = Column('network_id', Integer, ForeignKey("so_network.id"), nullable=False)

    brand = Column('brand', String(255), nullable=False, default='Skiply')
    model = Column('model', String(255))
    version = Column('version', String(255))

    def __init__(self, 
        created_date,
        skiply_id, device_description, lora_id, sigfox_id, 
        device_latitude, device_longitude, device_battery_level,
        device_button1_label, device_button2_label, device_button3_label, device_button4_label, device_button5_label,
        device_last_swipe, device_last_transmission, device_last_data_transmission,
        device_status,
        device_type,
        device_erp_ref, 
        billable, commissioning_on, data_from_api,
        entity_id, group_id, keyboard_id, question_id, network_id):
        self.created_date = created_date

        self.device_skiply_id = skiply_id
        self.device_description = device_description
        self.lora_id = lora_id
        self.sigfox_id = sigfox_id

        self.device_latitude = device_latitude
        self.device_longitude = device_longitude
        self.device_battery_level = device_battery_level

        self.device_button1_label = device_button1_label
        self.device_button2_label = device_button2_label
        self.device_button3_label = device_button3_label
        self.device_button4_label = device_button4_label
        self.device_button5_label = device_button5_label

        self.device_last_swipe = device_last_swipe
        self.device_last_transmission = device_last_transmission
        self.device_last_data_transmission = device_last_data_transmission

        self.device_status = device_status

        self.device_type = device_type

        self.device_erp_ref = device_erp_ref

        self.billable = billable
        self.commissioning_on = commissioning_on
        self.data_from_api = data_from_api

        self.entity_id = entity_id
        self.group_id = group_id
        self.keyboard_id = keyboard_id
        self.question_id = question_id
        self.network_id = network_id

    def __repr__(self):
        return '<Device %r>' % (self.device_skiply_id)

def device_exists(device_skiply_id):
    return get_device_from_skiply_id(device_skiply_id) is not None

def get_devices():
    session = db_session()
    try:
        results = session.query(Device).all()
    except:
        print("DB Request get_devices() Failed")
        results=None
    finally:
        session.close()

    return results

def get_devices_to_monitor(hours_start, hours_end, power_threshold, power_threshold_percent, default_monitoring):
    results = None;

    deltatime_start = datetime.now() - timedelta(hours=hours_start)
    deltatime_end = datetime.now() - timedelta(hours=hours_end)
  
    power = str(hex(power_threshold))
    if (not power.startswith("0x")):
        power = "0x"+power
    while (len(power) < 6):
        power = power[:2] + '0' + power[2:]
    print(power)
    
    session = db_session()
    try:
        if default_monitoring:
            #print("get_devices_to_monitor(hours_start, hours_end, power_threshold, power_threshold_percent, default_monitoring) : Start request contract/service")
            res_notin = skiply.cdm.contract.get_contract_with_service_code("CUSTOM_MONITORING")
            if res_notin is not None and len(res_notin)>0:
                ids = []
                for res in res_notin:
                    ids.append(res.entity_id)
                #print("get_devices_to_monitor(hours_start, hours_end, power_threshold, power_threshold_percent, default_monitoring) : Start request devices for all entities excluded {}".format(res_notin))
                # Get devices which did not emit since hours_end
                results_1 = session.query(Device).filter(Device.device_status == 'IN-SERVICE', Device.entity_id.notin_(ids)).filter(Device.device_last_transmission != None, Device.device_last_transmission > deltatime_start, Device.device_last_transmission <= deltatime_end).all()
                print('DEVICE 1 RESULTS: %s' % results_1)
                if results_1 is not None and len(results_1) > 0:
                    results = {}
                    for res in results_1:
                        results[res.device_skiply_id] = [res, None]
                
                try :
                    # Get devices with a power level under power_threshold or power_threshold_percent
                    power_results = skiply.cdm.powerSupply.get_powerSupply_with_level_under(hours_start, hours_end, power_threshold, power_threshold_percent)
                    print('POWER SUPPLY RESULTS: %s' % power_results)

                    if power_results is not None and len(power_results) > 0 :
                        try:
                            device_skiply_ids = {}
                            for res in power_results:
                                device_skiply_ids[res.device_skiply_id] = res

                            results_2 = session.query(Device).filter(Device.device_status == 'IN-SERVICE', Device.device_skiply_id.in_(device_skiply_ids.keys())).all()
                            print('DEVICE 2 RESULTS: %s' % results_2)

                            if results_2 is not None and len(results_2) > 0 :
                                if results is None:
                                    results = {}

                                for res in results_2:
                                    results[res.device_skiply_id] = [res, device_skiply_ids[res.device_skiply_id]]
                        except Exception as e:
                            print("DB Request get_devices_to_monitor(hours_start, hours_end, power_threshold, power_threshold_percent, default_monitoring) Failed with error : {}".format(e))
                            results=None
                        finally:
                            session.close()
                except Exception as e:
                    print("DB Request get_devices_to_monitor(hours_start, hours_end, power_threshold, power_threshold_percent, default_monitoring) Failed with error : {}".format(e))
                    results=None
                finally:
                    session.close()
            else:
                print("get_devices_to_monitor(hours_start, hours_end, power_threshold, power_threshold_percent, default_monitoring) : Start request devices")
                results = session.query(Device).filter(Device.device_last_transmission != None, Device.device_last_transmission > deltatime_start).filter(or_(Device.device_last_transmission <= deltatime_end, func.concat("0x", func.substr(Device.device_battery_level, 5, 4)) <= power)).all()
                
    except Exception as e:
        print("DB Request get_devices_to_monitor(hours_start, hours_end, power_threshold, power_threshold_percent, default_monitoring) Failed with error : {}".format(e))
        results=None
    finally:
        session.close()

    return results

def get_devices_lastTransmission_between(hours_start, hours_end):
    deltatime_start = datetime.now() - timedelta(hours=hours_start)
    print(deltatime_start)
    deltatime_end = datetime.now() - timedelta(hours=hours_end)
    print(deltatime_end)

    session = db_session()
    try:
        results = session.query(Device).filter((Device.device_last_transmission != None), (Device.device_last_transmission <= deltatime_start), (Device.device_last_transmission > deltatime_end)).all()
    except Exception as e:
        print("DB Request get_devices_lastTransmission_between(hours_start, hours_end) Failed with error : {}".format(e))
        results=None
    finally:
        session.close()

    return results

def get_devices_w_low_power(threshold_power):
    session = db_session()
    try:
        results = session.query(Device).filter((Device.device_battery_level != None), func.hex(func.substr(Device.device_battery_level, 4, 8)) <= hex(threshold_power)).all()
    except Exception as e:
        print("DB Request get_devices_w_low_power(threshold_power) Failed with error : {}".format(e))
        results=None
    finally:
        session.close()

    return results

def get_device(device_id):
    session = db_session()
    try:
        results = session.query(Device).filter(Device.id == device_id).first()
    except Exception as e:
        print("DB Request get_device(device_id) Failed with error : {}".format(e))
        results=None
    finally:
        session.close()

    return results

def get_device_from_skiply_id(device_skiply_id):
    session = db_session()
    try:
        results = session.query(Device).filter(Device.device_skiply_id == device_skiply_id).first()
    except Exception as e:
        print("DB Request get_device_from_skiply_id(device_skiply_id) Failed with error : {}".format(e))
        results=None
    finally:
        session.close()

    return results

def get_device_from_network_id(network_id):
    session = db_session()
    try:
        results = session.query(Device).filter((Device.sigfox_id == network_id) | (Device.lora_id == network_id)).first()
    except Exception as e:
        print("DB Request get_device_from_network_id(network_id) Failed with error : {}".format(e))
        results=None
    finally:
        session.close()

    return results

def get_device_from_skiply_id(device_skiply_id):
    session = db_session()
    try:
        results = session.query(Device).filter(Device.device_skiply_id == device_skiply_id).first()
    except Exception as e:
        print("DB Request get_device_from_skiply_id(device_skiply_id) Failed with error : {}".format(e))
        results=None
    finally:
        session.close()

    return results

def get_devices_of_entity(entity_id):
    session = db_session()
    try:
        results = session.query(Device).filter(Device.entity_id == entity_id).all()
    except Exception as e:
        print("DB Request get_devices_of_entity(entity_id) Failed with error : {}".format(e))
        results=None
    finally:
        session.close()

    return results

def update_device(device_skiply_id, device_desc, entity_id, group_id=None): 
    session = db_session()
    try:
        d = session.query(Device).filter(Device.device_skiply_id == device_skiply_id).first()

        if (d is not None):
            if ((entity_id is not None) & (d.entity_id != entity_id)):
                d.entity_id = entity_id
            if ((device_desc is not None) & (d.device_description != device_desc)):
                d.device_description = device_desc
            if ((group_id is not None) & (d.group_id != group_id)):
                d.group_id = group_id
            if not d.data_from_api:
                d.data_from_api = True
            if not d.device_status == "IN-SERVICE":
                d.device_status = "IN-SERVICE"

        session.commit()
    except Exception as e:
        print("DB Request update_device(device_skiply_id, device_desc, entity_id, group_id=None) Failed with error : {}".format(e))
        session.rollback()
    finally:
        session.close()
