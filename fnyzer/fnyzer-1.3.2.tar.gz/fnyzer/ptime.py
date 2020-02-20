"""getptime()=time.process_time() if available, time.clock() otherwise"""
"""time.clock() is removed from Python 3.8, and time.process_time() must be used"""
# TODO in the future (when no backward compability prior to Python 3.8 is required):
#    - remove this file ptime.py
#    - remove line "from fnyzer import ptime" from all files
#    - substitute "time.clock()" by "time.process_time()" in all files

import time

def getptime():
    if 'process_time' in dir(time):
        return time.process_time()
    else:
        return time.clock()
