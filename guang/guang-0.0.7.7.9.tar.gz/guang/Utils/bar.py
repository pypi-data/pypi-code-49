print(__name__)
from enum import IntEnum
import time
import datetime
from datetime import timedelta, timezone
import numpy as np
from .time import beijing
# class beijing:
#     # utc_time = datetime.utcnow()
#     utc_time = datetime.datetime.now(tz=timezone.utc)
#     bj_time = utc_time.astimezone(timezone(timedelta(hours=8)))
#     now = bj_time.now()

class Fc(IntEnum):
    """Foreground color"""
    black = 30
    red = 31
    green = 32
    yellow = 33
    blue = 34
    magenta = 35
    cyan = 36
    white = 37
class Bc(IntEnum):
    """Background color"""
    black = 40
    red = 41
    green = 42
    yellow = 43
    blue = 44
    magenta = 45
    cyan = 46
    white = 47
class Disp(IntEnum):
    """Effect of display"""
    default = 0
    highlight = 1
    underline = 4
    twinkle = 5 # 闪烁
    reverse = 6 # 反白显示
    invisible = 8

def cprint(string, fc=Fc.cyan, bg=False, bc=Bc.black, coverage='\r'):

    if bg:
        print(f'{coverage}\033[{Disp.highlight};{fc};{bc}m{string}\033[0m', end='', flush=True)
    else:
        print(f'{coverage}\033[{Disp.highlight};{fc}m{string}\033[0m', end='', flush=True)



def bar(current_size, total_size, first_time=[time.time()]):
    percent = current_size/total_size
    cost_time = time.time() - first_time[0]
    total_time = cost_time/percent
    remain_time = total_time - cost_time
    ETC = (datetime.datetime.now() + timedelta(seconds=remain_time)).strftime('%m-%d %H:%M:%S')

    cprint(f"{percent*100:.2f}%  ")
    cprint(f"ETC {ETC}", fc=Fc.black, coverage='')


class probar:
    """
    Simple progress bar display, to instead of tqdm.
    """

    def __init__(self, iterable, total_steps=None):
        self.iterable = iterable
        self.t0 = time.time()
        self.c = 0
        # self.cT = datetime.datetime.now()
        self.cT = beijing.now
        if hasattr(iterable, '__len__'):
            self.total_steps = len(iterable) - 1
        else:
            self.total_steps = total_steps
            if self.total_steps == None:
                raise ValueError(f'{iterable} has no __len__ attr, use total_steps param')

    def __iter__(self):
        for idx, i in enumerate(self.iterable):
            if idx == 0:
                print(f'\r{0:.2f}% \t  {0:.1f}|{np.inf:.1f}s \t', end='', flush=1)
                d_percent = 0.01
            else:
                percent = self.c / self.total_steps
                PERCENT = percent * 100

                if PERCENT >= d_percent:
                    d_percent += 0.01
                    cost_time = time.time() - self.t0
                    cost_minute, cost_second = divmod(cost_time, 60)

                    total_time = cost_time / percent
                    t_minute, t_second = divmod(total_time, 60)
                    dT = datetime.timedelta(0, total_time)
                    deadLine = self.cT + dT
                    print(f"\r{PERCENT:.2f}% \t{cost_minute:.0f}'{cost_second:.1f}\"|{t_minute:.0f}'{t_second:.1f}\"\t\t\
                    Expect:{deadLine.month}-{deadLine.day} \
                    {deadLine.hour}:{deadLine.minute}:{deadLine.second} \t", end='', flush=True)

            yield idx, i
            self.c += 1

def _test1():
    for i in range(1,10):
        time.sleep(1)
        bar(i, 9)
def _test2():
    for idx, i in probar(range(10)):
        time.sleep(1)


_test2()

if __name__=="__main__":
    # _test1()
    _test2()