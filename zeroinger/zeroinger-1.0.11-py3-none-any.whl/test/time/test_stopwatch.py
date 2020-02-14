from unittest import TestCase
from zeroinger.time.stopwatch import StopWatch
import time


class TestStopWatch(TestCase):
    # 创建实例
    timer = StopWatch.create_instance()
    time.sleep(1)
    # 获取从开始到现在的耗时
    print('当前耗时',timer.duration())
    # 添加一个计时快照
    cost = timer.add_snapshot()
    print('快照1时间点', cost)
    time.sleep(1)
    cost = timer.add_snapshot()
    print('快照2时间点', cost)
    snapshot_list = timer.list_snapshot()
    print('所有快照时间点', snapshot_list)
    # 重置计时器
    timer.reset()

    pass
