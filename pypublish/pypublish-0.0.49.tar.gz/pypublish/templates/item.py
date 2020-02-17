#!/usr/bin/env python2.7
#coding:utf-8

import codecs
import hjson

class Item(object):

  def __init__(self):
    self.name = ""
    self.surnames = ""

  def fullName (self):
    return (self.name if self.name is not None else "") + " " + (self.surnames if self.surnames is not None else "")

  @staticmethod
  def load (data):
    result = Item()

    dataObj = {}
    if type(data) == 'str':
      fp = codecs.open(data, mode='r', encoding='utf-8')
      dataObj = hjson.load(fp)
    elif type(data) == 'dict' or isinstance(data, dict):
      dataObj = data

    result.name = dataObj['name'] if 'name' in dataObj else None
    result.surnames = dataObj['surnames'] if 'surnames' in dataObj else None

    return result
