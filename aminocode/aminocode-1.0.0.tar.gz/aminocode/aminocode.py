#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import unidecode
import numpy as np

aminoCode_table = {
      "a": "YA",
      "b": "E",
      "c": "C",
      "d": "D",
      "e": "YE",
      "f": "F",
      "g": "G",
      "h": "H",
      "i": "YI",
      "j": "I",
      "k": "K",
      "l": "L",
      "m": "M",
      "n": "N",
      "o": "YQ",
      "p": "P",
      "q": "Q",
      "r": "R",
      "s": "S",
      "t": "T",
      "u": "YV",
      "v": "V",
      "x": "W",
      "z": "A",
      "w": "YW",
      "y": "YY",
      ".": "YP",
      "9": "YD",
      " ": "YS",
}

aminoCode_table_d = {
      "0": "YDA",
      "1": "YDQ",
      "2": "YDT",
      "3": "YDH",
      "4": "YDF",
      "5": "YDI",
      "6": "YDS",
      "7": "YDE",
      "8": "YDE",
      "9": "YDN",
}

aminoCode_table_p = {
      ".": "YPE",
      ",": "YPC",
      ";": "YPS",
      "!": "YPW",
      "?": "YPQ",
      ":": "YPT",
}

def details(text,all_tables):
    table = dict()
    for i in all_tables:
        table.update(i)
    for k,v in table.items():
        text = text.replace(k, v)
    return text        

def encodetext(text,detailing=''):
    det = detailing
    try:
        text = text.decode('utf-8') #decode
    except:
        pass
    
    text = unidecode.unidecode(text) #remove accents
    text = text.lower() #lower case
    text = re.sub('\s',' ',text) #all spaces to " "
    
    # apply expanded coding
    all_tables = []
    if 'd' in det:
        all_tables.append(aminoCode_table_d)
    else:
        text = re.sub('\d','9',text) #all numbers to 9
    if 'p' in det:
        all_tables.append(aminoCode_table_p)
    else:
        text = re.sub('[,;!?:]','.',text) #all punctuation to "."
    if len (all_tables) > 0:
        text = details(text,all_tables)
        
    # apply minimal coding
    for k,v in aminoCode_table.items():
        text = text.replace(k, v)
        
    # apply joker 
    for c,i in enumerate(text.lower()):
        if i not in aminoCode_table:
            text=re.sub('\\'+i,'YK',text)
    return (text)
et = encodetext

def details_r(text,all_tables):
    table = dict()
    mm = ''
    for i in all_tables:
        table.update(i)
        m = list(i.values())[0]
        m = m[1]
        mm += m
    for key,value in table.items():
        if re.search('Y['+mm+']\w',value):
            text = re.sub(value,key,text)
    return text
    
def decodetext(text,detailing=''):
    det = detailing
    all_tables = []
    if 'd' in det:
        all_tables.append(aminoCode_table_d)
    if 'p' in det:
        all_tables.append(aminoCode_table_p)
    if len (all_tables) > 0:
        text = details_r(text,all_tables)
        
    for key,value in aminoCode_table.items():
        if re.search('Y\w',value):
            text = re.sub(value,key,text)
    text = re.sub('YK','-',text)
    for key,value in aminoCode_table.items():
        text = re.sub(value,key,text)
    return text
dt = decodetext