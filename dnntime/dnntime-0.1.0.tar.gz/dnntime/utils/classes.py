import numpy as np

class timesteps:

    def __init__(self, freq):
        map = {'s': 1,
               't': 1/60,
               'min': 1/60,
               'h': 1/3600,
               'd': 1/(3600*24),
               'b': 1/(3600*24),
               'w': 1/(3600*24*7),
               'm': 1/(3600*24*30),
               'ms': 1/(3600*24*30),
               'q': 1/(3600*24*90),
               'qs': 1/(3600*24*90),
               'a': 1/(3600*24*365),
               'y': 1/(3600*24*365),
               'as': 1/(3600*24*365),
               'ys': 1/(3600*24*365),
               }
        convert = map[freq.lower()]
        # time durations (N timesteps or seq steps)
        sec = convert
        min = sec*60
        hr = min*60
        day = hr*24
        week = day*7
        biwk = day*14
        mth = day*30
        quar = day*90
        year = day*365
        # np.NaN is the converted timestep interval is < 1
        self.SEC = int(sec) if sec >= 1 else np.NaN
        self.MIN = int(min) if min >= 1 else np.NaN
        self.HOUR = int(hr) if hr >= 1 else np.NaN
        self.DAY = int(day) if day >= 1 else np.NaN
        self.WEEK = int(week) if week >= 1 else np.NaN
        self.BIWK = int(biwk) if biwk >= 1 else np.NaN
        self.MONTH = int(mth) if mth >= 1 else np.NaN
        self.QUARTER = int(quar) if quar >= 1 else np.NaN
        self.YEAR = int(year) if year >= 1 else np.NaN


class colorful:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
