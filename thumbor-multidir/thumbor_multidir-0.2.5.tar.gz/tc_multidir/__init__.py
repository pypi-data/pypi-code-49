 # -*- coding: utf-8 -*-
import os

from ._version import __version__

from thumbor.config import Config

Config.define(
        'TC_MULTIDIR_PATHS',
        os.environ.get('TC_MULTIDIR_PATHS', []),
        'The list of paths where the File Loader will try to find images',
        'File Loader'
)