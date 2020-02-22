import logging

import tracker_master.config as CFG
import tracker_master.util as util
from tracker_master.app_server.configure import ServerConfigure
from tracker_master.config import Environment

CFG.configure(Environment.DEVELOPMENT, '../../conf/app_master_config.yaml')
util.setup_logging('logging.json')
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    server_configure = ServerConfigure(CFG.zbx_api_url(), CFG.zbx_user(), CFG.zbx_pwd())
    server_configure.configure()
