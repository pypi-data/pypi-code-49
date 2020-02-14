import time

"""
计时器，主要用来快速测量程序的执行时间
"""


class RaceTimer:
    def __init__(self):
        self.reset()
        pass

    @staticmethod
    def create_instance():
        """
        创建并返回一个空的计时器对象，并设定初始时间为当前时刻
        :return: 
        """
        return RaceTimer()

    def snapshot(self):
        """
        添加一次计时，并返回距离开始时刻的毫秒时差
        :return: 
        """
        now = time.time()
        # self._points.append(now)
        return int(now * 1000 - self._start_time * 1000)
        pass

    def reset(self):
        """
        重置定时器
        :return: 
        """
        self._start_time = time.time()
        # self._points = []
        # self._points.append(self._start_time)
        pass

    def duriation(self):
        """
        计算当前时刻距离开始时刻过了多长时间
        :return: 
        """
        now = time.time()
        return int(now * 1000 - self._start_time * 1000)
