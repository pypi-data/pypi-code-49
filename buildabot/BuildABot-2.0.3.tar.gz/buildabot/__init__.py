name = 'buildabot'
__title__ = 'buildabot'
__author__ = 'Allen Lantz'
__copyright__ = 'Copyright 2020 Allen Lantz'
__version__ = '2.0.3'

from .bot import Bot
from .typer import Typer
from .logger import Logger
from . import utils
from .module_manager import ModuleManager
from .module import Module
from .event_handler import EventHandler
from collections import namedtuple

VersionInfo = namedtuple('VersionInfo', 'major minor micro releaselevel serial')

version_info = VersionInfo(major=2, minor=0, micro=3, releaselevel='beta', serial=0)
