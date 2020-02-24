import logging

from pyzabbix import ZabbixMetric
from pyzabbix.api import ZabbixAPI

logger = logging.getLogger(__name__)


class Fields:
    ## Zabbix json api fields const
    JSON_RESP_ = 'result'
    JSON_RESP_GROUP_ID = 'groupid'
    JSON_RESP_GROUP_IDS = 'groupids'
    JSON_RESP_HOST_ID = 'hostid'
    JSON_RESP_HOST_IDS = 'hostids'
    JSON_RESP_TEMPLATE_IDS = 'templateids'
    JSON_RESP_TEMPLATE_ID = 'templateid'

    ## Zabbix app_server entities
    ZBX_SLAVE_NAME_PREF = 'Slave_'
    ZBX_DEVICE_MONITORING_TEMPLATE_GROUP_NAME = 'Tracker Master Templates'
    ZBX_DEVICE_MONITORING_TEMPLATE_NAME = 'Master Template'

    ZBX_ITEM_TYPE_TRAPPER = 2  # Zabbix Trapper


class ZabbixClient:
    web_api = None

    def __init__(self, url, user, password):
        self.web_api = ZabbixAPI(url=url, user=user, password=password)
        # todo урл для апи, по идее такойже как в конфиге. Брать из одного места

    def get_host_group_id(self, name):
        logger.info('Request host group by name %s' % name)
        response = self.web_api.do_request('hostgroup.get', {'filter': {'name': name}})
        host_list = response[Fields.JSON_RESP_]
        host_cnt = len(host_list)
        logger.info('Find %s host groups' % host_cnt)
        if host_cnt == 1:
            logger.info('Host group % already exists' % name)
            return host_list[0][Fields.JSON_RESP_GROUP_ID]

        return None

    def get_host_id(self, name):
        logger.info('Request host by name %s' % name)
        response = self.web_api.do_request('host.get', {'filter': {'host': [name]}})
        host_list = response[Fields.JSON_RESP_]
        host_cnt = len(host_list)
        logger.info('Find %s hosts' % host_cnt)
        if host_cnt == 1:
            logger.info('Host % already exists' % name)
            return host_list[0][Fields.JSON_RESP_HOST_ID]

        return None

    def get_template_id(self, template_name):
        logger.info('Request template by name %s' % template_name)
        response = self.web_api.do_request('template.get', {'filter': {'host': template_name}})
        host_list = response[Fields.JSON_RESP_]
        host_cnt = len(host_list)
        logger.info('Find %s templates' % host_cnt)
        if host_cnt == 1:
            logger.info('Template %s exists' % template_name)
            return host_list[0][Fields.JSON_RESP_TEMPLATE_ID]

        return None

    def send(self, message):
        # assert isinstance(message, Message)
        packet = [ZabbixMetric('01', 'Slave_0.dev.alarm', 1)]
        self.web_sender.send(packet)

    def create_group_if_not_exists(self, group_name):
        group_id = self.get_host_group_id(group_name)
        if group_id is None:
            group_id = self.create_host_group(group_name)

        if group_id is None:
            # todo Critical
            logger.critical('Host group %s not initialized' % group_name)
            return False

        logger.info('Host group %s configured' % group_name)
        return group_id

    def create_host_group(self, name):
        logger.info('Create host group %s' % name)
        response = self.web_api.do_request('hostgroup.create', {'name': name})
        group_id = int(response[Fields.JSON_RESP_][Fields.JSON_RESP_GROUP_IDS][int(0)][int(0)])  # todo check if errors
        return group_id
