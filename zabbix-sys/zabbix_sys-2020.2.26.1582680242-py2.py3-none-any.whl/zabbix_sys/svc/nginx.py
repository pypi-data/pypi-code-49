
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function

import re
import requests
import requests.auth
import requests.exceptions
import sys


class Nginx:

    def __init__(self, cfg, logger):

        self.logger = logger
        self.dsn = {
            "user": "",
            "password": "",
            "scheme": "http",
            "host": "127.0.0.1",
            "port": "8080",
            "url": "/status",
            "timeout": 2
        }

        if cfg and 'nginx' in cfg:
            if 'user' in cfg['nginx']:
                self.dsn.update({"user": cfg['nginx']['user']})
            if 'password' in cfg['nginx']:
                self.dsn.update({"password": cfg['nginx']['password']})
            if 'host' in cfg['nginx']:
                self.dsn.update({"host": cfg['nginx']['host']})
            if 'port' in cfg['nginx']:
                self.dsn.update({"port": cfg['nginx']['port']})
            if 'url' in cfg['nginx']:
                self.dsn.update({"url": cfg['nginx']['url']})

        self.url = ""
        self.url += str(self.dsn['scheme']) + "://"
        self.url += str(self.dsn['host']) + ":" + str(self.dsn['port'])
        self.url += self.dsn["url"]

        if self.dsn['user'] and self.dsn['password']:
            self.auth = requests.auth.HTTPBasicAuth(username=self.dsn['user'], password=self.dsn['password'])
        else:
            self.auth = None

        self.logger.debug("nginx::init::dsn : " + str(self.dsn))
        self.logger.debug("nginx::init::auth : " + str(self.auth))

    def __get__status__(self):
        try:
            if self.auth:
                response = requests.get(self.url, auth=self.auth)
            else:
                response = requests.get(self.url)

            self.logger.debug("nginx::response::debug::status_code : " + str(response.status_code))
            self.logger.debug("nginx::response::debug::text : " + str(response.text))

            if response.status_code == 200 and "Active connections:" in response.text:
                return response.text
            else:
                return None

        except Exception:
            raise

    def lld_status(self):

        result = {
            'data': []
        }

        try:
            response = self.__get__status__()
            if response:
                result['data'].append(
                    {"_": "", "stats": True}
                )
            self.logger.debug("nginx::discovery result: " + str(result))
            return result

        except requests.exceptions.ConnectionError:
            return result
        except Exception as err:
            self.logger.error(msg=err.__str__(), exc_info=False)
            sys.exit(1)

    def raw_status(self):

        result = {}
        try:
            response = self.__get__status__()
            if response:
                result.update(
                    {
                        'active': re.search('^Active connections:\s(\d+)', response).group(1),
                        'accepts': re.search('\s+(\d+)\s+(\d+)\s+(\d+)', response).group(1),
                        'handled': re.search('\s+(\d+)\s+(\d+)\s+(\d+)', response).group(2),
                        'requests': re.search('\s+(\d+)\s+(\d+)\s+(\d+)', response).group(3),
                        'reading': re.search('Reading:\s+(\d+)', response).group(1),
                        'writing': re.search('Writing:\s+(\d+)', response).group(1),
                        'waiting': re.search('Waiting:\s+(\d+)', response).group(1)
                    }
                )
            self.logger.debug("nginx::metrics result: " + str(result))
            return result

        except requests.exceptions.ConnectionError:
            return result

        except Exception as err:
            self.logger.error(msg=err, exc_info=False)
            sys.exit(1)
