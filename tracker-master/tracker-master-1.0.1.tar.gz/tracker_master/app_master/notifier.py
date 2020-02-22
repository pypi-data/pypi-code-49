from pyzabbix import ZabbixSender, ZabbixMetric

from tracker_master.app_master.master import SlaveManager
from tracker_master.model.Message import Message
from tracker_master.model.Slave import MonitoringName
from tracker_master.zbx_client import Fields


class Notifier:

    def __init__(self):
        self.listeners = list()

    def receive_message(self, msg):
        for listener in self.listeners:
            listener.receive_message(msg)

    def add_listener(self, listener):
        assert isinstance(listener, MessageListener)
        self.listeners.append(listener)


class MessageListener:

    def receive_message(self, msg):
        pass


class ZabbixNotifier(MessageListener):

    def __init__(self, host_name, slave_manager):
        self.host_name = host_name
        self.sender = ZabbixSender(use_config="../../conf/zabbix_agentd.conf")
        assert isinstance(slave_manager, SlaveManager)
        self.slave_manager = slave_manager

    def receive_message(self, msg):
        assert isinstance(msg, Message)
        slave = self.slave_manager.get_slave(msg.hw_id)
        device_name = Fields.ZBX_SLAVE_NAME_PREF + str(slave.zbx_slave_number)
        msg_key_name = device_name + '.' + msg.type.name.lower()
        charge_key_name = device_name + '.' + MonitoringName.CHARGE.value

        packet = [
            ZabbixMetric(self.host_name, msg_key_name, 1),
            ZabbixMetric(self.host_name, charge_key_name, msg.charge)
        ]
        self.sender.send(packet)
