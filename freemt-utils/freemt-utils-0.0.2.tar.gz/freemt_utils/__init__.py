''' freemt __init__.py '''
# import sys
# from pathlib import Path
# import importlib

from .switch_to import switch_to
from .arun import arun
from .make_url import make_url
from .httpx_get import httpx_get
from .save_tempfile import save_tempfile
from .logger_level import logger_level

# sys.path.insert(0, '..')

# __file__ = '__init__.py'
_ = '''
for elm in Path(__file__).parent.glob('*.py'):
    stem = elm.stem
    _ = importlib.import_module(stem, package='freemt_utils')
    globals().update({stem: getattr(_, stem)})
# '''

# version__ = '0.0.1'
# date__ = '2020.2.12'
__version__ = '0.0.2'
__date__ = '2020.2.15'
VERSION = tuple(__version__.split('.'))
