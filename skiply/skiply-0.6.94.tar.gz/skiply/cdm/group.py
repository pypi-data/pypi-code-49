#!/usr/bin/python
# coding: utf8

# Copyright 2019 Skiply

from __future__ import unicode_literals


from .base import db_session, SkiplyBase

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String


class Group(SkiplyBase):
    ''' Device '''
    __tablename__ = 'so_groupe'
    
    id = Column(Integer, primary_key=True, autoincrement=True)

    group_label = Column('group_name', String(255))
    group_description = Column('description', String())

    send_api = Column('send_api', Boolean, default=False)
    push_url = Column('push_url', String(255))
    push_url_header = Column('push_url_header', String(1000))

    entity_id = Column('client_id', Integer, ForeignKey("so_client.id"), nullable=False)

    def __init__(self, 
        group_label, group_description,
        send_api, push_url, push_url_header,
        entity_id):
        self.group_label = group_label
        self.group_description = group_description

        self.send_api = send_api
        self.push_url = push_url
        self.push_url_header = push_url_header

        self.entity_id = entity_id

    def __repr__(self):
        return '<Group %r>' % (self.group_label)

def get_group(group_id):
    session = db_session()
    try:
        results = session.query(Group).filter(Group.id == group_id).first()
    except:
        print("DB Request get_group(group_id) Failed")
        results=None
    finally:
        session.close()

    return results

def get_groups_of_entity(entity_id):
    session = db_session()
    try:
        results = session.query(Group).filter(Group.entity_id == entity_id).all()
    except:
        print("DB Request get_groups_of_entity(entity_id) Failed")
        results=None
    finally:
        session.close()

    return results