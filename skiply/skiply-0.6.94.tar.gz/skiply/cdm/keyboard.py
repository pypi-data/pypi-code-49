#!/usr/bin/python
# coding: utf8

# Copyright 2019 Skiply

from __future__ import unicode_literals


from .base import db_session, SkiplyBase

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String


class Keyboard(SkiplyBase):
    ''' Device '''
    __tablename__ = 'so_frontage'
    
    id = Column(Integer, primary_key=True, autoincrement=True)

    keyboard_label = Column('label', String(255))
    keyboard_type = Column('type', Integer)

    def __init__(self, keyboard_label, keyboard_type):
        self.keyboard_label = keyboard_label
        self.keyboard_type = keyboard_type

    def __repr__(self):
        return '<Keyboard %r>' % (self.keyboard_label)

def get_keyboard(keyboard_id):
    session = db_session()
    try:
        results = session.query(Keyboard).filter(Keyboard.id == keyboard_id).first()
    except:
        print("DB Request get_keyboard(keyboard_id) Failed")
        results = None
    finally:
        session.close()

    return results