
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function

import sys
from pyrabbit2.api import Client
from pyrabbit2.http import NetworkError


class RabbitMQ:

    def __init__(self, cfg, logger):

        self.logger = logger
        self.dsn = {
            "user": "guest",
            "passwd": "guest",
            "scheme": "http",
            "host": "127.0.0.1",
            "port": "15672",
            "timeout": 2
        }

        if cfg and 'rabbitmq' in cfg:
            if 'user' in cfg['rabbitmq']:
                self.dsn.update({"user": cfg['rabbitmq']['user']})
            if 'password' in cfg['rabbitmq']:
                self.dsn.update({"passwd": cfg['rabbitmq']['password']})
            if 'scheme' in cfg['rabbitmq']:
                self.dsn.update({"scheme": cfg['rabbitmq']['scheme']})
            if 'host' in cfg['rabbitmq']:
                self.dsn.update({"host": cfg['rabbitmq']['host']})
            if 'port' in cfg['rabbitmq']:
                self.dsn.update({"port": cfg['rabbitmq']['port']})

        self.dsn.update({
            'api_url': str(self.dsn['host']) + ":" + str(self.dsn['port'])
        })

        del self.dsn['host']
        del self.dsn['port']

        self.logger.debug("rabbitmq::init::dsn : " + str(self.dsn))

        self.cnx = Client(**self.dsn)

    def lld_exchanges(self):

        result = {"data": []}

        try:
            self.cnx.is_alive()
            exchanges = self.cnx.get_exchanges()
            for exchange in exchanges:
                if exchange['name']:
                    result["data"].append(
                        {'vhost': exchange['vhost'], 'name': exchange['name'], 'type': exchange['type'], 'internal': exchange['internal']}
                    )
            return result
        except NetworkError:
            return result

        except Exception as err:
            self.logger.error(err.__str__(), exc_info=False)
            sys.exit(1)

    def lld_queues(self):

        result = {"data": []}

        try:
            self.cnx.is_alive()
            queues = self.cnx.get_queues()
            for queue in queues:
                if queue['name'] == 'aliveness-test':
                    continue
                delayed = False
                if "arguments" in queue and "x-dead-letter-exchange" in queue["arguments"]:
                    delayed = True
                result['data'].append({'vhost': queue['vhost'], 'name': queue['name'], 'delayed': delayed})

            self.logger.debug("rabbitmq::discovery::queues result: " + str(result))
            return result

        except NetworkError:
            return result

        except Exception as err:
            self.logger.error(err.__str__(), exc_info=False)
            sys.exit(1)

    def lld_server(self):

        result = {"data": []}

        try:
            self.cnx.is_alive()
            stats = self.cnx.get_overview()
            result["data"].append(
                {"_": "", "rabbitmq_version": stats["rabbitmq_version"]}
            )
            self.logger.debug("rabbitmq::discovery::server result: " + str(result))
            return result

        except NetworkError:
            return result

        except Exception as err:
            self.logger.error(err.__str__(), exc_info=False)
            sys.exit(1)

    def lld_shovels(self):

        result = {"data": []}

        try:
            self.cnx.is_alive()
            shovels = self.cnx.get_all_shovels()
            for shovel in shovels:
                result["data"].append({'vhost': shovel['vhost'], 'name': shovel['name']})
            self.logger.debug("rabbitmq::discovery::shovels result: " + str(result))
            return result

        except NetworkError:
            return result

        except Exception as err:
            self.logger.error(err.__str__(), exc_info=False)
            sys.exit(1)

    def raw_exchanges(self, vhost, exchange_name):
        try:
            self.cnx.is_alive()
            result = self.cnx.get_exchange(vhost=vhost, name=exchange_name)
            self.logger.debug("rabbitmq::metrics::exchanges result: " + str(result))
            return result
        except Exception as err:
            self.logger.error(msg=err.__str__(), exc_info=False)
            sys.exit(1)

    def raw_queues(self, vhost, queue):

        try:
            self.cnx.is_alive()
            result = self.cnx.get_queue(vhost=vhost, name=queue)
            if 'consumer_details' in result:
                del result['consumer_details']

            self.logger.debug("rabbitmq::metrics::queues result: " + str(result))
            return result

        except Exception as err:
            self.logger.error(msg=err.__str__(), exc_info=False)
            sys.exit(1)

    def raw_server(self):

        try:
            self.cnx.is_alive()
            result = self.cnx.get_overview()

            hostname = ""
            for context in result['contexts']:
                if 'node' in context:
                    hostname = context['node']
                    break

            nodes = self.cnx.get_nodes()
            for node in nodes:
                if 'name' in node and node['name'] == hostname:
                    result.update({"node_stats": node})
            self.logger.debug("rabbitmq::metrics::server result: " + str(result))
            return result

        except Exception as err:
            self.logger.error(msg=err.__str__(), exc_info=False)
            sys.exit(1)

    def raw_shovels(self, vhost, shovel_name):

        try:
            self.cnx.is_alive()
            result = self.cnx.get_shovel(vhost=vhost, shovel_name=shovel_name)
            self.logger.debug("rabbitmq::metrics::shovels result: " + str(result))
            return result
        except Exception as err:
            self.logger.error(msg=err.__str__(), exc_info=False)
            sys.exit(1)
