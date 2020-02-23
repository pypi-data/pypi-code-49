"""
timework 0.2.8

MIT License © bugstop

PyPI:   https://pypi.org/project/timework/
GitHub: https://github.com/bugstop/timework-timeout-decorator/


Cross-platform python module to set execution time limits as decorators.

timework.timer      - a decorator measuring the execution time.
timework.limit      - a decorator limiting the execution time.
timework.iterative  - a decorator used to process iterative deepening.
"""


from .timework import *

__name__ = 'timework'
__version__ = '0.2.8'
__all__ = ['timer', 'limit', 'iterative']
