import logging
from tracker_master.model.Master import Master
from tracker_master.model.Slave import Monitoring
from tracker_master.model.Slave import MonitoringName
from tracker_master.zbx_client import Fields
from tracker_master.zbx_client import ZabbixClient


class MasterConfigure(ZabbixClient):

    def __init__(self, url, user, password):
        ZabbixClient.__init__(self, url, user, password)
        # Zabbix entities name/id
        self.host_group = None
        self.host_group_id = None
        self.host = None
        self.host_id = None
        self.master_template_id = None
        self.logger = logging.getLogger(MasterConfigure.__name__)

    def configure(self, master, slaves, force_create=False):
        assert isinstance(master, Master)
        self.host_group = master.uniq_group_name
        self.host = master.uniq_master_name
        if slaves:
            assert isinstance(slaves, dict)

        self.logger.info('#### Init Zabbix Master configuration ####')
        self.logger.info('## Configure host group %s' % self.host_group)
        group_id = self.get_host_group_id(self.host_group)
        if group_id is None:
            if force_create:
                group_id = self.create_host_group(self.host_group)
            else:
                self.logger.warn('Host group %s not exists' % self.host_group)
                return
        if group_id:
            self.host_group_id = group_id
            self.logger.info('## Zabbix host group %s configured' % self.host_group_id)
        else:
            self.logger.error('Host group creation error')

        self.logger.info('## Looking for template: %s ' % Fields.ZBX_DEVICE_MONITORING_TEMPLATE_NAME)
        t_id = self.get_template_id(Fields.ZBX_DEVICE_MONITORING_TEMPLATE_NAME)
        if t_id:
            self.logger.info('## Zabbix template %s configured' % self.host_group_id)
            self.master_template_id = t_id
        else:
            self.logger.error('Master template is missed')
            return

        self.logger.info('## Configure host %s' % self.host)
        host_id = self.get_host_id(self.host)
        if host_id is None:
            if force_create:
                host_id = self.create_master_host(self.host, self.host)
            else:
                self.logger.error('Host creation error')
                return
        if host_id:
            self.host_id = host_id
        self.logger.info('## Zabbix host %s configured' % self.host)

        if not slaves or len(slaves) == 0:
            self.logger.warning('Device list is empty')
            return False
        # Configure devices
        self.logger.info('Find %s devices' % len(slaves))
        slave_items = self.get_slave_configure()

        for slave_idx, slave in slaves.items():
            self.logger.info('Configure %s%s' % (Fields.ZBX_SLAVE_NAME_PREF, slave_idx))
            slave_conf = slave_items[slave_idx]
            slave.monitorings = slave_conf
            for monitoring in slave.monitorings:
                if not monitoring.active:
                    self.enable_monitoring(monitoring)

        return True

    def get_slave_configure(self):
        response = self.web_api.do_request('item.get', {'hostids': self.host_id, 'sortfield': "name"})
        host_items_j = response[Fields.JSON_RESP_]
        assert isinstance(host_items_j, list)

        slave_monitorings = dict()
        for item_j in host_items_j:
            key_name = str(item_j['key_'])
            if not key_name.startswith(Fields.ZBX_SLAVE_NAME_PREF):
                continue

            slave_info = key_name.split('.')
            slave_name = slave_info[0]
            slave_number = int(slave_name[len(Fields.ZBX_SLAVE_NAME_PREF):])
            slave_monitoring = slave_info[1]  # todo check monitoring name in MonitoringName
            is_monitoring_active = int(item_j['status']) == 0
            monitoring_id = item_j['itemid']
            monitoring = Monitoring(monitoring_id, MonitoringName(slave_monitoring), is_monitoring_active)
            if slave_number not in slave_monitorings:
                monitoring_list = slave_monitorings[slave_number] = list()
            monitoring_list.append(monitoring)

        return slave_monitorings

    def create_host_if_not_exists(self, host_name):  # todo duplicated with __create_group_if_not_exists
        # todo Try to find Zabbix host group with name served_object_id
        host_id = self.get_host_id(host_name)
        if host_id is None:
            host_id = self.create_master_host(host_name)

        if host_id is None:
            # todo Critical
            self.logger.critical('Host %s not initialized' % host_name)
            return False

        self.logger.info('Host %s configured' % host_name)
        return host_id

    def create_master_host(self, name, view_name):
        response = self.web_api.do_request('host.create', {
            'host': name,
            'name': view_name,
            'interfaces': [
                {
                    'type': 1,
                    'main': 1,
                    'useip': 1,
                    'ip': '127.0.0.1',
                    'dns': '',
                    'port': '10050'
                }
            ],
            'templates': [
                {
                    'templateid': self.master_template_id
                }
            ],
            'groups': [{'groupid': self.host_group_id}]

        })
        host_id = int(response[Fields.JSON_RESP_][Fields.JSON_RESP_HOST_IDS][int(0)][int(0)])  # todo check if errors
        return host_id


    def enable_monitoring(self, monitoring):
        response = self.web_api.do_request('item.update', {'hostids': self.host_id, 'itemid': monitoring.zbx_id,
                                                           'status': 0})  # todo create status mapping or const
        host_items_j = response[Fields.JSON_RESP_]
