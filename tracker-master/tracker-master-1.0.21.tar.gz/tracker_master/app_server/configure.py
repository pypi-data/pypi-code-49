import logging

from tracker_master.zbx_client import Fields
from tracker_master.zbx_client import ZabbixClient
from tracker_master.model.Slave import MonitoringName

module_logger = logging.getLogger(__name__)


MASTER_DEVICE_MAX_CNT = 5

devices_conf = [{'key': MonitoringName.CHARGE.value, 'value_type': 0, 'delay': 10},  # todo think about delay
                {'key': MonitoringName.ALARM.value, 'value_type': 3, 'delay': 10},   #
                {'key': MonitoringName.TEST.value, 'value_type': 3, 'delay': 10}]


class ServerConfigure(ZabbixClient):

    def __init__(self, url, user, password):
        self.logger = logging.getLogger(ServerConfigure.__name__)
        ZabbixClient.__init__(self, url=url, user=user, password=password)

    # todo Move to other program used by admin
    def configure(self):
        self.logger.info('#### Init Zabbix Server configuration ####')

        # Initialize template group (create if not exists)
        self.logger.info('Check template group %s exists' % Fields.ZBX_DEVICE_MONITORING_TEMPLATE_GROUP_NAME)

        tg_id = self.get_host_group_id(Fields.ZBX_DEVICE_MONITORING_TEMPLATE_GROUP_NAME)
        if tg_id is None:
            tg_id = self.create_host_group(Fields.ZBX_DEVICE_MONITORING_TEMPLATE_GROUP_NAME)

        if tg_id is None:
            # todo Critical
            self.logger.error('Host group %s not initialized' % Fields.ZBX_DEVICE_MONITORING_TEMPLATE_GROUP_NAME)
            return False
        self.logger.info('Host group %s configured' % Fields.ZBX_DEVICE_MONITORING_TEMPLATE_GROUP_NAME)

        # Initialize template (create if not exists)
        self.logger.info('Check template %s exists' % Fields.ZBX_DEVICE_MONITORING_TEMPLATE_NAME)
        tmpl_id = self.get_template_id(Fields.ZBX_DEVICE_MONITORING_TEMPLATE_NAME)
        if not tmpl_id:
            response = self.web_api.do_request('template.create', {
                'host': Fields.ZBX_DEVICE_MONITORING_TEMPLATE_NAME,
                'groups': {Fields.JSON_RESP_GROUP_ID: tg_id}
            })
            tmpl_id = response[Fields.JSON_RESP_][Fields.JSON_RESP_TEMPLATE_IDS][0]  # Todo check exists

        if tmpl_id is None:
            # todo Critical
            self.logger.error('Template %s not initialized' % Fields.ZBX_DEVICE_MONITORING_TEMPLATE_NAME)
            return False
        self.logger.info('Template %s configured' % Fields.ZBX_DEVICE_MONITORING_TEMPLATE_NAME)

        # Initialize template items
        self.logger.info('Check template items')
        response = self.web_api.do_request('item.get', {'hostids': tmpl_id, 'sortfield': "name"})
        items_list = response[Fields.JSON_RESP_]
        if len(items_list) == 0:
            self.logger.info('Create template items')
            for device_number in range(MASTER_DEVICE_MAX_CNT):
                for conf in devices_conf:
                    self.create_slave_item('%s%s.%s' % (Fields.ZBX_SLAVE_NAME_PREF, device_number + 1, conf['key']),
                                           '%s%s.%s' % (Fields.ZBX_SLAVE_NAME_PREF, device_number + 1, conf['key']),
                                           tmpl_id, Fields.ZBX_ITEM_TYPE_TRAPPER, conf['value_type'], conf['delay'])
        elif len(items_list) == len(devices_conf) * MASTER_DEVICE_MAX_CNT:
            self.logger.info('Template items already created')
        else:
            self.logger.warning('Template has %s items but %s expected.')  # todo write guide message for manual check

        self.logger.info('Server configured')

    # parent_id - host_id or template_id
    def create_slave_item(self, name, key, parent_id, type, value_type, delay_sec):
        self.logger.info('Creating item %s for template_group %s. Type %s, value type %s. Delay % sec'
                         % (name, parent_id, type, value_type, delay_sec))
        response = self.web_api.do_request('item.create',
                                           {'name': name, 'key_': key, 'hostid': str(parent_id),
                                            'type': type, 'value_type': value_type, 'delay': delay_sec, 'status': 1})
