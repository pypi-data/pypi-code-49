from itertools import filterfalse


class Stream:

    def __init__(self, iterator):
        self.item = iterator

    def get(self):
        return self.item

    def get_list(self):
        return list(self.item)

    def filter(self, func):
        self.item = filter(func, self.item)
        return self

    def filterfalse(self, func):
        self.item = filterfalse(func, self.item)
        return self

    def map(self, func):
        self.item = map(func, self.item)
        return self

    def sort(self, key=None, reverse=False):
        self.item = sorted(self.item, key=key, reverse=reverse)
        return self

    def reverse(self):
        self.item = iter(list(self.item)[::-1])
        return self


def streaming(iterator):
    return Stream(iterator)
