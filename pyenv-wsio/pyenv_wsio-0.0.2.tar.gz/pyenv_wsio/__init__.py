# -*- coding: utf-8 -*-

"""
                pyenv_wsio.py:
VirtualPyEnv websocket library
"""

__author__ = "beanjs"
__copyright__ = "Copyright 2019"
__credits__ = ["beanjs"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "beanjs"
__email__ = "502554248@qq.com"
__status__ = "Development"


from ._wsio import *
from ._events import *
from ._client import *
from ._packet import *

# if __name__ == "__main__":
#     raise Exception(
#         "This is a library not meant to be executed as a standalone script")