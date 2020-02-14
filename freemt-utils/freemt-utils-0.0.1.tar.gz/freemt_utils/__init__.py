import sys
from pathlib import Path
import importlib

# from .make_url import make_url
# from .arun import arun

# sys.path.insert(0, '..')

# __file__ = '__init__.py'
_ = '''
for elm in Path(__file__).parent.glob('*.py'):
    stem = elm.stem
    _ = importlib.import_module(stem, package='freemt_utils')
    globals().update({stem: getattr(_, stem)})
# '''

__version__ = '0.0.1'
__date__ = '2020.2.12'
VERSION = tuple(__version__.split('.'))