import yaml

CONFIG = None
PROFILE = None


def configure(yml_cfg, profile):
    global PROFILE
    PROFILE = profile

    global CONFIG
    if CONFIG is None:
        with open(yml_cfg, 'r') as stream:
            try:
                CONFIG = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)


def log_file():
    return CONFIG[PROFILE]['log_file']


def zbx_user():
    return CONFIG[PROFILE]['zabbix']['user']


def zbx_pwd():
    return CONFIG[PROFILE]['zabbix']['password']


def zbx_api_url():
    return CONFIG[PROFILE]['zabbix']['api_url']


def zbx_sender_url():
    return CONFIG[PROFILE]['zabbix']['sender_url']

def zbx_client_cfg():
    return CONFIG[PROFILE]['zabbix']['client_cfg']


def master_state_file():
    return CONFIG[PROFILE]['master']['state_file']


def slave_state_file():
    return CONFIG[PROFILE]['slave']['state_file']


def slave_com_port():
    return CONFIG[PROFILE]['slave']['com_port']['port']


def slave_com_port_baudrate():
    return CONFIG[PROFILE]['slave']['com_port']['baudrate']
