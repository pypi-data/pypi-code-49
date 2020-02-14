import time

"""
计时器，主要用来快速测量程序的执行时间
"""


class StopWatch:
    def __init__(self):
        self.reset()
        pass

    @staticmethod
    def create_instance():
        """
        创建并返回一个空的计时器对象，并设定初始时间为当前时刻
        :return: 
        """
        return StopWatch()

    def add_snapshot(self) -> int:
        """
        递加计时，并返回距离开始时刻的毫秒时差
        :return: 
        """
        now = time.time()
        cost = int(now * 1000 - self._start_time * 1000)
        self._snapshots.append(cost)
        return cost
        pass

    def list_snapshot(self) -> list:
        """
        返回全部的递加计时结果
        :return: 
        """
        return self._snapshots
        pass

    def reset(self) -> None:
        """
        重置定时器
        :return: 
        """
        self._start_time = time.time()
        self._snapshots = []
        pass

    def duration(self) -> int:
        """
        计算当前时刻距离开始时刻过了多长时间,返回毫秒时间
        :return: 
        """
        now = time.time()
        cost = int(now * 1000 - self._start_time * 1000)
        return cost
