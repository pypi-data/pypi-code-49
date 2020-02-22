import datetime
import functools
import inspect
import logging
import python_agent

import time
from freezegun import freeze_time

log = logging.getLogger(__name__)


def sum(x, y):
    return x + y


def subtract(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


def test_sum():
    assert sum(1, 2) == 3


@freeze_time("2017-09-03")
def test_mul1():
    from python_agent.packages import requests
    log.info("time module is=%s" % time)
    requests.get("https://google.com")
    e = datetime.datetime.utcnow()
    d = time.time()
    log.info("======================start %s" % d)
    x = 0
    while x < 45:
        time.sleep(1)
        x += 1
    assert mul(3, 5) == 15
    log.info("======================end %s" % d)


# __builtins__.__import__ = handle_import(__builtins__.__import__)
#
# import time
# print(time.time())
