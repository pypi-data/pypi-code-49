#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import platform
import uuid
import os
import geocoder
import json
import requests
from datetime import datetime

class Client(object):
    def __init__(self, config):
        self.time_registration      = self.get_current_time()
        self.tags_registration      = ""
        self.name_registration      = self.get_device_name()
        self.chipset_registration   = self.get_device_chipset()
        self.mac_registration       = self.get_device_mac() 
        self.serial_registration    = self.get_device_serial_number() 
        self.processor_registration = self.get_device_processor()
        self.channel_registration   = self.get_device_ntw_channel()
        self.location_registration  = self.get_device_location()
        self.config = config
        self.client_registered   = False
        self.url = (config.DEFAULT_DIMS_URI + '/' + config.CLIENT_ENDPOINT).replace('"',"")

    def get_current_time(self):
        return str(datetime.now())
    
    def get_device_tags(self):
        return self.tags_registration
    
    def set_tags(self,tags):
        self.tags_registration = tags

    def get_device_name(self):
        #Verify FORMAT
        return platform.system()
    
    def get_device_chipset(self):
        #Verify FORMAT
        return  platform.system()
    
    def get_device_mac(self):
        mac = uuid.getnode()
        mac = ":".join(("%012X" % mac )[i:i+2] for i in range(0,12,2))
        return mac

    def get_device_serial_number(self):
        #Verify FORMAT
        cpuserial = ""
        try:
            f = open('/proc/cpuinfo','r')
            for line in f:
                if ("Serial" in line):
                    cpuserial = line.split(":")[1].strip()
                f.close()
        except:
            cpuserial = "0000000000000000"
        
        return cpuserial

    def get_device_processor(self):
        return  platform.processor()

    def get_device_ntw_channel(self):
        #Verify FORMAT
        cur_iface = os.popen("ip route list | grep default | awk '{print $5}'").read().replace("\n","")
        return cur_iface

    def get_device_location(self):
        try:
            g = geocoder.ip('me')
            lat_lng = g.latlng
        except Exception as e:
            lat_lng = [0,0]

        return str(lat_lng[0])+":"+str(lat_lng[1])

    def get_JSON_registration(self):
                
        json_registration = {
            'time'      : self.time_registration,
            'tags'      : self.tags_registration,
            'name'      : self.name_registration,
            'chipset'   : self.chipset_registration,
            'mac'       : self.mac_registration ,
            'serial'    : self.serial_registration,
            'processor' : self.processor_registration,
            'channel'   : self.channel_registration,
            'location'  : self.location_registration
        }
        if json_registration["tags"] == "":
            del json_registration["tags"]
        return json.dumps(json_registration)

    def log_event(self, msg, event):
        
        if not self.config.LOG_ENABLED:
            return

        event = json.dumps(event, sort_keys=True, indent=4)
        final_msg = "[{0}] STATUS: {1} \nINFO: {2}\n\n".format(str(datetime.today()), msg, str(event)) 
        log_path = ""
        if(os.path.isdir("../app_logs")):
            log_path = "logs/"
        else:
            log_path = "app_logs/logs/"

        log_file_name = "log-" + str(datetime.today()).split(" ")[0] + ".log"
        log_file_name = log_path + log_file_name            
        log_file = open(log_file_name, "a")
        log_file.write(final_msg)
        print (final_msg)

    def register_client(self, tags=""):
        try:
            data = {}
            self.set_tags(tags)
            headers = {'content-type': 'application/json'}
            r = requests.post(self.url, data = self.get_JSON_registration(), headers = headers)
            if(r.status_code == 200):
                data = json.loads(r.text)
                self.log_event("Cliente Registrado com sucesso.\n",data)
                self.client_registered = data["message"] == "Success"
                return [True, data]
            else:
                data = json.loads(r.text)
                self.log_event( "Um erro ocorreu no servidor durante o tratamento da requisição.\n", data) 
                return [False, data]

        except requests.exceptions.HTTPError as e:
            data['error'] = e.args[0]
            self.log_event( "Uma exceção ocorreu durante o envio da requisição.\n", data) 
            return [False, data]
        except requests.exceptions.RequestException as e:
            data['error'] = e.args[0]
            self.log_event( "Uma exceção ocorreu durante o envio da requisição.\n", data) 
            return [False, data]       


