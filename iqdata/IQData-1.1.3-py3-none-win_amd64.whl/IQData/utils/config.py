import os

from IQCommon.utils import read_config, ObjectDict
from IQData.utils import BASE_PATH

__DEFAULT_CONFIG_PATH = os.path.join(BASE_PATH, 'utils', 'default_config.yml')


DEFAULT_CONFIG = ObjectDict(
    read_config(
        __DEFAULT_CONFIG_PATH
    )
)
