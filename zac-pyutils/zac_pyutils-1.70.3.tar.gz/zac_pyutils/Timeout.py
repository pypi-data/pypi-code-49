# author: zac
# create-time: 2019-09-04 14:58
# usage: -
import threading
import multiprocessing
import time
import sys
import os
from queue import Queue,Empty

is_py2 = sys.version[0] == '2'
if is_py2:
    print("Timeout not available for py2")


class ThreadStopException(Exception):
    pass


class _BasicStopThread(threading.Thread):
    def _bootstrap(self, stop_thread=False):
        def stop():
            nonlocal stop_thread
            stop_thread = True

        self.stop = stop

        def tracer(*_):
            if stop_thread:
                raise ThreadStopException()
            return tracer

        sys.settrace(tracer)
        super(_BasicStopThread, self)._bootstrap()


class TimeoutThread():
    """
    使用示例：
        t2 = TimeoutThread(target=target_func, args=(30, 8), time_limit=3)
        res2=t2.start()
    """
    def __init__(self, target, args=(), time_limit=1, verbose=False):
        self.resultQ = Queue()
        _target = self._put_res_in_result_queue(target)
        # 用来运行目标函数的线程
        self.target_thread = _BasicStopThread(target=_target, args=args)
        self.target_thread.setDaemon(True)
        # 用来计时的线程
        self.timing_thread = _BasicStopThread(target=self.timing, args=(time_limit, verbose, ))
        self.timing_thread.setDaemon(True)

    def timing(self, timeout, verbose=False):
        pid = os.getpid()
        for i in range(timeout):
            time.sleep(1)
            if verbose:
                print("[pid]:{} [timing]:{}".format(pid, i))
        time.sleep(0.1)  # 多等0.1秒再kill掉进程，让达到timeout那一瞬间时的print之类的程序能执行下去
        if verbose:
            print("[pid]: {} timing计时完毕，kill目标子线程..".format(pid))
        self.target_thread.stop()

    def start(self):
        self.target_thread.start()
        self.timing_thread.start()
        # while循环block住主线程，直到self.t运行结束或者超时(self.timing_thread结束)
        while True:
            if self.target_thread.isAlive() and self.timing_thread.isAlive():
                continue
            else:
                break
        self.target_thread.stop()
        self.timing_thread.stop()
        q = self.resultQ.queue
        res_ = q[0] if len(q) > 0 else None
        return res_



    def _put_res_in_result_queue(self, func):
        """
        # 给target方法做个wrap，把其返回结果放到self.resultQ里
        :param func: 即target方法
        :return:
        """
        def wraps(*args, **kwargs):
            res = func(*args, **kwargs)
            # print("func运行完毕，结果将要放入resultQ队列中")
            self.resultQ.put(res)
        return wraps

class TimeoutProcess():
    def __init__(self, target, args=(), time_limit=1, verbose=False, delta=0.5):
        self.time_limit = time_limit
        self.delta = delta
        self.verbose = verbose

        self.resultQ = multiprocessing.Queue()
        _target = self._put_res_in_result_queue(target)
        self.p = multiprocessing.Process(target=_target, args=args)
        self.p.daemon = True

    def start(self):
        self.p.start()
        b_time = time.time()
        while True:
            time.sleep(0.25)
            if time.time()-b_time >= self.time_limit or not self.p.is_alive():
                # 每0.25s检查一次，如果已经超时或者process已经结束
                break
        self.p.terminate()
        try:
            res_ = self.resultQ.get_nowait()  # ==> get(block=False)
        except Empty as e:
            res_ = None
        return res_


    def _put_res_in_result_queue(self, func):
        """
        # 给target方法做个wrap，把其返回结果放到self.resultQ里
        :param func: 即target方法
        :return:
        """
        def wraps(*args, **kwargs):
            res = func(*args, **kwargs)
            self.resultQ.put(res)
            # print("func运行完毕，结果将要放入resultQ队列中")
        return wraps
