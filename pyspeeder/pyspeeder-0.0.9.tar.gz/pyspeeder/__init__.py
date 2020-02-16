from gevent import monkey

monkey.patch_all()

from .core import Spider
from .config import config
from .browser import Chrome
from .proxy import Proxy, Data5u
from . import helper

redis = helper.redis
