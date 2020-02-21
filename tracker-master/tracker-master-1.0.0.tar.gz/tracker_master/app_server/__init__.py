import logging

from tracker_master.app_server.configure import ServerConfigure

import tracker_master.util as util

util.setup_logging('logging.json')
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    server_configure = ServerConfigure(url="http://192.168.56.101/zabbix/")
    server_configure.configure()
