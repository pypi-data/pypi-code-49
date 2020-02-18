#!/usr/bin/python
# coding: utf8

# Copyright 2019 Skiply
# 
from __future__ import unicode_literals

import logging
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declared_attr, as_declarative

from sqlalchemy import Column, Integer

logging.info(os.environ['SQLALCHEMY_DATABASE_URI'])
SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
logging.info(SQLALCHEMY_DATABASE_URI)

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True, pool_recycle=280, pool_size=10) # pool_size/overflow
db_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@as_declarative()
class SkiplyBase(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()