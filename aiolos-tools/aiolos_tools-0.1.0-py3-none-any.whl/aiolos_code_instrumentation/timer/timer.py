
import inspect
import os
import time
import sys
import logging

from aiolos_code_instrumentation.timer import __version__
from aiolos_code_instrumentation.add_logging_level import addLoggingLevel, TIMER
addLoggingLevel("TIMER", TIMER, methodName=None)

log = logging.getLogger(__name__)

class Timer:

    m_name: str
    m_mod: str
    m_start: float
    m_pid: int

    def __init__(self):

        self.m_name = func_name()
        self.m_mod  = mod_name()
        self.m_start = time.time()
        self.m_pid = os.getppid()

    def __del__(self):
        log.timer("<%s.%s> completed in %.2f ms" % (self.m_mod, self.m_name, (time.time() - self.m_start)*1000))


def func_name():
    return inspect.stack()[2][3]

def mod_name():
    # return inspect.stack()[3][3]
    return inspect.getmodule(inspect.stack()[2][0]).__name__

def test():

    timer = Timer()
    for i in range(10000):
        x = i**2
        print(x)


if __name__ == '__main__':
    log.setLevel(TIMER)
    strm = logging.StreamHandler()
    strm.setLevel(TIMER)
    log.addHandler(strm)


    test()
    input('Press <Enter> to exit')