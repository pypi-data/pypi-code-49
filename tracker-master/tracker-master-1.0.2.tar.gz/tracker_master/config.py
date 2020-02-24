from enum import Enum
import yaml


class Environment(Enum):
    DEVELOPMENT = 'development',
    TESTING = 'testing'

CONFIG = None
ENVIRONMENT = Environment.DEVELOPMENT


def configure(environment, yml_cfg):
    global ENVIRONMENT
    assert isinstance(environment, Environment)
    ENVIRONMENT = environment

    global CONFIG
    if CONFIG is None:
        with open(yml_cfg, 'r') as stream:
            try:
                CONFIG = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)


def log_file():
    return CONFIG[ENVIRONMENT.value[0]]['log_file']


def zbx_user():
    return CONFIG[ENVIRONMENT.value[0]]['master']['zabbix']['user']


def zbx_pwd():
    return CONFIG[ENVIRONMENT.value[0]]['master']['zabbix']['password']


def zbx_api_url():
    return CONFIG[ENVIRONMENT.value[0]]['master']['zabbix']['api_url']


def zbx_sender_url():
    return CONFIG[ENVIRONMENT.value[0]]['master']['zabbix']['sender_url']


def master_state_file():
    return CONFIG[ENVIRONMENT.value[0]]['master']['state_file']


def slave_state_file():
    return CONFIG[ENVIRONMENT.value[0]]['slave']['state_file']


def slave_com_port():
    return CONFIG[ENVIRONMENT.value[0]]['slave']['com_port']['port']


def slave_com_port_baudrate():
    return CONFIG[ENVIRONMENT.value[0]]['slave']['com_port']['baudrate']
