import logging
logger = logging.getLogger(__name__)

import systemd_unit
from elevate import elevate
from os import geteuid
from os.path import dirname, join, realpath

def InstallService():
    logger.info("Begining installation of eurekaroom service!!!")

    current_dir_path = dirname(realpath(__file__))
    service_script_path = join(current_dir_path, 'installScripts', 'eurekaroom.service')
    
    try:
        with open(service_script_path, "r") as f:
            content = f.read()
    except IOError:
        logger.warning("Could not read file, {}".format(service_script_path))

    myservice = systemd_unit.Unit(name = "eurekaroom", content = content)
    
    # TODO: Make this check for sudo su
    elevate()
    if geteuid() == 0:
        myservice.ensure()
    else:
        logger.warning("Service was not installed, try '$sudo su' then install the service")
