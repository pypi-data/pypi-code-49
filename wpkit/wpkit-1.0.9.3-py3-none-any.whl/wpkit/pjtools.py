import time, os, glob, shutil, random
import functools


class PointDict(dict):
    __no_value__='<__no_value__>'
    def __getattr__(self, key):
        return self.get(key)
    def __setattr__(self, key, value):
        self[key]=value
    def __call__(self, key , value=__no_value__):
        if value is self.__no_value__:
            self[key]=PointDict()
        else:
            self[key]=value
        return self[key]
    @classmethod
    def from_dict(cls,dic):
        dic2=cls()
        for k,v in dic.items():
            if not isinstance(v,dict):
                dic2[k]=v
            else:
                dic2[k]=cls.from_dict(v)
        return dic2

class Config(dict):
    def __setattr__(self, key, value):
        self[key] = value
        self.description={}

    def __getattr__(self, item):
        try:
            v = self[item]
            return v
        except:
            raise Exception('Config object has no key %s ' % item)

    def add(self, key, value, description=''):
        self[key] = value
        self.description[key] = description


class Timer:
    def __init__(self, verbose=True,msg=None,mute=None):
        self.history = []
        self.dt_history = []
        self.steps = 0
        self.start_time = time.time()
        self.history.append(self.start_time)
        self.verbose = verbose
        self.mute=mute
        if self.verbose:
            self.print('Timer started at %s' % (self.start_time))
        if msg:
            self.print(msg)
    def print(self,*args,**kwargs):
        if not self.mute:
            print(*args,**kwargs)
    def step(self,msg=None):
        t = time.time()
        dt = t - self.history[-1]
        self.dt_history.append(dt)
        self.history.append(t)
        self.steps += 1
        if self.verbose:
            self.print('step=%s , %s time since last step: %s' % (self.steps,'msg=%s'%(msg) if msg else '',dt))
        return dt
    def mean(self):
        if not len(self.dt_history):return None
        return sum(self.dt_history)/len(self.dt_history)
    def plot_dt_history(self,title='Timer History',*args,**kwargs):
        from matplotlib import pyplot as plt
        plt.plot(self.dt_history)
        plt.show(title=title,*args,**kwargs)

    def end(self):
        t = time.time()
        self.end_time = t
        dt = t - self.history[-1]
        self.dt_history.append(dt)
        self.history.append(t)
        self.steps += 1
        if self.verbose:
            self.print('time since last step: %s' % (dt))
        return dt
DEFALUT_TIMER=None
def timer_step(msg=None):
    global DEFALUT_TIMER
    if not DEFALUT_TIMER:
        DEFALUT_TIMER=Timer()
    else:
        DEFALUT_TIMER.step(msg)


def run_timer(func):
    name = func.__name__

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('running %s ...' % (name))
        t = Timer(verbose=False)
        ret = func(*args, **kwargs)
        dt = t.end()
        print('finished running %s ,time consumed: %s' % (name, dt))
        return ret
    return wrapper


class BatchIterator:
    def __init__(self, mylist, batch_size):
        self.list = mylist
        self.batch_size = batch_size
        self.length = len(mylist)
        self.num_batch = self.length // self.batch_size
        self.cur_batch_idx = -1
        self.cur_batch = None

    def next(self):
        self.cur_batch_idx += 1
        if self.cur_batch_idx >= self.num_batch:
            self.cur_batch_idx = 0
        self.cur_batch = self.get_batch_by_idx(self.cur_batch_idx)
        return self.cur_batch

    def get_batch_by_idx(self, batch_idx):
        st = batch_idx * self.batch_size
        ed = st + self.batch_size
        return self.list[st:ed]
