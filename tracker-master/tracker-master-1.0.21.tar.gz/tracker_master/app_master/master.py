import logging.config
import os.path
import yaml

import tracker_master.config as CFG
from tracker_master.model.Message import Message
from tracker_master.model.Slave import Slave
from tracker_master.model.Master import Master


def parse(message_string):
    return Message(hw_id=int(message_string[0:6]),
                   _type=int(message_string[8]),
                   charge=float(message_string[9:13]))


class TrackerMaster:

    def __init__(self):
        self.slave_manager = SlaveManager()
        self.hw_id_to_slaves = dict()
        self.master = None

    def initialize(self):
        self.init_from_conf()

    def apply_configure(self, master_group_name, master_name):
        self.master.uniq_group_name = master_group_name
        self.master.uniq_master_name = master_name

        self.__write_conf()
        self.init_from_conf()

    def apply_slave_configure(self, _dict):
        self.master.set_slaves(_dict)

        self.__write_conf()
        self.init_from_conf()

    def is_master_configured(self):
        return self.master and self.master.is_configured()

    def is_slave_configured(self):
        return self.slave_manager.is_configured()

    def get_master(self) -> Master:
        return self.master

    def get_slave(self, hw_id):
        return self.hw_id_to_slaves[hw_id]

    def get_slaves(self):
        return self.master.get_slaves()

    def init_from_conf(self):
        if not os.path.exists(CFG.master_state_configuration()):
            return False

        with open(CFG.master_state_configuration(), 'r') as f:
            cfg = yaml.safe_load(f)
            master = Master(
                cfg.get('master_group'), cfg.get('master_name')
            )
            slaves_cfg_dict = cfg.get('slaves')

            if slaves_cfg_dict:
                slaves_dict = dict()
                for zbx_slave_idx, slave_data in slaves_cfg_dict.items():
                    slaves_dict[zbx_slave_idx] = Slave(slave_data['hw_id'], zbx_slave_idx)
                master.set_slaves(slaves_dict)

            self.master = master
            return True

    def __write_conf(self):
        conf = {
            'master_group': self.master.uniq_group_name,
            'master_name': self.master.uniq_master_name
        }

        slaves = self.master.get_slaves()
        slaves_dict = dict()
        if slaves:
            for zbx_slave_idx, slave in slaves.items():
                slaves_dict[zbx_slave_idx] = {
                    'hw_id': slave.hw_id
                }
        conf['slaves'] = slaves_dict
        conf = yaml.dump(conf)

        with open(CFG.master_state_configuration(), 'w') as f:
            f.write(conf)


class SlaveManager:

    def __init__(self):
        self.logger = logging.getLogger(SlaveManager.__name__)

        pass

    def is_configured(self):
        return self.slaves and len(self.slaves) > 0

    def get_slave(self, hw_id):
        return self.hw_id_to_slaves[hw_id]


class SlavesConfigurer:

    def __init__(self):
        self.slaves = dict()
        self.logger = logging.getLogger(SlavesConfigurer.__name__)

    def register_slave(self, msg):
        slave = Slave(msg.hw_id)
        if slave in self.slaves.values():
            self.logger.info('Slave %s is already existed' % msg.hw_id)
            return False

        zbx_new_slave_idx = len(self.slaves) + 1
        slave.zbx_slave_number = zbx_new_slave_idx
        self.slaves[zbx_new_slave_idx] = slave
        self.logger.info('Slave %s %s has registered' % (zbx_new_slave_idx, msg.hw_id))
        return True
