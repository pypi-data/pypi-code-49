 # -*- coding: utf-8 -*-
from thumbor.config import Config

Config.define(
        'TC_MULTIDIR_PATHS',
        [],
        'The list of paths where the File Loader will try to find images',
        'File Loader'
)