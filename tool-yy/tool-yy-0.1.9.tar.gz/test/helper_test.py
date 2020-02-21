"""
Create by yy on 2019-07-25
"""
import threading
from concurrent.futures import ThreadPoolExecutor

from tool_yy import debug


class HelperTest(object):
    def __init__(self, init_db=None):
        self.db = init_db("INSOMNIA_MUSIC_DATABASE_CONFIG")

    def __del__(self):
        self.db.close()


def thread_func(info):
    print(threading.current_thread().name)
    print(info)


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=5) as thread_pool:
        for i in range(10):
            thread_pool.submit(thread_func, i)
