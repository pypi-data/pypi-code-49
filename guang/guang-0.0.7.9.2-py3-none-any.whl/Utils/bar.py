from enum import IntEnum
import time
import datetime
from datetime import timedelta, timezone
import numpy as np
from .time import beijing
from colorama import init, Fore, Back, Style


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

def get_bar(percent):
    unit_percent = 0.034
    total_space = 30
    n_sign1, mod_sign1 = divmod(percent, unit_percent)
    N1 = int(n_sign1)
    sign1 = "█" * N1
    N0 = int((mod_sign1/unit_percent) * (total_space - N1))
    sign0 = '>' * N0
    SIGN = '|' + sign1 + sign0 + (total_space- N1 - N0-1) * ' ' + '|'
    return SIGN, N1

def get_color(N_color, update=True, COLOR=[0]):
    if update == True or COLOR[0] == 0:
        color_list = ['CYAN', 'GREEN', 'RED', 'YELLOW', 'RESET', \
                      'LIGHTGREEN_EX',  'LIGHTRED_EX', \
                      'LIGHTYELLOW_EX',  'LIGHTBLACK_EX', 'LIGHTBLUE_EX', 'LIGHTCYAN_EX']
        # 'LIGHTMAGENTA_EX', 'MAGENTA', 'BLUE',

        color = [Fore.LIGHTCYAN_EX]  # Manually specify the first color
        for i in range(N_color - 2):
            color.append(eval("Fore." + np.random.choice(color_list)))
        color.append(Fore.LIGHTBLUE_EX)  # and the last color
        COLOR[0] = color

        return COLOR[0]
    else:
        return COLOR[0]

def bar(index, total_size, color='constant_random', first_time=[time.time()], flag_list=[1000], COLOR=[0]):
    """
    :arg color: options  'constant_random', 'update_random', 'reset'
    """
    # init(autoreset=True)
    _index = index + 1
    percent = (_index)/total_size # index+1 for index start from 0
    cost_time = time.time() - first_time[0]
    total_time = cost_time/percent
    remain_time = int(total_time - cost_time)
    remain_time = timedelta(seconds=remain_time)
    total_time = timedelta(seconds=int(total_time))
    ETC_1 = f"{remain_time}|{total_time} "
    ETC_2 = f"ETC: {(datetime.datetime.now() + remain_time).strftime('%m-%d %H:%M:%S')}"

    SIGN, N1 = get_bar(percent)

    if color == "update_random":
        if flag_list[0] != N1:
            flag_list[0] = N1
            COLOR[0] = get_color(N_color=4, update=True)
            [color1, color2, color3, color4] = COLOR[0]
        else:
            [color1, color2, color3, color4] = COLOR[0]

        print(color1 + f"\r{percent * 100: >6.2f}% ", color2 + SIGN, color3 + f"{ETC_1}", color4 + f"{ETC_2}", Fore.RESET, end='',
              flush=True)
    elif color == 'constant_random':
        [color1, color2, color3, color4] = get_color(N_color=4, update=False)
        print(f"\r{color1}{percent * 100: >6.2f}% "+ color2 + SIGN + color3 + f"{ETC_1}"+ color4 + f"{ETC_2}"+ Fore.RESET, end='',
              flush=True)
    elif color == 'reset':

        print(f"\r{percent * 100: >6.2f}% "+ SIGN + f"{ETC_1} {ETC_2}", end='', flush=True)
    else:
        raise ValueError("Invalid input!")

    if _index == total_size:
        print('\n')



class probar:
    """
    Simple progress bar display, to instead of tqdm.
    """

    def __init__(self, iterable, total_steps=None):
        self.iterable = iterable
        self.t0 = time.time()

        if hasattr(iterable, '__len__'):
            self.total_steps = len(iterable)
        else:
            self.total_steps = total_steps
            if self.total_steps == None:
                raise ValueError(f'{iterable} has no __len__ attr, use total_steps param')

    def __iter__(self):
        for idx, i in enumerate(self.iterable):
            c = idx + 1

            if idx == 0:
                print(f"\r{0:.2f}% \t  {0:.1f}|{np.inf:.1f}s ", end='', flush=True)
                d_percent = 0.01
            else:
                # percent = self.c / self.total_steps
                percent = c / self.total_steps
                PERCENT = percent * 100

                if PERCENT >= d_percent:
                    d_percent += 0.01
                    cost_time = time.time() - self.t0
                    total_time = cost_time / percent

                    remain_time = int(total_time - cost_time)
                    remain_time = datetime.timedelta(seconds=remain_time)
                    total_time = timedelta(seconds=int(total_time))
                    cost_time = datetime.timedelta(seconds=int(cost_time))

                    _PERCENT=f"{PERCENT: >6.2f}%"
                    SIGN, N1 = get_bar(percent)
                    _COST = f"{cost_time}|{total_time} "
                    _ETC = f"  ETC: {(datetime.datetime.now() + remain_time).strftime('%m-%d %H:%M:%S')}"

                    print('\r'+ Fore.CYAN +f"{_PERCENT}"+Fore.LIGHTBLACK_EX+SIGN+  \
                          Fore.LIGHTGREEN_EX +_COST+ Fore.LIGHTBLUE_EX +_ETC+ Fore.RESET, end='', flush=True)
                    # cprint(_PERCENT, fc=Fc.cyan)
                    # cprint(_COST, fc=Fc.green, coverage='')
                    # cprint(_ETC, fc=Fc.yellow, coverage='')
            if c == self.total_steps:
                print('\n')

            yield idx, i



if __name__=="__main__":
    def test_bar():
        for i in range(10):
            time.sleep(1)
            bar(i, 10)

    def test_probar():
        for idx, i in probar(range(15)):
            time.sleep(1)

    test_bar()