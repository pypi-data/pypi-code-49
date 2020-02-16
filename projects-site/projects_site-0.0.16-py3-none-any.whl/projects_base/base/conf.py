# Common configuration
import os
import configparser

# Load config.ini
res_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                        '..', 'res', 'config.ini')
config = configparser.SafeConfigParser()
config.read(res_path)

# common static folder path
config.get('BASE', 'static_folder')
config.get('BASE', 'upload_folder')
config.get('BASE', 'db_lock')
