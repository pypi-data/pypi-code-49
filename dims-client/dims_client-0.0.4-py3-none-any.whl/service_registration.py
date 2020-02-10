#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from datetime import datetime
import platform
import uuid
import os
import json
from .client_registration import Client
import configparser


class Service(Client):
    def __init__(self, config):
        self.config = config
        self.time_registration = super(Service, self).get_current_time()
        self.number_registration = self.config.SERVICE_NUMBER
        self.chipset_registration = super(Service, self).get_device_chipset()
        self.mac_registration = super(Service, self).get_device_mac()
        self.url = (config.DEFAULT_DIMS_URI + '/' +
                    config.SERVICE_ENDPOINT).replace('"', "")
        self.tags_registration = ""
        self.service_name = ""
        self.parameter_registration = ""
        self.unit_registration = ""
        self.numeric_registration = ""
        self.service_registered   = False

    def get_service_tags(self):
        return self.tags_registration

    def set_tags(self, tags_registration):
        self.tags_registration = tags_registration

    def get_service_name(self):
        return self.service_name

    def set_service_name(self, service_name):
        self.service_name = service_name

    def get_service_parameter(self):
        return self.parameter_registration

    def set_service_parameter(self, parameter_registration):
        self.parameter_registration = parameter_registration

    def get_service_unit(self):
        return self.unit_registration

    def set_service_unit(self, unit_registration):
        self.unit_registration = unit_registration

    def get_service_numeric(self):
        return self.numeric_registration

    def set_service_numeric(self, numeric_registration):
        self.numeric_registration = numeric_registration

    def get_JSON_registration(self):

        json_registration = {
            "time": self.time_registration,
            "tags": self.tags_registration,
            "number": self.number_registration,
            "chipset": self.chipset_registration,
            "mac": self.mac_registration,
            "name": self.service_name,
            "parameter": self.parameter_registration,
            "unit": self.unit_registration,
            "numeric": self.numeric_registration,
        }
        if json_registration["tags"] == "":
            del json_registration["tags"]
        return json.dumps(json_registration)

    def log_event(self, msg, event):
        if not self.config.LOG_ENABLED:
            return
        event = json.dumps(event, sort_keys=True, indent=4)
        final_msg = "[{0}] STATUS: {1} \nINFO: {2}\n\n".format(
            str(datetime.today()), msg, str(event))
        log_path = ""
        if(os.path.isdir("../app_logs")):
            log_path = "logs/"
        else:
            log_path = "app_logs/logs/"

        log_file_name = "log-" + str(datetime.today()).split(" ")[0] + ".log"
        log_file_name = log_path + log_file_name
        log_file = open(log_file_name, "a")
        log_file.write(final_msg)
        print(final_msg)

    def service_registed(self):
        return self.service_registered

    def register_service(self, service_name, service_parameter, service_unit, service_numeric, tags=""):
        try:
            data = {}
            self.set_tags(tags)
            self.set_service_name(service_name)
            self.set_service_parameter(service_parameter)
            self.set_service_unit(service_unit)
            self.set_service_numeric(service_numeric)
            headers = {'content-type': 'application/json'}
            r = requests.post(
                self.url, data=self.get_JSON_registration(), headers=headers)
            if(r.status_code == 200):
                data = json.loads(r.text)
                self.service_registered = data["message"] == "Success"
                self.log_event("Serviço registrado com sucesso.\n", data)
                return [True, data]
            else:
                data = json.loads(r.text)
                self.log_event(
                    "Um erro ocorreu no servidor durante o tratamento da requisição.\n", data)
                return [False, data]

        except requests.exceptions.HTTPError as e:
            data['error'] = e.args[0]
            self.log_event(
                "Uma exceção ocorreu durante o envio da requisição.\n", data)
            return [False, data]
        except requests.exceptions.RequestException as e:
            data['error'] = e.args[0]
            self.log_event(
                "Uma exceção ocorreu durante o envio da requisição.\n", data)
            return [False, data]
