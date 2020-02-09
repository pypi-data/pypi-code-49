from threading import Lock


class OutOfSizeError(IndexError):
    def __index__(self, msg: str = ''):
        super(OutOfSizeError, self).__index__(msg)


class DStack:

    def __init__(self, clz: type = object, max_size: int = -1):
        # 初始化相关配置
        self._clz = clz
        self._data = []
        self._lock = Lock()
        self._max = max_size

    def push(self, item: object):
        '''
        添加单元
        :param item:
        :return:
        '''
        assert isinstance(item, self._clz), TypeError(f'current item is not belong {self._clz}')
        # 栈最大值过滤断言
        assert self._max == -1 or len(self._data) <= self._max, OutOfSizeError('stack full of size')
        try:
            self._lock.acquire(False, 2)
        except:
            pass
        else:
            self._data.append(item)
        finally:
            self._lock.release()

    def pop(self, index: int = 0):
        '''
        弹出单元
        :param index:
        :return:
        '''
        assert len(self._data) > 0, IndexError('pop from empty stack')
        self._data.pop(index)

    def flush(self):
        '''
        冲刷数据域
        :return:
        '''
        self._data = []

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
