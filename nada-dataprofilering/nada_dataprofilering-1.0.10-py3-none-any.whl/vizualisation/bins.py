import datetime as dt


class Interval:
    def __init__(self, left, right, count=0, closed='left'):
        self._left = left
        self._right = right
        self._closed = closed
        self._count = count
        self._width = self._right - self._left

        if isinstance(self._left, dt.datetime) & isinstance(self._right, dt.datetime):
            delta = (self._right - self._left) / 2
            self._mid = self._left + delta
        else:
            self._mid = (self._left + self._right) / 2

    def to_string(self):
        if self._closed == 'left':
            print_string = f"Interval:[{self._left},{self._right}) \n"

        elif self._closed == 'right':
            print_string = f"Interval:({self._left},{self._right}] \n"

        elif self._closed == 'both':
            print_string = f"Interval:[{self._left},{self._right}] \n"

        elif self._closed == 'none':
            print_string = f"Interval:({self._left},{self._right}) \n"

        print_string += f"Midpoint: {self._mid} \n"
        print_string += f"Count: {self._count}"

        return print_string

    def is_in(self, x):
        if self._closed == 'left':
            if self._left <= x < self._right:
                return True
            else:
                return False
        elif self._closed == 'right':
            if self._left < x <= self._right:
                return True
            else:
                return False

        elif self._closed == 'both':
            if self._left <= x <= self._right:
                return True
            else:
                return False

        elif self._closed == 'none':
            if self._left < x < self._right:
                return True
            else:
                return False

    def set_count(self, x):
        self._count = x

    def add_count(self, x):
        self._count += x

    def plot_info(self):
        return self._mid, self._width, self._count

