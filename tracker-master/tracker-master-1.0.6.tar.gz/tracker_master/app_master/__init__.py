import logging
import queue
import sys

from tracker_master.app_master.slave_data_consumer import ConfigurerConsumer
from tracker_master.app_master.slave_data_consumer import MainConsumer
from tracker_master.app_master.slave_data_producer import VirtualSalveReaderThread
from tracker_master.app_master.slave_data_producer import SlaveReaderThread
from tracker_master.app_master.notifier import Notifier
from tracker_master.app_master.notifier import ZabbixNotifier

from tracker_master.model.Master import Master
from tracker_master.app_master.configure import MasterConfigure
from tracker_master.app_master.master import SlaveManager
from tracker_master.app_master.master import TrackerMaster
from tracker_master.app_master.master import SlavesConfigurer

import tracker_master.config as CFG
import tracker_master.util as util

CFG.configure("../conf/app_master_config.yaml", 'development')

util.setup_logging()
logger = logging.getLogger(__name__)

SLAVE_QUEUE_BUFFER_MAX_SIZE = 100


def print_conf(master, slaves):
    print_master_conf(master)
    print_slave_conf(slaves)


def print_master_conf(master):
    if master and isinstance(master, Master) and master.is_initialized():
        print('## Master: \n# Group: %s\n# Name: %s\n' % (master.uniq_group_name, master.uniq_master_name))
    else:
        print('## Master: NOT INITIALIZED\n')


def print_slave_conf(slaves):
    if slaves and isinstance(slaves, dict) and len(slaves) > 0:
        print('## Slaves: %s slaves configured' % len(slaves))
        for slave in slaves.values():
            print('# %s %s' % (slave.zbx_slave_number, slave.hw_id))
        print()
    else:
        print('## Slaves: NOT INITIALIZED\n')


if __name__ == "__main__":
    slave_message_queue = queue.Queue(SLAVE_QUEUE_BUFFER_MAX_SIZE)

    tracker_master = TrackerMaster()
    tracker_master.initialize()
    notifier = Notifier()

    print_conf(tracker_master.get_master(), tracker_master.get_slaves())
    while True:
        cmd = input()
        if cmd == 'init master':
            print_master_conf(tracker_master.get_master())
            master_group_name = input('Set master group name: ').strip()
            master_name = input('Set master name: ').strip()
            tracker_master.apply_configure(master_group_name, master_name)

            print_master_conf(tracker_master.get_master())
        elif cmd == 'init slaves':
            print_slave_conf(tracker_master.get_slaves())

            slave_configurer = SlavesConfigurer()
            p = VirtualSalveReaderThread(slave_message_queue)
            c = ConfigurerConsumer(slave_message_queue, slave_configurer)
            p.start()
            c.start()

            while True:
                cmd = input()
                if cmd == 'stop':
                    c.stop_working()
                    p.stop_working()
                    tracker_master.apply_slave_configure(slave_configurer.slaves)
                    print_slave_conf(tracker_master.get_slaves())
                    break
        elif cmd == 'start':
            p = SlaveReaderThread(slave_message_queue)
            #p = ProducerThread(slave_message_queue)
            c = MainConsumer(slave_message_queue, notifier)
            notifier.add_listener(ZabbixNotifier(
                tracker_master.get_master().uniq_master_name, tracker_master.slave_manager
            ))  # todo make dict __name__: Notifier
            p.start()
            c.start()
        elif cmd == 'show config':
            print_conf(tracker_master.get_master(), tracker_master.get_slaves)
        elif cmd == 'configure zabbix':
            zabbix_configure = MasterConfigure(CFG.zbx_api_url(), CFG.zbx_user(), CFG.zbx_pwd())
            zabbix_configure.configure(tracker_master.get_master(), tracker_master.get_slaves(), force_create=True)
        elif cmd == 'exit':
            sys.exit()  # todo check resources released

