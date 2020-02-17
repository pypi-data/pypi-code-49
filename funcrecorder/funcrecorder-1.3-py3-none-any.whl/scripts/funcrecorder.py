import pickle
import os
from enum import Enum
from functools import wraps
# https://www.geeksforgeeks.org/class-as-decorator-in-python/


class RecordMode(Enum):
    N0NE = 0
    RECORD = 1
    REPLAY = 2


__is_record__ = None


class Rec:
    __RecordFileName__ = "recorder"

    def __init__(self):
        self.index = 0
        self.__record_mode__ = 0
        self.directory = ""

    def make_dir(self):
        directory = f"./tmp/recorder"
        if not os.path.exists(directory):
            os.makedirs(directory)
        self.directory = directory

    @property
    def record_path(self):
        return f"{self.directory}/{self.__RecordFileName__}_{self.index}.pickle"

    def store(self, val):
        self.make_dir()
        with open(self.record_path, 'wb') as file:
            pickle.dump(val, file)
        self.index += 1

    def replay(self):
        val = None
        self.make_dir()
        with open(self.record_path, 'rb') as file:
            val = pickle.load(file)
        self.index += 1
        return val


class RecordMgr(Rec):
    pass


recorder = RecordMgr()


def set_mode(mode):
    recorder.__record_mode__ = mode


def get_mode():
    return recorder.__record_mode__


def RecorderClass(f):
    @wraps(f)
    def _impl(self, *args, **kwargs):
        if recorder.__record_mode__ == RecordMode.N0NE.value:
            # do nothing
            return f(self, *args, **kwargs)

        elif recorder.__record_mode__ == RecordMode.RECORD.value:
            val = f(self, *args, **kwargs)
            # store val
            recorder.store(val)
            return f(self, *args, **kwargs)

        elif recorder.__record_mode__ == RecordMode.REPLAY.value:
            # replay val
            val = recorder.replay()
            # print(val)
            return val
    return _impl


class RecorderFunc(Rec):
    def __init__(self, f):
        Rec.__init__(self)
        self.f = f
        self.index = 0
        self.__record_mode__ = 0
        self.directory = ""

    def __call__(self, *argv, **kwargs):
        if __is_record__ == RecordMode.N0NE.value:
            # do nothing
            return self.f(*argv, **kwargs)

        elif __is_record__ == RecordMode.RECORD.value:
            val = self.f(*argv, **kwargs)
            # store val
            self.store(val)
            return self.f(*argv, **kwargs)
        elif __is_record__ == RecordMode.REPLAY.value:
            # replay val
            val = self.replay()
            # print(val)
            return val
