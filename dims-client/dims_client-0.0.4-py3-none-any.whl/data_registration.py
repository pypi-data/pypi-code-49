#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from datetime import datetime
import platform
import uuid
import os
import configparser
import json
from .service_registration import Service


class Data(Service):
    def __init__(self, config):
        self.config = config
        self.time_registration = super(Data, self).get_current_time()
        self.tags_registration = ""
        self.sensitive_registration = 0
        self.name_registration = self.get_device_name()
        self.chipset_registration = super(Data, self).get_device_chipset()
        self.mac_registration = super(Data, self).get_device_mac()
        self.service_number_registration = self.config.SERVICE_NUMBER
        self.url = (config.DEFAULT_DIMS_URI + '/' +
                    config.DATA_ENDPOINT).replace('"', "")

    def get_data_tags(self):
        return self.tags_registration

    def set_tags(self, tags):
        self.tags_registration = tags

    def set_data_sensitive(self, sensitive):
        self.sensitive = sensitive

    def set_values_registration(self, values):
        self.values_registration = str(values)

    def get_data_values(self):
        return self.values_registration

    def get_JSON_registration(self):

        json_registration = {
            "time": self.time_registration,
            "tags": self.tags_registration,
            "sensitive": self.sensitive_registration,
            "chipset": self.chipset_registration,
            "mac": self.mac_registration,
            "serviceNumber": self.service_number_registration,
            "value": self.values_registration
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

    def register_data(self, values, sensitive=0, tags=""):
        try:
            self.set_values_registration(values)
            self.set_data_sensitive(sensitive)
            self.set_tags(tags)
            data = {}
            headers = {'content-type': 'application/json'}
            r = requests.post(
                self.url, data=self.get_JSON_registration(), headers=headers)
            if(r.status_code == 200):
                data = json.loads(r.text)
                self.log_event("Dados registrados com sucesso.\n", data)
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
