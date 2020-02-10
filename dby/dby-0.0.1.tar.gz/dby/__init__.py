#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 14:06:37 2020

@author: fblavoie
"""

import os, os.path
import pickle
import urllib.request as ur

url = "http://bochats.ddns.net:8991/GetFile/"


def get_obs(file_id,obs_name):    
    file_id = str(file_id)
    action = "get_obs"
    args = {"file_id":file_id,"obs_name":obs_name}
    data = {"action":action,"args":args}
    data = pickle.dumps(data)
    res = ur.urlopen(url,data=data).read()
    return pickle.loads(res)
    

#%% Get param

def get_param(file_id,obs_name):
    file_id = str(file_id)
    action = "get_param"
    args = {"file_id":file_id,"obs_name":obs_name}
    data = {"action":action,"args":args}
    data = pickle.dumps(data)
    res = ur.urlopen(url,data=data).read()
    return pickle.loads(res)
    

    
#%% Set Parameter

def set_param(file_id,param_name,param_value):

    file_id = str(file_id)
    action = "set_param"
    args = {"file_id":file_id,"param_name":param_name,"param_value":param_value}
    data = {"action":action,"args":args}
    data = pickle.dumps(data)
    res = ur.urlopen(url,data=data).read()
    return pickle.loads(res)
    


#%% Save file

def save_file(file_id,file_name,value):

    file_id = str(file_id)
    action = "save_file"
    args = {"file_id":file_id,"file_name":file_name,"value":value}
    data = {"action":action,"args":args}
    data = pickle.dumps(data)
    res = ur.urlopen(url,data=data).read()
    return pickle.loads(res)

    
def load_file(file_id,file_name):
    
    file_id = str(file_id)
    action = "load_file"
    args = {"file_id":file_id,"file_name":file_name}
    data = {"action":action,"args":args}
    data = pickle.dumps(data)
    res = ur.urlopen(url,data=data).read()
    return pickle.loads(res)


#%% Auto file

def update_auto(file_id,file_url):

    file_id = str(file_id)
    action = "update_auto"
    
    file = open(file_url,"r")
    contents = file.read()
    file.close()
    
    args = {"file_id":file_id,"contents":contents}
    data = {"action":action,"args":args}
    data = pickle.dumps(data)
    
    res = ur.urlopen(url,data=data).read()
    
    return pickle.loads(res)



def get_auto(file_id):

    file_id = str(file_id)
    action = "get_auto"
    
    args = {"file_id":file_id}
    data = {"action":action,"args":args}
    data = pickle.dumps(data)
    
    res = ur.urlopen(url,data=data).read()
    
    return pickle.loads(res)


def read_report(file_id):
    
    file_id = str(file_id)
    action = "read_report"
    
    args = {"file_id":file_id}
    data = {"action":action,"args":args}
    data = pickle.dumps(data)
    
    res = ur.urlopen(url,data=data).read()
    
    return pickle.loads(res)
