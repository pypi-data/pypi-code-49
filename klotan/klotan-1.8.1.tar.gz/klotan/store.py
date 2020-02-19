class Storage:
    def __init__(self):
        pass

    def store(self, name, fn, *kargs, **kwargs):
        pass


class ValueStorage(Storage):
    def __init__(self):
        super().__init__()
        self.fn = None
        self.kargs = None
        self.kwargs = None
        self.value = None

    def store(self, fn, *kargs, **kwargs):
        self.fn = fn
        self.kargs = kargs
        self.kwargs = kwargs
        self.value = kargs[0]


class ListStorage(Storage):
    def __init__(self):
        super().__init__()
        self.values = []

    def store(self, fn, *kargs, **kwargs):
        new_value = ValueStorage()
        new_value.store(fn, *kargs, **kwargs)
        self.values.append(new_value)
