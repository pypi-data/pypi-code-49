from unittest import TestCase
from zeroinger.time.race_timer import RaceTimer
import time


class TestRaceTimer(TestCase):
    timer = RaceTimer.create_instance()
    time.sleep(1)
    print(timer.snapshot())
    time.sleep(1)
    print(timer.duriation())
    timer.reset()
    time.sleep(1)
    print(timer.duriation())
    pass
