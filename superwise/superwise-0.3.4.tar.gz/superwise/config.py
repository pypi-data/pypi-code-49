import os

import yaml

from superwise.project_root import PROJECT_ROOT


class Config:

    config_file_path = os.path.join(PROJECT_ROOT, "resources", "config.yml")

    with open(config_file_path, 'r') as config_file:
        config = yaml.safe_load(config_file)

