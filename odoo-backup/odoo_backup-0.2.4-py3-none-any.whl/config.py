import configparser
import os

odoo_backup_conf_path = os.path.join('/', 'etc', 'odoo_backup.conf')
config = configparser.ConfigParser()
config.read(odoo_backup_conf_path)

CONFIGURATION_DIR = config.get('config', 'configuration_dir')
DATA_DIR = config.get('config', 'data_dir')